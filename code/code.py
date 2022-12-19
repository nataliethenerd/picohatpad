import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes

keyboard = KMKKeyboard()

underglow = RGB(
    pixel_pin=board.GP10,
    num_pixels=2,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(underglow)

keyboard.matrix = KeysScanner(
    [
        board.GP0, board.GP2,
    ]
)
encoder_handler = EncoderHandler()
media_keys = MediaKeys()
keyboard.modules = [encoder_handler, media_keys]

encoder_handler.pins = ((board.GP3, board.GP4, board.GP5, False),)

keyboard.keymap = [[KC.MNXT, KC.MPRV]]

encoder_handler.map = (((KC.VOLU, KC.VOLD, KC.MPLY),),)

if __name__ == "__main__":
    keyboard.go()
