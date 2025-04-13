import pygame
import random
import math

#def music_start():
#	if move == True: 
#		pygame.mixer.music.load('audioassets/runninginthe.wav')
#	if move == False:
#		pygame.mixer.music.stop()

def reset_to_top():
	rand_genx = random.randint(0, WIDTH)
	rand_geny = random.randint(0, HEIGHT)
	if lake.y > HEIGHT:
		lake.x = rand_genx
		lake.y = -40
	if rock1.y > HEIGHT:
		rock1.x = rand_genx
		rock1.y = -40
	if rock2.y > HEIGHT:
		rock2.x = rand_genx
		rock2.y = -40
	if bush1.y > HEIGHT:
		bush1.x = rand_genx
		bush1.y = -40
	if bush2.y > HEIGHT:
		bush2.x = rand_genx
		bush2.y = -40
	if bush3.y > HEIGHT:
		bush3.x = rand_genx
		bush3.y = -40
	if bush4.y > HEIGHT:
		bush4.x = rand_genx
		bush4.y = -40
	if house.y > HEIGHT:
		house.x = rand_genx
		house.y = -40
	if house2.y > HEIGHT:
		house2.x = rand_genx
		house2.y = -40
	if house3.y > HEIGHT:
		house3.x = rand_genx
		house3.y = -40
	if house4.y > HEIGHT:
		house4.x = rand_genx
		house4.y = -40
	if cloud_p1.y > HEIGHT:
		cloud_p1.x = rand_genx
		cloud_p1.y = -40
	if cloud_p2.y > HEIGHT:
		cloud_p2.x = rand_genx
		cloud_p2.y = -40
	if cloud2_p1.y > HEIGHT:
		cloud2_p1.x = rand_genx
		cloud2_p1.y = -40
	if cloud2_p2.y > HEIGHT:
		cloud2_p2.x = rand_genx
		cloud2_p2.y = -40
	elif rock1.x > WIDTH:
		rock1.x = 0
		rock1.y = rand_geny
	elif rock1.x < 0:
		rock1.x = WIDTH
		rock1.y = rand_geny
	elif rock2.x > WIDTH:
		rock2.x = 0
		rock2.y = rand_geny
	elif rock2.x < 0:
		rock2.x = WIDTH
		rock2.y = rand_geny
	elif bush1.x > WIDTH:
		bush1.x = 0
		bush1.y = rand_geny
	elif bush1.x < 0:
		bush1.x = WIDTH
		bush1.y = rand_geny
	elif bush2.x > WIDTH:
		bush2.x = 0
		bush2.y = rand_geny
	elif bush2.x < 0:
		bush2.x = WIDTH
		bush2.y = rand_geny
	elif bush3.x > WIDTH:
		bush3.x = 0
		bush3.y = rand_geny
	elif bush3.x < 0:
		bush3.x = WIDTH
		bush3.y = rand_geny
	elif bush4.x > WIDTH:
		bush4.x = 0
		bush4.y = rand_geny
	elif bush4.x < 0:
		bush4.x = WIDTH
		bush4.y = rand_geny
	elif house.x > WIDTH:
		house.x = 0
		house.y = rand_geny
	elif house.x < 0:
		house.x = WIDTH
		house.y = rand_geny
	elif house2.x > WIDTH:
		house2.x = 0
		house2.y = rand_geny
	elif house2.x < 0:
		house2.x = WIDTH
		house2.y = rand_geny
	elif house3.x > WIDTH:
		house3.x = 0
		house3.y = rand_geny
	elif house3.x < 0:
		house3.x = WIDTH
		house3.y = rand_geny
	elif house4.x > WIDTH:
		house4.x = 0
		house4.y = rand_geny
	elif house4.x < 0:
		house4.x = WIDTH
		house4.y = rand_geny
	elif cloud_p1.x > WIDTH:
		cloud_p1.x = 0
		cloud_p1.y = rand_geny
	elif cloud_p1.x < 0:
		cloud_p1.x = WIDTH
		cloud_p1.y = rand_geny
	elif cloud_p2.x > WIDTH:
		cloud_p2.x = 0
		cloud_p2.y = rand_geny
	elif cloud_p2.x < 0:
		cloud_p2.x = WIDTH
		cloud_p2.y = rand_geny
	elif cloud2_p1.x > WIDTH:
		cloud2_p1.x = 0
		cloud2_p1.y = rand_geny
	elif cloud2_p1.x < 0:
		cloud2_p1.x = WIDTH
		cloud2_p1.y = rand_geny
	elif cloud2_p2.x > WIDTH:
		cloud2_p2.x = 0
		cloud2_p2.y = rand_geny
	elif cloud2_p2.x < 0:
		cloud2_p2.x = WIDTH
		cloud2_p2.y = rand_geny
	elif lake.x > WIDTH:
		lake.x = 0
		lake.y = rand_geny
	elif lake.x < 0:
		lake.x = WIDTH
		lake.y = rand_geny

