cmake_minimum_required (VERSION 2.6)
set(CMAKE_CXX_COMPILER "/usr/bin/clang++")
project (Cmake_homework)

execute_process(COMMAND python3 A/script.py)

include_directories("${PROJECT_BINARY_DIR}")
add_subdirectory("A")

# set(SOURCE_FILES A/index.cpp B/main.cpp)
# add_executable(build ${SOURCE_FILES})

add_executable(Cmake_homework A/index.cpp B/main.cpp)
# add_executable(Cmake_homework B/main.cpp)
