import pygame
from pygame.locals import *
import time
import random


size = 30
snake_len=2

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

    def increase_length(self):
        self.length +=1   
        self.x.append(-1)
        self.y.append(-1) 

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
        self.snake = Snake(self.surface, snake_len)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def collision(self, x1, x2, y1, y2):
        if (x1 >= x2 and x1 < x2 + size):
            if (y1 >= y2 and y1 < y2 + size):
                return True

        return False        

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()  
        
        # snake eats the apple
        if self.collision(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake collides with itself
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.x[i], self.snake.y[0], self.snake.y[i]):
                raise "Game Over"

    def game_over(self):     
        self.surface.fill((117, 186, 189))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Score : {self.snake.length-snake_len}", True, (0, 0, 0))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (0, 0, 0))
        self.surface.blit(line2, (200,350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, snake_len)   
        self.apple = Apple(self.surface)

    def display_score(self):
        font = pygame.font.SysFont('arial', 25)
        score = font.render(f"Score: {self.snake.length-snake_len}", True, (0, 0, 0))
        self.surface.blit(score, (950, 10))

    def run(self):
        running = True
        pause = False
        while(running):
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                    
                    if not pause:
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

            try:
                if not pause:
                    self.play()    
            except Exception as e:
                self.game_over()    
                pause = True    
                self.reset() 

            time.sleep(0.4)


if __name__ == "__main__":

    game = Game()
    game.run()
