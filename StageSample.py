from Stage import Stage
from ActorTest import ActorTest

class StageSample(Stage):

    def __init__(self, screen):
        super().__init__(screen)

        button1 = ActorTest()
        self.add_actor(button1)

