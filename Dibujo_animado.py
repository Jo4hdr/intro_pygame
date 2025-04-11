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
gris_os = (51,47,44)
amarillo_pas = (253,253,150)
rojo_claro = (255,105,97)
PI = math.pi
 
numero_lineas = 100

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Trabajo en clase")

clock = pygame.time.Clock()

cara = 0
direccion = 1

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

    cara += direccion
    if cara > 3 or cara < -3:
        direccion *= -1

    # Rellenar la ventana de color 
    ventana.fill(marron)


     # Rectangulo relleno, ubicado en la coordenada sup. izq(200,200), y de ancho 200 y altura 100
    pygame.draw.rect(ventana, azul, (50,100, 400,350))


    # Circulo"area"

    pygame.draw.circle(ventana , gris, (120,310), 70, 100) 

    # REctangulo
    pygame.draw.rect(ventana, gris, ((130,240), (310,150)), 100)
    pygame.draw.rect(ventana, blanco, ((120,250), (10,130)), 100)
    pygame.draw.rect(ventana, negro, ((80,220), (40,180)), 100)
    pygame.draw.rect(ventana, gris_os, ((140,190), (40,50)), 100)
    pygame.draw.rect(ventana, naranja, ((125,180), (70,30)), 100)
    pygame.draw.rect(ventana, gris_os, ((270,110), (140,130)), 100)
    pygame.draw.rect(ventana, blanco, ((305,160), (70,70)), 100)
    pygame.draw.rect(ventana, naranja, ((255,120), (170,30)), 100)
    pygame.draw.rect(ventana, naranja, ((260,110), (160,10)), 100)
 
    # Dibujar un circul
    # Centro del circulo: (300,100)
    # Radio del circulo : 100
    # Grosor contorno circulo : 1
    pygame.draw.circle(ventana , verde, (400,400), 50, 100)
    pygame.draw.circle(ventana , gris_os, (180,400), 50, 100)
    pygame.draw.circle(ventana , amarillo, (290,400), 50, 100)

    # Rectangulo sin relleno, esquina sup. izq: (100,100), esquina . inf, der: (150,200), Y de grosor 1.
    pygame.draw.rect(ventana, negro, ((200,385), (70,30)), 100)
    pygame.draw.rect(ventana, negro, ((310,385), (70,30)), 100)

    # Cara 

    pygame.draw.circle(ventana , amarillo, (340 + cara,190), 40, 100)
    pygame.draw.circle(ventana , blanco, (360 + cara,185), 15, 100)
    pygame.draw.circle(ventana , blanco, (320 + cara,185), 15, 100)
    pygame.draw.circle(ventana , gris, (320 + cara,185), 5, 100)
    pygame.draw.circle(ventana , gris, (360 + cara,185), 5, 100)
    pygame.draw.circle(ventana , rojo_claro, (340 + cara,210), 10, 100)
    
    
    # cejas
    pygame.draw.line(ventana,amarillo_pas,(330,175),(320,165),5)
   




    # Texto
    # Fuente de tipo Arial,tamaño 35, negrilla y cursiva
    fuente_arial = pygame.font.SysFont("Arial", 30, 1,1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1,blanco)
    ventana.blit(texto,(30,20))

    fuente_arial = pygame.font.SysFont("Arial", 20 ,1)
    texto = fuente_arial.render("Especialidad Sistemas", 1,gris)
    ventana.blit(texto,(135,60))

    fuente_arial = pygame.font.SysFont("Arial", 20 , 1,1)
    texto = fuente_arial.render("Johan Stiven Fiallo Aparicio", 1,negro)
    ventana.blit(texto,(150,300))



    # Actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################