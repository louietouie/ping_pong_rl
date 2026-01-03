1. `conda activate env_isaaclab`
2. Not `python ./scripts/ping_pong_robot/create_scene.py`
3. Yes
    - `cd ping_pong_rl`
    - `python -m scripts.ping_pong_robot.create_manager`

Running via Gymnasium
1. `python -m scripts.ping_pong_robot.register_rl_manager --task Isaac-PingPong-v0`
    - This script calls `import isaaclab_tasks` which will call it's own `__init__.py` to look for all subpackages and register their environments.
    - The ping pong environment registration must be in the init file... `/home/louis/Documents/isaac_projects/ping_pong_rl/scripts/ping_pong_robot/__init__.py` for it to show up as an environment
    - `python -m scripts.ping_pong_robot.list_envs`
    - Looking at the structure of the environments in the IsaacLab project (like `source/isaaclab_tasks/isaaclab_tasks/manager_based/classic/cartpole/__init__.py`)... note that these are in the source folder, not scripts... I may want to move mine eventually. Only their `random_agent` (analogus to my `register_rl_manager` script) script is in the `scripts/` folder, but it is ok to seperate the environments into the `source/` folder because I believe the `import isaaclab_tasks` will find them.