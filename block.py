import pygame
import random

class Block(pygame.sprite.Sprite):
	
	def __init__(self, color, width, height):
		
		#inherit from the Sprite class in pygame
		super().__init__()
		
		#Make an image of a block and fill it with what ever color provided
		self.image = pygame.Surface([width,height])
		self.image.fill(color)

		self.rect = self.image.get_rect()
	#used to reset the position of the block if it falls off the screen
	
	
	def reset_pos(self,screen_width):
		
		self.rect.y = random.randrange(-300,-20)
		self.rect.x = random.randrange(0, screen_width)
		
	#used to update the position of the block (to move it with the mouse)	
	def update(self,screen_width):
		
		self.rect.y += 5
		
		if self.rect.y > 410:
			self.reset_pos(screen_width)
			
