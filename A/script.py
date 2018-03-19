import os

index_h_text = '''

#ifndef INDEX_H
#define INDEX_H

#include <iostream>

void indicate();

#endif
'''

index_cpp_text = '''

void indicate(){
    std::cout << "Generated correctly!";
    std::cout << std::endl;
    return;
}
'''

with open(os.path.abspath('A/index.h'), 'w') as file:
    file.write(index_h_text)

with open(os.path.abspath('A/index.cpp'), 'w') as file:
    file.write(index_cpp_text)
