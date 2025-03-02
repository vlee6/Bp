from states.state import State
from states.BoatMenu import BoatMenu
import pygame, os

class Title(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.actions = []

	def update(self, delta_time, actions):
		self.actions = actions
		if actions["ANY_KEY_PRESSED"]:
			new_state = BoatMenu(self.game)
			new_state.enter_state()
		self.game.reset_keys()

	def render(self, display):
		display.fill((255,255,255))
		self.image = pygame.image.load(os.path.join(self.game.assets_dir, "cat_reelin.png"))
		display.blit(self.image, (self.game.GAME_W/4, self.game.GAME_H/8))
		self.game.draw_text(display, "CAT FISHING GAME", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)