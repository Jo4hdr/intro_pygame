# Estructura de un juego en pygame

## Inicializacion

como en todo programa en python, se deben importar los modulos o librerias a utilizar.

`import pygame`

- inicializar pygame usando la funcion init(). Inicializa todos los modulos de pygame importados.

``pygame.init()``

## Visualizacion de la ventanz

``ventana= pygame.display.set_mode((600,400))``

- set_mode es la funcon encargada de definir el tamaño de la ventana. En el ejemplo se esta definiendo una ventana de 600 pixeles de ancho y 400 pixeles de alto. 

``pygame.display.set_caption("mi ventana")``

- set_caption es la funcion que añade un titulo a la ventana.

### Funcion set_mode()

``set_mode(size =(0,0), flags = 0, depth = 0, display = 0)``

- size = (600,400) : define el tamaño de la ventana
- flags : define uno o mas comportamientos para la ventana
    - valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla completa, dimensiones modificables.

## Bucle de juego - game loop

- bucle infinito quese interrumpira al cumplir ciertos criterios 

- reloj interno del juego

- en cada interacion del buce del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado a otro, o que se a cruzado la linea de llegada lo que quiere decir que la partida ha terminado.

- cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado de la partida.

- en cada iteracion se realisan las siguientes tareas:
    1. comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteracion actual
    3. Obtener las entradas del sistemas, o de interaccion con el jugador.
    4. actualizar todas las identidades que
    caracterizan el juego.
    5. refrescar la pantalla.

## Superficies pygame

- Superficie: 
    - elemento geometrico 
    - linea , poligono, imagen, texto, que se muestra en la pantalla.
    - El poligono se puede o no rellenar de color.
    - Las supericies se crean de diferente manera dependiendo del tipo:
        - imagen: image.load()
        - texto: font.render()
        - superficie generica: con pygame.surface()
        - ventana del juego: pygame.display.set_mode()

# Ejemplo bandera de colombia 
```# importamos la libreria pygame

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
```
![imagen bandera](screen02.png)