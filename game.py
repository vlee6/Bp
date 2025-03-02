import os, time, pygame
from states.title import Title

class Game():
	def __init__(self):
		pygame.init()
		self.GAME_W, self.GAME_H = 1920, 1080
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1920, 1080
		self.canvas = pygame.Surface((self.GAME_W, self.GAME_H))
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.running, self.playing = True, True
		self.dt, self.prev_time = 0, 0
		self.state_stack = []
		self.load_assets()
		self.load_states()
		self.actions = {
			"FORWARD_PITCH_1": False,
			"FORWARD_PITCH_2": False,
			"FORWARD_PITCH_3": False,
			"FORWARD_PITCH_4": False,
			"FORWARD_PITCH_5": False,
			"FORWARD_PITCH_6": False,
			"FORWARD_PITCH_7": False,
			"FORWARD_PITCH_8": False,
			"FORWARD_PITCH_9": False,
			"BACKWARD_PITCH_1": False,
			"BACKWARD_PITCH_2": False,
			"BACKWARD_PITCH_3": False,
			"BACKWARD_PITCH_4": False,
			"BACKWARD_PITCH_5": False,
			"BACKWARD_PITCH_6": False,
			"BACKWARD_PITCH_7": False,
			"BACKWARD_PITCH_8": False,
			"BACKWARD_PITCH_9": False,
			"REEL_UP": False,
			"UP_Y": False,
			"DOWN_Y": False,
			"FORWARDS_X_1": False,
			"FORWARDS_X_2": False,
			"FORWARDS_X_3": False,
			"FORWARDS_X_4": False,
			"FORWARDS_X_1": False,
			"FORWARDS_X_2": False,
			"FORWARDS_X_3": False,
			"FORWARDS_X_4": False,
			"SELECT_UP": False,
			"SELECT_DOWN": False,
			"SELECT_LEFT": False,
			"SELECT_RIGHT": False,
			"SELECT": False,
			"CUT": False,
			"ROLL_FORWARD": False,
			"ROLL_BACKWARD": False,
			"ANY_KEY_PRESSED": False,
		}

	def game_loop(self):
		while self.playing:
			self.get_dt()
			self.get_events()
			self.update()
			self.render()

	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
			if event.type == pygame.KEYDOWN:
				self.actions["ANY_KEY_PRESSED"] = True
				if event.key == pygame.K_ESCAPE:
					self.playing = False
					self.running = False

				# Rest of the keyboard input
				# Fishing
				if event.key == pygame.K_1:
					self.actions["FORWARD_PITCH_1"] = True
				if event.key == pygame.K_2:
					self.actions["FORWARD_PITCH_2"] = True
				if event.key == pygame.K_3:
					self.actions["FORWARD_PITCH_3"] = True
				if event.key == pygame.K_4:
					self.actions["FORWARD_PITCH_4"] = True
				if event.key == pygame.K_4:
					self.actions["FORWARD_PITCH_4"] = True
				if event.key == pygame.K_5:
					self.actions["FORWARD_PITCH_5"] = True
				if event.key == pygame.K_6:
					self.actions["FORWARD_PITCH_6"] = True
				if event.key == pygame.K_7:
					self.actions["FORWARD_PITCH_7"] = True
				if event.key == pygame.K_8:
					self.actions["FORWARD_PITCH_8"] = True
				if event.key == pygame.K_9:
					self.actions["FORWARD_PITCH_9"] = True

				if event.key == pygame.K_q:
					self.actions["BACKWARD_PITCH_1"] = True
				if event.key == pygame.K_w:
					self.actions["BACKWARD_PITCH_2"] = True
				if event.key == pygame.K_e:
					self.actions["BACKWARD_PITCH_3"] = True
				if event.key == pygame.K_r:
					self.actions["BACKWARD_PITCH_4"] = True
				if event.key == pygame.K_t:
					self.actions["BACKWARD_PITCH_5"] = True
				if event.key == pygame.K_y:
					self.actions["BACKWARD_PITCH_6"] = True
				if event.key == pygame.K_u:
					self.actions["BACKWARD_PITCH_7"] = True
				if event.key == pygame.K_i:
					self.actions["BACKWARD_PITCH_8"] = True
				if event.key == pygame.K_o:
					self.actions["BACKWARD_PITCH_9"] = True
				if event.key == pygame.K_p:
					self.actions["REEL_UP"] = True

				# Descaling
				if event.key == pygame.K_l:
					self.actions["UP_Y"] = True
				if event.key == pygame.K_SEMICOLON:
					self.actions["DOWN_Y"] = True

				if event.key == pygame.K_a:
					self.actions["FOWARDS_X_1"] = True
				if event.key == pygame.K_s:
					self.actions["FOWARDS_X_2"] = True
				if event.key == pygame.K_d:
					self.actions["FOWARDS_X_3"] = True
				if event.key == pygame.K_f:
					self.actions["FOWARDS_X_4"] = True

				if event.key == pygame.K_g:
					self.actions["BACKWARDS_X_1"] = True
				if event.key == pygame.K_h:
					self.actions["BACKWARDS_X_2"] = True
				if event.key == pygame.K_j:
					self.actions["BACKWARDS_X_3"] = True
				if event.key == pygame.K_k:
					self.actions["BACKWARDS_X_4"] = True

				# Select
				if event.key == pygame.K_z:
					self.actions["SELECT_UP"] = True
				if event.key == pygame.K_x:
					self.actions["SELECT_DOWN"] = True
				if event.key == pygame.K_c:
					self.actions["SELECT_LEFT"] = True
				if event.key == pygame.K_v:
					self.actions["SELECT_RIGHT"] = True
				if event.key == pygame.K_b:
					self.actions["SELECT"] = True

				# Arrow keys for adittional movement
				if event.key == pygame.K_UP:
					self.actions["SELECT_UP"] = True
				if event.key == pygame.K_DOWN:
					self.actions["SELECT_DOWN"] = True
				if event.key == pygame.K_LEFT:
					self.actions["SELECT_LEFT"] = True
				if event.key == pygame.K_RIGHT:
					self.actions["SELECT_RIGHT"] = True
				if event.key == pygame.K_RETURN:
					self.actions["SELECT"] = True

				# Cutting
				if event.key == pygame.K_n:
					self.actions["CUT"] = True

				# Rolling
				if event.key == pygame.K_m:
					self.actions["ROLL_FORWARD"] = True
				if event.key == pygame.K_COMMA:
					self.actions["ROLL_BACKWARD"] = True

			if event.type == pygame.KEYUP:
				self.actions["ANY_KEY_PRESSED"] = False

				# Fishing
				if event.key == pygame.K_1:
					self.actions["FORWARD_PITCH_1"] = False
				if event.key == pygame.K_2:
					self.actions["FORWARD_PITCH_2"] = False
				if event.key == pygame.K_3:
					self.actions["FORWARD_PITCH_3"] = False
				if event.key == pygame.K_4:
					self.actions["FORWARD_PITCH_4"] = False
				if event.key == pygame.K_4:
					self.actions["FORWARD_PITCH_4"] = False
				if event.key == pygame.K_5:
					self.actions["FORWARD_PITCH_5"] = False
				if event.key == pygame.K_6:
					self.actions["FORWARD_PITCH_6"] = False
				if event.key == pygame.K_7:
					self.actions["FORWARD_PITCH_7"] = False
				if event.key == pygame.K_8:
					self.actions["FORWARD_PITCH_8"] = False
				if event.key == pygame.K_9:
					self.actions["FORWARD_PITCH_9"] = False

				if event.key == pygame.K_q:
					self.actions["BACKWARD_PITCH_1"] = False
				if event.key == pygame.K_w:
					self.actions["BACKWARD_PITCH_2"] = False
				if event.key == pygame.K_e:
					self.actions["BACKWARD_PITCH_3"] = False
				if event.key == pygame.K_r:
					self.actions["BACKWARD_PITCH_4"] = False
				if event.key == pygame.K_t:
					self.actions["BACKWARD_PITCH_5"] = False
				if event.key == pygame.K_y:
					self.actions["BACKWARD_PITCH_6"] = False
				if event.key == pygame.K_u:
					self.actions["BACKWARD_PITCH_7"] = False
				if event.key == pygame.K_i:
					self.actions["BACKWARD_PITCH_8"] = False
				if event.key == pygame.K_o:
					self.actions["BACKWARD_PITCH_9"] = False
				if event.key == pygame.K_p:
					self.actions["REEL_UP"] = False

				# Descaling
				if event.key == pygame.K_l:
					self.actions["UP_Y"] = False
				if event.key == pygame.K_SEMICOLON:
					self.actions["DOWN_Y"] = False

				if event.key == pygame.K_a:
					self.actions["FOWARDS_X_1"] = False
				if event.key == pygame.K_s:
					self.actions["FOWARDS_X_2"] = False
				if event.key == pygame.K_d:
					self.actions["FOWARDS_X_3"] = False
				if event.key == pygame.K_f:
					self.actions["FOWARDS_X_4"] = False

				if event.key == pygame.K_g:
					self.actions["BACKWARDS_X_1"] = False
				if event.key == pygame.K_h:
					self.actions["BACKWARDS_X_2"] = False
				if event.key == pygame.K_j:
					self.actions["BACKWARDS_X_3"] = False
				if event.key == pygame.K_k:
					self.actions["BACKWARDS_X_4"] = False

				# Select
				if event.key == pygame.K_z:
					self.actions["SELECT_UP"] = False
				if event.key == pygame.K_x:
					self.actions["SELECT_DOWN"] = False
				if event.key == pygame.K_c:
					self.actions["SELECT_LEFT"] = False
				if event.key == pygame.K_v:
					self.actions["SELECT_RIGHT"] = False
				if event.key == pygame.K_b:
					self.actions["SELECT"] = False

				# Arrow keys for adittional movement
				if event.key == pygame.K_UP:
					self.actions["SELECT_UP"] = False
				if event.key == pygame.K_DOWN:
					self.actions["SELECT_DOWN"] = False
				if event.key == pygame.K_LEFT:
					self.actions["SELECT_LEFT"] = False
				if event.key == pygame.K_RIGHT:
					self.actions["SELECT_RIGHT"] = False
				if event.key == pygame.K_RETURN:
					self.actions["SELECT"] = False

				# Cutting
				if event.key == pygame.K_n:
					self.actions["CUT"] = False

				# Rolling
				if event.key == pygame.K_m:
					self.actions["ROLL_FORWARD"] = False
				if event.key == pygame.K_COMMA:
					self.actions["ROLL_BACKWARD"] = False

	def update(self):
		self.state_stack[-1].update(self.dt, self.actions)

	def render(self):
		self.state_stack[-1].render(self.canvas)
		self.screen.blit(pygame.transform.scale(self.canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
		pygame.display.flip()

	def get_dt(self):
		now = time.time()
		self.dt = now - self.prev_time
		self.prev_time = now

	def draw_text(self, surface, text, color, x, y):
		text_surface = self.font.render(text, True, color)
		#text_surface.set_colorkey((0,0,0))
		text_rect = text_surface.get_rect()
		text_rect.center = (x, y)
		surface.blit(text_surface, text_rect)

	def load_assets(self):
		# Create pointers to directories 
		self.assets_dir = os.path.join("assets")
		self.font= pygame.font.SysFont('Calibri', 100)

	def load_states(self):
		self.title_screen = Title(self)
		self.state_stack.append(self.title_screen)

	def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False

if __name__ == "__main__":
	g = Game()
	while g.running:
		g.game_loop()