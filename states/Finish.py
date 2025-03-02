from states.state import State
# from states.BoatMenu import BoatMenu
import pygame, os

class Finish(State):
	def __init__(self, game, caught):
		State.__init__(self, game)
		self.actions = []
		self.caught = caught

	def update(self, delta_time, actions):
		self.actions = actions
		# if actions["REEL_UP"]:
		# 	new_state = BoatMenu(self.game)
		# 	new_state.enter_state()
		self.game.reset_keys()

	def render(self, display):
		display.fill((255,255,255))
		if (len(self.caught) == 0):
			self.game.draw_text(display, "You caught no fish! U kinda suck...", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)
		else:
			self.game.draw_text(display, "You caught:" + ','.join(self.caught), (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)

		self.image = pygame.image.load(os.path.join(self.game.assets_dir, "HE_CAUGHT_IT.png"))
		display.blit(self.image, (self.game.GAME_W/2, self.game.GAME_H/2))


	def load_sprites(self):
		self.sprite_dir = os.path.join(self.game.sprite_dir, "player")