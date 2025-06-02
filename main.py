import pygame
import os
import random

class FlappyBirdGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Flappy Bird")

        self.clock = pygame.time.Clock()
        self.running = True

        self.bird_img = pygame.image.load(os.path.join("assets", "yellowbird-downflap.png")).convert_alpha()
        self.background_img = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "background-day.png")).convert(),
            (self.screen_width, self.screen_height))
        self.pipe_img = pygame.image.load(os.path.join("assets", "pipe-green.png")).convert_alpha()
        self.base_img = pygame.image.load(os.path.join("assets", "base.png")).convert()

        self.bird_x = 150
        self.bird_y = 300
        self.gravity = 0
        self.score = 0

        self.pipes = []
        self.pipe_gap = 200
        self.pipe_distance = 300
        self.pipe_speed = 3
        self.font = pygame.font.SysFont(None, 48)

        self.base_speed = 1  # Scroll speed
        self.base_rect = self.base_img.get_rect()


        self.spawn_pipe()

    def spawn_pipe(self):
        height = random.randint(100, 400)
        top_pipe = pygame.transform.flip(self.pipe_img, False, True)
        bottom_pipe = self.pipe_img.copy()
        self.pipes.append({
            'x': self.screen_width,
            'top_y': height - self.pipe_gap // 2 - top_pipe.get_height(),
            'bottom_y': height + self.pipe_gap // 2,
            'top_pipe': top_pipe,
            'bottom_pipe': bottom_pipe,
            'passed': False
        })

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.gravity = -7

    def update(self):
        self.gravity += 0.5
        self.bird_y += self.gravity

        if self.bird_y > self.screen_height - self.base_img.get_height():
            self.running = False

        

        for pipe in self.pipes:
            pipe['x'] -= self.pipe_speed
            # Collision
            bird_rect = self.bird_img.get_rect(center=(self.bird_x, self.bird_y))
            top_rect = pipe['top_pipe'].get_rect(topleft=(pipe['x'], pipe['top_y']))
            bottom_rect = pipe['bottom_pipe'].get_rect(topleft=(pipe['x'], pipe['bottom_y']))

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                self.running = False

            if not pipe['passed'] and pipe['x'] + self.pipe_img.get_width() < self.bird_x:
                pipe['passed'] = True
                self.score += 1

        # Remove offscreen pipes and spawn new
        if self.pipes and self.pipes[0]['x'] < -self.pipe_img.get_width():
            self.pipes.pop(0)
        if not self.pipes or self.pipes[-1]['x'] < self.screen_width - self.pipe_distance:
            self.spawn_pipe()

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))

        for pipe in self.pipes:
            self.screen.blit(pipe['top_pipe'], (pipe['x'], pipe['top_y']))
            self.screen.blit(pipe['bottom_pipe'], (pipe['x'], pipe['bottom_y']))

        self.screen.blit(self.bird_img, self.bird_img.get_rect(center=(self.bird_x, self.bird_y)))
        self.screen.blit(self.base_img, (0, self.screen_height - self.base_img.get_height()))
        self.screen.blit(self.base_img,(self.base_rect.width, self.screen_height - self.base_img.get_height()))
        self.screen.blit(self.base_img,(self.base_rect.width*2, self.screen_height - self.base_img.get_height()))

        score_surface = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(score_surface, (self.screen_width // 2, 50))

        pygame.display.update()

    def run(self):
        while self.running:
            self.control()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = FlappyBirdGame()
    game.run()
