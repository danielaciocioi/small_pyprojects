import pygame
import time
import random
pygame.init()
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()

pygame.display.set_caption("Snake game by DNA")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)
game_over = False



clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10



font_style = pygame.font.SysFont(None, 30)

def your_score(score):
	value = font_style.render("Your score: "+ str(score), True, yellow)
	dis.blit(value, [0,0])
def our_snake(snake_block, snake_List):
	for x in snake_List:
		pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [dis_width/2.5, dis_height/2])


def game_loop():
	game_over = False
	game_close = False

	x1 = dis_width/2
	y1 = dis_height/2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, dis_width - snake_block)/10)*10
	foody = round(random.randrange(0, dis_height - snake_block)/10)*10


	while not game_over:
		while game_close == True:
			dis.fill(blue)
			message("You lost! Press Q-Quit or C-Play", red)
			your_score(Length_of_snake-1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					
					if event.key == pygame.K_c:
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				#game_close = True
				pygame.display.update()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -snake_block
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = snake_block

		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
			game_close = True

		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)
		pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_List.append(snake_head)
		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_head:
				game_close = True

		pygame.display.update()



		our_snake(snake_block, snake_List)
		your_score(Length_of_snake-1)
		pygame.display.update()

		if foodx == x1 and foody ==y1:
			foodx = round(random.randrange(0, dis_width - snake_block)/10)*10
			foody = round(random.randrange(0, dis_height - snake_block)/10)*10
			Length_of_snake +=1
		clock.tick(snake_speed)

	#message("You lost", red)
	#pygame.display.update()
	#time.sleep(2)
	pygame.quit()
	quit()

game_loop()
