CXX = g++
CXXFLAGS = -Wall -std=c++11

# Find all .cpp files in the current directory
SOURCES = $(wildcard *.cpp)
# Get the corresponding executable names
EXECUTABLES = $(SOURCES:.cpp=)

.PHONY: all clean

all: $(EXECUTABLES)

# Rule to build each executable
%: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f $(EXECUTABLES)
