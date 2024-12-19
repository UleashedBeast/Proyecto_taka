#import pygame
from OpenGL.GL import *
import math

def draw_camera(drone_position):
    """Dibuja un objeto rectangular que representa la cámara del drone a 45 grados atrás."""

    glColor3f(1, 1, 1)  # Vectores blancos para indicar el ángulo de visión
    
    glPushMatrix()
    # Posición de la cámara en el drone
    glTranslatef(drone_position[0], drone_position[1] + 0.5, drone_position[2] - 1)
    glRotatef(45, 1, 0, 0)  # Giro a 45 grados respecto al drone
    glBegin(GL_LINES)
    
    # Vectores de la cámara indicando su ángulo de visión
    glVertex3f(-0.5, 0, -0.5)  # Punto 1
    glVertex3f(0.5, 0, -0.5)   # Punto 2
    
    glVertex3f(-0.5, 0, 0.5)   # Punto 3
    glVertex3f(0.5, 0, 0.5)    # Punto 4
    
    glVertex3f(-0.5, 0, -0.5)  # Punto 5
    glVertex3f(-0.5, 0, 0.5)   # Punto 6
    
    glVertex3f(0.5, 0, -0.5)   # Punto 7
    glVertex3f(0.5, 0, 0.5)    # Punto 8
    glEnd()
    glPopMatrix()