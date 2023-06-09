from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from stable_baselines import DQN
from stable_baselines.bench import Monitor
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.deepq.policies import MlpPolicy, CnnPolicy, LnCnnPolicy
from stable_baselines.common.atari_wrappers import FrameStack, WarpFrame, MaxAndSkipEnv, EpisodicLifeEnv
from stable_baselines.common.callbacks import CallbackList, EvalCallback, CheckpointCallback
from callbacks import ProgressBarManager
import tensorflow as tf
import cv2
import os
import argparse

import hyperparams as hp

# Suppress warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def test_env(env, frame_by_frame=False):
    obs = env.reset()
    while True:
        obs, rewards, dones, info = env.step(env.action_space.sample())
        print(obs._frames)
        if (frame_by_frame):
            cv2.imshow("frames", obs._frames[0])
            cv2.waitKey()
        else:
            env.render()
        print("reward:", rewards)
        print("timestep:", info['timestep'])

def run(run_name, existing_model):

    # Create log dir
    log_dir = "./monitor_logs/"
    os.makedirs(log_dir, exist_ok=True)

    print ("Setting up environment...")
    env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    env = EpisodicLifeEnv(env)

    # Preprocessing
    env = WarpFrame(env)
    env = FrameStack(env, n_frames=hp.FRAME_STACK)

    # Evaluate every kth frame and repeat action
    env = MaxAndSkipEnv(env, skip=hp.FRAME_SKIP)

    # Logs will be saved in log_dir/monitor.csv
    env = Monitor(env, log_dir)

    # Save a checkpoint every 1000 steps
    checkpoint_callback = CheckpointCallback(save_freq=100000, save_path='./models/',
                                            name_prefix=run_name)

    eval_callback = EvalCallback(env,
                                best_model_save_path='./models/',
                                log_path='./models/',
                                eval_freq=2500000,
                                deterministic=True,
                                render=False)

    print("Compiling model...")

    if existing_model:
        try:
            model = DQN.load(existing_model, env, tensorboard_log="./mario_tensorboard/")
        except:
            print(f"{existing_model} does not exist!")
            exit(0)
    else:
        model = DQN(LnCnnPolicy,
                    env,
                    batch_size=hp.BATCH_SIZE, # Optimizable (higher batch sizes ok according to https://arxiv.org/pdf/1803.02811.pdf)
                    verbose=1, 
                    learning_starts=10000,
                    learning_rate=hp.LEARNING_RATE,
                    exploration_fraction=hp.EXPLORATION_FRACT,
                    exploration_initial_eps=1.0,
                    exploration_final_eps=0.1,
                    prioritized_replay=True, 
                    prioritized_replay_alpha=hp.P_REPLAY_ALPHA,
                    train_freq=hp.TRAINING_FREQ,
                    target_network_update_freq=hp.TARGET_UPDATE_FREQ,
                    tensorboard_log="./mario_tensorboard/"
                )

    print("Training starting...")
    with ProgressBarManager(hp.TIME_STEPS) as progress_callback:
        model.learn(total_timesteps=hp.TIME_STEPS,
                    log_interval=1,
                    callback=[progress_callback, checkpoint_callback, eval_callback],
                    tb_log_name=run_name)

    print("Done! Saving model...")
    model.save("models/{}_final".format(run_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-existing", nargs='?', help="Train existing model")
    args = parser.parse_args()

    run("dqn", args.train_existing)
