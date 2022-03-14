import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption("Screensaver")
class Word:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        font = pygame.font.Font(None, 50)
        text = font.render(str("Hello"),1, (255, 0, 0))
        screen.blit(text, (self.xpos, self.ypos))
    def move(self):
        self.ypos += .223
    def reset(self):
        if self.ypos + 20 > 700:
            self.ypos = -20
class Word2:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        font = pygame.font.Font(None, 45)
        text = font.render(str("Hello"),1, (0,255, 0))
        screen.blit(text, (self.xpos, self.ypos))
    def move(self):
        self.ypos += .222
    def reset(self):
        if self.ypos + 20 > 700:
            self.ypos = -21.5
class Word3:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        font = pygame.font.Font(None, 40)
        text = font.render(str("Hello"),1, (0,0, 255))
        screen.blit(text, (self.xpos, self.ypos))
    def move(self):
        self.ypos += .221
    def reset(self):
        if self.ypos + 20 > 700:
            self.ypos = -22
w1 = Word(200, -20)
w2 = Word2(204, -21.5)
w3 = Word3(204.5, -22)
doExit = False
while not doExit:
    w1.move()
    w2.move()
    w3.move()
    w1.reset()
    w2.reset()
    w3.reset()
    screen.fill((0,0,0))
    w3.draw()
    w2.draw()
    w1.draw()
#font = pygame.font.Font(None, 55)
#text = font.render(str("Hello"),1, (255, 0, 0))
#screen.blit(text, (195, 9))
#font = pygame.font.Font(None, 60)
#text = font.render(str("Hello"),1, (0, 0, 255))
#screen.blit(text, (190, 9))

    pygame.display.flip()

pygame.quit()

