# Towards Human-Level Safe Reinforcement Learning in Atari Library Environment

Using [Gym Super Mario Bros](https://pypi.org/project/gym-super-mario-bros/) as the environment 
Using [Stable Baselines](https://github.com/hill-a/stable-baselines), a fork of OpenAI's popular [Baselines](https://github.com/openai/baselines) reinforcement learning library

using the concept of modified reward, as the simplest safety constraint to enforce safety behaviour of the agent.

## Setup
must use Python version < 3.8, preferrably Python-3.7.6
```
this research is using vscode with virtual environment
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Fix stable_baselines3 (if error)
'''
pip install git+https://github.com/carlosluis/stable-baselines3@fix_tests
