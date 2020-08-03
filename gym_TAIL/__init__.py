from gym.envs.registration import register
from gym_TAIL.SocketRegister import SocketRegister
from gym_TAIL.envs.TAIL_env import debug



register(
    id='TAIL-v0',
    entry_point='gym_TAIL.envs:TAILEnv',
)

register(
    id='TAIL-v1',
    entry_point='gym_TAIL.envs:TAILEnv',
    kwargs={'discrete_actions': True}
)

register(
    id='TAIL-v2',
    entry_point='gym_TAIL.envs:TAILEnv',
    kwargs={'discrete_states': True}
)

register(
    id='TAIL-v3',
    entry_point='gym_TAIL.envs:TAILEnv',
    kwargs={'discrete_actions': True, 'discrete_states': True}
)