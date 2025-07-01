import random
import numpy as np

# Environment settings
states = [0, 1, 2]  # Positions on the road
actions = ["left", "stay", "right"]
goal_state = 2

# Q-table: states x actions
q_table = np.zeros((len(states), len(actions)))

# Learning parameters
alpha = 0.1        # Learning rate
gamma = 0.9        # Discount factor
epsilon = 0.2      # Exploration rate
episodes = 1000

# Helper: get next state
def get_next_state(state, action):
    if action == "right":
        return min(state + 1, 2)
    elif action == "left":
        return max(state - 1, 0)
    else:
        return state

# Helper: get reward
def get_reward(state):
    return 1 if state == goal_state else -0.1

# Training
for episode in range(episodes):
    state = 0  # Start from position 0
    done = False
    
    while not done:
        # Choose action: exploration vs exploitation
        if random.random() < epsilon:
            action_index = random.randint(0, 2)
        else:
            action_index = np.argmax(q_table[state])
        
        action = actions[action_index]
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # Q-learning update
        old_value = q_table[state][action_index]
        next_max = np.max(q_table[next_state])
        new_value = old_value + alpha * (reward + gamma * next_max - old_value)
        q_table[state][action_index] = new_value

        # Move to next state
        state = next_state

        # Check if goal reached
        if state == goal_state:
            done = True

# After training: Test policy
state = 0
path = [state]
while state != goal_state:
    action_index = np.argmax(q_table[state])
    action = actions[action_index]
    state = get_next_state(state, action)
    path.append(state)

print("Learned path to goal:", path)
print("Q-table:\n", q_table)
