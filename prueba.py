import pygame
import constantes
from personaje import Personaje
from armas import arma
import os
from textos import DamageText
from mundo import Mundo
from item import Item


#Funciones
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

def contar_elementos(directorio):
    return len(os.listdir(directorio))

def nombres_carpetas(directorio):
    return os.listdir(directorio)

#inicializamos el programa
pygame.init()

#muestra la ventana llamandola de contantes
ventana = pygame.display.set_mode((constantes.ANCHO_PANTALLA, constantes.ALTURA_PANTALLA))

pygame.display.set_caption("Prueba kodland")



#Fuente
font = pygame.font.Font("./fuentes/fuente.ttf", 25)

font_perder = pygame.font.Font("./fuentes/fuente.ttf", 74)
perder_texto = font_perder.render('GAME OVER', True, constantes.COLOR_MALLA)

font_ganar = pygame.font.Font("./fuentes/fuente.ttf", 74)
ganar_texto = font_ganar.render('WINNER', True, constantes.COLOR_MALLA)

font_inicio = pygame.font.Font("./fuentes/fuente.ttf", 20)
font_titulo = pygame.font.Font("./fuentes/fuente.ttf", 74)

boton_jugar = pygame.Rect(constantes.ANCHO_PANTALLA/2-100, constantes.ALTURA_PANTALLA/2 - 50, 200, 50)
boton_salir = pygame.Rect(constantes.ANCHO_PANTALLA/2-100, constantes.ALTURA_PANTALLA/2 + 50, 200, 50)
texto_boton_jugar = font_inicio.render('JUGAR', True, constantes.COLOR_NEGRO)
texto_boton_salir = font_inicio.render('SALIR', True, constantes.COLOR_NEGRO)

def pantalla_inicio():
    ventana.fill(constantes.COLOR_ng)
    dibujar_puntuacion("Winter Game", font_titulo, constantes.COLOR_MALLA,
                       constantes.ALTURA_PANTALLA / 2 - 200,
                       constantes.ALTURA_PANTALLA / 2 - 200)
    pygame.draw.rect(ventana, constantes.COLOR_PUNTUACION, boton_jugar)
    pygame.draw.rect(ventana, constantes.COLOR_GOLPE, boton_salir)

    ventana.blit(texto_boton_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))



#importar imagenes
corazon1= pygame.image.load("./items/vida0.png").convert_alpha()
corazon1 = escalar_img(corazon1, constantes.ESCALA_VIDA)
corazon2= pygame.image.load("./items/vida1.png").convert_alpha()
corazon2 = escalar_img(corazon2, constantes.ESCALA_VIDA)
corazon3= pygame.image.load("./items/vida2.png").convert_alpha()
corazon3 = escalar_img(corazon3, constantes.ESCALA_VIDA)
corazon4= pygame.image.load("./items/vida3.png").convert_alpha()
corazon4 = escalar_img(corazon4, constantes.ESCALA_VIDA)
corazon5= pygame.image.load("./items/vida4.png").convert_alpha()
corazon5 = escalar_img(corazon5, constantes.ESCALA_VIDA)

#personaje
animaciones = []
for i in range (6):
    img = pygame.image.load(f"./movimiento/mov{i}.png")
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)

    animaciones.append(img)

#enemigos
directorio_enemigos = "./enemigos"
tipo_enemigos = nombres_carpetas(directorio_enemigos)
animaciones_enemigo = []

for eni in tipo_enemigos:
    lista_temp=[]
    ruta_temp = f"./enemigos/{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}{i}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo, constantes.ESCALA_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigo.append(lista_temp)

#Armas

imagen_secador = pygame.image.load(f"./armas/secador.png").convert_alpha()
imagen_secador = escalar_img(imagen_secador, constantes.ESCALA_SECADOR)


imagen_calor = pygame.image.load(f"./armas/calor.png").convert_alpha()
imagen_calor = escalar_img(imagen_calor, constantes.ESCALA_SECADOR)


tile_list = []
for x in range(7):
    tile_image = pygame.image.load(f"./items/tiles/mapa{x+1}.png")
    tile_image = pygame.transform.scale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
    tile_list.append(tile_image)












def dibujar_puntuacion(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x, y))


def vida_jugador():
    c_mitad_dibujado = False
    for i in range(5):
        if jugador.energia >= ((i+1)*20):
            ventana.blit(corazon5, (5+i*50, 5))
        elif jugador.energia == 0:
            ventana.blit(corazon1, (5 + i * 50, 5))
        elif jugador.energia % 25 >=0 and c_mitad_dibujado == False:
            ventana.blit(corazon3, (5+i*50, 5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon1, (5 + i * 50, 5))




world_data = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 3],
    [5, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 3],
    [5, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 1, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [5, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 3],
    [5, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]


world = Mundo()
world.process_data(world_data, tile_list)




def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.COLOR_MALLA, (x * constantes.ESCALA_CUADRICULA, 0), (x * constantes.ESCALA_CUADRICULA, constantes.ALTURA_PANTALLA))
        pygame.draw.line(ventana, constantes.COLOR_MALLA, (0, x * constantes.ESCALA_CUADRICULA), (constantes.ANCHO_PANTALLA, x * constantes.ESCALA_CUADRICULA))

#Importar imagenes









#crear jugador de la lcase personaje
jugador = Personaje(50,50, animaciones, 75)

