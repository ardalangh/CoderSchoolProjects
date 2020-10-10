"""
Snake with PyGame 
Ardy Ghoorchian 
"""

from gui import*

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 10


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction



# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    
    """
    The line above listens for an event. which in this case is when you press the key while you are playing the game and based on
    What you press, it will change the "change_to" variable. it is not so important for you to understand how that happens
    what is really important for you to understand is that after that infromation is given to you now how do you change the 
    poisition of your snake.

    1.  Making sure the snake cannot move in the opposite direction instantaneously
    """
    if change_to =='UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to =="DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    



    """
    2. Moving the snake
    """

    if direction =="UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] +=10
    if direction =="LEFT":
        snake_pos[0] -=10
    if direction == "RIGHT":
        snake_pos[0] += 10 
    
   
   """
   3.Snake body growing mechanism
   replace the commented line with code
   """
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    
    """
    4.Spawning food on the screen
    you do not need to writ anything for this part but you should be able to understand what it means 
    """
    if food_spawn == False:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True


    # The code below is in charge of GUI code (NOT FOR YOU)
    # ASK ME IF YOU ARE CURIOUS TO LEARN ABOUT THESE LINES 
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))




    """
    4.Game Over conditions
    uncomment the code if it is commented and fill in the blanks 
    The code is in charge of  calling the game over function when we break the rules of the game
    a.  when we go out of bounds 
    b.  when we hit ourseleves 
    """

    
    
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()

    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()





    # DO NOT WORRY ABOUT THE CODE BELOW 
    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(difficulty)