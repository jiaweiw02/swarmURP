
from __future__ import unicode_literals

import gym
import Gridworld

#to make the environment 
environment = gym.make('Grid-v0')
while environment.verbose:
	start_ = environment.reset()
    - = environment.step(env.action_space.sample())


