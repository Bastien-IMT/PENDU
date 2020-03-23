import pygame
import string

# Assigning all the primary/secondary colors to a dictionary to use more practically
colors = {"black": (0, 0, 0), "darkgray": (70, 70, 70), "gray": (128, 128, 128), "lightgray": (200, 200, 200),
          "white": (255, 255, 255), "red": (255, 0, 0),
          "darkred": (128, 0, 0), "green": (0, 255, 0), "darkgreen": (0, 128, 0), "blue": (0, 0, 255),
          "navy": (0, 0, 128), "darkblue": (0, 0, 128),
          "yellow": (255, 255, 0), "gold": (255, 215, 0), "orange": (255, 165, 0), "lilac": (229, 204, 255),
          "lightblue": (135, 206, 250), "teal": (0, 128, 128),
          "cyan": (0, 255, 255), "purple": (150, 0, 150), "pink": (238, 130, 238), "brown": (139, 69, 19),
          "lightbrown": (222, 184, 135), "lightgreen": (144, 238, 144),
          "turquoise": (64, 224, 208), "beige": (245, 245, 220), "honeydew": (240, 255, 240),
          "lavender": (230, 230, 250), "crimson": (220, 20, 60)}

# Loading images to a dictionary
images = {"bg": pygame.image.load("img/bg.jpg"), "play": pygame.image.load("img/play.png"),
          0: pygame.image.load("img/tree/0.png"),
          1: pygame.image.load("img/tree/1.png"), 2: pygame.image.load("img/tree/2.png"),
          3: pygame.image.load("img/tree/3.png"), 4: pygame.image.load("img/tree/4.png"),
          5: pygame.image.load("img/tree/5.png"), 6: pygame.image.load("img/tree/6.png")}

alphabet = list(string.ascii_uppercase)  # Getting all the letters in the latin alphabet

wordsEN = ["NEW YORK", "WASHINGTON", "LAS VEGAS", "CALIFORNIA", "TEXAS", "MEXICO", "LONDON",
           "ENGLAND", "AMERICA", "BRAZIL", "CHILE", "ARGENTINA", "AUSTRALIA",
           "GREECE", "AFRICA", "EGYPT", "CHINA", "JAPAN", "JAPANESE", "ASTRONOMY", "METEORITE", "STAR", "SOLAR SYSTEM",
           "GALAXY", "BURGER", "BURGER KING", "COUNTRY", "DRAGON", "LIZARD", "GOOGLE", "MICROSOFT",
           "WINDOWS", "LINUX", "HEADPHONES"
           ]
