#!/usr/bin/python
"""
Purpose:
    pip install -U autopy --user
"""
import autopy

print(f"{autopy.__doc__}")

# To display an alert
autopy.alert.alert("Hello, world!")

# To move cursor to top left corner of screen
autopy.mouse.move(1, 1)

# To move mouse cursor realistically
autopy.mouse.smooth_move(10, 45)

autopy.bitmap.capture_screen().save("screenshot.png")


# print(dir(autopy))
# 'bitmap', 'color', 'key', 'mouse', 'screen'
