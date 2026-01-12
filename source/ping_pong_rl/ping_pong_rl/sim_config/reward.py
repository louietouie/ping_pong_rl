# Rewards for robot
# Penalize all joint velocities
#     Penalize joint accelerations
#     I would rather have the arm move back to the center between hits slowly rather than quickly... but penalizing something like distance traveled would penalize these the same, regardless of if it did it slow or fast
# Penalize joint limits (or terminate if past joint limit, and penalize termination)

# Reward ping pong ball landing on other side of table on first bounce
#     Reward contact with ping pong ball
#     Reward paddle close to ball
#     Reward ball contact that moves it in the correct direction

import torch

from isaaclab.managers import RewardTermCfg as RewTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.assets import RigidObject
from isaaclab.sensors import FrameTransformer
from isaaclab.envs import ManagerBasedRLEnv

import isaaclab_tasks.manager_based.classic.cartpole.mdp as mdp


def object_ee_distance(
    env: ManagerBasedRLEnv,
    std: float,
    ball_cfg: SceneEntityCfg = SceneEntityCfg("ball"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("end_effector_frame"),
) -> torch.Tensor:
    """Reward the agent for reaching the object using tanh-kernel."""
    # extract the used quantities (to enable type-hinting)
    ball: RigidObject = env.scene[ball_cfg.name]
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # Target object position: (num_envs, 3)
    ball_pos_w = ball.data.root_pos_w
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    # Distance of the end-effector to the object: (num_envs,)
    object_ee_distance = torch.norm(ball_pos_w - ee_w, dim=1)

    return 1 - torch.tanh(object_ee_distance / std)

@configclass
class RewardsCfg:
    """Reward terms for the MDP."""

    # (1) Constant running reward
    # alive = RewTerm(func=mdp.is_alive, weight=1.0)
    # (2) Failure penalty
    # terminating = RewTerm(func=mdp.is_terminated, weight=-2.0)

    paddle_reach_ball = RewTerm(
        func=object_ee_distance,
        params={"std": 0.1},
        weight=1.0
    )

    robot_vel = RewTerm(
        func=mdp.joint_vel_l1,
        weight=-0.01,
        params={"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"])},
    )

    # Temporary placeholder reward that makes the robot want to put all joints at position 1.0
    # pole_pos = RewTerm(
    #     func=mdp.joint_pos_target_l2,
    #     weight=-1.0,
    #     params={"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"]), "target": 0.5},
    # )

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