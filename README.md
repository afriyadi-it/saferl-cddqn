# Towards Human-Level Safe Reinforcement Learning in Atari Library Environment

Using [Gym Super Mario Bros](https://pypi.org/project/gym-super-mario-bros/) as the environment 
Using [Stable Baselines](https://github.com/hill-a/stable-baselines), a fork of OpenAI's popular [Baselines](https://github.com/openai/baselines) reinforcement learning library

using the concept of modified reward, as the simplest safety constraint to enforce safety behaviour of the agent.
falling into pit is set as unsafe / catastrophic state
below are the results of experimenting in multiple iterations:

### Safe DDQN
| Notes | GIFs |
| --- | :---: |
| <ins>**mostly still fails**</ins> <br> <ul><li>reward 629.2 <li>violation 20 <li>completion rate 0%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/safeddqn-100k.gif) |
| <ins>**Mario shows hesitation**</ins> <br> <ul><li>reward 1001.7 <li>violation 19 <li>completion rate 0%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/safeddqn-500k.gif) |
| <ins>**proceed smoothly but violation in the end**</ins> <br> <ul><li>reward 921.5 <li>violation 24 <li>completion rate 0%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/safeddqn-1m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 2331 <li>violation 18 <li>completion rate 18%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/safeddqn-5m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 2703.9 <li>violation 2 <li>completion rate 71%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/safeddqn-10m.gif) |

### DDQN

| Notes | GIFs |
| --- | :---: |
| <ins>**can avoid enemies but violate safety**</ins> <br> <ul><li>reward 679.6 <li>violation 24 <li>completion rate 0%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/ddqn-100k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 1151.4 <li>violation 23 <li>completion rate 0%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/ddqn-500k.gif) |
| <ins>**farthest record of the model**</ins> <br> <ul><li>reward 700.2 <li>violation 27 <li>completion rate 0%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/ddqn-1m.gif) |
| <ins>**complete the level but stuck for a while**</ins> <br> <ul><li>reward 2755.5 <li>violation 24 <li>completion rate 47%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/ddqn-5m.gif) |
| <ins>**mostly completed level without problem**</ins> <br> <ul><li>reward 2637.5 <li>violation 18 <li>completion rate 62%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/ddqn-10m.gif) |

### PPO
| Notes | GIFs |
| --- | :---: |
| <ins>**some_description**</ins> <br> <ul><li>reward 295.5 <li>violation 0 <li>completion rate 0%</ul> |**Iteration: 100k**<br> ![alt_text](/assets/ppo-100k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 719.7 <li>violation 23 <li>completion rate 0%</ul> |**Iteration: 500k**<br> ![alt_text](/assets/ppo-500k.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 165.5 <li>violation 0 <li>completion rate 0%</ul> |**Iteration: 1m**<br> ![alt_text](/assets/ppo-1m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 815.3 <li>violation 30 <li>completion rate 0%</ul> |**Iteration: 5m**<br> ![alt_text](/assets/ppo-5m.gif) |
| <ins>**some_description**</ins> <br> <ul><li>reward 858.7 <li>violation 32 <li>completion rate 0%</ul> |**Iteration: 10m**<br> ![alt_text](/assets/ppo-10m.gif) |


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
