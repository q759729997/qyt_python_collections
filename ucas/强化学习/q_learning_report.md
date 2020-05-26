# 强化学习第一次作业

- 作业内容：实现Q-learning
- 姓名：乔咏田
- 学号：2019Z8020661027

## 环境说明

- 使用OpenAI Gym环境中的FrozenLake模拟器：http://gym.openai.com/envs/FrozenLake-v0/

- 环境说明：冰湖环境（4x4），使用文字进行描述，如下示例：

~~~wiki
SFFF    (S: starting point, safe)
FHFH    (F: frozen surface, safe)
FFFH    (H: hole, fall to your doom)
HFFG    (G: goal, where the frisbee is located)
~~~

- 任务目标：智能体从S走到G，并绕开H；

  奖惩：The episode ends when you reach the goal or fall in a hole. You receive a reward of 1 if you reach the goal, and zero otherwise.

  可选动作：`('LEFT', 'DOWN', 'RIGHT', 'UP')`

- 依赖安装：

~~~shell
pip install gym
~~~

## 运行命令

~~~python
python q_learning_2019Z8020661027.py
~~~

## 运行结果

- 随机行走，可以看step4就掉到冰窟里面了（因包含随机性，每次运行结果会有不同）：

~~~wiki
============step:1=============

?[41mS?[0mFFF
FHFH
FFFH
HFFG
action：3-UP
observation:0, reward:0.0, done:False, info:{'prob': 0.3333333333333333}
============step:2=============
  (Up)
?[41mS?[0mFFF
FHFH
FFFH
HFFG
action：2-RIGHT
observation:0, reward:0.0, done:False, info:{'prob': 0.3333333333333333}
============step:3=============
  (Right)
?[41mS?[0mFFF
FHFH
FFFH
HFFG
action：1-DOWN
observation:4, reward:0.0, done:False, info:{'prob': 0.3333333333333333}
============step:4=============
  (Down)
SFFF
?[41mF?[0mHFH
FFFH
HFFG
action：1-DOWN
observation:5, reward:0.0, done:True, info:{'prob': 0.3333333333333333}
  (Down)
SFFF
F?[41mH?[0mFH
FFFH
HFFG
~~~

- 训练结果：

~~~wiki
训练500轮：train_result:42/500；agent执行25step后失败
训练1000轮：train_result:259/1000；agent执行27step后成功
训练2000轮：train_result:829/2000；agent执行25step后成功
训练5000轮：train_result:2964/5000；agent执行16step后成功
~~~

