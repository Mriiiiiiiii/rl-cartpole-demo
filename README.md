\# RL CartPole Demo (PPO + Stable-Baselines3 + Gymnasium)



Trains a PPO agent to balance CartPole. Produces a trained model, a simple evaluation plot, and a GIF demo.



Run:

1\) .\\.venv\\Scripts\\activate.bat

2\) pip install -r requirements.txt

3\) python train\_cartpole.py

4\) python watch\_cartpole.py



Outputs:

\- models/ppo\_cartpole.zip

\- training\_plot.png

\- out/cartpole\_demo.gif



Notes:

PPO learns a policy mapping observations (cart position/velocity, pole angle/angular velocity) to actions (left/right) to maximize cumulative reward (keep pole upright).



