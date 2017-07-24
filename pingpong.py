# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:22:09 2017

@author: prasanth
"""

'''
Import Modules here
'''
from PIL import Image
import pygame
import sys
import os
  
'''
Reference: http://www.nerdparadise.com/programming/pygame/part2
'''      
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep)
                canonicalized_path = canonicalized_path.replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
        
def initializePygame():
    width=600
    height=600
    screen = startWindow(width,height)
    handleEvents(screen)

def handleEvents(screen):
    while True:
        for event in pygame.event.get():
            clickStart(event,screen)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
def startWindow(width,height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ping Pong")
    screen.blit(get_image('start_button.jpg'), (200, 200)) 
    imageSize = Image.open('start_button.jpg').size
    pygame.display.flip()
    return screen
                
def clickStart(event,screen):
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        if(isWithinStart (pos)):               
            loading(screen)
            
def loading(screen):
    screen.fill(black)
    x = 200
    y = 300
    width = 1
    height = 50
    font = pygame.font.SysFont("Trebuchet MS",25)
    text = font.render("Loading...", True, green)
    screen.blit(text,(235,250))
    pygame.draw.rect(screen,green,(x,y,width,height),0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        width = width + 0.1
        if(isWithinStart([width+200,height+200])):
            pygame.draw.rect(screen,green,(x,y,width,height),0)
        else:
            loadGameWindow(screen)
        pygame.display.flip()
        pygame.display.update()
    
    
def loadGameWindow(screen):
    screen.fill(black)
    pygame.draw.lines(screen, white, False, [(300,0),(300,600)], 1)
    racket_width =5
    racket_height = 60
    left_x=0
    left_y=270
    right_x=595
    right_y=270
    pygame.draw.rect(screen,yellow,
                     (left_x,left_y,racket_width,
                     racket_height),0)
    pygame.draw.rect(screen,yellow,
                     (right_x,right_y,racket_width,
                     racket_height),0)

def isWithinStart(pos):   
    x = pos[0]
    y=  pos[1]
    if x>=200 and x<=425 and y>=200 and y<=425:
        return True
    else:
        return False
               
def main():
    initializePygame()
 
_image_library={}
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
green=(0,128,0)

main()