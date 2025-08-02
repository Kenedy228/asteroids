import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("Arial", 24)
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                running = False

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    player.score += asteroid.split()
                    shot.kill()

        text_surface = font.render(f"SCORE: {player.score}", True, "white")
        text_rect = text_surface.get_rect()
        text_rect.topright = (SCREEN_WIDTH, 0)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        dt = clock.tick(120) / 1000
        player.update(dt)


if __name__ == "__main__":
    main()
