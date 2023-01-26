import pygame
import sys

from settings import *
from sound import *
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectReender
from sprite_object import SpriteObject, AnimatedSprite
from object_handler import ObjectHandler
from weapon import Weapon


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pygame.USEREVENT
        pygame.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectReender(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)

        """
        self.static_sprite = SpriteObject(self)
        self.animated_sprite = AnimatedSprite(self)
        """

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()

        """
        self.static_sprite.update()
        self.animated_sprite.update()
        """

        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f"{self.clock.get_fps():.1f}")

    def draw(self):
        self.object_render.draw()
        self.weapon.draw()

        #self.screen.fill(BLACK)
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True

            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()

