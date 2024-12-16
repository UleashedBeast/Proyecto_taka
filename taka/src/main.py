import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW_COLOR = (0, 0, 0)  # Color de fondo (negro)
DRONE_COLOR = (255, 0, 0)  # Rojo
DRONE_SIZE = 20
VELOCITY = 5
GRID_SIZE = 50  # Tamaño de los cuadrados de la grilla

# Inicializar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Drone - Entorno con Vectores")

# Posición inicial del drone
drone_x = WIDTH // 2
drone_y = HEIGHT // 2

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Salir con la X de la ventana
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el drone con WASD
    if keys[pygame.K_w]:  # Arriba
        drone_y -= VELOCITY
    if keys[pygame.K_s]:  # Abajo
        drone_y += VELOCITY
    if keys[pygame.K_a]:  # Izquierda
        drone_x -= VELOCITY
    if keys[pygame.K_d]:  # Derecha
        drone_x += VELOCITY

    # Limpiar la pantalla
    screen.fill(WINDOW_COLOR)

    # Dibuja el suelo como cuadrículas
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect, 1)  # Cuadrícula con borde verde fluor

    # Dibuja el drone
    pygame.draw.rect(screen, DRONE_COLOR, (drone_x, drone_y, DRONE_SIZE, DRONE_SIZE))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()
