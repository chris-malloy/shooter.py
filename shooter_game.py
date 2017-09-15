import pygame


from Player import Player    
from Bad_guy import Bad_guy


pygame.init()


screen_size = (1000,800)

background_color = (82,111,53)


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("This is just like Dark Souls.")


the_player = Player('dude.png', 100, 100, screen)
bad_guy = Bad_guy(screen)


game_on = True

while game_on: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up",True)
			elif event.key == 274:
				the_player.should_move("down",True)
			if event.key == 275:
				the_player.should_move("right",True)
			elif event.key == 276:
				the_player.should_move("left",True)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			elif event.key == 274:
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)

	screen.fill(background_color)

	# update the bad guy (based on where thge player is)
	bad_guy.update_me(the_player)
	# draw the bad guy
	bad_guy.draw_me()

	the_player.draw_me()

	pygame.display.flip()

