import pygame
import pygame_menu

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width,height))
game_speed = 25
game_size = 600
border_width = 10
border_color = "Grey"
clock = pygame.time.Clock()

score = 0

def main_menu():
    main_menu = pygame_menu.Menu("Snake Game", width=width, height=height, theme=pygame_menu.themes.THEME_DARK)
    main_menu.add.button("Play", game_loop)
    main_menu.add.button("Options", options_menu)
    main_menu.add.button("Exit", pygame_menu.events.EXIT)
    main_menu.mainloop(screen)

def options_menu():
    screen.fill("black")
    options_menu = pygame_menu.Menu("Options", width, height, theme=pygame_menu.themes.THEME_DARK)
    options_menu.add.selector("Game Size: ", [("Small", 400), ("Medium", 500), ("Large", 700)], onchange = set_game_size)
    options_menu.add.selector(title="Speed: ", items=[("Slow", 25), ("Fast", 50), ("Faster", 75)], onchange = set_game_speed)
    options_menu.add.button("Back to Main Menu", main_menu)
    options_menu.mainloop(screen)

def esc_menu():
    screen.fill("black")
    esc_menu = pygame_menu.Menu("Options", width, height, theme=pygame_menu.themes.THEME_DARK)
    esc_menu.add.button("Back to Main Menu", main_menu)
    esc_menu.mainloop(screen)

def set_game_speed(selected_value,speed):
    global game_speed
    game_speed = speed

def set_game_size(selected_value,size):
    global game_size
    game_size = size

def draw_grid(screen):
    borderdiff = (width - game_size) // 2
    pygame.draw.line(screen, border_color, (borderdiff, borderdiff), (width - borderdiff, borderdiff), border_width)
    pygame.draw.line(screen, border_color, (borderdiff, borderdiff), (borderdiff, height - borderdiff), border_width)
    pygame.draw.line(screen, border_color, (borderdiff, height - borderdiff),(width - borderdiff, height - borderdiff), border_width)
    pygame.draw.line(screen, border_color, (width - borderdiff, borderdiff), (width - borderdiff, height - borderdiff), border_width)

def show_score():
    score_font = pygame.font.SysFont("consolas",40)
    score_surface = score_font.render("Score: " + str(score), True, "Yellow")
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width//2, 10)
    screen.blit(score_surface, score_rect)

class Snake:
    def __init__(self):
        ...

def handle_movement(keys):
    ...

def game_loop():
    while True:
        screen.fill("black")
        draw_grid(screen)
        show_score()

        pygame.display.update()

def main():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        screen.fill("black")
        main_menu()

        pygame.display.update()

        clock.tick(game_speed)

if __name__  == "__main__":
    main()