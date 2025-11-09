# watch_cartpole.py (Gymnasium API)
import os
import imageio
import gymnasium as gym
from stable_baselines3 import PPO

model_path = "models/ppo_cartpole.zip" if os.path.exists("models/ppo_cartpole.zip") else "models/ppo_cartpole"
model = PPO.load(model_path)

env = gym.make("CartPole-v1", render_mode='rgb_array')
frames = []

obs, info = env.reset()
for _ in range(1000):
    frame = env.render()
    frames.append(frame)
    
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        break

env.close()
os.makedirs("out", exist_ok=True)
imageio.mimsave("out/cartpole_demo.gif", frames, fps=30)
print("Saved out/cartpole_demo.gif")
