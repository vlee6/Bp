import pygame, os
from states.state import State
from states.FishingState import FishingState

class BoatMenu(State):
	def __init__(self, game):
		State.__init__(self, game)
	
	def update(self, delta_time, actions):
		self.actions = actions
		if actions["ANY_KEY_PRESSED"]:
			new_state = FishingState(self.game)
			new_state.enter_state()

	def render(self, display):
		display.fill("purple")
		self.game.draw_text(display, "Get ready to fish!!1!", (0,0,0), self.game.GAME_W/2, 4 * self.game.GAME_H/5)

		pygame.image.load(os.path.join(self.game.assets_dir, "swordfish.png"))