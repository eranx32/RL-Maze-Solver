import time
import turtle
import numpy as np


class Agent:
    def __init__(self):
        self.G = 0
        self.Gsa = np.zeros((10, 10, 4))
        self.Nsa = np.zeros((10, 10, 4))
        self.Qsa = np.full((10, 10, 4), 0.)
        self.Qsa[9][5] = [0, 0, 0, 0]
        self.all_states = []
        self.gamma = 0.99
        self.epsilon = 0.25
        self.rewards = []
        self.actions = []

    def act(self, state, legal_moves):
        row, col = state[0], state[1]
        choice = np.random.rand()
        q_values_for_legal_moves = self.Qsa[row][col][legal_moves]

        if choice > self.epsilon:
            maximum = np.max(q_values_for_legal_moves)
            relative_indices = [idx for idx, item in enumerate(q_values_for_legal_moves) if item == maximum]
            chosen_relative_index = np.random.choice(relative_indices)
            return legal_moves[chosen_relative_index]
        else:
            return np.random.choice(legal_moves)

    def reset(self, epsilon=1.):
        self.G = 0
        self.all_states = []
        self.rewards = []
        self.actions = []
        self.epsilon *= epsilon


class MazeEnvironment:
    def __init__(self, games):
        self.legit_actions = {"00": [1, 2], "01": [1, 3], "02": [1,3], "03":[1, 3], "04": [1, 2, 3], "05": [1, 3], "06": [1,3], "07": [2, 3], "08": [1, 2], "09": [2, 3],
                              "10": [0, 1], "11": [2, 3], "12": [1,2], "13":[3], "14": [0, 2], "15": [1, 2], "16": [1,3], "17": [0, 3], "18": [0, 2], "19": [0, 2],
                              "20": [2], "21": [0, 2], "22": [0,1], "23":[1, 2, 3], "24": [0, 3], "25": [0, 2], "26": [1,2], "27": [1, 3], "28": [0, 3], "29": [0, 2],
                              "30": [0, 1], "31": [0, 3], "32": [2], "33":[0, 2], "34": [1, 2], "35": [0, 3], "36": [0, 2], "37": [1, 2], "38": [3], "39": [0, 2],
                              "40": [1, 2], "41": [2, 3], "42": [0, 1, 2], "43":[0, 2, 3], "44": [0, 1, 2], "45": [1, 3], "46": [0, 1, 3], "47": [0, 3], "48": [1, 2], "49": [0, 2, 3],
                              "50": [0], "51": [0, 2], "52": [0, 2], "53":[0], "54": [0, 1], "55": [2, 3], "56": [1, 2], "57": [3], "58": [0, 2], "59": [0, 2],
                              "60": [1, 2], "61": [0, 3], "62": [0, 1], "63":[2, 3], "64": [1, 2], "65": [0, 1, 3], "66": [0, 3], "67": [1, 2], "68": [0, 3], "69": [0, 2],
                              "70": [0, 1], "71": [2, 3], "72": [1, 2], "73":[0, 3], "74": [0, 2], "75": [1, 2], "76": [2, 3], "77": [0, 2], "78": [1], "79": [0, 3],
                              "80": [1, 2], "81": [0, 3], "82": [0, 1], "83":[2, 3], "84": [0, 1], "85": [0, 3], "86": [0], "87": [0, 1], "88": [1, 2, 3], "89": [2, 3],
                              "90": [0, 1], "91": [1, 3], "92": [1, 3], "93":[0, 1, 3], "94": [3], "95": ["?"], "96": [1, 3], "97": [1, 3], "98": [0, 3], "99": [0]}
        self.start_pos = (0, 0)
        self.end_pos = (9, 5)
        self.current_pos_row, self.current_pos_col = self.start_pos
        self.counter = 0
        self.possible_values = np.arange(4)
        self.done = False
        self.games = games
        self.counter_list = []

        self.screen = turtle.Screen()
        self.screen.title("Maze")
        self.screen.bgpic("assets/maze.gif")
        self.screen.setup(width=620, height=620)
        self.screen.tracer(0)

        self.agent = turtle.Turtle()
        self.agent.shape("circle")
        self.agent.color("red")
        self.agent.shapesize(stretch_wid=1.3, stretch_len=1.3)
        self.agent.pencolor("blue")
        self.agent.pensize(3)
        self.agent.penup()
        self.agent.goto(-270, 265)

        self.target = turtle.Turtle()
        self.target.shape("square")
        self.target.color(0.2, 0.4, 0.6)
        self.target.shapesize(stretch_wid=1.7, stretch_len=1.7)
        self.target.penup()
        self.target.goto(30, -275)

    def get_pos(self):
        return self.current_pos_row, self.current_pos_col

    def reset(self):
        self.agent.clear()
        self.agent.penup()
        self.current_pos_row, self.current_pos_col = np.random.choice(np.arange(8)), np.random.choice(np.arange(8))
        self.agent.goto(-270+60*self.current_pos_col, 265-60*self.current_pos_row)
        self.agent.pendown()
        print("Agent position:", -270 + 60 * self.current_pos_col, 265 - 60 * self.current_pos_row)
        self.counter_list.append(self.counter)
        self.counter = 0
        self.games -= 1
        self.done = False

    def step(self, action):
        reward = -1
        if action == 0:
            self.current_pos_row -= 1
        if action == 1:
            self.current_pos_col += 1
        if action == 2:
            self.current_pos_row += 1
        if action == 3:
            self.current_pos_col -= 1
        self.agent.goto(-270+60*self.current_pos_col, 265-60*self.current_pos_row)
        self.counter += 1
        if self.current_pos_row == 9 and self.current_pos_col == 5:
            reward = 10
            self.done = True
        return (self.current_pos_row, self.current_pos_col), reward, self.done


