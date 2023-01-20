import pygame


class Sound:
    def __init__(self, game):
        pygame.mixer.init()

        self.game = game
        self.path = "resources/sound/"

        self.shotgun = pygame.mixer.Sound(f"{self.path}/shotgun.wav")
