# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

# https://isaac-sim.github.io/IsaacLab/main/source/tutorials/01_assets/add_new_robot.html

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

##
# Configuration
##

USD_MODEL_PATH = "models/ping_pong_arm/ping_pong_arm.usd"
URDF_MODEL_PATH = "models/ping_pong_arm_from_xacro.urdf"

PINGPONG_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=True,
        merge_fixed_joints=False,
        make_instanceable=False,
        asset_path=URDF_MODEL_PATH,
        activate_contact_sensors=True,
        # How the robot behaves as a physical object in the simulation
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
        ),
        # How the solver steps the robot's joints through time
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=None, damping=None)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.0),
        joint_pos={
            "shoulder": 0.0,
            "elbow": 0.0,
            "wrist_orbit": 0.0,
            "wrist_spin": 0.0
        }
    ),
    actuators={
        "shoulder_actuator": ImplicitActuatorCfg(
            joint_names_expr=["shoulder"],
            effort_limit_sim=400.0,
            stiffness=0.0,
            damping=10.0,
        ),
        "elbow_actuator": ImplicitActuatorCfg(
            joint_names_expr=["elbow"],
            effort_limit_sim=400.0,
            stiffness=0.0,
            damping=0.0
        ),
        "wrist_orbit_actuator": ImplicitActuatorCfg(
            joint_names_expr=["wrist_orbit"],
            effort_limit_sim=400.0,
            stiffness=0.0,
            damping=0.0
        ),
        "wrist_spin_actuator": ImplicitActuatorCfg(
            joint_names_expr=["wrist_spin"],
            effort_limit_sim=400.0,
            stiffness=0.0,
            damping=0.0
        ),
    },
)

# PINGPONG_CFG = ArticulationCfg(
#     spawn=sim_utils.UsdFileCfg(
#         usd_path=USD_MODEL_PATH,
#         # How the robot behaves as a physical object in the simulation
#         rigid_props=sim_utils.RigidBodyPropertiesCfg(
#             rigid_body_enabled=True,
#             max_linear_velocity=1000.0,
#             max_angular_velocity=1000.0,
#             max_depenetration_velocity=100.0,
#             enable_gyroscopic_forces=True,
#         ),
#         # How the solver steps the robot's joints through time
#         articulation_props=sim_utils.ArticulationRootPropertiesCfg(
#             enabled_self_collisions=False,
#             solver_position_iteration_count=4,
#             solver_velocity_iteration_count=0,
#             sleep_threshold=0.005,
#             stabilization_threshold=0.001,
#         ),
#     ),
#     init_state=ArticulationCfg.InitialStateCfg(
#         pos=(0.0, 0.0, 0.0),
#         joint_pos={
#             "shoulder": 0.0,
#             "elbow": 0.0,
#             "wrist_orbit": 0.0,
#             "wrist_spin": 0.0
#         }
#     ),
#     actuators={
#         "shoulder_actuator": ImplicitActuatorCfg(
#             joint_names_expr=["shoulder"],
#             effort_limit_sim=400.0,
#             stiffness=0.0,
#             damping=10.0,
#         ),
#         "elbow_actuator": ImplicitActuatorCfg(
#             joint_names_expr=["elbow"],
#             effort_limit_sim=400.0,
#             stiffness=0.0,
#             damping=0.0
#         ),
#         "wrist_orbit_actuator": ImplicitActuatorCfg(
#             joint_names_expr=["wrist_orbit"],
#             effort_limit_sim=400.0,
#             stiffness=0.0,
#             damping=0.0
#         ),
#         "wrist_spin_actuator": ImplicitActuatorCfg(
#             joint_names_expr=["wrist_spin"],
#             effort_limit_sim=400.0,
#             stiffness=0.0,
#             damping=0.0
#         ),
#     },
# )