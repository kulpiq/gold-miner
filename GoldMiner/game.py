import pygame
import random
from line import Linka
from gold import Gold
from stone import Stone
from gold2 import Gold2
from gold3 import Gold3
from stone2 import Stone2
from diamond import Diament
from mole import Kret
from molediamond import KretDiament
from cashbag import Cashbag
from lvl import *  


class Gra:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.linka = Linka(self.screen_width // 2, 100)

        self.levels = [Poziom1(self.screen), Poziom2(self.screen)]
        self.current_level_index = 0
        self.current_level = self.levels[self.current_level_index]
        self.money = 0
        self.state = "start"
        self.start_button_rect = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 - 50, 200, 100)
        self.start_background = pygame.image.load("images/start_background.png")
        self.start_background = pygame.transform.scale(self.start_background, (self.screen_width, self.screen_height))

        self.level_start_time = pygame.time.get_ticks()  
        self.level_time_limit = 60 * 1000 
        self.level_timer = 60  

        self.next_level_button_rect = pygame.Rect(self.screen_width - 100, 35, 30, 30)

    def show_start_screen(self):
        self.screen.blit(self.start_background, (0, 0))
        pygame.draw.rect(self.screen, (195, 195, 195), self.start_button_rect)
        font = pygame.font.SysFont(None, 60)
        text = font.render("Start", True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width // 2 - 50, self.screen_height // 2 - 19))
        pygame.display.flip()

    def check_collisions(self):
        self.current_level.check_collisions(self.linka)

    def update_caught_object(self):
        if self.linka.reach_top():
            self.money+=500
            self.linka.caught_object = None
            self.linka.direction_down = True  
            self.linka.moving = False  


    def advance_to_next_level(self):
        self.current_level_index += 1
        if self.current_level_index < len(self.levels):
            self.current_level = self.levels[self.current_level_index]
            self.current_level.setup_objects()
            self.level_start_time = pygame.time.get_ticks()  
            self.level_timer = 60  
            self.show_level_goal_screen()
        else:
            self.show_game_over_screen()

    def show_level_goal_screen(self):      
        pygame.image.load('level_goal_background.png')

    def show_level_goal_screen(self):
        background_image = pygame.image.load("images/level_goal_background.png")
        background_image = pygame.transform.scale(background_image, (self.screen_width, self.screen_height))
        self.screen.blit(background_image, (0, 0))
        font = pygame.font.SysFont(None, 50)
        text = font.render(f"${self.current_level.money_goal}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 100))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)

    def show_game_over_screen(self):
        font = pygame.font.SysFont(None, 60)
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        self.screen.fill((0, 0, 0))  
        text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.flip()

    def update_timer(self):
        elapsed_time = pygame.time.get_ticks() - self.level_start_time
        self.level_timer = max(0, 60 - elapsed_time // 1000)

 
        font = pygame.font.SysFont(None, 40)
        timer_text = font.render(f"{self.level_timer}", True, (255, 255, 255))
        self.screen.blit(timer_text, (self.screen_width - 150, 40))

        if elapsed_time >= self.level_time_limit:
            if self.money >= self.current_level.money_goal:
                self.advance_to_next_level()
            else:
                self.show_game_over_screen()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "start" and self.start_button_rect.collidepoint(event.pos):
                        self.state = "playing"
                    elif self.state == "playing" and self.next_level_button_rect.collidepoint(event.pos):
                        if self.money >= self.current_level.money_goal:
                            self.advance_to_next_level()

                if event.type == pygame.KEYDOWN and self.state == "playing":
                    if event.key == pygame.K_DOWN and not self.linka.moving:
                        self.linka.start_moving()

            if self.state == "start":
                self.show_start_screen()
            elif self.state == "playing":
                self.current_level.draw()  
                self.check_collisions()
                self.update_caught_object()  
                self.linka.update()  
                self.linka.draw(self.screen) 
                self.update_timer()  
                
                pygame.draw.rect(self.screen, (13, 16, 65), self.next_level_button_rect)              

                font = pygame.font.SysFont(None, 26)
                money_text = font.render(f"$: {self.money}", True, (0, 0, 0))
                self.screen.blit(money_text, (20, 25))

                pygame.display.flip()
                self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    gra = Gra()
    gra.run()