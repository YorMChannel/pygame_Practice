import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pygame Practice")

background = pygame.image.load("C:/Users/User/Desktop/Python Lang/workspace/pygame_Practice/background.png")

character = pygame.image.load("C:/Users/User/Desktop/Python Lang/workspace/pygame_Practice/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1 
            elif event.key == pygame.K_UP:
                to_y -= 1 
            elif event.key == pygame.K_DOWN: 
                to_y += 1
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width: 
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos + character_height > screen_height: 
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()