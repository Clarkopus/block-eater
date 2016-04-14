import pygame
import random
from block import Block

class Player(Block):
	
	def update(self, screen_width,x_change,y_change):
		
		self.rect.x += x_change
		self.rect.y += y_change
		print(self.rect.x)

	def reset_pos(self,screen_width):
		
		self.rect.y = 200
		self.rect.x = 350
