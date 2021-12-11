# Makefile for AoC2021 D1
#
# Stanley Gao, 12/7/21

OBJS = day1.o
LIBS =

CFLAGS = -Wall -pedantic -std=c11 -ggdb -lm
CC = gcc
MAKE = make
VALGRIND = valgrind --leak-check=full --show-leak-kinds=all

day1: $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

day1.o:

.PHONY: test valgrind clean

clean:
	rm -rf *.dSYM
	rm -f *~ *.o
	rm -f core
	rm -f day1
