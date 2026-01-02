import math
import torch

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass

from scripts.ping_pong_robot.sim_config.models import PINGPONG_CFG
# from models import PINGPONG_CFG

@configclass
class PingPongSceneCfg(InteractiveSceneCfg):
    """Configuration for a cart-pole scene."""

    # ground plane
    ground = AssetBaseCfg(prim_path="/World/defaultGroundPlane", spawn=sim_utils.GroundPlaneCfg())

    # lights
    dome_light = AssetBaseCfg(
        prim_path="/World/Light", spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75))
    )

    # articulation
    # "Any entity that has the ENV_REGEX_NS variable in its prim path will be cloned for each environment"
    ping_pong: ArticulationCfg = PINGPONG_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
