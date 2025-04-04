# importamos la libreria pygame

import pygame

# inicializamos los modulos de pygame

pygame.init()

# Establecer titulo a la ventana

pygame.display.set_caption("surface")

# Establecemos las dimenciones de la ventana

ventana = pygame.display.set_mode((300,300))

# definimos un color

azul = (180, 27, 219)

# creamos una superficie

azul_superficie = pygame.Surface((300,300))

# rellenamos la superficie de azul

azul_superficie.fill((azul))

# inserto o muevo la superficie en la ventana

ventana.blit(azul_superficie, (0,0))

# actualiza la visualizacion de la ventana

pygame.display.flip()

# bucle del juego

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit() 