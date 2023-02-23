import gym
from gym import spaces


class customEnv(gym.Env):
    # custom environment that follows gym interface
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(customEnv, self).__init__()

        # declare type and shape of action space
        self.action_space = spaces.Discrete(5)

    # def stop(self):

