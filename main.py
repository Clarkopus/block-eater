
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
from bullet import Bullet
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

background_image = pygame.image.load('background.jpg')

#used to group all the block sprites in one list
block_list = pygame.sprite.Group()
#used to group all the sprites in the game in one list
all_sprites_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

pygame.display.set_caption("Nom nom")
number_of_blocks = 20


#used to create x amount of blocks
def create_blocks():
	
	print("respawning blocks")
	number_of_blocks = 20
	for i in range (number_of_blocks):
		#make a block with the color black and set its width and height
		block = Block(GREEN, 20,15)
		
		#set a random location for the block's x and y cords
		block.rect.x = random.randrange(screen_width)
		block.rect.y = random.randrange(screen_height)
		
		#add the block to both the block list and the sprite list
		block_list.add(block)
		all_sprites_list.add(block)


#init the player block and add it to the all_sprites_list
player = Player(RED,20,15)
player_list.add(player)
bullet = Bullet((250,250,250), 1,1)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
x_change = 0
y_change =0
create_blocks()
# -------- Main Program Loop -----------
while not done:

	
# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
			elif event.key == pygame.K_UP:
				y_change = -5
			elif event.key == pygame.K_DOWN:
				y_change = 5
			elif event.key == pygame.K_SPACE:
				bullet = Bullet(YELLOW, 10,10)
				bullet.rect.x = player.rect.x
				bullet.rect.y = player.rect.y
				all_sprites_list.add(bullet)
				bullet_list.add(bullet)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_change = 0
	screen.fill(WHITE)
    # --- Game logic should go here
    
    #calls the update function on all the sprites in the sprite list
	all_sprites_list.update(screen_width)
	player.update(screen_width,x_change,y_change)
	
	#see if the player block has collided with anything. if True is set then it removes the sprite. If set Flase it doesn't
	blocks_hit_list = pygame.sprite.spritecollide(player,block_list, False)
	#See if the bullet has collided with anything
	bullet_hit_list = pygame.sprite.spritecollide(bullet,block_list, True)
	
	#every time a block on block_hit_list add 1 to the current score
	
	for block in blocks_hit_list:
		player.reset_pos(screen_width)	
		
	#every time a block in bullet_hit_list shows up, reset the position of the blocks.
	for block in bullet_hit_list:
		print("Colision detected")
		number_of_blocks -= 1
		block.reset_pos(screen_width)
		if number_of_blocks == 0:
			create_blocks()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here
	screen.blit(background_image,(0,0))
	all_sprites_list.draw(screen)
	player_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 30 frames per second
	clock.tick(30)
 
# Close the window and quit.
pygame.quit()
