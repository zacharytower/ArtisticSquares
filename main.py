import pdb

import pygame
import random
import sys

from pygame.locals import *

GLOBAL_WIDTH = 600
GLOBAL_HEIGHT = 400
GLOBAL_LENGTH_LIMIT = 30

size = (GLOBAL_WIDTH, GLOBAL_HEIGHT)

GLOBAL_LOWER_MULTIPLIER = 0.5
GLOBAL_UPPER_MULTIPLIER = 0.75

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

screen = pygame.display.set_mode(size, 0, 32)

#background = pygame.Surface(screen.get_size())
#background = background.convert()
# background.fill(WHITE)

def recursive_rect_list(
	left_bound = 0, 
	right_bound = GLOBAL_WIDTH,
	top_bound = 0, 
	bottom_bound = GLOBAL_HEIGHT,
	length_limit = GLOBAL_LENGTH_LIMIT,
	lower_mult = GLOBAL_LOWER_MULTIPLIER,
	upper_mult = GLOBAL_UPPER_MULTIPLIER):

	width_difference = right_bound - left_bound
	height_difference = bottom_bound - top_bound

	if width_difference < length_limit or height_difference < length_limit: 
		# if the new rectangle is too small to render

		return [] # stop branch

	width_addend = width_difference * random.uniform(lower_mult, upper_mult)
	height_addend = height_difference * random.uniform(lower_mult, upper_mult)

	width_addend = int(width_addend)
	height_addend = int(height_addend)

	new_left_bound = left_bound + width_addend

	current_rect_obj = pygame.Rect((left_bound, top_bound),
		(left_bound + width_addend,top_bound + height_addend))

	bottom_rects = recursive_rect_list(left_bound = left_bound, 
		right_bound = right_bound - width_addend,
		top_bound = top_bound + height_addend, 
		bottom_bound = bottom_bound)

	right_rects = recursive_rect_list(left_bound = left_bound + width_addend,
		right_bound = right_bound,
		top_bound = top_bound,
		bottom_bound = bottom_bound - height_addend)

	bottomright_rects = recursive_rect_list(left_bound = left_bound + width_addend,
		right_bound = right_bound,
		top_bound = top_bound + height_addend,
		bottom_bound = bottom_bound
		)

	return [current_rect_obj] + bottom_rects + right_rects + bottomright_rects

def main():

	screen.fill(WHITE)
	rect_list = recursive_rect_list()

	for rect in rect_list:
		random_color = tuple(int(random.randint(0,255)) for _ in range(3))
		
		pygame.draw.rect(screen, random_color, rect)
		pygame.display.update()
	# screen.blit(screen, (0,0))
	
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		pygame.display.flip()

if __name__ == '__main__':
	main()


