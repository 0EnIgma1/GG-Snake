import pygame
import time
import random
from pygame import mixer

snake_speed=18
#window resolution
window_x=720
window_y=480
#color
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(205,38,38)
green=pygame.Color(0,201,87)
blue=pygame.Color(0,0,255)
aqua=pygame.Color(0,255,255)
yellow=pygame.Color(255,215,0)

pygame.init()
game_window=pygame.display.set_mode((window_x,window_y))
fps=pygame.time.Clock()
#name and logo
pygame.display.set_caption("GG Snake")
icon=pygame.image.load('snake.png')
pygame.display.set_icon(icon)
#background
bg=pygame.image.load('forest.jpg')
#position fruit shape and snake body 
snake_pos=[100,50]
snake_bod=[[100,50],[90,50],[80,50],[70,50]]
fruit_pos=[random.randrange(1,(window_x//10))*10,random.randrange(1,(window_y//10))*10]
fruit_spawn=True
direction='RIGHT'
change_to=direction
score=0
#function to show score
def show_score(chocie,color,font,size):
    score_font=pygame.font.SysFont(font,size)
    score_surface=score_font.render('SCORE:'+str(score),True,color)
    score_rect=score_surface.get_rect()
    game_window.blit(score_surface,score_rect)
#function to display final score and end game
def game_over():
    my_font=pygame.font.SysFont('Showcard Gothic',70)
    game_over_surface=my_font.render('YOUR SCORE :'+ str(score),True,black)
    game_over_rect=game_over_surface.get_rect()
    game_over_rect.midtop=(window_x/2,window_y/4)
    game_window.blit(game_over_surface,game_over_rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    quit()
#movements and input
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to='UP'
            if event.key==pygame.K_DOWN:
                change_to='DOWN'
            if event.key==pygame.K_LEFT:
                change_to='LEFT'
            if event.key==pygame.K_RIGHT:
                change_to='RIGHT'
    if change_to=='UP' and direction !='DOWN':
        direction='UP'
    if change_to=='DOWN' and direction !='UP':
        direction='DOWN'
    if change_to=='LEFT' and direction !='RIGHT':
        direction='LEFT'
    if change_to=='RIGHT' and direction !='LEFT':
        direction='RIGHT'
    if direction=='UP':
        snake_pos[1]-=10
    if direction=='DOWN':
        snake_pos[1]+=10
    if direction=='LEFT':
        snake_pos[0]-=10
    if direction=='RIGHT':
        snake_pos[0]+=10
    snake_bod.insert(0,list(snake_pos))
    if snake_pos[0]==fruit_pos[0] and snake_pos[1]==fruit_pos[1]:
        score+=10
        fruit_spawn=False
    else:
        snake_bod.pop()
    #fruit spawn random
    if not fruit_spawn:
        fruit_pos=[random.randrange(1,(window_x//10))*10,random.randrange(1,(window_y//10))*10]
    fruit_spawn=True

    game_window.fill(black)
    game_window.blit(bg,(0, 0))
    #color for snake , fruit 
    for pos in snake_bod:
        pygame.draw.rect(game_window,yellow,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_window,red,pygame.Rect(fruit_pos[0],fruit_pos[1],10,10))
    if snake_pos[0]<0 or snake_pos[0]>window_x-10:
        game_over()
    if snake_pos[1]<0 or snake_pos[1]>window_y-10:
        game_over()
    for block in snake_bod[1:]:
        if snake_pos[0]==block[0] and snake_pos[1]==block[1]:
            game_over()

    show_score(1,black,'Showcard Gothic',40)
    pygame.display.update()
    fps.tick(snake_speed) 
          

