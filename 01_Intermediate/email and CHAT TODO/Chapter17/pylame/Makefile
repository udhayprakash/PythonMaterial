all: clame pylame.so

clame: clame.c
	gcc -Wall -lmp3lame clame.c -o clame

pylame1.so: pylame1.c clame.c
	gcc -Wall -shared -I/usr/include/python2.4 pylame1.c clame.c -lmp3lame -o pylame1.so

pylame2.so: pylame2.c
	gcc -Wall -shared -I/usr/include/python2.4 pylame2.c -lmp3lame -o pylame2.so

pylame3.so: pylame3.c
	gcc -Wall -shared -I/usr/include/python2.4 pylame3.c -lmp3lame -o pylame3.so

clean:
	rm -f clame
	rm -f pylame.so

