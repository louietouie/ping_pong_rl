import math
import torch

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, RigidObjectCfg, AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass

from source.ping_pong_rl.ping_pong_rl.sim_config.models import PINGPONG_CFG
# from models import PINGPONG_CFG

# Notes
# "Any entity that has the ENV_REGEX_NS variable in its prim path will be cloned for each environment"

ROBOT_INSET = 0.03
TABLE_HEIGHT_FROM_FLOOR = 0.76
TABLE_LENGTH = 2.74
TABLE_WIDTH = 1.525
TABLE_HEIGHT = 0.02
NET_HEIGHT = 0.1524
NET_THICKNESS = 0.005
BALL_RADIUS = 0.02

@configclass
class PingPongSceneCfg(InteractiveSceneCfg):
    """Configuration for a cart-pole scene."""

    ground_plane = AssetBaseCfg(prim_path="/World/defaultGroundPlane", spawn=sim_utils.GroundPlaneCfg())

    dome_light = AssetBaseCfg(
        prim_path="/World/Light", spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75))
    )

    # I don't think the table and net have to be a rigid object, since it doesn't need to be moved.
    # Using the asset base class "means that the asset will be spawned but cannot be interacted with via the asset class"
    # scripts/tutorials/05_controllers/run_diff_ik.py uses a table as an asset base class
    # Do not add rigid_props or ?mass_props? (so table stays fixed)
    table = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/Table",
        spawn=sim_utils.CuboidCfg(
            size= [TABLE_LENGTH, TABLE_WIDTH, TABLE_HEIGHT],
            collision_props=sim_utils.CollisionPropertiesCfg(),
            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(5.0/255, 18.0/255, 8.0/255), metallic=0.2, roughness=0.8),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(TABLE_LENGTH/2, 0, TABLE_HEIGHT_FROM_FLOOR-TABLE_HEIGHT)),
        collision_group=0, # only collides with objects in same environment, -1 would be with all scene assets
    )

    net = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/Net",
        spawn=sim_utils.CuboidCfg(
            size= [NET_THICKNESS, TABLE_WIDTH, NET_HEIGHT],
            collision_props=sim_utils.CollisionPropertiesCfg(),
            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 1.0, 1.0), metallic=0.0, roughness=0.8),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(TABLE_LENGTH/2, 0, TABLE_HEIGHT_FROM_FLOOR-TABLE_HEIGHT+NET_HEIGHT/2)),
        collision_group=0,
    )

    ball = RigidObjectCfg(
        prim_path="{ENV_REGEX_NS}/Ball",
        spawn=sim_utils.SphereCfg(
            radius = .02,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
            mass_props=sim_utils.MassPropertiesCfg(mass=1.0),
            collision_props=sim_utils.CollisionPropertiesCfg(),
            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 0.2, 0.0), metallic=0.0, roughness=0.8),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(0,0,TABLE_HEIGHT_FROM_FLOOR + 0.4)), # This should be randomized by environment
    )
    
    # articulation at environment origin (+X a bit since robot center is on table a few cm)
    PINGPONG_CFG_UPDATED = PINGPONG_CFG.replace(
        prim_path="{ENV_REGEX_NS}/Robot",
        init_state=PINGPONG_CFG.init_state.replace(pos=(ROBOT_INSET, 0, TABLE_HEIGHT_FROM_FLOOR)),
    )
    ping_pong: ArticulationCfg = PINGPONG_CFG_UPDATED

