EXEC = main
SOURCES = main.cpp
HEADERS = $(wildcard *.h)
OBJECTS = $(SOURCES:.cpp=.o)

CXX = g++
CXXFLAGS = -std=c++14
LDFLAGS =
LDLIBS =
INCLUDE_PATH =

all: $(EXEC)

$(EXEC): $(OBJECTS)
	$(CXX) $(LDFLAGS) $^ -o $@ $(LDLIBS)

%.o: %.cpp $(HEADERS)
	$(CXX) $(INCLUDE_PATH) $(CXXFLAGS) $< -c -o $@

clean:
	rm -f $(OBJECTS) $(EXEC)
