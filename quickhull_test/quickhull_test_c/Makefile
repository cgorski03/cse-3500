# Compiler
CC = g++

# Compiler flags
CFLAGS = -Wall -std=c++11

# Source files
SRCS = gift_wrapping.cpp graham_scan.cpp quickhull.cpp test_hull_algorithms.cpp

# Output binary
OUT = test_hull_algorithms

all: $(OUT)

$(OUT): $(SRCS)
	$(CC) $(CFLAGS) -o $(OUT) $(SRCS)

clean:
	rm -f $(OUT)
