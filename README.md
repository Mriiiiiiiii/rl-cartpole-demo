# 🧠 Reinforcement Learning: CartPole PPO Agent

<p align="center">
  <img src="./cartpole_demo.gif" width="400">
</p>

This project demonstrates **Reinforcement Learning for gaming applications** using the classic **CartPole-v1** environment from Gymnasium. A PPO (Proximal Policy Optimization) agent is trained to balance a pole on a moving cart using the Stable-Baselines3 library.

---

## ✅ Features

- Trains a PPO agent on the CartPole game  
- Generates a training performance plot (`training_plot.png`)  
- Produces a gameplay GIF of the trained agent (`cartpole_demo.gif`)  
- Includes training and evaluation scripts (beginner-friendly)  

---

## ✅ Files in This Repository

| File / Folder | Description |
|---------------|-------------|
| `train_cartpole.py` | Trains PPO on CartPole for 20k timesteps |
| `watch_cartpole.py` | Loads the model and records gameplay GIF |
| `training_plot.png` | Plot of evaluation rewards after training |
| `cartpole_demo.gif` | Demonstration of the trained agent |
| `models/ppo_cartpole.zip` | Trained PPO model (optional) |
| `requirements.txt` | Dependencies list |

---

## ✅ About the Environment: CartPole-v1

The **game** involves balancing a pole on a moving cart.

- **State (observations):**
  - Cart position  
  - Cart velocity  
  - Pole angle  
  - Pole angular velocity  
- **Actions:**
  - `0` = Move Left  
  - `1` = Move Right  
- **Reward:** +1 for every timestep the pole stays upright

The episode ends when the pole falls or the cart moves out of bounds.

---

## ✅ Algorithm Used: PPO (Proximal Policy Optimization)

PPO is a stable and efficient policy-gradient RL algorithm commonly used in:

- Game AI  
- Robotics  
- Control systems

The agent learns by interacting with the environment and maximizing expected cumulative reward.

---

## ✅ Installation & Setup

### 1) Create and activate a virtual environment (Windows CMD)
python -m venv .venv
.\.venv\Scripts\activate.bat
> If you use PowerShell, run:
.\.venv\Scripts\Activate.ps1
> 
### 2) Install dependencies
pip install -r requirements.txt

---

## ✅ Training

Run:
python train_cartpole.py
This will:
- Train the agent (default 20k timesteps in the script)  
- Save the model to `models/ppo_cartpole` (Stable-Baselines3 saves model files, e.g. `models/ppo_cartpole.zip`)  
- Produce `training_plot.png`

---

## ✅ Generating the Gameplay GIF

After training, run:
python watch_cartpole.py
This runs the saved model in the environment, records frames, and saves the GIF as:
cartpole_demo.gif
(or `out/cartpole_demo.gif` if your version of the script writes to `out/` — check the script to confirm the exact path)

---

## ✅ Results

- The agent typically learns to balance the pole for **150–200+ steps** after ~20k timesteps.  
- `training_plot.png` shows evaluation returns; `cartpole_demo.gif` demonstrates the trained policy.

---

## ✅ Summary

This repository contains a complete RL pipeline for a simple game environment:
- Environment setup ✅  
- PPO training ✅  
- Model saving ✅  
- Evaluation and plotting ✅  
- Gameplay recording ✅

It’s suitable as a basic demonstrator for RL in gaming and control tasks.

---

## ✅ Author

**Mri**

Feel free to fork, extend, or use this for coursework or demos.

