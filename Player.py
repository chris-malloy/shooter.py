import pygame
# research what the sprite class does
from pygame.sprite import Sprite

class Player(Sprite):
	# Classes always contain 2 parts:
	# 1. the __init__ section where you define all attributes.
	# Init, only runs once, When the object i instantiuated
	# Becasue this is a subclass, we need to call the parent's (Sprite) __init__
	def __init__(self,image,start_x,start_y,screen):
		super(Player,self).__init__()
		self.image = pygame.image.load(image)
		# self.image = pygame.transform.scale(self.image,(200,200))
		self.x = start_x
		self.y = start_y
		self.speed = 10
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
	# 2. The methods where you define all the clas functions *(methods)

	def draw_me(self):
		if(self.should_move_up):
			self.y -= self.speed
		elif(self.should_move_down):
			self.y += self.speed
		if(self.should_move_left):
			self.x -= self.speed
		elif(self.should_move_right):
			self.x += self.speed
		self.screen.blit(self.image, [self.x,self.y])

	def should_move(self,direction,yes_or_no):
		if(direction == "up"):
			self.should_move_up = yes_or_no
		if(direction == "down"):
			self.should_move_down = yes_or_no
		if(direction == "left"):
			self.should_move_left = yes_or_no
		if(direction == "right"):
			self.should_move_right = yes_or_no



