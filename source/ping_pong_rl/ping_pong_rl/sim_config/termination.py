from isaaclab.managers import TerminationTermCfg as DoneTerm

from isaaclab.utils import configclass
import isaaclab_tasks.manager_based.classic.cartpole.mdp as mdp

@configclass
class TerminationsCfg:
    """Termination terms for the MDP."""

    # (1) Time out
    # "The episode length is greater than the defined max_episode_length"... where is max_episode_length set?
    time_out = DoneTerm(func=mdp.time_out, time_out=True)
    # (2) Cart out of bounds
    # cart_out_of_bounds = DoneTerm(
    #     func=mdp.joint_pos_out_of_manual_limit,
    #     params={"asset_cfg": SceneEntityCfg("robot", joint_names=["slider_to_cart"]), "bounds": (-3.0, 3.0)},
    # )