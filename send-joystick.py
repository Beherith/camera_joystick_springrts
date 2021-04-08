import socket, time
import pygame
from socketserver import BaseRequestHandler, TCPServer
import json

# Main configuration
TCP_IP = "127.0.0.1" # Localhost
TCP_PORT = 51234  # This port match the ones using on other scripts

update_rate = 0.0166666  # 60 hz loop cycle
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
numbuttons = 0
numaxes = 0
numhats = 0
joyname = ''
try:
	pygame.init()
	pygame.joystick.init()
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	numbuttons = joystick.get_numbuttons()
	numaxes = joystick.get_numaxes()
	numhats = joystick.get_numhats()
	print ("Found a joystick:", joystick.get_name(),", with", numaxes,"axes and",numbuttons,"buttons", numhats, 'hats')

except Exception as  error:
	print ("No joystick connected on the computer, " + str(error))

messagestr = "empty"
class handler(BaseRequestHandler):
	def handle(self):
		print ("Starting handler")
		i = 0
		while True:
			current = time.time()
			elapsed = 0

			pygame.event.pump()
			i += 1
			joydata = {'time': current}
			joydata['axes'] = [0.0] * numaxes
			joydata['buttons'] = [0] * numbuttons
			joydata['hats'] = [0.0] * 2

			for ax in range(numaxes):
				joydata['axes'][ax] = joystick.get_axis(ax)
			for but in range(numbuttons):
				joydata['buttons'][but] = joystick.get_button(but)
			for hat in range(min(1,numhats)):
				joydata['hats'] = joystick.get_hat(hat)
			if i%60 == 0 :
				print(i, current, 'buttons = ', joydata['buttons'], 'axes = ', joydata['axes'], 'hats = ', joydata['hats'])
			msgstr = json.dumps(joydata)
			# sock.sendto(json.dumps(joydata),(TCP_IP,TCP_PORT))
			# Make this loop work at update_rate
			while elapsed < update_rate:
				elapsed = time.time() - current
				time.sleep(0.0001)  # 100us?
			self.request.send(str.encode(msgstr))


with TCPServer(("",51234),handler) as server:
	server.timeout = 0.5
	server.serve_forever(poll_interval= 0.016)

while True:
	current = time.time()
	elapsed = 0

	pygame.event.pump()

	joydata = {'time':current}
	joydata['axes'] = [0.0] * numaxes
	joydata['buttons'] = [0] * numbuttons

	for ax in range(numaxes):
		joydata['axes'][ax] = joystick.get_axis(ax)
	for but in range(numbuttons):
		joydata['buttons'][but] = joystick.get_button(but)
	print (current, 'buttons = ',joydata['buttons'], 'axes = ',joydata['axes'])
	msgstr = json.dumps(joydata)
	#sock.sendto(json.dumps(joydata),(TCP_IP,TCP_PORT))
	# Make this loop work at update_rate
	while elapsed < update_rate:
		elapsed = time.time() - current
		time.sleep(0.0001) # 100us?