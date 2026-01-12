# Notes
# "Any entity that has the ENV_REGEX_NS variable in its prim path will be cloned for each environment"

import math
import torch

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, RigidObjectCfg, AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass
from isaaclab.sensors import FrameTransformerCfg
from isaaclab.sensors.frame_transformer.frame_transformer_cfg import OffsetCfg
from isaaclab.markers.config import FRAME_MARKER_CFG 

import source.ping_pong_rl.ping_pong_rl.sim_config.constants as c
from source.ping_pong_rl.ping_pong_rl.sim_config.models import PINGPONG_CFG
# from models import PINGPONG_CFG

@configclass
class PingPongSceneCfg(InteractiveSceneCfg):

    """Configuration for a cart-pole scene."""

    def __post_init__(self):

        self.ground_plane = AssetBaseCfg(prim_path="/World/defaultGroundPlane", spawn=sim_utils.GroundPlaneCfg())

        self.dome_light = AssetBaseCfg(
            prim_path="/World/Light", spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75))
        )

        # I don't think the table and net have to be a rigid object, since it doesn't need to be moved.
        # Using the asset base class "means that the asset will be spawned but cannot be interacted with via the asset class"
        # scripts/tutorials/05_controllers/run_diff_ik.py uses a table as an asset base class
        # Do not add rigid_props or ?mass_props? (so table stays fixed)
        self.table = AssetBaseCfg(
            prim_path="{ENV_REGEX_NS}/Table",
            spawn=sim_utils.CuboidCfg(
                size= [c.TABLE_LENGTH, c.TABLE_WIDTH, c.TABLE_HEIGHT],
                # rigid_props=sim_utils.RigidBodyPropertiesCfg(disable_gravity=True, kinematic_enabled=False),
                # mass_props=sim_utils.MassPropertiesCfg(mass=100.0),
                collision_props=sim_utils.CollisionPropertiesCfg(),
                physics_material=sim_utils.RigidBodyMaterialCfg(
                    static_friction=0.5,
                    restitution=0.9,
                    # When two physics materials with different combine modes collide, the combine mode with the higher priority will be used.
                    restitution_combine_mode="max" 
                ),
                visual_material=sim_utils.PreviewSurfaceCfg(
                    diffuse_color=(5.0/255, 18.0/255, 8.0/255),
                    metallic=0.2,
                    roughness=0.8
                ),
            ),
            init_state=RigidObjectCfg.InitialStateCfg(
                pos=(c.TABLE_LENGTH/2, 0, c.TABLE_HEIGHT_FROM_FLOOR-c.TABLE_HEIGHT/2)
            ),
            collision_group=0, # only collides with objects in same environment, -1 would be with all scene assets
        )

        self.net = AssetBaseCfg(
            prim_path="{ENV_REGEX_NS}/Net",
            spawn=sim_utils.CuboidCfg(
                size= [c.NET_THICKNESS, c.TABLE_WIDTH, c.NET_HEIGHT],
                # rigid_props=sim_utils.RigidBodyPropertiesCfg(disable_gravity=True, kinematic_enabled=False),
                # mass_props=sim_utils.MassPropertiesCfg(mass=100.0),
                collision_props=sim_utils.CollisionPropertiesCfg(),
                visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 1.0, 1.0), metallic=0.0, roughness=0.8),
            ),
            init_state=RigidObjectCfg.InitialStateCfg(
                pos=(c.TABLE_LENGTH/2, 0, c.TABLE_HEIGHT_FROM_FLOOR+c.NET_HEIGHT/2)
            ),
            collision_group=0,
        )

        self.ball = RigidObjectCfg(
            prim_path="{ENV_REGEX_NS}/Ball",
            spawn=sim_utils.SphereCfg(
                radius = .02,
                rigid_props=sim_utils.RigidBodyPropertiesCfg(),
                mass_props=sim_utils.MassPropertiesCfg(
                    mass=c.BALL_MASS,
                ),
                collision_props=sim_utils.CollisionPropertiesCfg(
                    # https://nvidia-omniverse.github.io/PhysX/physx/5.1.2/docs/AdvancedCollisionDetection.html
                    # A larger time step will need the difference to be larger. The drawback of setting it too large is that contacts will be generated sooner as two shapes approach, which drives up the total number of contacts that the simulation has to worry about.
                    contact_offset=0.05,
                    rest_offset=0.0,
                ),
                physics_material=sim_utils.RigidBodyMaterialCfg(
                    static_friction=.05,
                    dynamic_friction=.05,
                    restitution=0.9,
                    # When two physics materials with different combine modes collide, the combine mode with the higher priority will be used.
                    friction_combine_mode="min",
                    restitution_combine_mode="max" 
                ),
                visual_material=sim_utils.PreviewSurfaceCfg(
                    diffuse_color=(1.0, 0.2, 0.0),
                    metallic=0.0,
                    roughness=0.8
                ),
            ),
            init_state=RigidObjectCfg.InitialStateCfg(
                pos=(0,0,0)
            ), # This should be randomized by event configuration
            collision_group=0,
        )
        
        # articulation at environment origin (+X a bit since robot center is on table a few cm)
        # does making this a variable make it part of scene?
        PINGPONG_CFG_UPDATED = PINGPONG_CFG.replace(
            prim_path="{ENV_REGEX_NS}/Robot",
            init_state=PINGPONG_CFG.init_state.replace(pos=(c.ROBOT_INSET, 0, c.TABLE_HEIGHT_FROM_FLOOR)),
        )
        self.ping_pong: ArticulationCfg = PINGPONG_CFG_UPDATED

        marker_cfg = FRAME_MARKER_CFG.copy()
        marker_cfg.markers["frame"].scale = (0.1, 0.1, 0.1)
        marker_cfg.prim_path = "/Visuals/FrameTransformer"
        self.end_effector_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/odrive_base",
            debug_vis=False,
            visualizer_cfg=marker_cfg,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/end_effector",
                    name="end_effector",
                    offset=OffsetCfg(
                        pos=[0.0, 0.0, 0.1034],
                    ),
                ),
            ],
        )

