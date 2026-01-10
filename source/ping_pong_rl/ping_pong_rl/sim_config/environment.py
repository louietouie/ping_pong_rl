from isaaclab.envs import ManagerBasedEnvCfg
from isaaclab.utils import configclass

from source.ping_pong_rl.ping_pong_rl.sim_config.scene import PingPongSceneCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.action import ActionsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.event import EventCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.observation import ObservationsCfg

@configclass
class PingPongEnvCfg(ManagerBasedEnvCfg):
    """Configuration for the pingpong environment."""

    # Scene settings
    scene = PingPongSceneCfg(num_envs=2, env_spacing=2.5)
    # Basic settings
    observations = ObservationsCfg()
    actions = ActionsCfg()
    events = EventCfg()

    def __post_init__(self):
        """Post initialization."""
        # viewer settings
        self.viewer.eye = [4.5, 0.0, 6.0]
        self.viewer.lookat = [0.0, 0.0, 2.0]
        # step settings
        self.decimation = 4  # env step every 4 sim steps: 200Hz / 4 = 50Hz
        # simulation settings
        self.sim.dt = 0.005  # sim step every 5ms: 200Hz