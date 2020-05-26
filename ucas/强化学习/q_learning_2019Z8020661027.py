"""
1、使用OpenAI Gym环境中的FrozenLake模拟器：http://gym.openai.com/envs/FrozenLake-v0/
2、环境说明：冰湖环境，使用文字进行描述，如下示例：
SFFF       (S: starting point, safe)
FHFH       (F: frozen surface, safe)
FFFH       (H: hole, fall to your doom)
HFFG       (G: goal, where the frisbee is located)
3、任务目标：智能体从S走到G，并绕开H；
奖惩：The episode ends when you reach the goal or fall in a hole. You receive a reward of 1 if you reach the goal, and zero otherwise.
4、依赖安装：
pip install gym
5、个人信息：
- 姓名：乔咏田
- 学号：2019Z8020661027
"""
import time
import random

import gym
import numpy as np

# 常量
action_names = ('LEFT', 'DOWN', 'RIGHT', 'UP')  # 动作名称
max_run_step = 100  # 最多尝试100次
# 初始化FrozenLake环境
env = gym.make('FrozenLake-v0')


def run_random():
    """随机行走"""
    # 初始化环境对象env
    env.reset()
    step_id = 1
    while True:
        print('============step:{}============='.format(step_id))
        step_id += 1
        # 显示当前环境
        env.render()
        action = env.action_space.sample()
        print('action：{}-{}'.format(action, action_names[action]))
        observation, reward, done, info = env.step(action)
        print('observation:{}, reward:{}, done:{}, info:{}'.format(observation, reward, done, info))
        time.sleep(0.3)
        if done:
            env.render()
            break


def train(q_table, gama=0.9, epsilon=1.0, alpha=0.5, max_epoch=1000):
    """ learning训练.

        @params:
            q_table - q值表.
            gama - gama.
            epsilon - epsilon.
            alpha - 学习率(眼前奖励和记忆中的奖励如何权衡).
            max_epoch - 训练次数.

        @return:
            On success - q_table.
            On failure - 错误信息.
    """
    train_scores = []
    for epoch in range(1, max_epoch+1):
        observation = env.reset()
        epsilon = max(epsilon - 1/500, 0)  # 衰减函数
        step_id = 0
        while True:
            step_id += 1
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[observation, :])
            observation_next, reward, done, info = env.step(action)
            # q-learning公式
            q_table[observation][action] = q_table[observation][action] + (alpha * (reward + gama * np.max(q_table[observation_next, :]) - q_table[observation][action]))
            observation = observation_next
            if done or step_id >= max_run_step:
                train_scores.append(reward)
                break
        if epoch % 10 == 0:
            print('train epoch:{}'.format(epoch))
            print('准确率：{}/{}'.format(train_scores.count(1), len(train_scores)))
    return q_table, '{}/{}'.format(train_scores.count(1), len(train_scores))


def run_by_q_table(q_table):
    """通过q_table行走"""
    # 初始化环境对象env
    observation = env.reset()
    step_id = 1
    while True:
        print('============step:{}============='.format(step_id))
        step_id += 1
        # 显示当前环境
        env.render()
        # action = env.action_space.sample()
        action = np.argmax(q_table[observation, :])
        print('action：{}-{}'.format(action, action_names[action]))
        observation, reward, done, info = env.step(action)
        print('observation:{}, reward:{}, done:{}, info:{}'.format(observation, reward, done, info))
        time.sleep(0.3)
        if done:
            env.render()
            break
        if step_id >= max_run_step:
            print('到达最大尝试次数{}，退出探索'.format(max_run_step))
            break


if __name__ == "__main__":
    print('查看环境基本信息：')
    print('action_space：{}'.format(env.action_space))  # Discrete(4)
    print('observation_space：{}'.format(env.observation_space))  # Discrete(16)
    print('随机行走：')
    # run_random()
    # 初始化q-learning参数
    q_table = np.zeros(shape=(env.nS, env.nA))  # observation大小*action大小
    print('q_table:{}'.format(q_table.shape))  # (16, 4)
    # print('未训练通过q_table行走：')
    # run_by_q_table(q_table)
    q_table, train_result = train(q_table, max_epoch=5000)
    print('训练后通过q_table行走：')
    run_by_q_table(q_table)
    print('train_result:{}'.format(train_result))
    env.close()
