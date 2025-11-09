import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, font, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.font = font
        self.position = pygame.Vector2(x, y)
    
    def getScore(self):
        return self.score
        
    def draw(self, screen):
        text_surface = self.font.render(str(self.score), True, (255, 255, 255))
        rect = text_surface.get_rect(topleft=self.position)
        screen.blit(text_surface, rect)

    def update(self, radius):
        if radius == 60:
            self.score += 1
        elif radius == 40:
            self.score += 2
        else:
            self.score += 3
