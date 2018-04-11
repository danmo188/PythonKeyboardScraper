from pynput import keyboard
from filelock import Timeout, FileLock
from string import ascii_lowercase
import os.path
data = []
file = 'results.txt'
lock_path = 'results.txt.lock'


numkeys = 0

lock = FileLock(lock_path, timeout=10)

def on_press(key):
	
	global numkeys
	global data
	numkeys = numkeys + 1
	try:
		if(key.char.isalnum()):
			for i in range(0,len(data)):
				if key.char == data[i][0]:
					line = data[i]
					lst = line.split(' ')
					newval = int(lst[1]) + 1
					newline = lst[0] + ' ' + str(newval) + ' ' + '0\n'
					print(newline)
					data[i] = newline
	except AttributeError:
		pass
	if( numkeys == 10 ):
		with lock:
			with open(file,'w+') as f:
				f.writelines(data)
				numkeys = 0
						

def createResultsFile():
	dataCreate = []
	with open('results.txt','w+') as f:
		for c in ascii_lowercase:
			line = c + ' ' + '0' + ' ' + '0\n'
			dataCreate.append(line)
		for i in range(1,10):
			line = str(i) + ' ' + '0' + ' ' + '0\n'
			dataCreate.append(line)
		f.writelines(dataCreate)
		return dataCreate


def on_release(key):
	pass

if not os.path.exists('results.txt'):
	data = createResultsFile()
else:
	with open(file,'r+') as f:
		data = f.readlines()
			
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()