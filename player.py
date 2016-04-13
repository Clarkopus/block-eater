import pygame
import random
from block import Block

class Player(Block):
	
	def update(self, screen_width,x_change,y_change):
		
		self.rect.x += x_change
		self.rect.y += y_change
		print(self.rect.x)

		