#Crear Enemigo
mn1 = Personaje(300, 300, animaciones_enemigo[0], 80)
mn4 = Personaje(600, 200, animaciones_enemigo[0], 80)
mn5 = Personaje(200, 600, animaciones_enemigo[0], 80)
mn2 = Personaje(500, 400, animaciones_enemigo[1], 100)
mn3 = Personaje(500, 600, animaciones_enemigo[1], 100)



imagen_posion = pygame.image.load(f"./items/posion.png").convert_alpha()
imagen_posion = escalar_img(imagen_posion, constantes.ESCALA_POSION)


coin_image = []
ruta_img = "./items/moneda"
num_coin_images = contar_elementos(ruta_img)
for i in range(num_coin_images):
    img = pygame.image.load(f"./items/moneda/mon{i}.png")
    img = escalar_img(img, constantes.ESCALA_MONEDA)
    coin_image.append(img)


lista_enemigos = []
lista_enemigos.append(mn1)
lista_enemigos.append(mn2)
lista_enemigos.append(mn3)
lista_enemigos.append(mn4)
lista_enemigos.append(mn5)


#Crear arma de la clase armas
secador = arma(imagen_secador, imagen_calor)

#Crear un grupo de sprites
grupo_calor = pygame.sprite.Group()
grupo_damage_text = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()


moneda = Item(100, 100, 0, coin_image)
moneda2 = Item(300, 600, 0, coin_image)
moneda3 = Item(500, 180, 0, coin_image)
moneda4 = Item(200, 100, 0, coin_image)
moneda5 = Item(600, 700, 0, coin_image)
posion = Item(200, 200, 1, [imagen_posion])

grupo_items.add(moneda, moneda2, moneda3, moneda4, moneda5)
grupo_items.add(posion)

#temporal y borrar

#Variables del movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False


#--------------------------------------------------------------------------------------------
#No se cierra la ventana mientras hayan eventos de la libreria pygame
reloj = pygame.time.Clock()

mostrar_inicio = True
run = True
while run:
    if mostrar_inicio:
        pantalla_inicio()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir.collidepoint(event.pos):
                    run=False
    else:

        reloj.tick(constantes.FPS)

        ventana.fill(constantes.COLOR_ng)


        dibujar_grid()
        if jugador.vivo == True:

            #Movimiento del jugador
            delta_x = 0
            delta_y = 0

            if mover_derecha == True:
                delta_x = constantes.VELOCIDAD

            if mover_izquierda == True:
                delta_x = -constantes.VELOCIDAD

            if mover_arriba == True:
                delta_y = -constantes.VELOCIDAD

            if mover_abajo == True:
                delta_y = constantes.VELOCIDAD




            #mover el jugador
            jugador.movimiento(delta_x,delta_y, world.obstaculos_tiles)

            #Actualiza estado del jugador
            jugador.update()

            # Actualiza estado del enemigo
            for ene in lista_enemigos:
                ene.update()


            #actualiza el stado del arma
            calor = secador.update(jugador)
            if calor:
                grupo_calor.add(calor)
            for calor in grupo_calor:
                damage, pos_damage =calor.update(lista_enemigos, world.obstaculos_tiles)

                if damage:
                    damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.COLOR_GOLPE)
                    grupo_damage_text.add(damage_text)

            #actualizar golpe
            grupo_damage_text.update()

            #actualizar  items
            grupo_items.update( jugador)

            world.draw(ventana)

            #dibuja jugador
            jugador.dibujar(ventana)

            # dibuja enemigo
            for ene in lista_enemigos:
                if ene.energia == 0:
                    lista_enemigos.remove(ene)
                if ene.energia>0:
                    ene.enemigos(jugador, world.obstaculos_tiles)
                    ene.dibujar(ventana)

            #dibuja el arma
            secador.dibujar(ventana)

            #dibujar balas
            for calor in grupo_calor:
                calor.dibujar(ventana)

            #dibujar vida
            vida_jugador()

            # dibujar_textos
            grupo_damage_text.draw(ventana)
            dibujar_puntuacion(f"Puntuacion: {jugador.score}", font, constantes.COLOR_PUNTUACION, 700, 5)


            #dibujar items
            grupo_items.draw(ventana)
        if jugador.score == 5:
            ventana.fill(constantes.COLR_VERDE)
            text_rect = ganar_texto.get_rect(center=(constantes.ANCHO_PANTALLA / 2, constantes.ALTURA_PANTALLA / 2))
            ventana.blit(ganar_texto, text_rect)

        if jugador.vivo == False:
            ventana.fill(constantes.ROJO_OSCURO)
            text_rect = perder_texto.get_rect(center=(constantes.ANCHO_PANTALLA/2, constantes.ALTURA_PANTALLA/2))
            ventana.blit(perder_texto, text_rect)



        for event in pygame.event.get():
            #cerrar el juego
            if event.type == pygame.QUIT:
                run = False

            #movimiento
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True

                if event.key == pygame.K_w:
                    mover_arriba = True

                if event.key == pygame.K_s:
                    mover_abajo = True

                if event.key == pygame.K_d:
                    mover_derecha = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False

                if event.key == pygame.K_w:
                    mover_arriba = False

                if event.key == pygame.K_s:
                    mover_abajo = False

                if event.key == pygame.K_d:
                    mover_derecha = False


        pygame.display.update()

pygame.quit()

#--------------------------------------------------------------------------------------------