import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from drone import draw_drone, update_physics, move_drone
from terrain import draw_base

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, -1.0, -20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Controles del drone
        keys = pygame.key.get_pressed()
        move_drone(keys)

        # Actualizar físicas
        update_physics()

        # Renderizar la escena
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_base()
        draw_drone()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
