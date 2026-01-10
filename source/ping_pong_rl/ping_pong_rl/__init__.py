import gymnasium as gym

from . import sim_config

gym.register(
    id="Isaac-PingPong-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{sim_config.__name__}.environment_rl:PingPongRLEnvCfg",
        # "env_cfg_entry_point": f"{__name__}.
        # "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        # "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:CartpolePPORunnerCfg",
        # "rsl_rl_with_symmetry_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:CartpolePPORunnerWithSymmetryCfg",
        "skrl_cfg_entry_point": f"{sim_config.__name__}:skrl_ppo_cfg.yaml",
        # "sb3_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
    },
)

# from isaaclab_tasks.utils import import_packages

# # The blacklist is used to prevent importing configs from sub-packages
# _BLACKLIST_PKGS = ["utils", ".mdp"]
# # Import all configs in this package
# import_packages(__name__, _BLACKLIST_PKGS)
