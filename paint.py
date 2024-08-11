import pygame as pg

WINDOW_SIZE = (1000,500)

# Colors
WHITE = (255, 255, 255)
GREY = (175, 175, 175)

def main():
    # Initialize
    pg.init()
    running = True

    screen = pg.display.set_mode(WINDOW_SIZE, pg.RESIZABLE)
    pg.display._set_autoresize(False)
    # screen.fill(WHITE)
    screen.fill(GREY)

    mouse_prev_x = 0
    mouse_prev_y = 0
    mouse_down = False
    # Inifinite loop
    while (running):
        if (mouse_down):
            mouse_x, mouse_y = pg.mouse.get_pos()
            if (mouse_prev_x != 0 and mouse_prev_y != 0):
                pg.draw.line(screen, (0, 0, 0), (mouse_prev_x, mouse_prev_y), (mouse_x, mouse_y))
            mouse_prev_x = mouse_x
            mouse_prev_y = mouse_y
        # Event listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                print("Mouse button clicked!")
                mouse_down = True
            if event.type == pg.MOUSEBUTTONUP:
                print("Mouse button up!")
                mouse_down = False
                mouse_prev_x = 0
                mouse_prev_y = 0
            if event.type == pg.WINDOWRESIZED:
                screen = pg.display.get_surface()
                screen.fill(WHITE)
        # Refresh display
        pg.display.update()
    pg.quit()

if __name__ == "__main__":
    main()