def move_background():
	ground_scroll_speed = 8
	cloud_scroll_speed = 5.5
	key = pygame.key.get_pressed()
	rock1.move_ip(0, ground_scroll_speed)
	rock2.move_ip(0, ground_scroll_speed)
	bush1.move_ip(0, ground_scroll_speed)
	bush2.move_ip(0, ground_scroll_speed)
	bush3.move_ip(0, ground_scroll_speed)
	bush4.move_ip(0, ground_scroll_speed)
	house.move_ip(0, ground_scroll_speed)
	house2.move_ip(0, ground_scroll_speed)
	house3.move_ip(0, ground_scroll_speed)
	house4.move_ip(0, ground_scroll_speed)
	lake.move_ip(0, ground_scroll_speed)
	cloud_p1.move_ip(0, cloud_scroll_speed)
	cloud_p2.move_ip(0, cloud_scroll_speed)
	cloud2_p1.move_ip(0, cloud_scroll_speed)
	cloud2_p2.move_ip(0, cloud_scroll_speed)
	if key[pygame.K_a]:
		rock1.move_ip(ground_scroll_speed, 0)
		rock2.move_ip(ground_scroll_speed, 0)
		bush1.move_ip(ground_scroll_speed, 0)
		bush2.move_ip(ground_scroll_speed, 0)
		bush3.move_ip(ground_scroll_speed, 0)
		bush4.move_ip(ground_scroll_speed, 0)
		house.move_ip(ground_scroll_speed, 0)
		house2.move_ip(ground_scroll_speed, 0)
		house3.move_ip(ground_scroll_speed, 0)
		house4.move_ip(ground_scroll_speed, 0)
		lake.move_ip(ground_scroll_speed, 0)
		cloud_p1.move_ip(cloud_scroll_speed, 0)
		cloud_p2.move_ip(cloud_scroll_speed, 0)
		cloud2_p1.move_ip(cloud_scroll_speed, 0)
		cloud2_p2.move_ip(cloud_scroll_speed, 0)
	if key[pygame.K_d]:
		rock1.move_ip(-ground_scroll_speed, 0)
		rock2.move_ip(-ground_scroll_speed, 0)
		bush1.move_ip(-ground_scroll_speed, 0)
		bush2.move_ip(-ground_scroll_speed, 0)
		bush3.move_ip(-ground_scroll_speed, 0)
		bush4.move_ip(-ground_scroll_speed, 0)
		house.move_ip(-ground_scroll_speed, 0)
		house2.move_ip(-ground_scroll_speed, 0)
		house3.move_ip(-ground_scroll_speed, 0)
		house4.move_ip(-ground_scroll_speed, 0)
		lake.move_ip(-ground_scroll_speed, 0)
		cloud_p1.move_ip(-cloud_scroll_speed, 0)
		cloud_p2.move_ip(-cloud_scroll_speed, 0)
		cloud2_p1.move_ip(-cloud_scroll_speed, 0)
		cloud2_p2.move_ip(-cloud_scroll_speed, 0)

