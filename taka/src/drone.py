import pygame
from OpenGL.GL import *
import math

# Variables globales para la posición y físicas del drone
drone_position = [0, 5, 0]  # Posición inicial del drone
drone_velocity = [0, 0, 0]  # Velocidad inicial del drone
gravity = -0.01  # Gravedad simulada
propeller_angle = 0  # Ángulo de rotación de las hélices

def draw_drone():
    """Dibuja el drone en forma de X con líneas de colores y hélices giratorias."""
    global propeller_angle
    
    glBegin(GL_LINES)
    # Línea roja
    glColor3f(1, 0, 0)
    glVertex3f(drone_position[0] - 1, drone_position[1], drone_position[2] - 1)
    glVertex3f(drone_position[0] + 1, drone_position[1], drone_position[2] + 1)
    
    # Línea azul
    glColor3f(0, 0, 1)
    glVertex3f(drone_position[0] + 1, drone_position[1], drone_position[2] - 1)
    glVertex3f(drone_position[0] - 1, drone_position[1], drone_position[2] + 1)
    glEnd()
    
    # Dibujar hélices en cada extremo
    glColor3f(1, 1, 1)  # Hélices blancas
    draw_propeller(drone_position[0] - 1, drone_position[1], drone_position[2] - 1, propeller_angle)
    draw_propeller(drone_position[0] + 1, drone_position[1], drone_position[2] + 1, propeller_angle)
    draw_propeller(drone_position[0] + 1, drone_position[1], drone_position[2] - 1, propeller_angle)
    draw_propeller(drone_position[0] - 1, drone_position[1], drone_position[2] + 1, propeller_angle)
    
    # Actualizar el ángulo de las hélices para que giren
    propeller_angle = (propeller_angle + 10) % 360

def draw_propeller(x, y, z, angle):
    """Dibuja una pequeña X que representa una hélice, con rotación."""
    size = 0.3  # Tamaño de las hélices
    
    glPushMatrix()
    glTranslatef(x, y, z)  # Mover a la posición de la hélice
    glRotatef(angle, 0, 1, 0)  # Rotar alrededor del eje Y
    
    # Dibujar la pequeña X
    glBegin(GL_LINES)
    glVertex3f(-size, 0, -size)
    glVertex3f(size, 0, size)
    glVertex3f(-size, 0, size)
    glVertex3f(size, 0, -size)
    glEnd()
    glPopMatrix()

def update_physics():
    """Actualiza las físicas del drone (gravedad y colisión con el suelo)."""
    global drone_position, drone_velocity
    drone_velocity[1] += gravity  # Aplicar gravedad
    drone_position[1] += drone_velocity[1]

    # Limitar caída al suelo
    if drone_position[1] < 0:
        drone_position[1] = 0
        drone_velocity[1] = 0

def move_drone(keys, move_speed=0.5):
    """Controla el movimiento del drone basado en teclas presionadas."""
    if keys[pygame.K_w]:
        drone_position[2] -= move_speed
    if keys[pygame.K_s]:
        drone_position[2] += move_speed
    if keys[pygame.K_a]:
        drone_position[0] -= move_speed
    if keys[pygame.K_d]:
        drone_position[0] += move_speed
    if keys[pygame.K_SPACE]:
        drone_velocity[1] = 0.2
    if keys[pygame.K_LCTRL]:
        drone_velocity[1] = -0.2