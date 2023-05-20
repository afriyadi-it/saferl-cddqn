# Towards Human-Level Safe Reinforcement Learning in Atari Library Environment

Using [Gym Super Mario Bros](https://pypi.org/project/gym-super-mario-bros/) as the environment 
Using [Stable Baselines](https://github.com/hill-a/stable-baselines), a fork of OpenAI's popular [Baselines](https://github.com/openai/baselines) reinforcement learning library

using the concept of modified reward, as the simplest safety constraint to enforce safety behaviour of the agent.

### Safe DDQN
| Notes | GIFs |
| --- | :---: |
| <ins>**mostly still fails**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/safeddqn-100k.gif) |
| <ins>**Mario shows hesitation**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/safeddqn-500k.gif) |
| <ins>**proceed smoothly but violation in the end**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/safeddqn-1m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/safeddqn-5m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/safeddqn-10m.gif) |
### DDQN

| Notes | GIFs |
| --- | :---: |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/ddqn-100k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/ddqn-500k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/ddqn-1m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/ddqn-5m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/ddqn-10m.gif) |

### PPO
| Notes | GIFs |
| --- | :---: |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/ppo-100k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/ppo-500k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/ppo-1m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/ppo-5m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 9999 <li>violation 8888 <li>completion rate 99%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/ppo-10m.gif) |


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