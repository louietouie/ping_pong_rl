from isaaclab.managers import RewardTermCfg as RewTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass

import isaaclab_tasks.manager_based.classic.cartpole.mdp as mdp

"""
Ping Pong Brainstorm

Rewards for robot
Penalize all joint velocities
    Penalize joint accelerations
    I would rather have the arm move back to the center between hits slowly rather than quickly... but penalizing something like distance traveled would penalize these the same, regardless of if it did it slow or fast
Penalize joint limits (or terminate if past joint limit, and penalize termination)

Reward ping pong ball landing on other side of table on first bounce
    Reward contact with ping pong ball
    Reward paddle close to ball
    Reward ball contact that moves it in the correct direction
"""

@configclass
class RewardsCfg:
    """Reward terms for the MDP."""

    # (1) Constant running reward
    alive = RewTerm(func=mdp.is_alive, weight=1.0)
    # (2) Failure penalty
    terminating = RewTerm(func=mdp.is_terminated, weight=-2.0)
    # (3) Primary task: keep pole upright

    # Temporary placeholder reward that makes the robot want to put all joints at position 1.0
    pole_pos = RewTerm(
        func=mdp.joint_pos_target_l2,
        weight=-1.0,
        params={"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"]), "target": 1.0},
    )
    # # (4) Shaping tasks: lower cart velocity
    # cart_vel = RewTerm(
    #     func=mdp.joint_vel_l1,
    #     weight=-0.01,
    #     params={"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["slider_to_cart"])},
    # )
    # # (5) Shaping tasks: lower pole angular velocity
    # pole_vel = RewTerm(
    #     func=mdp.joint_vel_l1,
    #     weight=-0.005,
    #     params={"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["cart_to_pole"])},
    # )