# https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.envs.html#isaaclab.envs.ManagerBasedRLEnvCfg

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass
from isaaclab.sim import PhysxCfg, SimulationCfg

from source.ping_pong_rl.ping_pong_rl.sim_config.scene import PingPongSceneCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.action import ActionsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.event import EventCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.observation import ObservationsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.reward import RewardsCfg
from source.ping_pong_rl.ping_pong_rl.sim_config.termination import TerminationsCfg
import source.ping_pong_rl.ping_pong_rl.sim_config.constants as c

@configclass
class PingPongRLEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for the cartpole environment."""

    # Scene settings
    # clone_in_fabric seems to break my URDF (links not connected) and simulation
    # https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.scene.html
    # num_envs is overridden in main by the cli arg
    scene = PingPongSceneCfg(num_envs=7, env_spacing=5.0, clone_in_fabric=False)
    # Basic settings
    observations: ObservationsCfg = ObservationsCfg()
    actions: ActionsCfg = ActionsCfg()
    events: EventCfg = EventCfg()
    # MDP settings
    rewards: RewardsCfg = RewardsCfg()
    terminations: TerminationsCfg = TerminationsCfg()

    # time step is handled below
    # sim = SimulationCfg(
    #     # dt=1 / 200,
    #     # device=args_cli.device,
    #     physx=PhysxCfg(
    #         enable_ccd=True
    #     )
    # )  

    # Post initialization
    def __post_init__(self) -> None:
        """Post initialization."""
        # general settings
        self.decimation = c.DECIMATION
        self.episode_length_s = 5
        # viewer settings
        self.viewer.eye = (8.0, 0.0, 5.0)
        # simulation settings
        self.sim.dt = c.SIM_TIME_STEP 
        self.sim.render_interval = self.decimation
        # Enable CCD to avoid tunneling
        self.sim.physx.enable_ccd = True # "CCD is not supported on GPU, ignoring request to enable it"
        # The `enable_external_forces_every_iteration` parameter in the PhysxCfg is set to False. If you are experiencing noisy velocities, consider enabling this flag. You may need to slightly increase the number of velocity iterations (setting it to 1 or 2 rather than 0), together with this flag, to improve the accuracy of velocity updates.
        self.sim.physx.enable_external_forces_every_iteration = True
        self.sim.physx.solver_type = 0
        # self.sim.device="cpu"