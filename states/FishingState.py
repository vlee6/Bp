import pygame, os, random, time
from states.state import State
from states.Finish import Finish

class FishingState(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.camera_velocity = 0
		self.camera_position = 0
		self.hook = Hook(self.game, self.camera_position)

		self.start = time.time()
		self.elapsed = 0

		self.fishes = []

	def update(self, delta_time, actions):
		if (random.randint(0, 5) == 0):
			print(self.hook.caught)
			self.fishes.append(Fish(self.game, self.hook, self.camera_position))

		self.hook.update(delta_time, actions, self.camera_position)

		for fish in self.fishes:
			fish.update(delta_time, actions, self.camera_position)

		# Camera
		if (self.hook.position["y"] > 500):
			self.camera_velocity = -1 * self.hook.velocity["y"]
		self.camera_position += self.camera_velocity * delta_time
		print(self.camera_position)

		self.elapsed = time.time() - self.start

		if (self.elapsed > 30):
			new_state = Finish(self.game, self.hook.caught)
			new_state.enter_state()

	def render(self, display):
		display.fill((50, 50, 215))
		self.hook.render(display)

		for fish in self.fishes:
			fish.render(display)

		self.game.draw_text(display, str(round(self.elapsed, 2)), (0,0,0), self.game.GAME_W/2, self.game.GAME_H/6)

class Hook:
	def __init__(self, game, camera_position):
		self.camera_position = camera_position
		self.game = game
		self.position = {"x": 1000, "y": 160} # Starting position of hook
		self.velocity = {"x": 0, "y": 0}
		self.acceleration = {"x": 0, "y": 2}
		self.terminal_velocity = 100
		self.hitbox = {
			"position": {
				"x": self.position["x"],
				"y": self.position["y"]
			},
			"width": 27,
			"height": 48,
			"color": (255, 0, 0)
		}
		self.image = pygame.image.load(os.path.join(game.assets_dir, "hook.png"))
		self.image = pygame.transform.scale(self.image, (27, 48))
		self.caught = []

	def update(self, delta_time, actions, camera_position):
		self.camera_position = camera_position
		self.update_hitbox()

		if (actions["FORWARD_PITCH_1"]):
			self.acceleration["x"] = 0.3
		elif (actions["FORWARD_PITCH_2"]):
			self.acceleration["x"] = 0.6
		elif (actions["FORWARD_PITCH_3"]):
			self.acceleration["x"] = 0.9
		elif (actions["FORWARD_PITCH_4"]):
			self.acceleration["x"] = 1.2
		elif (actions["FORWARD_PITCH_5"]):
			self.acceleration["x"] = 1.5
		elif (actions["FORWARD_PITCH_6"]):
			self.acceleration["x"] = 1.8
		elif (actions["FORWARD_PITCH_7"]):
			self.acceleration["x"] = 2.1
		elif (actions["FORWARD_PITCH_8"]):
			self.acceleration["x"] = 2.4
		elif (actions["FORWARD_PITCH_9"]):
			self.acceleration["x"] = 2.7
		elif (actions["BACKWARD_PITCH_1"]):
			self.acceleration["x"] = -0.3
		elif (actions["BACKWARD_PITCH_2"]):
			self.acceleration["x"] = -0.6
		elif (actions["BACKWARD_PITCH_3"]):
			self.acceleration["x"] = -0.9
		elif (actions["BACKWARD_PITCH_4"]):
			self.acceleration["x"] = -1.2
		elif (actions["BACKWARD_PITCH_5"]):
			self.acceleration["x"] = -1.5
		elif (actions["BACKWARD_PITCH_6"]):
			self.acceleration["x"] = -1.8
		elif (actions["BACKWARD_PITCH_7"]):
			self.acceleration["x"] = -2.1
		elif (actions["BACKWARD_PITCH_8"]):
			self.acceleration["x"] = -2.4
		elif (actions["BACKWARD_PITCH_9"]):
			self.acceleration["x"] = -2.7

		self.velocity["x"] += self.acceleration["x"]
		self.position["x"] += self.velocity["x"] * delta_time

		if (self.velocity["y"] < self.terminal_velocity):
				self.velocity["y"] += self.acceleration["y"]
		self.position["y"] += self.velocity["y"] * delta_time

	def render(self, display):
		# pygame.draw.rect(display, (255, 0, 0), (self.hitbox["position"]["x"], self.hitbox["position"]["y"], self.hitbox["width"], self.hitbox["height"]))

		display.blit(self.image, (self.position["x"], self.position["y"] + self.camera_position))
		
	def update_hitbox(self):
		self.hitbox["position"]["x"] = self.position["x"]
		self.hitbox["position"]["y"] = self.position["y"] + self.camera_position

class Fish:
	def __init__(self, game, hook, camera_position):
		self.camera_position = camera_position
		self.hook = hook
		fish_types = ["tuna", "salmon", "swordfish"]
		self.position = {"x": 0, "y": 0}
		self.hitbox = {
			"position": {
				"x": self.position["x"],
				"y": self.position["y"]
			},
			"width": 0,
			"height": 0,
			"color": (255, 0, 0)
		}
		self.velocity = {"x": 0, "y": 0}
		self.acceleration = {"x": 0, "y": 0}

		self.game = game
		self.type = fish_types[random.randint(0, len(fish_types) - 1)]
		self.direction = random.choice(["left", "right"])
		self.speed = 2
		self.caught = False
		self.spawn()

	def spawn(self):
		scale = 2

		match(self.type):
			case "tuna":
				self.position["y"] = random.randint(100, 10000)
				self.hitbox["width"] = 61 * scale
				self.hitbox["height"] = 33 * scale
				self.speed = 2
				self.image = pygame.image.load(os.path.join(self.game.assets_dir, "tuna.png"))
				self.image = pygame.transform.scale(self.image, (61 * scale, 33 * scale))
			case "salmon":
				self.position["y"] = random.randint(500, 10000)
				self.hitbox["width"] = 40 * scale
				self.hitbox["height"] = 19 * scale
				self.speed = 3
				self.image = pygame.image.load(os.path.join(self.game.assets_dir, "salmono.png"))
				self.image = pygame.transform.scale(self.image, (40 * scale, 19 * scale))
			case "trout":
				self.position["y"] = random.randint(800, 10000)
				self.hitbox["width"] = 54 * scale
				self.hitbox["height"] = 69 * scale
				self.speed = 5
				self.image = pygame.image.load(os.path.join(self.game.assets_dir, "trout.png"))
				self.image = pygame.transform.scale(self.image, (54 * scale, 69 * scale))
			case "swordfish":
				self.position["y"] = random.randint(1000, 10000)
				self.hitbox["width"] = 90
				self.hitbox["height"] = 36
				self.speed = 5
				self.image = pygame.image.load(os.path.join(self.game.assets_dir, "swordfish.png"))
				self.image = pygame.transform.scale(self.image, (90 * scale, 36 * scale))
			case "shark":
				self.position["y"] = random.randint(1200, 10000)
				self.hitbox["width"] = 65
				self.hitbox["height"] = 56
				self.speed = 5
				self.image = pygame.image.load(os.path.join(self.game.assets_dir, "shark.png"))
				self.image = pygame.transform.scale(self.image, (65 * scale, 56 * scale))
		
		if self.direction == "left":
			self.position["x"] = 2100
		elif self.direction == "right":
			self.position["x"] = -100
			self.image = pygame.transform.flip(self.image, False, True)

	def update(self, delta_time, actions, camera_position):
		self.camera_position = camera_position
		self.update_hitbox()

		if (not self.caught):
			fish_box = pygame.Rect(self.hitbox["position"]["x"], self.hitbox["position"]["y"], self.hitbox["width"], self.hitbox["height"])
			hook_box = pygame.Rect(self.hook.hitbox["position"]["x"], self.hook.hitbox["position"]["y"], self.hook.hitbox["width"], self.hook.hitbox["height"])

			if fish_box.colliderect(hook_box):
				self.hook.caught.append(self.type)
				self.caught = True
				self.image = pygame.transform.rotate(self.image, random.randint(0, 360))


			self.acceleration["x"] = random.randint(0, 2)

			if self.direction == "left":
				self.acceleration["x"] *= -1

			self.velocity["x"] += self.acceleration["x"]	
			self.position["x"] += self.velocity["x"] * delta_time
		else:
			self.position["x"] = self.hook.position["x"]
			self.position["y"] = self.hook.position["y"]
				

	def update_hitbox(self):
		self.hitbox["position"]["x"] = self.position["x"]
		self.hitbox["position"]["y"] = self.position["y"] + self.camera_position

	def render(self, display):
			# pygame.draw.rect(display, (255, 0, 0), (self.hitbox["position"]["x"], self.hitbox["position"]["y"], self.hitbox["width"], self.hitbox["height"]))
			display.blit(self.image, (self.position["x"], self.position["y"] + self.camera_position))