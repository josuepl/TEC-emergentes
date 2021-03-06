from random import choice
from pyknow import *


class Light(Fact):
    """Info about the traffic light."""
    pass


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(L('green')))
    def green_light(self):
        print("Walk")

    @Rule(Light(L('red')))
    def red_light(self):
        print("Don't walk")

    @Rule('light' << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])
