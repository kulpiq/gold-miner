import pygame
from gold import Gold
from gold2 import Gold2
from gold3 import Gold3
from stone import Stone
from stone2 import Stone2
from mole import Kret
from molediamond import KretDiament
from diamond import Diament
from cashbag import Cashbag


class Poziom:
    def __init__(self, level_number, money_goal, screen):
        self.level_number = level_number
        self.money_goal = money_goal
        self.screen = screen
        self.objects = []
        self.background_image = pygame.image.load('images/lvl_background.png')

    def setup_objects(self):
        raise NotImplementedError("Subklasy powinny implementować tę metodę.")

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        for obj in self.objects:
            if not obj.caught:
                obj.draw(self.screen)

    def check_collisions(self, linka):
        for obj in self.objects:
            if not obj.caught and linka.check_collision(obj):
                linka.caught_object = obj
                obj.caught = True

    def update_objects(self):
        pass

class Poziom1(Poziom):
    def __init__(self, screen):
        super().__init__(level_number=1, money_goal=1000, screen=screen)
        self.setup_objects()

    def setup_objects(self):
        self.objects = [
            Gold(100, 470),
            Gold2(120, 400),
            Gold2(180, 430),
            Cashbag(500, 460)
            
        ]

    

class Poziom2(Poziom):
    def __init__(self, screen):
        super().__init__(level_number=2, money_goal=2500, screen=screen)
        self.setup_objects()

    def setup_objects(self):
        self.objects = [
            Gold(100, 450),
            Gold2(200, 350),
            Stone2(300, 450),
            Kret(100, 300)

        ]