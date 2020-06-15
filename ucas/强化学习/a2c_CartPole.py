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


class PPOReplayerBuffer(object):
    """经验缓存区"""
    def __init__(self):
        self.memory = pd.DataFrame()
    
class PPOAgent(object):
    """PPO智能体"""
    def __init__(self, clip_ratio=0.1, gamma=0.99, lambd=0.99, min_trajectory_length=1000,
            batches=1, batch_size=64):
        self.action_n = env.action_space.n
        self.gamma = gamma
        self.lambd = lambd
        self.clip_ratio = clip_ratio
        self.min_trajectory_length = min_trajectory_length
        self.batches = batches
        self.batch_size = batch_size
        self.trajectory = []
        self.replayer = PPOReplayerBuffer()

    def learn(self, observation, action, reward, done):
        self.trajectory.append((observation, action, reward))
        if done:
            df = pd.DataFrame(self.trajectory, columns=['observation', 'action', 'reward'])
            observations = np.stack(df['observation'])
            df['v'] = critic_net.predict(observations)
            pis = actor_net.predict(observations)
            df['pi'] = [pi[action] for pi, action in zip(pis, df['action'])]
            df['next_v'] = df['v'].shift(-1).fillna(0.)
            df['u'] = df['reward'] + self.gamma * df['next_v']
            df['delta'] = df['u'] - df['v']
            df['return'] = df['reward']
            df['advantage'] = df['delta']
            for i in df.index[-2::-1]:
                df.loc[i, 'return'] += self.gamma * df.loc[i + 1, 'return']
                df.loc[i, 'advantage'] += self.gamma * self.lambd * df.loc[i + 1, 'advantage']
            fields = ['observation', 'action', 'pi', 'advantage', 'return']
            self.replayer.store(df[fields])
            self.trajectory = []
            if len(self.replayer.memory) > self.min_trajectory_length:
                for batch in range(self.batches):
                    observations, actions, pis, advantages, returns = \
                            self.replayer.sample(size=self.batch_size)
                    # 训练执行者
                    s_tensor = tf.convert_to_tensor(observations, dtype=tf.float32)
                    gather_tensor = tf.convert_to_tensor([(i, a) for i, a in enumerate(actions)], dtype=tf.int32)
                    pi_old_tensor = tf.convert_to_tensor(pis, dtype=tf.float32)
                    advantage_tensor = tf.convert_to_tensor(advantages, dtype=tf.float32)
                    with tf.GradientTape() as tape:
                        all_pi_tensor = actor_net(s_tensor)
                        pi_tensor = tf.gather_nd(all_pi_tensor, gather_tensor)
                        surrogate_advantage_tensor = (pi_tensor / pi_old_tensor) * advantage_tensor
                        clip_times_advantage_tensor = self.clip_ratio * surrogate_advantage_tensor
                        max_surrogate_advantage_tensor = advantage_tensor + tf.where(advantage_tensor > 0., clip_times_advantage_tensor, -clip_times_advantage_tensor)
                        clipped_surrogate_advantage_tensor = tf.minimum(surrogate_advantage_tensor,  max_surrogate_advantage_tensor)
                        loss_tensor = -tf.reduce_mean(clipped_surrogate_advantage_tensor)
                    actor_grads = tape.gradient(loss_tensor, actor_net.variables)
                    actor_net.optimizer.apply_gradients(zip(actor_grads, actor_net.variables))
                    # 训练评论者
                    critic_net.fit(observations, returns, verbose=0)
                self.replayer = PPOReplayerBuffer()
