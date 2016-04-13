import pygame
import random
from block import Block

class Player(Block):
	
	def update(self, screen_width):
		
		#get the position of the mouse
		pos = pygame.mouse.get_pos()
		
		#set the x and y of the player to where ever the mouse position is
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		
