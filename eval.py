from nes_py.wrappers import JoypadSpace
from stable_baselines.deepq.policies import MlpPolicy, CnnPolicy
import gym_super_mario_bros
from gym.wrappers import Monitor
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT, RIGHT_ONLY, COMPLEX_MOVEMENT
from stable_baselines import DQN
from stable_baselines.common.evaluation import evaluate_policy
from stable_baselines.common.atari_wrappers import FrameStack, WarpFrame, MaxAndSkipEnv, EpisodicLifeEnv
import tensorflow as tf
# Suppress warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import datetime
from datetime import datetime
import hyperparams as hp

nowstring = datetime.strftime(datetime.now(),"%d%m%Y%H%M%S")

env = Monitor(gym_super_mario_bros.make('SuperMarioBros-1-1-v0'), './videos/video'+nowstring, force=True)
env = JoypadSpace(env, SIMPLE_MOVEMENT)
env = EpisodicLifeEnv(env)
env = WarpFrame(env)
env = FrameStack(env, n_frames=hp.FRAME_STACK)
env = MaxAndSkipEnv(env, skip=hp.FRAME_SKIP)

# model = DQN.load("_fixed_models/dqn_500k_steps")
model = DQN.load("models/dqn_10000000_steps")

obs = env.reset()

# cr = 0
# while True:
#     action, _states = model.predict(obs, deterministic=False)
#     obs, rewards, done, info = env.step(action)
#     env.step(action)
#     cr += rewards
#     print("Reward: {}\t\t".format(cr), end='\r')
#     env.render()
#     if (done):
#         print("Finished an episode with total reward: ", cr)
#         cr = 0
#         break

print(evaluate_policy(model, env, n_eval_episodes=100, deterministic=False, render=False))

print("Done.")
