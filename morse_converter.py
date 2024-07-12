from pathlib import Path
import platform
import pygame
import time
import os


# Define constants for Morse signs and Morse code dictionary
SHORT_SIGN = '•'
LONG_SIGN = '-'
SPACE_SIGN = '╱'
morse_book = {
    'a': '•-', 'b': '-•••', 'c': '-•-•', 'd': '-••', 'e': '•', 'f': '••-•',
    'g': '--•', 'h': '••••', 'i': '••', 'j': '•---', 'k': '-•-', 'l': '•-••',
    'm': '--', 'n': '-•', 'o': '---', 'p': '•--•', 'q': '--•-', 'r': '•-•',
    's': '•••', 't': '-', 'u': '••-', 'v': '•••-', 'w': '•--', 'x': '-••-',
    'y': '-•--', 'z': '--••', '1': '•----', '2': '••---', '3': '•••--',
    '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••', '8': '---••',
    '9': '----•', '0': '-----', ' ': '╱'
}


def text_to_morse(text):
    return ' '.join(morse_book.get(char, 'ERR') for char in text.lower())


def morse_converter():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    pygame.mixer.init()

    short_beep = pygame.mixer.Sound(Path("assets/fx/short_beep.mp3"))
    long_beep = pygame.mixer.Sound(Path("assets/fx/long_beep.mp3"))

    while True:

        original_text = input('Enter text [a-z0-9]:\n> ')
        converted_text = text_to_morse(original_text)

        if 'ERR' not in converted_text:
            print(f'Morse code: {converted_text}\n'
                  f'--------------------------------------------------------')
            for morse in converted_text:
                sound = short_beep if morse == SHORT_SIGN else long_beep if morse == LONG_SIGN else None
                if sound:
                    sound.play()
                time.sleep(0.2 if morse == SHORT_SIGN else 0.4)
        else:
            print('Text contains chars that are not defined in the morse book.')


if __name__ == '__main__':
    morse_converter()
