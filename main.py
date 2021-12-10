import pygame
from pygame.locals import *
import time
import random


size = 30

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        
        self.image = pygame.image.load("resources/apple.jpg").convert()
        
        self.x = 90
        self.y = 90

    def draw(self):    
        
        self.parent_screen.blit(self.image, (self.x, self.y)) 
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25)*size
        self.y = random.randint(1, 20)*size  
  
class Snake:
    def __init__(self, parent_screen, length):
        
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.png").convert()
        self.direction = 'right'

        self.length = length
        self.x=[30]*length
        self.y=[30]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -=size

        if self.direction == 'down':
            self.y[0] +=size

        if self.direction == 'left':
            self.x[0] -=size

        if self.direction == 'right':
            self.x[0] +=size

        self.draw() 

    def draw(self):
        self.parent_screen.fill((117, 186, 189))

        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) 
        pygame.display.update()

    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)    

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1100, 700))
        self.snake = Snake(self.surface, 3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()    

    def run(self):
        running = True

        while(running):
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False   

            self.play()         

            time.sleep(0.4)


if __name__ == "__main__":

    game = Game()
    game.run()