env = MazeEnvironment(6000)
agent = Agent()
while env.games > 0:
    if env.games <= 300:
        time.sleep(0.1)
    current_state = env.get_pos()
    string_pos = f"{current_state[0]}{current_state[1]}"
    legal_moves = env.legit_actions[string_pos]
    act = agent.act(current_state, legal_moves)
    next_state, r, is_done = env.step(act)
    agent.rewards.append(r)
    agent.actions.append(act)
    agent.all_states.append(current_state)
    if env.done:
        print(f"Game No. {env.games} is done")
        actions_reversed = agent.actions[::-1]
        rewards_reversed = agent.rewards[::-1]
        all_states_reversed = agent.all_states[::-1]
        agent.G = 0
        for idx, state in enumerate(all_states_reversed):
            act = actions_reversed[idx]
            agent.G = rewards_reversed[idx] + agent.G * agent.gamma
            agent.Gsa[state[0]][state[1]][act] += agent.G
            agent.Nsa[state[0]][state[1]][act] += 1
        for row in range(10):
            for col in range(10):
                for action in range(4):
                    if agent.Nsa[row][col][action] > 0:
                        agent.Qsa[row][col][action] = agent.Gsa[row][col][action]/agent.Nsa[row][col][action]
        if env.games <= 1000:
            agent.reset(0.99)
        else:
            agent.reset()
        env.reset()
    if env.games <= 300:
        env.screen.update()


for counter_id, counter in enumerate(env.counter_list):
    print(f"Game No. {counter_id+1}: {counter} steps")

print("Best move per state:")
num_to_act = {0: "UP", 1: "RIGHT", 2: "DOWN", 3: "LEFT"}
for r in range(10):
    for c in range(10):
        # print(f"({r}, {c}) --> {num_to_act[np.argmax(agent.Qsa[r][c])]}")
        string_pos = f"{r}{c}"
        legal = env.legit_actions[string_pos]
        best = legal[np.argmax(agent.Qsa[r][c][legal])]
        print(f"({r}, {c}) --> {num_to_act[best]}")


