cmake_minimum_required(VERSION 2.8)
project(Cmake_homework_A)

set(CMAKE_CXX_COMPILER "/usr/bin/clang++")

set(SOURCE_EXE index.cpp)
add_library(index.h index.cpp)
