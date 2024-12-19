from OpenGL.GL import *

def draw_base():
    """Dibuja el terreno infinito con cuadrícula de líneas verdes."""
    glColor3f(0, 1, 0)  # Verde fluor
    glBegin(GL_LINES)

    # Líneas horizontales
    for z in range(-50, 51):
        glVertex3f(-50, 0, z)
        glVertex3f(50, 0, z)

    # Líneas verticales
    for x in range(-50, 51):
        glVertex3f(x, 0, -50)
        glVertex3f(x, 0, 50)

    glEnd()
