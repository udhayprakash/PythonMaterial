import pylame2

INBUFSIZE = 4096

encoder = pylame2.Encoder('test2.mp3')
input = file('test.raw', 'rb')

data = input.read(INBUFSIZE)
while data != '':
	encoder.encode(data)
	data = input.read(INBUFSIZE)

input.close()
encoder.close()

