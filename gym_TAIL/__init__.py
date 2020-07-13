from gym.envs.registration import register

register(
    id='TAIL-v0',
    entry_point='gym_TAIL.envs:TAILEnv'
)