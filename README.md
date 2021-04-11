# camera_joystick_springrts

This forwards joystick data to the Spring engine via TCP LuaSocket at 60fps. 

Usage:

1. Get python3

2. Run "install_and_start_send-joystick.bat", OR open a command window and type: "pip install pygame"  and then "python send-joystick.py" 

3. This program opens up a TCP server on port 51234, and reports back what kind of joystick it found, e.g.:

Found a joystick: XiaoMi Bluetooth Wireless GameController , with 8 axes and 21 buttons 1 hats

4. Add camera_joystick to your /luaui/widgets folder, open it up and uncomment the right configuration for your ps4 or Xbox360 controller (they may be incorrect)

5. Disable the CameraFlip widget to prevent flipbacks when turning cam around

6. Launch your game, enable the widget in f11 mode, and make sure to change camera mode to **rotateable overhead camera (CTRL+F4)** and fly around!


- Left stick move camera 
- Right stick turn camera
- Right trigger move down
- Left trigger move up
- A button pause game
- B button hide interface
- shoulder buttons change gamespeed
- d-pad change smoothing/speed

Notes:

Your game needs Spring.Utilities.json.decode(str) widget-side for this to work.
Also for BAR replays, this wont work on replays older than 2021 apr 7
