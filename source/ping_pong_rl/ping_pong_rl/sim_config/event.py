import isaaclab.envs.mdp as mdp
from isaaclab.managers import EventTermCfg as EventTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass

@configclass
class EventCfg:
    """Configuration for events."""

    # on startup
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
    # reset_robot_position = EventTerm(
    #     func=mdp.reset_joints_by_offset,
    #     mode="reset",
    #     params={
    #         "asset_cfg": SceneEntityCfg("robot", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"]),
    #         "position_range": (-1.0, 1.0),
    #         "velocity_range": (-0.1, 0.1),
    #     },
    # )

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