def enemy_movement():
	global score  
	if enemy1_hitbox.y != 100:
		enemy1_hitbox.move_ip(0, 5)
	if score >= 10:
		if enemy3_hitbox.y != 100:
			enemy3_hitbox.move_ip(0, 5)
	if score >= 20:
		if enemy2_hitbox.y != 100:
			enemy2_hitbox.move_ip(0, 5)
	if score < 5:
		enemy2_hitbox.y = -250
		bullet3.y = enemy2_hitbox.y
		enemy3_hitbox.y = -250
		bullet4.y = enemy3_hitbox.y

def shoot_player():
	global health, move  
	key = pygame.key.get_pressed()
	if key[pygame.K_a]:
		enemy1_hitbox.move_ip(5, 0)
		enemy2_hitbox.move_ip(5, 0)
		enemy3_hitbox.move_ip(5, 0)
		bullet.move_ip(2, 0)
		bullet3.move_ip(2, 0)
		bullet4.move_ip(2, 0)
	if key[pygame.K_d]:
		enemy1_hitbox.move_ip(-5, 0)
		enemy2_hitbox.move_ip(-5, 0)
		enemy3_hitbox.move_ip(-5, 0)
		bullet.move_ip(-2, 0)
		bullet3.move_ip(-2, 0)
		bullet4.move_ip(-2, 0)
	if move == True:
		if bullet.y != WIDTH + 20:
			bullet.move_ip(0, 5)
	if bullet.y >= WIDTH:
		bullet.x = enemy1_hitbox.x + 20
		bullet.y = enemy1_hitbox.y + 100
	if bullet.colliderect(plane_hitbox) or bullet.colliderect(plane_hitbox_y):
		pygame.mixer.Sound.play(hitsound)
		pygame.mixer.music.stop()
		health -= 1
		bullet.x = enemy1_hitbox.x + 20
		bullet.y = enemy1_hitbox.y + 100
		if health == 0:
			move = False
	if score >= 20:
		if bullet3.y != WIDTH + 20:
			bullet3.move_ip(0, 7)
		if bullet3.y >= WIDTH:
			bullet3.x = enemy2_hitbox.x + 20
			bullet3.y = enemy2_hitbox.y + 100
		if bullet3.colliderect(plane_hitbox) or bullet3.colliderect(plane_hitbox_y):
			pygame.mixer.Sound.play(hitsound)
			pygame.mixer.music.stop()
			health -= 1
			if health == 0:
				highscore + score 
			bullet3.x = enemy2_hitbox.x + 20
			bullet3.y = enemy2_hitbox.y + 100
			if health == 0:
				move = False
	if score >= 10:
		if bullet4.y != WIDTH + 20:
			bullet4.move_ip(0, 6)
		if bullet4.y >= WIDTH:
			bullet4.x = enemy3_hitbox.x + 20
			bullet4.y = enemy3_hitbox.y + 100
		if bullet4.colliderect(plane_hitbox) or bullet4.colliderect(plane_hitbox_y):
			pygame.mixer.Sound.play(hitsound)
			pygame.mixer.music.stop()
			health -= 1
			bullet4.x = enemy3_hitbox.x + 20
			bullet4.y = enemy3_hitbox.y + 100
			if health == 0:
				move = False
	
def kill_enemy():
	global score
	key = pygame.key.get_pressed()
	if move == True:
		if bullet2.y != -35:
			bullet2.move_ip(0, -5)
	if bullet2.y == -20:
		bullet2.x = plane_hitbox.x  
		bullet2.y = plane_hitbox.y  
	if bullet2.colliderect(enemy1_hitbox):
		pygame.mixer.Sound.play(hitsound)
		pygame.mixer.music.stop()
		score += 1  
		bullet2.x = plane_hitbox.x  
		bullet2.y = plane_hitbox.y 
		enemy1_hitbox.x = random.randint(30, WIDTH - 30)
		enemy1_hitbox.y = -350
	if bullet2.colliderect(enemy2_hitbox):
		pygame.mixer.Sound.play(hitsound)
		pygame.mixer.music.stop()
		score += 1  
		bullet2.x = plane_hitbox.x  
		bullet2.y = plane_hitbox.y 
		enemy2_hitbox.x = random.randint(30, WIDTH - 30)
		enemy2_hitbox.y = -350
	if bullet2.colliderect(enemy3_hitbox):
		pygame.mixer.Sound.play(hitsound)
		pygame.mixer.music.stop()
		score += 1  
		bullet2.x = plane_hitbox.x  
		bullet2.y = plane_hitbox.y 
		enemy3_hitbox.x = random.randint(30, WIDTH - 30)
		enemy3_hitbox.y = -350

