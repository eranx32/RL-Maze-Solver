Reinforcement Learning from Scratch: Maze Solver 🤖
This repository contains a pure Python implementation of fundamental Reinforcement Learning algorithms (Monte Carlo, SARSA, and Q-Learning) designed to solve a complex maze environment.

Unlike projects that rely on high-level RL libraries (like Stable Baselines or Ray), this project implements the agents, environment, and learning logic from scratch using only NumPy for matrix operations. This approach demonstrates a deep understanding of the underlying mathematical concepts and the Bellman equations.

(Note: If the GIF isn't loading, ensure assets/maze.gif is present)

🧠 Algorithms Implemented
I explored three different approaches to solving the tabular RL problem:
Monte Carlo Methods: Updates Q-values based on complete episodes. The agent learns from the full return ($G$) of a trajectory.
SARSA (State-Action-Reward-State-Action): An on-policy algorithm where the agent learns the value of the policy being carried out, including the exploration steps.
Q-Learning: An off-policy algorithm where the agent learns the optimal policy (using the max operator) independently of the agent's actions used to explore the environment.
🛠️ Tech Stack & ArchitectureLanguage: 
Python 3.x
Math: NumPy (Matrix manipulations for Q-Tables, G-Values)
Visualization: Turtle Graphics (Custom rendering of the agent and environment)
Environment: A custom grid-world with:
Obstacles and defined legal moves.
Sparse rewards (-1 step penalty, +10 goal reward).
Epsilon-Greedy exploration strategy with decay.
📂 Project Structure
Bash
├── assets/             # Graphical assets (backgrounds, etc.)
├── MonteCarlo.py       # Monte Carlo implementation
├── SARSA.py            # SARSA implementation
├── Q-Learning.py       # Q-Learning implementation
└── README.md           # Project documentation

🚀 How to Run
1. Clone the repository:
Bash
git clone https://github.com/eranx32/RL-Maze-Solver.git
2. Navigate to the directory:
Bash
cd RL-Maze-Solver
Run any of the algorithms (e.g., Q-Learning):
Bash
python Q-Learning.py

📈 Results & Observations
Convergence: Q-Learning tended to find the optimal path faster due to its aggressive max-operator updates compared to SARSA's safer exploration path.
Exploration: Implemented an decaying epsilon-greedy strategy to balance exploration (early games) and exploitation (late games).

🔜 Future Work
Implementation of Deep Q-Networks (DQN) to handle continuous state spaces.Applying the agent to more complex environments (e.g., Connect-4).