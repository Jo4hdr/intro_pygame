import pygame
import sys
import math
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,195,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
marron = (128, 0, 0)
gris = (128, 128, 128)
PI = math.pi
 
numero_lineas = 100

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Trabajo en clase")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # Rellenar la ventana de color 
    ventana.fill(marron)

    # Rectangulo sin relleno, esquina sup. izq: (100,100), esquina . inf, der: (150,200), Y de grosor 1.
    pygame.draw.rect(ventana, blanco, ((50,100), (400,350)), 1)


    # Texto
    # Fuente de tipo Arial,tamaño 35, negrilla y cursiva
    fuente_arial = pygame.font.SysFont("Arial", 30, 1,1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1,blanco)
    ventana.blit(texto,(30,20))

    fuente_arial = pygame.font.SysFont("Arial", 20 ,1)
    texto = fuente_arial.render("Especialidad Sistemas", 1,gris)
    ventana.blit(texto,(135,60))

    fuente_arial = pygame.font.SysFont("Arial", 25 , 1,1)
    texto = fuente_arial.render("Johan Stiven Fiallo Aparicio", 1,negro)
    ventana.blit(texto,(85,460))

    # lineas
    for i in range(numero_lineas):
        linea1 = random.randint(50,50 + 400)
        linea2 = random.randint(100,100 + 350)
        linea3 = random.randint(50,20 + 400)
        linea4 = random.randint(100,100 + 350)

        color_linea = random.choice((rojo,azul,verde,rosado,amarillo,naranja,cian))
        pygame.draw.line(ventana,color_linea,(linea1,linea2),(linea3,linea4))

    # Actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################
