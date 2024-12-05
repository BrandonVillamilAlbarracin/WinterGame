import math
import random

import pygame
from pygame.examples.cursors import image

import constantes


#cordenadas al crear un personaje
class Personaje():
    def __init__(self, x, y, animaciones, energia):
        self.score = 0
        self.energia = energia
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.vivo = True
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)
        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()

    def enemigos(self, jugador, obstaculos_tiles):
        ene_dx = 0
        ene_dy = 0

        distancia =  math.sqrt(((self.forma.centerx - jugador.forma.centerx)**2) + ((self.forma.centery - jugador.forma.centery)**2))

        if distancia < constantes.RANGO:

            if self.forma.centerx > jugador.forma.centerx:
                ene_dx = -constantes.VELOCIDAD_ENEMIGO
            if self.forma.centerx < jugador.forma.centerx:
                ene_dx = constantes.VELOCIDAD_ENEMIGO

            if self.forma.centery > jugador.forma.centery:
                ene_dy = -constantes.VELOCIDAD_ENEMIGO
            if self.forma.centery < jugador.forma.centery:
                ene_dy = constantes.VELOCIDAD_ENEMIGO
        self.movimiento(ene_dx, ene_dy, obstaculos_tiles)


        if distancia < constantes.RANGO_ATAQUE and jugador.golpe == False:
            jugador.energia -= 10
            jugador.golpe = True
            jugador.ultimo_golpe = pygame.time.get_ticks()


    def update(self):

        #comprobar vida

        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        #Reiniciar Golpe
        golpe_cooldown = 500

        if self.golpe == True:
            if pygame.time.get_ticks() - self.ultimo_golpe > golpe_cooldown:
                self.golpe = False

        cooldown_animacion = 150
        self.image = self.animaciones[self.frame_index]

        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)


    def movimiento(self, delta_x, delta_y, obstaculos_tile):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        self.forma.x = self.forma.x + delta_x

        for obstaculo in obstaculos_tile:
            if obstaculo[1].colliderect(self.forma):
                if delta_x > 0:
                    self.forma.right = obstaculo[1].left
                if delta_x < 0:
                    self.forma.left = obstaculo[1].right


        self.forma.y = self.forma.y + delta_y

        for obstaculo in obstaculos_tile:
            if obstaculo[1].colliderect(self.forma):
                if delta_y > 0:
                    self.forma.bottom = obstaculo[1].top
                if delta_y < 0:
                    self.forma.top = obstaculo[1].bottom
