import imp
import pygame                                               #kniznica
import random
import sys
from config import config

def update_position(snake, direction, step):                          # pohyb hadika
    if direction == "UP":                                       # pokud jede nahoru....
        snake = [snake[0],snake[1] -step]                          # posune hadina nahoru o hodnotu step
    if direction == "DOWN":                                      
        snake = [snake[0],snake[1] + step] 
    if direction == "LEFT":                                      
        snake = [snake[0] -step, snake[1]] 
    if direction == "RIGHT":                                      
        snake = [snake[0] +step, snake[1]] 
    return snake                

def update_direction(direction, keys):
    if keys [pygame.K_LEFT]:
        return "LEFT" if direction != "RIGHT" else direction                # nesmi se vracet pres sebe
    if keys [pygame.K_RIGHT]:
        return "RIGHT" if direction != "LEFT" else direction 
    if keys [pygame.K_UP]:
        return "UP" if direction != "DOWN" else direction 
    if keys [pygame.K_DOWN]:
        return "DOWN" if direction != "UP" else direction 
    return direction

def is_out(snake, game_res):
    if snake[0] < 0 or snake[1] < 0 or snake[0] > game_res[0] or snake[1] > game_res[1]:
        return True
    return False 

def generate_apple(game_res, snake_size):
    x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
    y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
    return [x, y]

def is_collision(snake_head, apple):
    if snake_head[0] == apple[0] and snake_head[1] == apple[1]:
        return True
    return False

def end_game(window):                                           # definovani funkce 
    print("GAME OVER")
    window.fill(config.BACKGROUND_COLOR)
    pygame.quit()
    sys.exit() 


if __name__ == "__main__":                                  #musi byt zapsane
    pygame.init()        
    clock = pygame.time.Clock()                                   # musi byt zapsane
    window = pygame.display.set_mode(config.GAME_RES)
    snake = [[config.GAME_RES[0]//2, config.GAME_RES[1]//2]]      #pozice hadika - 0 = osa X / 1 = osa Y
    apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
    direction = "UP"                                            # akym smerom pojde had na zaciatku
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                           # pokud zmacknu X v liste, hra se vypne
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        direction = update_direction(direction, keys)
        new_position = update_position(snake[0], direction, config.SNAKE_SIZE)
        snake.insert(0, new_position)
        if is_collision(snake[0], apple):
            print("Collision")
            apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE) 
        else:
            snake.pop()                                                             # smaze chvost hada    

        if is_out(snake[0], config.GAME_RES):
            end_game(window)

        for part in snake:
            pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(part[0], part[1], config.SNAKE_SIZE, config.SNAKE_SIZE))         #Kde bude hadik (stvorec)
        pygame.draw.rect(window, config.APPLE_COLOR,pygame.Rect(apple[0], apple[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        pygame.display.update() 
        window.fill(config.BACKGROUND_COLOR)        # vyplni zadek hadika cernou barvou
        clock.tick(config.GAME_FPS)                 #spomaluje cyklus obnovy
