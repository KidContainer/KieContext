cmake_minimum_required(VERSION 3.15)
project(kie_context CXX)

set(CMAKE_CXX_STANDARD 20)


find_package(Boost REQUIRED)

add_library(kie_context INTERFACE)
target_include_directories(kie_context INTERFACE include)
target_link_libraries(kie_context INTERFACE boost::boost)

option(ENABLE_TEST "if enable test code" OFF)

if(ENABLE_TEST)
    include(CTest)
    add_subdirectory(test)    
endif()

install(TARGETS kie_context)
install(DIRECTORY include/ DESTINATION include)
install(FILES LICENSE DESTINATION license)
