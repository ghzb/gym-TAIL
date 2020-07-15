from gym.envs.registration import register
from gym_TAIL.SocketRegister import SocketRegister

register(
    id='TAIL-v0',
    entry_point='gym_TAIL.envs:TAILEnv',
    kwargs={'discrete_actions': True}
)