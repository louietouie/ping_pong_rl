# Setup

All setup is currently in Google doc notes...

## IsaacSim Install
## IsaacLab Install
## conda environment setup



# Getting Started: Scripts

## Before Running Any Script...
1. `conda activate env_isaaclab`
2. `cd ping_pong_rl`
3. `python -m scripts.ping_pong_robot.create_manager`, not `python ./scripts/ping_pong_robot/create_scene.py` (not sure why... something about being run as a module)

## Running Random-Agent Environment via Gymnasium
1. `python -m scripts.ping_pong_robot.create_agent_random --task Isaac-PingPong-v0`

## Hard-coded environment scripts
1. `python -m scripts.ping_pong_robot.create_manager`
2. `python -m scripts.ping_pong_robot.create_rl_manager`
3. `python -m scripts.ping_pong_robot.create_scene`

## Running SKRL-PPO-Agent Environment via Gymnasium
1. `python -m scripts.ping_pong_robot.train_agent_skrl --task Isaac-PingPong-v0`
2. Default algorithm used is PPO... which I believe is an actor/critic policy gradient method. Critic learns value function V(s) to allow for training during a run, rather than vanilla policy gradient or something where a full run needs to be completed to get the actual Q(s,a) for that run and make a gradient step.
3. Other commands
    - `python ./scripts/reinforcement_learning/skrl/train.py --task Isaac-Place-Toy2Box-Agibot-Right-Arm-RmpFlow-v0`

## Listing Registered Gymasium Environments
1. `python -m scripts.ping_pong_robot.list_envs`
2. While some scripts like `create_manager` and `create_rl_manager` hardcode an environment, others can use any registered gymnasium environment passed in via `--task`
3. This script calls `import isaaclab_tasks` which will call it's own `__init__.py` to look for all subpackages and register their environments.
4. The ping pong environment registration must be in the init file... `source/ping_pong_rl/ping_pong_rl/__init__.py` for it to show up as an environment
5. Looking at the structure of the environments in the IsaacLab project (like `source/isaaclab_tasks/isaaclab_tasks/manager_based/classic/cartpole/__init__.py`)... note that these are in the source folder, not the script folder. Only their `random_agent` (analogus to my `create_agent_random` script) script is in the `scripts/` folder, but it is ok to seperate the environments into the `source/` folder because the `import isaaclab_tasks` will find them.



# RL Library

1. I chose [SKRL][1] because it has lots of documentation, IssacLab examples, and both vectorized and distributed training (I don't fully know what these mean yet however... how does Stable Baselines use Pytorch and not have vectorized training... Pytorch's `autograd` must use vectors)
    - *"Vectorized Environments are a method for stacking multiple independent environments into a single environment"*



[1]: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html