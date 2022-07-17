import pygame
from random import randint
from math import sin, cos

from assets.viking.enums import *

class Entity:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.dt = pygame.time.get_ticks()

    def update(self, keys):
        pass

    def reset(self):
        self.dt = pygame.time.get_ticks()
    
    def draw(self):
        pygame.draw.rect(self.surface, (255, 0, 0), self.rect)


class Player(Entity):
    def __init__(self, surface, x, y, image, data):
        super().__init__(surface, x, y, data[0][0], data[0][1])

        self.data = data
        self.image = pygame.image.load(image).convert_alpha()

        self.index = 0
        self.images = []
        self.load_images()

        self.action = IDLE
        self.running = False
        self.jumping = False
        self.attacking = False
        self.shielding = False
        self.faceleft = False

        self.vel_y = 0

    def load_images(self):
        for y, row_n in enumerate(self.data[2]):
            temp_arr = []
            for x in range(row_n):
                temp_arr.append(pygame.transform.scale(self.image.subsurface(x * self.rect.width, y * self.rect.height, self.rect.width, self.rect.height), (self.rect.width * self.data[1][0], self.rect.height * self.data[1][1])))
            self.images.append(temp_arr)

    def update(self, keys):
        super().update(keys)
        self.running = False
        dx, dy = 0, 0
        vel = 5

        if keys[pygame.K_RIGHT]:
            self.running = True
            dx += vel
            self.faceleft = False
        if keys[pygame.K_LEFT]:
            self.running = True
            dx -= vel
            self.faceleft = True
        if keys[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.vel_y = -20
        if keys[pygame.K_s]:
            self.shield()
        if keys[pygame.K_a]:
            self.attack()

        self.vel_y += 1
        dy += self.vel_y

        if self.rect.left < 0:
            self.rect.x += -self.rect.left
        if self.rect.right > 640 - self.rect.width * self.data[1][0]:
            self.rect.x += 640 - self.rect.width * self.data[1][0] - self.rect.right
        if self.rect.bottom + dy > 480 - self.rect.width * (self.data[1][1] - 1):
            self.vel_y = 0
            dy = 480 - self.rect.width * (self.data[1][1] - 1) - self.rect.bottom
            self.jumping = False
        

        self.rect.x += dx
        self.rect.y += dy
        
        

        if self.shielding:
            if self.action != SHIELD:
                self.action = SHIELD
                self.index = 0
                self.reset()
        elif self.attacking:
            if self.action != ATTACK:
                self.action = ATTACK
                self.index = 0
                self.reset()
        elif self.jumping:
            if self.action != JUMP:
                self.action = JUMP
                self.index = 0
                self.reset()
        elif self.running:
            if self.action != RUN:
                self.action = RUN
                self.index = 0
                self.reset()
        else:
            if self.action != IDLE:
                self.action = IDLE
                self.index = 0
                self.reset()

        if pygame.time.get_ticks() - self.dt > 50:
            self.index += 1
            if self.index > self.data[2][self.action] - 1:
                self.index = 0
                if self.action == JUMP:
                    self.action = IDLE
                    self.vel_y = 0
                    self.jumping = False
                if self.action == ATTACK:
                    self.action = IDLE
                    self.attacking = False
                if self.action == SHIELD:
                    self.action = IDLE
                    self.shielding = False
            self.reset()

    def attack(self):
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 2 * self.data[1][0], self.rect.height * self.data[1][1])
        pygame.draw.rect(self.surface, (0, 0, 255), attack_rect)
    
    def shield(self):
        self.shielding = True
        shield_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 2 * self.data[1][0], self.rect.height * self.data[1][1])
        pygame.draw.rect(self.surface, (0, 255, 0), shield_rect)

    def draw(self):
        self.surface.blit(pygame.transform.flip(self.images[self.action][self.index], self.faceleft, False), (self.rect.x, self.rect.y))

class Dice(Entity):
    def __init__(self, surface, x, y, square, num_image, data):
        super().__init__(surface, x, y, data[0][0] * data[1][0], data[0][1] * data[1][1])
        self.data = data
        self.square = pygame.transform.scale(pygame.image.load(square).convert_alpha(), (self.data[0][0] * self.data[1][0], self.data[0][1] * self.data[1][1]))
        self.image = pygame.image.load(num_image).convert_alpha()

        self.n = randint(1, 6)
        self.rolling = False

        self.theta = 0
        self.scale = 0

        self.dice_image = pygame.transform.scale(self.image.subsurface(self.n * self.data[0][0], 0, self.data[0][0], self.data[0][1]), (self.data[0][0] * self.data[1][0], self.data[0][1] * self.data[1][1]))

    def update(self, keys):
        super().update(keys)
        if keys[pygame.K_SPACE]:
            self.roll()

    def roll(self):
        if not self.rolling:
            self.rolling = True
            self.scale = -1
        if self.rolling:
            if pygame.time.get_ticks() - self.dt > 10:
                self.theta += 10
                self.reset()
            if self.theta == 360:
                self.theta = 0
                self.n = randint(1, 6)
                self.rolling = False
            if self.theta == 180:
                self.scale = 1
            
            self.sqaure = pygame.transform.scale(self.square, (self.square.get_rect().width - (self.scale * 10), self.square.get_rect().height - (self.scale * 10)))

    def draw(self):
        #super().draw()
        self.surface.blit(pygame.transform.rotate(self.square, self.theta), (self.rect.x, self.rect.y))
        if not self.rolling:
            self.surface.blit(self.dice_image, (self.square.get_rect().x, self.square.get_rect().y))

        if self.rolling:
            self.roll()
