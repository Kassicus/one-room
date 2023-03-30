import pygame

import lib

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption("One Room")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

    def run(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        self.screen.fill(lib.color.BLACK)

    def update(self):
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) * 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()