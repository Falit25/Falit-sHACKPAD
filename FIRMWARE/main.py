import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.neopixel import NeoPixel

keyboard = KMKKeyboard()

# ---------- MACROS ----------
macros = Macros()
keyboard.modules.append(macros)

# ---------- KEYS (from your schematic) ----------
PINS = [
    board.GP26,  # SW1
    board.GP27,  # SW2
    board.GP28,  # SW3
    board.GP29,  # SW4
    board.GP6,   # SW5
    board.GP7,   # SW6
    board.GP0,   # SW7
    board.GP1,   # SW8
    board.GP4,   # SW9
    board.GP2,   # SW10
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ---------- RGB LEDs ----------
led = NeoPixel(
    pin=board.GP3,   # GPIO3 -> D1 DIN
    n=4,
    brightness=0.3,
    pixel_order=NeoPixel.GRB,
)
keyboard.extensions.append(led)

# ---------- GENERIC SHORTCUTS ----------
ALT_TAB = KC.Macro(
    Press(KC.LALT),
    Tap(KC.TAB),
    Release(KC.LALT),
)

MINIMIZE_ALL = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.D),
    Release(KC.LGUI),
)

NEXT_DESKTOP = KC.Macro(
    Press(KC.LCTL),
    Press(KC.LGUI),
    Tap(KC.RIGHT),
    Release(KC.LGUI),
    Release(KC.LCTL),
)

PREV_DESKTOP = KC.Macro(
    Press(KC.LCTL),
    Press(KC.LGUI),
    Tap(KC.LEFT),
    Release(KC.LGUI),
    Release(KC.LCTL),
)

SHUTDOWN = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.X),
    Release(KC.LGUI),
    Tap(KC.U),
    Tap(KC.U),
)

# ---------- APP LAUNCH MACROS (Win + type + Enter) ----------
OPEN_SPOTIFY = KC.Macro(
    Tap(KC.LGUI),
    Tap(KC.S),
    Tap(KC.P),
    Tap(KC.O),
    Tap(KC.T),
    Tap(KC.I),
    Tap(KC.F),
    Tap(KC.Y),
    Tap(KC.ENTER),
)

OPEN_VSCODE = KC.Macro(
    Tap(KC.LGUI),
    Tap(KC.V),
    Tap(KC.S),
    Tap(KC.C),
    Tap(KC.O),
    Tap(KC.D),
    Tap(KC.E),
    Tap(KC.ENTER),
)

OPEN_CHROME = KC.Macro(
    Tap(KC.LGUI),
    Tap(KC.C),
    Tap(KC.H),
    Tap(KC.R),
    Tap(KC.O),
    Tap(KC.M),
    Tap(KC.E),
    Tap(KC.ENTER),
)

LOCK_SCREEN = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.L),
    Release(KC.LGUI),
)

OPEN_WHATSAPP = KC.Macro(
    Tap(KC.LGUI),
    Tap(KC.W),
    Tap(KC.H),
    Tap(KC.A),
    Tap(KC.T),
    Tap(KC.S),
    Tap(KC.A),
    Tap(KC.P),
    Tap(KC.P),
    Tap(KC.ENTER),
)

# ---------- KEYMAP ----------
keyboard.keymap = [
    [
        ALT_TAB,        # SW1
        MINIMIZE_ALL,   # SW2
        NEXT_DESKTOP,   # SW3
        PREV_DESKTOP,  # SW4
        SHUTDOWN,      # SW5
        OPEN_SPOTIFY,  # SW6
        OPEN_VSCODE,   # SW7
        OPEN_CHROME,   # SW8
        LOCK_SCREEN,   # SW9
        OPEN_WHATSAPP, # SW10
    ]
]

if __name__ == '__main__':
    keyboard.go()
