import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
from score import Score
from pausemenu import PauseMenu
from powerup import PowerUp
import sys

def main():
    pygame.init()

    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Score.containers = (drawable)
    PowerUp.containers = (drawable, updatable)


    score_font = pygame.font.Font(None, 36)  # create a font object
    score = Score(score_font, 10, 10)  

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    asteroidfield = AsteroidField()
    pause = PauseMenu()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    paused = False
    powerup_menu_shown = False

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        
        if score.getScore() % 10 != 0:
            powerup_menu_shown = False

        if not paused and not powerup_menu_shown and score.getScore() % 10 == 0 and score.getScore() != 0:
            paused = True
            pause.selection = 0
            powerup_menu_shown = True

        elif paused == True:
            pause.draw(screen)
            pause.update(player)
            if pause.selection > 0:
                paused = False
            
        else:
            updatable.update(dt)


            for ast in asteroids:
                for shot in shots:

                    if shot.collides_with(ast) == True:
                        log_event("asteroid_shot")
                        ast.split()
                        shot.kill()
                        score.update(ast.get_radius())
                        log_event("score_updated", score=score.getScore())

                if ast.collides_with(player) == True:
                    log_event("player_hit")
                    print("Game Over!")
                    sys.exit()

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
