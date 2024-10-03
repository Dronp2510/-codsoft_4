import pygame
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)



rock_img = pygame.image.load('rps_rock.png')
paper_img = pygame.image.load('rps_paper.png')
scissors_img = pygame.image.load('rps_scissors.png')


rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))


choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    # player_score = 0
    # computer_score = 0
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def display_text(text, x, y):
    result_text = font.render(text, True, WHITE)
    text_rect = result_text.get_rect(center=(WIDTH // 2, y))
    screen.blit(result_text, text_rect)

def draw_button(text, x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    x = (WIDTH - width) // 2

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    button_text = font.render(text, True, BLACK)
    screen.blit(button_text, (x + 10, y + 10))

def reset_game():
    global player_choice, computer_choice, result
    player_choice = None
    computer_choice = None
    result = None

running = True
player_choice = None
computer_choice = None
result = None

while running:
    screen.fill(BLACK)

    if not player_choice:
        display_text("Pick a choice." , 50 , 50)

    screen.blit(rock_img, (50, 150))
    screen.blit(paper_img, (250, 150))
    screen.blit(scissors_img, (450, 150))

    # display_text(f"Player Score: {player_score}", 0 , 10)  # Display player score
    # display_text(f"Computer Score: {computer_score}", 100 , 10)  # Display computer score


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not result:
            x, y = event.pos
            if 50 <= x <= 150 and 150 <= y <= 250:
                player_choice = 'rock'
            elif 250 <= x <= 350 and 150 <= y <= 250:
                player_choice = 'paper'
            elif 450 <= x <= 550 and 150 <= y <= 250:
                player_choice = 'scissors'

            if player_choice:
                computer_choice = get_computer_choice()
                result = determine_winner(player_choice, computer_choice)


    if player_choice and computer_choice:
        display_text(f"Player Choice: {player_choice.capitalize()}", 50 , 50)
        display_text(f"Computer Choice: {computer_choice.capitalize()}", 350 , 100)
        display_text(result, 230, 300)
        draw_button("Play Again", 240, 350, 145, 40, GREEN, RED, reset_game)

    pygame.display.flip()


pygame.quit()
