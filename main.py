from data import *
from Button import *

import sys
import pygame
import random

pygame.mixer.pre_init(44100, -16, 1, 512)  # TO REDUCE SOUND DELAY

pygame.init()

screenWidth, screenHeight = (1280, 720)
screenCenter = (screenWidth / 2, screenHeight / 2)
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Hanged man game by Bastien")
default_font = pygame.font.SysFont(None, 40)

images["bg"] = pygame.transform.scale(images["bg"], (screenWidth, screenHeight + 200))  # resize bg image

letters = []
j = 0  # TO ALIGN THE LETTERS ON THE SCREEN (VERTICALLY)

for number, letter in enumerate(alphabet):
    if number > 12:  # TO ALIGN THE LETTERS ON THE SCREEN (HORIZONTALLY)
        number = number - 13
        j = 1
    letters.append(Button(colors["gray"], (70 + number * 90, 140 + j * 60), 50, 50, letter))

errorCount = 0
guessed = []

currentWord = random.randrange(0, len(wordsEN))
print(wordsEN[currentWord])

lineWidth = 40  # WIDTH OF THE LINE FOR THE LETTERS
lineSpace = 10  # SPACE BETWEEN THE LINES

# needRestart = False  # FOR CONDITIONS IN WHICH YOU NEED TO RESTART THE GAME, LIKE CHANGING THE LANGUAGE
winCount = 0
pointCount = 0
spaceCount = 0  # COUNTING HOW MANY SPACES A WORD HAS, IT'LL BE IMPORTANT WHEN CHECKING

for letter in wordsEN[currentWord]:
    if letter == " ":
        spaceCount += 1

# Loading sounds to a dictionary
sounds = {"win": pygame.mixer.Sound("sound/win.wav"), "lose": pygame.mixer.Sound("sound/lose.wav"),
          "click": pygame.mixer.Sound("sound/click.wav"), "music": pygame.mixer.Sound("sound/music.wav")}


def mouse_motion():
    for letter_button in letters:  # Check if mouse is on any button, button position got by calling get_rect()
        currentRect = letter_button.subsurface.get_rect(topleft=(letter_button.pos[0], letter_button.pos[1]))
        if currentRect.collidepoint(pygame.mouse.get_pos()):  # if colliding with mouse cursor
            letter_button.rollOver = True
        else:
            letter_button.rollOver = False


if __name__ == "__main__":
    sounds["music"].play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_motion()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # LEFT CLICK
                    for button in letters:
                        if button.rollOver and not button.clicked:
                            sounds["click"].play()
                            button.clicked = True
                            guessed.append(button.letter)
                            noError = False

                            for letter in wordsEN[currentWord]:
                                if button.letter == letter:
                                    noError = True

                            if errorCount < 6 and not noError:
                                errorCount += 1

        screen.fill(colors["white"])
        screen.blit(images["bg"], (0, -100))
        screen.blit(images[errorCount], (screenCenter[0] - images[errorCount].get_rect().width / 2 + 120,
                                         screenCenter[1] - images[errorCount].get_rect().height / 2 + 150))

        for letter in letters:
            letter.draw(screen)

        stats_font = pygame.font.SysFont(None, 25, False, True)
        winCountText = stats_font.render("Total wins       : " + str(winCount), True, colors["black"])
        pointCountText = stats_font.render("Total points    : " + str(pointCount), True, colors["black"])
        screen.blit(winCountText, (30, 300))
        screen.blit(pointCountText, (30, 330))

        totalShown = 0

        for i, letter in enumerate(wordsEN[currentWord]):
            text = default_font.render(letter, True, colors["black"])
            posX = (screenWidth - len(wordsEN[currentWord]) * (lineWidth + lineSpace)) / 2 + i * (lineWidth + lineSpace)
            posY = 100
            if letter != " ":
                pygame.draw.rect(screen, colors["black"], (posX, posY, lineWidth, 3))
            if letter in guessed:
                totalShown += 1
                screen.blit(text, (posX + lineWidth / 3, posY - 30))

        pygame.display.update()

        final_font = pygame.font.SysFont(None, 80)
        lose_text = final_font.render("You lose", True, colors["darkred"])
        win_text = final_font.render("You win", True, colors["darkgreen"])

        if errorCount >= 6:
            sounds["lose"].play()
            screen.blit(lose_text, (500, 300))
            pygame.display.update()
            pygame.time.wait(1000)

            # RESET ALL

            guessed.clear()
            pointCount = 0
            errorCount = 0
            winCount = 0
            for letter in letters:
                letter.clicked = False
            currentWord = random.randrange(0, len(wordsEN))
            print(wordsEN[currentWord])
            spaceCount = 0
            for letter in wordsEN[currentWord]:
                if letter == " ":
                    spaceCount += 1
            pygame.time.wait(1000)

        if totalShown == len(wordsEN[currentWord]) - spaceCount:  # win
            sounds["win"].play()
            screen.blit(win_text, (520, 270))
            pygame.display.update()
            pygame.time.wait(1000)
            guessed.clear()
            pointCount += 600 + winCount * 10 - errorCount * 100
            errorCount = 0
            winCount += 1

            for letter in letters:
                letter.clicked = False
            currentWord = random.randrange(0, len(wordsEN))
            print(wordsEN[currentWord])
            spaceCount = 0
            for letter in wordsEN[currentWord]:
                if letter == " ":
                    spaceCount += 1
            pygame.time.wait(1000)
