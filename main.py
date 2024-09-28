def on_gesture_tilt_left():
    global ans
    ans = n1 + n2
    basic.show_string("=" + str(ans))
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    global ans
    ans = n1 - n2
    basic.show_string("=" + str(ans))
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

ans = 0
n2 = 0
n1 = 0
n1 = 0
n2 = 0
ans = 0

def on_forever():
    global n1, n2
    if input.button_is_pressed(Button.A):
        n1 += 1
        basic.show_number(n1)
        basic.pause(100)
        basic.clear_screen()
    elif input.button_is_pressed(Button.B):
        n2 += 1
        basic.show_number(n2)
        basic.pause(100)
        basic.clear_screen()
basic.forever(on_forever)
