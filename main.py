import tkinter as tk
from tkinter import messagebox
import platform

GRID_SIZE = 10

#Ships and Sizes
ships = {
    'Destroyer': 2,
    'Submarine': 3, 
    'Battleship': 4,
}

# Emoji representations
ship_emojis = {
"Destroyer": "🚢",
"Submarine": "🚤",
"Battleship": "🛳️"
}

# OS-based emoji adjustment
system = platform.system()
if system == "Windows":
    EMOJI_FONT = "Segoe UI Emoji"
elif system == "Darwin": # macOS
    EMOJI_FONT = "Apple Color Emoji"
else:
    EMOJI_FONT = "Noto Color Emoji"