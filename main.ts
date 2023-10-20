input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.compassHeading())
    if (input.compassHeading() <= 5 && input.compassHeading() >= 355) {
        basic.showString("N")
    } else if (input.compassHeading() <= 95 && input.compassHeading() >= 85) {
        basic.showString("E")
    } else if ((0 as any) <= (185 as any) && input.compassHeading() >= 175) {
        basic.showString("S")
        basic.showArrow(ArrowNames.South)
    } else if (input.compassHeading() <= 175 && input.compassHeading() >= 165) {
        basic.showString("W")
    } else {
        basic.clearScreen()
    }
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showIcon(IconNames.Happy)
    soundExpression.hello.playUntilDone()
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        `)
    soundExpression.slide.playUntilDone()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Surprised)
    soundExpression.giggle.playUntilDone()
})
input.onGesture(Gesture.TiltRight, function () {
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
    soundExpression.soaring.playUntilDone()
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showIcon(IconNames.Asleep)
    soundExpression.yawn.playUntilDone()
})
input.calibrateCompass()
basic.clearScreen()
