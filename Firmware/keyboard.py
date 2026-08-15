

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
import board

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP0,  board.GP1,  board.GP2,  board.GP3,
    board.GP4,  board.GP5,  board.GP6,  board.GP7,
    board.GP8,  board.GP9,  board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15,
)

keyboard.row_pins = (
    board.GP17, board.GP18, board.GP19,
    board.GP20, board.GP21, board.GP22,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
    
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,
        KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.PAUS, KC.DEL,
    
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,
        KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.NO,   KC.BSPC, KC.HOME,

        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.NO,   KC.BSLS, KC.PGUP,

        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NO,   KC.ENT,  KC.PGDN, KC.NO,

        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
        KC.COMM, KC.DOT,  KC.SLSH, KC.NO,   KC.RSFT, KC.UP,   KC.END,  KC.NO,

        KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.RALT, KC.MO(1),KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,
    ],
   
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()


