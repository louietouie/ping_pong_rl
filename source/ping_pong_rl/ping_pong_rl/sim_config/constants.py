ROBOT_INSET = 0.03
TABLE_HEIGHT_FROM_FLOOR = 0.76
TABLE_LENGTH = 2.74
TABLE_WIDTH = 1.525
TABLE_HEIGHT = TABLE_HEIGHT_FROM_FLOOR # 0.02 # thicker to prevent phasing?
NET_HEIGHT = 0.1524
NET_THICKNESS = 0.005
BALL_RADIUS = 0.02
BALL_MASS = 0.0027

SIM_TIME_STEP = 1 / 60 # Time steps that are too long can lead to instabilities, especially with fast-moving objects
DECIMATION = 1 # Number of control action updates @ sim dt per policy dt.