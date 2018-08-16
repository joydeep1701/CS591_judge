all: main.o module.o
	gcc main.o module.o -o program -std=c99
main.o: main.c module.h
	gcc -I . -c main.c -std=c99
module.o: module.c module.h
	gcc -I . -c module.c -std=c99
clean:
	rm -rf *.o
	rm program
