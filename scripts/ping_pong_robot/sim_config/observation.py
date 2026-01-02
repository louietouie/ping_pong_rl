import isaaclab.envs.mdp as mdp
from isaaclab.managers import ObservationGroupCfg as ObsGroup
from isaaclab.managers import ObservationTermCfg as ObsTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass

@configclass
class ObservationsCfg:
    """Observation specifications for the environment."""

    # the measurements to take from our environment
    # joint positions and velocities
    # ball position?
    # ball velocity?

    @configclass
    class PolicyCfg(ObsGroup):
        """Observations for policy group."""

        # observation terms (order preserved)
        # https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.envs.mdp.html#isaaclab.envs.mdp.observations.joint_pos_rel
        joint_pos_rel = ObsTerm(
            func=mdp.joint_pos_rel,
            
            params = {"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"])}
        )
        joint_vel_rel = ObsTerm(
            func=mdp.joint_vel_rel,
            params = {"asset_cfg": SceneEntityCfg("ping_pong", joint_names=["shoulder", "elbow", "wrist_spin", "wrist_orbit"])}
        )

        def __post_init__(self) -> None:
            self.enable_corruption = False
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()