import pygame
import math

from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False

    def single_fire_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloding:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloding = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        """ -- controle do ângulo usado teclas --
        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        """

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pygame.draw.line(self.game.screen, YELLOW, (self.x * 100, self.y * 100),
                         (self.x * 100 + WIDTH * math.cos(self.angle),
                         self.y * 100 + WIDTH * math.sin(self.angle)), 2)

        pygame.draw.circle(self.game.screen, GREEN, (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSIVTY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
