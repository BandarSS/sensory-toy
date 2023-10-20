def on_button_pressed_a():
    basic.show_number(input.compass_heading())
    if input.compass_heading() == 0 or input.compass_heading() == 360:
        basic.show_string("N")
    elif input.compass_heading() == 90:
        basic.show_string("E")
    elif input.compass_heading() == 180:
        basic.show_string("S")
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() == 270:
        basic.show_string("W")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_icon(IconNames.HAPPY)
    soundExpression.hello.play_until_done()
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    soundExpression.slide.play_until_done()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
    soundExpression.giggle.play_until_done()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    soundExpression.soaring.play_until_done()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    basic.show_icon(IconNames.ASLEEP)
    soundExpression.yawn.play_until_done()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

input.calibrate_compass()
basic.clear_screen()