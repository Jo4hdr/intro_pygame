# importamos la libreria pygame

import pygame

# inicializamos los modulos de pygame

pygame.init()

# Establecer titulo a la ventana

pygame.display.set_caption("surface")

# Establecemos las dimenciones de la ventana

ventana = pygame.display.set_mode((400,400))

# definimos un color
amarillo = (255,255,0)
azul = (0,0,255)
rojo = (255,0,0)
# creamos una superficie

amarillo_superficie = pygame.Surface((400,200))
azul_superficie = pygame.Surface((400,100))
rojo_superficie = pygame.Surface((400,100))

# rellenamos la superficie de azul

amarillo_superficie.fill((amarillo))
azul_superficie.fill((azul))
rojo_superficie.fill((rojo))

# inserto o muevo la superficie en la ventana

ventana.blit(amarillo_superficie, (0,0))
ventana.blit(azul_superficie, (0,200))
ventana.blit(rojo_superficie, (0,300))

# actualiza la visualizacion de la ventana

pygame.display.flip()

# bucle del juego

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit() 