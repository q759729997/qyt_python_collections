"""
100次:平均奖励为5400.0/100=54.0
keras参考：https://www.jianshu.com/p/d02980fd7b54
"""
import gym
import numpy as np
import tensorflow.compat.v2 as tf
from tensorflow import keras

# 日志初始化
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info('logging test')

env = gym.make('CartPole-v0')


# 输入是一个状态，是CartPole的位置、速度、角度和角速度四个变量
observation = env.reset()
# np.newaxis 在使用和功能上等价于 None
input_shape = tf.convert_to_tensor(observation[np.newaxis], dtype=tf.float32).get_shape()
logging.info('input_shape:{}'.format(input_shape))

# 临时
actor_net = None
critic_net = None


class AdvantageActorCriticAgent(object):
    """A2C智能体"""
    def __init__(self, gamma=0.99):
        self.action_n = env.action_space.n
        self.gamma = gamma
        self.discount = 1.

    def decide(self, observation):
        """actor网络对observation进行预测，按概率求取下一步动作"""
        probs = actor_net.predict(observation[np.newaxis])[0]
        action = np.random.choice(self.action_n, p=probs)
        return action

    def learn(self, observation, action, reward, next_observation, done):
        x = observation[np.newaxis]
        next_x = next_observation[np.newaxis]
        # 使用critic网络计算observation与next_observation状态价值
        u = reward + (1. - done) * self.gamma * critic_net.predict(next_x)
        td_error = u - critic_net.predict(x)

        # 训练执行者网络
        x_tensor = tf.convert_to_tensor(observation[np.newaxis], dtype=tf.float32)
        # 使用梯度带计算梯度
        with tf.GradientTape() as tape:
            pi_tensor = actor_net(x_tensor)[0, action]
            logpi_tensor = tf.math.log(tf.clip_by_value(pi_tensor, 1e-6, 1.))
            loss_tensor = -self.discount * td_error * logpi_tensor
        grad_tensors = tape.gradient(loss_tensor, actor_net.variables)
        # 更新执行者网络
        actor_net.optimizer.apply_gradients(zip(grad_tensors, actor_net.variables))

        # 训练评论者网络
        critic_net.fit(x, u, verbose=0)  # 更新评论者网络

        if done:
            self.discount = 1.  # 为下一回合初始化累积折扣
        else:
            self.discount *= self.gamma  # 进一步累积折扣
