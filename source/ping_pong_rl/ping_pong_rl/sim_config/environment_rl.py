from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass

from source.ping_pong_rl.ping_pong_rl.sim_config.scene import PingPongSceneCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.action import ActionsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.event import EventCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.observation import ObservationsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.reward import RewardsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.termination import TerminationsCfg

@configclass
class PingPongRLEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for the cartpole environment."""

    # Scene settings
    # clone_in_fabric seems to break my URDF (links not connected) and simulation
    # https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.scene.html
    # num_envs is overridden in main by the cli arg
    scene = PingPongSceneCfg(num_envs=1, env_spacing=4.0, clone_in_fabric=False)
    # Basic settings
    observations: ObservationsCfg = ObservationsCfg()
    actions: ActionsCfg = ActionsCfg()
    events: EventCfg = EventCfg()
    # MDP settings
    rewards: RewardsCfg = RewardsCfg()
    terminations: TerminationsCfg = TerminationsCfg()

    # Post initialization
    def __post_init__(self) -> None:
        """Post initialization."""
        # general settings
        self.decimation = 2
        self.episode_length_s = 5
        # viewer settings
        self.viewer.eye = (8.0, 0.0, 5.0)
        # simulation settings
        self.sim.dt = 1 / 120
        self.sim.render_interval = self.decimation