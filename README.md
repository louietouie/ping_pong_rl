1. `conda activate env_isaaclab`
2. Not `python ./scripts/ping_pong_robot/create_scene.py`
3. Yes
    - `cd ping_pong_rl`
    - `python -m scripts.ping_pong_robot.create_manager`

Running Random-Agent Environment via Gymnasium
1. `python -m scripts.ping_pong_robot.create_agent_random --task Isaac-PingPong-v0`
    - Unlike `create_manager` and `create_rl_manager`, this script does not hardcode an environment. It can use any registered gymnasium environment.
    - This script calls `import isaaclab_tasks` which will call it's own `__init__.py` to look for all subpackages and register their environments.
    - The ping pong environment registration must be in the init file... `/home/louis/Documents/isaac_projects/ping_pong_rl/scripts/ping_pong_robot/__init__.py` for it to show up as an environment
    - `python -m scripts.ping_pong_robot.list_envs`
    - Looking at the structure of the environments in the IsaacLab project (like `source/isaaclab_tasks/isaaclab_tasks/manager_based/classic/cartpole/__init__.py`)... note that these are in the source folder, not scripts... I may want to move mine eventually. Only their `random_agent` (analogus to my `create_agent_random` script) script is in the `scripts/` folder, but it is ok to seperate the environments into the `source/` folder because I believe the `import isaaclab_tasks` will find them.

Running SKRL-PPO-Agent Environment via Gymnasium
1. I chose [SKRL][1] because it has lots of documentation, IssacLab examples, and both vectorized and distributed training (I don't fully know what these mean yet however... how does Stable Baselines use Pytorch and not have vectorized training... Pytorch's `autograd` must use vectors)
    - *"Vectorized Environments are a method for stacking multiple independent environments into a single environment"*



[1]: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html