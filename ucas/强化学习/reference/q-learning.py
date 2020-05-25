# -*- coding: utf-8 -*-
# Author: 常雪松, 2019Z8020661038
# Running cmd: 
#   python q-learning-2019Z8020661038-ChangXueSong.py --case case_1
#   or
#   python q-learning-2019Z8020661038-ChangXueSong.py --case case_2

import argparse
import numpy as np

MAX_EPISODES = 100
EPSILON = 0.9   # greedy 贪婪度
EPSILON_RATE = 0.5
ALPHA = 0.1     # 学习率
GAMMA = 0.8     # 奖励递减值

def drawCase(case):
    if case == 'case_1':
        print('Target: Goto room 5 from any room.\n')
        print('              outdoor(room 5)')
        print('  +---------+-----| |--+')
        print('  | room 0  |  room 1  |')
        print('  +----| |--+----| |---+----------+')
        print('  |        -+-        -+-         |')
        print('  | room 4     root 3     room 2  |')
        print('  |        -+-        -+-         |')
        print('  +---------+----------+----------+\n')
    else:
        print('drawCase: Not support case.')
  

def initRQ(case):
    if case == 'case_1':
        R = np.array([
            # Action: Goto room(Col)
            # 0   1   2   3   4    5      # State: Now, in room(Row)
            [-1, -1, -1, -1, 10,  -1],    # 0
            [-1, -1, -1, 10, -1, 100],    # 1
            [-1, -1, -1, 10, -1,  -1],    # 2
            [-1, 10, 10, -1, 10,  -1],    # 3
            [10, -1, -1, 10, -1,  -1],    # 4
            [-1, 10, -1, -1, -1, 100]])   # 5
    else:
        print('initRQ: Not support case.')
        exit()

    Q = np.zeros(R.shape)

    return R, Q

# Return: start state, end state
def initTrainState(case):
    if case == 'case_1':
        return np.random.randint(6), [5]
    else:
        print('randomState: Not support case.')
        exit()

def initTestState(case):
    if case == 'case_1':
        action_mean = ['Room 0', 'Room 1', 'Room 2',
                       'Room 3', 'Room 4', 'Room 5']
        start_state = [0, 1, 2, 3, 4, 5]
        end_state = [5]
    else:
        print('randomState: Not support case.')

    return start_state, end_state, action_mean

def getNewState(case, current_state, action_idx):
    new_state = 0
    if case == 'case_1':
        new_state = action_idx

    return new_state

def updateStateAndQ(case, R, Q, current_state, action_idx):
    new_state = getNewState(case, current_state, action_idx)

    if case == 'case_1': R[current_state][action_idx] -= 1
    Q[current_state][action_idx] += ALPHA * (R[current_state][action_idx] + \
                                GAMMA * np.max(Q[new_state]) - \
                                Q[current_state][action_idx])
    if case == 'case_1' and R[current_state][action_idx] == 0: R[current_state][action_idx] = 2

    return new_state, Q

def trainer(case, R, Q):
    start_state, end_state = initTrainState(case)
    current_state = start_state

    while 1:
        brave = False
        if np.random.random() >= EPSILON: brave = True

        action_idx = np.argmax(R[current_state])    # brave = False
        if brave: 
            # Get action that can be performed for current state.
            action_list = np.argwhere(R[current_state] >= 0).transpose()[0]
            action_idx = np.random.choice(action_list)
                
        current_state, Q = updateStateAndQ(case, R, Q, current_state, action_idx)

        if current_state in end_state:
            return Q
            
    return Q

def tester(case, Q):
    print('\n-------------------[test]-------------------\n')
    start_state, end_state, action_mean = initTestState(case)
    drawCase(case)


    print('\n-----------------[Go Go Go]-----------------\n')
    for current_state in start_state:
        print('  [Start]')
        if case == 'case_1':
            print(action_mean[current_state])
        while 1:
            best_action = np.argmax(Q[current_state])
            print('->', action_mean[best_action])
            current_state = getNewState(case, current_state, best_action)

            if current_state in end_state:
                print('[End]')
                break
    print

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", "-c", default="case_1", type=str, help="case_1.")
    args = parser.parse_args()

    case_type = args.case
    if case_type not in ['case_1']:
        print('ERROR: --case need \'case_1\'')
        exit()

    ten_percent_max_episode = MAX_EPISODES / 10

    R, Q = initRQ(case_type)
    for episode in range(MAX_EPISODES):
        # From:
        #   We don't know anything about our environment, I need to follow my experience.
        # To:
        #   We know a lot about our environment, I'm brave, so I want do more explore.
        if (EPSILON > 0.1 and episode % ten_percent_max_episode == 0):
            EPSILON *= EPSILON_RATE

        Q = trainer(case_type, R, Q)

    print('R:', R)
    print('Q:', Q)
    print
    tester(case_type, Q)


