import random
import pygame

from block import Block


class Bullet(Block):
		
	#Update the bullet's location.
	def update(self,screen_width):
		
		self.rect.y -= 5
		
