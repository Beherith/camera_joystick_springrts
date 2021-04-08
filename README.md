# camera_joystick_springrts

This forwards joystick data to the Spring engine via TCP LuaSocket at 60fps. 

Usage:

Get python3, and then pip install pygame.

Run send-joystick.py, this opens up a TCP server on port 51234, and reports back what kind of joystick it found, e.g.:

Found a joystick: XiaoMi Bluetooth Wireless GameController , with 8 axes and 21 buttons 1 hats


Add camera_joystick to your /luaui/widgets folder, open it up and uncomment the right configuration for your ps4 or Xbox360 controller (they may be incorrect)

Launch your game, enable the widget in f11 mode, and make sure to change camera mode to *rotateable overhead camera CTRL+F4* and fly around!

Left stick move camera 
Right stick turn camera
Right trigger move down
Left trigger move up
A button dump debug info
d-pad change smoothing/speed
