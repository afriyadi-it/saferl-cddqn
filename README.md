# Towards Human-Level Safe Reinforcement Learning in Atari Library Environment

Using [Gym Super Mario Bros](https://pypi.org/project/gym-super-mario-bros/) as the environment 
Using [Stable Baselines](https://github.com/hill-a/stable-baselines), a fork of OpenAI's popular [Baselines](https://github.com/openai/baselines) reinforcement learning library

using the concept of modified reward, as the simplest safety constraint to enforce safety behaviour of the agent.

### Dueling Double DQN
| Notes | GIFs |
| --- | :---: |
| <ins>**Proceed smoothly but violation in the end**</ins> <br> <ul><li>Reward 9999 <li>Violation 8888 <li>Completion rate 99%</ul> |**Iteration: 100k**<br> ![Safe DDQN 1 million iteration](/assets/01.safeddqn-1m.gif) |
| <ins>**Proceed smoothly, but violation in the end **</ins> <br> <ul><li>Reward 9999 <li>Violation 8888 <li>Completion rate 99%</ul> |**Iteration: 100k**<br> ![1-1-v0](/assets/01.safeddqn-1m.gif) |


## Setup
must use Python version < 3.8, preferrably Python-3.7.6
this research is using vscode with virtual environment
```
pip install -r requirements.txt
```
## Training

Training process is started with

```
python train.py
```

## Evaluation

Evaluation process is started with

```
python eval.py
```

# Details

RL algorithms hide a lot of implementation tricks and they are highly sensitive
to parameters change. Often, it is painful to search for an optimal
actor-critic architecture, observation image preprocessing steps, etc.

This section provides information about such tricks that are used to
successfully train an agent to play Super Mario Bros game.