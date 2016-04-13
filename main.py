
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
from block import Block
from player import Player 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

#used to group all the block sprites in one list
block_list = pygame.sprite.Group()
#used to group all the sprites in the game in one list
all_sprites_list = pygame.sprite.Group()

pygame.display.set_caption("Nom nom")

#used to create x amount of blocks
for i in range (20):
	#make a block with the color black and set its width and height
	block = Block(BLACK, 20,15)
	
	#set a random location for the block's x and y cords
	block.rect.x = random.randrange(screen_width)
	block.rect.y = random.randrange(screen_height)
	
	#add the block to both the block list and the sprite list
	block_list.add(block)
	all_sprites_list.add(block)


#init the player block and add it to the all_sprites_list
player = Player(RED,20,15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
# -------- Main Program Loop -----------
while not done:
# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print("User quit detected. Closing")
				pygame.quit()
	screen.fill(WHITE)
    # --- Game logic should go here
    
    #calls the update function on all the sprites in the sprite list
	all_sprites_list.update(screen_width)
	
	#see if the player block has collided with anything. if True is set then it removes the sprite. If set Flase it doesn't
	blocks_hit_list = pygame.sprite.spritecollide(player,block_list, False)
	
	#every time a block on block_hit_list add 1 to the current score
	for block in blocks_hit_list:
		score += 1
		print(score)
		#when the block is gone 
		block.reset_pos(screen_width)
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here
	all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(30)
 
# Close the window and quit.
pygame.quit()
