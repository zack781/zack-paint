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

    # Inifinite loop
    while (running):
        # Event listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                print("Mouse button clicked!")
            if event.type == pg.WINDOWRESIZED:
                screen = pg.display.get_surface()
                screen.fill(WHITE)
        # Refresh display
        pg.display.update()
    pg.quit()

if __name__ == "__main__":
    main()
