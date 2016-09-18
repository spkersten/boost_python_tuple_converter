CC=clang++

test_tuple_converter.so : test_tuple_converter.cpp ../tuple_converter.hpp
	${CC} -shared test_tuple_converter.cpp -o test_tuple_converter.so -lboost_python -lPython2.7 -I /usr/include/python2.7/
    
test : test_tuple_converter.so test.py
	python test.py