def enemy_stay():
	if enemy1_hitbox.x >= WIDTH:
		enemy1_hitbox.x = 10
	if enemy1_hitbox.x <= 0:
		enemy1_hitbox.x = WIDTH -50
	if enemy2_hitbox.x >= WIDTH:
		enemy2_hitbox.x = 10
	if enemy2_hitbox.x <= 0:
		enemy2_hitbox.x = WIDTH -50
	if enemy3_hitbox.x >= WIDTH:
		enemy3_hitbox.x = 10
	if enemy3_hitbox.x <= 0:
		enemy3_hitbox.x = WIDTH -50

pygame.init()
WIDTH = 1050
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('Plain Plane Game: 1.4')
plane = pygame.image.load('assets/plane.png')
plane = pygame.transform.scale(plane, (250, 200))
plane = pygame.transform.rotate(plane, 270)
plane_hitbox = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 + 110, 20, 200)
plane_hitbox_y = pygame.Rect(plane_hitbox.x - 65, plane_hitbox.y + 110, 150, 20)
lake = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 50)
lake_tex = pygame.image.load('assets/lake.png')
lake_tex = pygame.transform.scale(lake_tex, (200, 200))
bush1 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 30, 50)
bush2 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 35)
bush3 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 40, 25)
bush4 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 25, 35)
rock1 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 25, 20)
rock2 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 15)
rock3 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 15)
house = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 70)
house2 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 70)
house3 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 70)
house4 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 50, 70)
house_texture = pygame.image.load('assets/house.png')
house_texture = pygame.transform.scale(house_texture, (50, 80))
cloud_p1 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 150, 100)
cloud_p2 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 100, 80)
cloud2_p1 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 200, 150)
cloud2_p2 = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 150, 50)
move = False
font1 = pygame.font.SysFont('comicsans', 100)
enemy1 = pygame.image.load('assets/enemy1.png')
enemy1 = pygame.transform.scale(enemy1, (250, 250))
enemy1_hitbox = pygame.Rect(random.randint(30, WIDTH - 30), -400, 50, 200)
enemy2 = pygame.image.load('assets/enemy2.png')
enemy2 = pygame.transform.scale(enemy2, (250, 250))
enemy2_hitbox = pygame.Rect(random.randint(30, WIDTH - 30), -400, 50, 200)
enemy3 = pygame.image.load('assets/enemy3.png')
enemy3 = pygame.transform.scale(enemy3, (250, 250))
enemy3_hitbox = pygame.Rect(random.randint(30, WIDTH - 30), -400, 50, 200)
bullet = pygame.Rect(enemy1_hitbox.x + 20, enemy1_hitbox.y + 100, 15, 15)
bullet2 = pygame.Rect(plane_hitbox.x, plane_hitbox.y, 15, 15) 
bullet3 = pygame.Rect(enemy2_hitbox.x + 20, enemy2_hitbox.y + 100, 15, 15)
bullet4 = pygame.Rect(enemy3_hitbox.x + 20, enemy3_hitbox.y + 100, 15, 15)
font2 = pygame.font.SysFont('8bit', 80)
score: abs = 0
paused = False
health = 3 
full_heart = pygame.image.load('assets/filled_heart.png')
full_heart = pygame.transform.scale(full_heart, (50, 50))
empty_heart = pygame.image.load('assets/empty_heart.png')
empty_heart = pygame.transform.scale(empty_heart, (50, 50))
hitsound = pygame.mixer.Sound('audioassets/hitmarker.wav')
highscore = 0  
real_highscore = 0  
#run_music = pygame.mixer.music.load('audioassets/runninginthe.wav')
main_text = pygame.image.load('assets/main_text.png')
main_text = pygame.transform.scale(main_text, (1000, 800))

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				move = True 
				health = 3
				score = 0
			if event.key == pygame.K_ESCAPE:
				paused = True
			elif event.key == pygame.K_ESCAPE:
				paused = False

	clock.tick(FPS)
	plan_hitboxs = pygame.draw.rect(screen, 'red', plane_hitbox), pygame.draw.rect(screen, 'red', plane_hitbox_y)
	enemy_hitboxs = pygame.draw.rect(screen, 'red', enemy1_hitbox), pygame.draw.rect(screen, 'red', enemy2_hitbox)
	pygame.draw.rect(screen, 'red', enemy3_hitbox)
	screen.fill('light green')
	pygame.draw.rect(screen, 'aquamarine4', lake)
	pygame.draw.rect(screen, 'silver', rock1), pygame.draw.rect(screen, 'silver', rock2)
	pygame.draw.rect(screen, 'seagreen3', bush1), pygame.draw.rect(screen, 'seagreen3', bush2)
	pygame.draw.rect(screen, 'seagreen3', bush3), pygame.draw.rect(screen, 'seagreen3', bush4)
	pygame.draw.rect(screen, 'burlywood4', house), pygame.draw.rect(screen, 'burlywood4', house2)
	screen.blit(lake_tex, (lake.x - 45, lake.y - 45))
	screen.blit(house_texture, (house.x, house.y))
	screen.blit(house_texture, (house2.x, house2.y))
	pygame.draw.rect(screen, 'burlywood4', house3), pygame.draw.rect(screen, 'burlywood4', house4)
	screen.blit(house_texture, (house3.x, house3.y))
	screen.blit(house_texture, (house4.x, house4.y)) 
	score_text = font1.render(f'{score}', True, 'darkturquoise')
	score_text1 = screen.blit(score_text, (WIDTH / 2 - 10, 100))
	screen.blit(full_heart, (25, HEIGHT - 80))
	screen.blit(full_heart, (60, HEIGHT - 80))
	if health <= 1:
		screen.blit(empty_heart, (60, HEIGHT - 80))
	screen.blit(full_heart, (95, HEIGHT - 80))
	if health <= 2:
		screen.blit(empty_heart, (95, HEIGHT - 80))
	pygame.draw.rect(screen, 'gainsboro', cloud_p1), pygame.draw.rect(screen, 'gainsboro', cloud_p2)
	pygame.draw.rect(screen, 'gainsboro', cloud2_p1), pygame.draw.rect(screen, 'gainsboro', cloud2_p2)
	pygame.draw.ellipse(screen, 'indianred3', bullet)
	pygame.draw.ellipse(screen, 'indianred3', bullet3)
	screen.blit(enemy3, (enemy3_hitbox.x - 125, enemy3_hitbox.y))
	screen.blit(enemy1, (enemy1_hitbox.x - 125, enemy1_hitbox.y))
	screen.blit(enemy2, (enemy2_hitbox.x - 125, enemy2_hitbox.y))
	pygame.draw.ellipse(screen, 'indianred3', bullet2)
	pygame.draw.ellipse(screen, 'indianred3', bullet4)
	if move == False:
		screen.fill('light green')
		##3 place main_text here
		screen.blit(main_text, (0, 0))
		highscore = highscore + score
		if highscore > real_highscore:
			real_highscore = 0
			real_highscore = real_highscore + highscore 
		highscore_text = font1.render(f'SCORE {highscore}', True, 'darkturquoise')
		real_highscore_text = font2.render(f'HIGHSCORE {real_highscore}', True, 'darkturquoise')
		screen.blit(highscore_text, (WIDTH / 2 + 150, HEIGHT / 2 + 200))
		screen.blit(real_highscore_text, (WIDTH / 2 + 55, HEIGHT / 2 + 300))
		score = 0  
	else:
		highscore = 0  
		pass
	screen.blit(plane, (WIDTH / 2 - 100, HEIGHT / 2 + 100))
	if paused == True:
		screen.fill('aquamarine')

	if move == True:
		move_background()
	reset_to_top()
	enemy_movement()
	shoot_player()
	kill_enemy()
	enemy_stay()
#	music_start()

	pygame.display.flip()
	pygame.display.update()

pygame.quit()
if __name__ == '__main__':
	main()