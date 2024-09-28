input.onGesture(Gesture.TiltLeft, function () {
    ans = n1 + n2
    basic.showString("=" + ans)
    basic.pause(1000)
    basic.clearScreen()
})
input.onGesture(Gesture.TiltRight, function () {
    ans = n1 - n2
    basic.showString("=" + ans)
    basic.pause(1000)
    basic.clearScreen()
})
let ans = 0
let n2 = 0
let n1 = 0
n1 = 0
n2 = 0
ans = 0
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        n1 += 1
        basic.showNumber(n1)
        basic.pause(100)
        basic.clearScreen()
    } else if (input.buttonIsPressed(Button.B)) {
        n2 += 1
        basic.showNumber(n2)
        basic.pause(100)
        basic.clearScreen()
    }
})
