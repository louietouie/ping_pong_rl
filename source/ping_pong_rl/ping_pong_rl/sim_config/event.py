# https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.managers.html#isaaclab.managers.EventManager

import isaaclab.envs.mdp as mdp
from isaaclab.managers import EventTermCfg as EventTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass

import source.ping_pong_rl.ping_pong_rl.sim_config.constants as c

@configclass
class EventCfg:
    """Configuration for events."""

    # on startup (camera position?)
    # add_pole_mass = EventTerm(
    #     func=mdp.randomize_rigid_body_mass,
    #     mode="startup",
    #     params={
    #         "asset_cfg": SceneEntityCfg("robot", body_names=["pole"]),
    #         "mass_distribution_params": (0.1, 0.5),
    #         "operation": "add",
    #     },
    # )

    # on reset
    reset_ball_state = EventTerm(
        func=mdp.reset_root_state_uniform,
        mode="reset",
        params={
            "asset_cfg": SceneEntityCfg("ball"),
            "pose_range": {
                # I believe this pose is relative to the pose in scene.py
                "x": (c.TABLE_LENGTH, c.TABLE_LENGTH - .2),
                "y": (-c.TABLE_WIDTH/3, c.TABLE_WIDTH/3),
                "z": (c.TABLE_HEIGHT_FROM_FLOOR + 0.05, c.TABLE_HEIGHT_FROM_FLOOR + 0.1)
                # "yaw": (-3.14, 3.14),
            }, 
            "velocity_range": {
                "x": (-2.5, -3.5),
                "y": (-0.3, 0.3),
                "z": (3.5, 4.5),
            },
        }
    )


    # https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.envs.mdp.html#isaaclab.envs.mdp.events.reset_joints_by_scale
    # resets the robot joints by scaling the default position and velocity by the given ranges
    reset_robot_joints = EventTerm(
        func=mdp.reset_joints_by_scale,
        mode="reset",
        params={
            "asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"]),
            "position_range": (0.75, 1.25),
            "velocity_range": (0.0, 0.0),
        },
    )
