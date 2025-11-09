from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PAUSE_HEIGHT, PAUSE_WIDTH
from player import Player
from logger import log_event
import pygame
class PauseMenu(pygame.sprite.Sprite):
    
    def __init__(self):
        # if hasattr(self, "containers"):
        #     super().__init__(self.containers)
        # else:
        #     super().__init__()
        self.x = (SCREEN_WIDTH - PAUSE_WIDTH)/2
        self.y = (SCREEN_HEIGHT - PAUSE_HEIGHT)/2
        self.powerups = [
            {"name": "Speed", "rect": pygame.Rect(self.x + 20, self.y + 50, 100, 100)},
            {"name": "Big Shot", "rect": pygame.Rect(self.x + PAUSE_WIDTH - 100 - 20, self.y + 50, 100, 100)}
        ]
        self.selection = 0

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, PAUSE_WIDTH, PAUSE_HEIGHT)
        pygame.draw.rect(screen, "green", rect)
        for powerup in self.powerups:
            pygame.draw.rect(screen, "white", powerup["rect"])
    
    def update(self, player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            player.powerup = "speed"
            self.selection = 1
        elif keys[pygame.K_2]:
            player.powerup = "bigger"
            self.selection = 2



