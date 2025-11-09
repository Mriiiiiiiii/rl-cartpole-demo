# train_cartpole.py (Gymnasium API)
import os
import matplotlib.pyplot as plt
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")  # Gymnasium env
model = PPO("MlpPolicy", env, verbose=1)

os.makedirs("models", exist_ok=True)
TIMESTEPS = 20000  # safe for 1-day deadline, fast
print(f"Training for {TIMESTEPS} timesteps...")

model.learn(total_timesteps=TIMESTEPS)
model.save("models/ppo_cartpole")
print("Model saved.")

# Quick evaluation + plot
def evaluate(model, env, episodes=10):
    results = []
    for _ in range(episodes):
        obs, info = env.reset()
        terminated = False
        truncated = False
        total = 0
        while not (terminated or truncated):
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            total += reward
        results.append(total)
    return results

rets = evaluate(model, env, 10)
plt.plot(rets, marker='o')
plt.title("CartPole - PPO Evaluation")
plt.xlabel("Episode")
plt.ylabel("Return")
plt.tight_layout()
plt.savefig("training_plot.png")
print("Saved training_plot.png")
