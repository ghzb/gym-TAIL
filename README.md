# Gym TAIL

## How to use
1. Download repo
1. Place folder where needed
1. Replace gym_TAIL/envs/TAIL_env.py with your own.
1. In another project run `pip install -e /path/to/gym-TAIL`
1. Import package
1. Use environment

## Known issue
- Sockets use a "busy wait". The current thread maxes out CPU usage and may cause other problems as a result. This article appears to have a solution. https://pymotw.com/2/select/

## Example usage
```python
import gym
import gym_TAIL

env = gym.make('TAIL-v0')
```