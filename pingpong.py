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

class pong:
    def _init_(self,x,y,image):
        self.x=x;
        self.y=y;
        self.image=image;
  
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
    screen.fill((0,0,0))
    x = 200
    y = 300
    width = 1
    height = 50
    font = pygame.font.SysFont("Trebuchet MS",25)
    text = font.render("Loading...", True, (0, 128, 0))
    screen.blit(text,(235,250))
    pygame.draw.rect(screen,(0,128,0),(x,y,width,height),0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        width = width + 0.1
        if(isWithinStart([width+200,height+200])):
            pygame.draw.rect(screen,(0,128,0),(x,y,width,height),0)
        pygame.display.flip()
        pygame.display.update()
    
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
main()