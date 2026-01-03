import isaaclab.envs.mdp as mdp
from isaaclab.utils import configclass

# @configclass
# class ActionsCfg:
#     """Action specifications for the environment."""

#     joint_efforts = mdp.JointEffortActionCfg(asset_name="robot", joint_names=["slider_to_cart"], scale=5.0)

@configclass
class ActionsCfg:
    """Action specifications for the MDP."""

    # this does not seem to be moving the ping pong robot
    # joint_positions = mdp.JointPositionActionCfg(
    #     # asset name is the variable name of the robot in the InteractiveSceneConfig (uses python reflection)
    #     asset_name="ping_pong", 
    #     joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"],
    #     scale=5.0, 
    #     # use_default_offset=True, 
    #     # debug_vis=True
    # )

    joint_efforts = mdp.JointEffortActionCfg(
        asset_name="ping_pong", 
        joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"],
        scale=5.0, 
    )
