############################
# Alien Invasion Game
# Copyright : Naman Sharma
# 
#
import sys 
import pygame
from ai_setting import Settings
from ship import Ship
class AlienInvasion:
    def __init__ (self):
        pygame.init()
        self.ai_setting = Settings()
        self.screen = pygame.display.set_mode((self.ai_setting.screen_width, self.ai_setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.ai_setting.bg_color) 
            self.ship.blitme()     
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
