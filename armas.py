import pygame
import math
import random
import constantes


class arma():
    def __init__(self, image, imagen_calor):
        self.imagen_calor = imagen_calor
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.dispara = False
        self.ultimo_disparo = pygame.time.get_ticks()


    def update(self, personaje):
        calor = None
        disparo_cooldown = constantes.COLDOWN_BALAS
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x += personaje.forma.width / 5
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x -= personaje.forma.width / 5
            self.rotar_arma(True)


        #mover pistola con mouse

        mouse_pos = pygame.mouse.get_pos()
        diferencia_x = mouse_pos[0] - self.forma.centerx
        diferencia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferencia_y, diferencia_x))


        #detectar los click del mouse
        if pygame.mouse.get_pressed()[0] and self.dispara == False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_cooldown):
            calor = Bullet(self.imagen_calor, self.forma.centerx, self.forma.centery, self.angulo)
            self.dispara = True
        #resetear el click del mouse
        if pygame.mouse.get_pressed()[0]== False:
            self.dispara = False
        return calor



    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)


    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip= pygame.transform.flip(self.imagen_original, False, False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        if rotar == False:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
        self.delta_y = -(math.sin(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA)

    def update(self, lista_enemigos, obstaculos_tiles):

        golpe = 0
        pos_golpe = None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        if self. rect.right < 0 or self.rect.left > constantes.ANCHO_PANTALLA or self.rect.bottom <0 or self.rect.top > constantes.ALTURA_PANTALLA:
            self.kill()

        #verificar impacto
        for enemigo in lista_enemigos:
            if enemigo.forma.colliderect(self.rect):
                golpe = 15 + random.randint(-7,0)
                pos_golpe = enemigo.forma
                enemigo.energia -= golpe
                self.kill()
                break
        for obs in obstaculos_tiles:
            if obs[1].colliderect(self.rect):
                self.kill()
                break

        return golpe, pos_golpe

    def dibujar(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery -int(self.image.get_height() - 15)))