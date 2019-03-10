import pylame3

INBUFSIZE = 4096

class MyFile(file):

	def __init__(self, path, mode):
		file.__init__(self, path, mode)
		self.n = 0

	def write(self, s):
		file.write(self, s)
		self.n += 1

output = MyFile('test3.mp3', 'wb')
encoder = pylame3.Encoder(output)
input = file('test.raw', 'rb')

data = input.read(INBUFSIZE)
while data != '':
	encoder.encode(data)
	data = input.read(INBUFSIZE)

input.close()
encoder.close()
output.close()

print 'output.write was called %d times' % output.n

