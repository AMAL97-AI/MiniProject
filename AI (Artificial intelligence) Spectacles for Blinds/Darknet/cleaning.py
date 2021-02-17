
with open('/home/pi/Desktop/New/darknet/result.txt','r') as f1, open('/home/pi/Desktop/New/darknet/output.txt', 'w') as f2:
	f2.write("".join([c for c in f1.read() if not c.isdigit()]))


import re

string = open('/home/pi/Desktop/New/darknet/output.txt').read()
new_str = re.sub('[^a-zA-Z\n\.]', '', string)
open('/home/pi/Desktop/New/darknet/b.txt', 'w').write(new_str)

with open('/home/pi/Desktop/New/darknet/b.txt', 'r') as fin:
	data = fin.read().splitlines(True)
with open('/home/pi/Desktop/New/darknet/c.txt', 'w') as fout:
	fout.writelines(data[1:])
