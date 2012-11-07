cmake_minimum_required(VERSION 2.8)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

project(PyGFunc)
enable_language(Fortran)
find_package(Python REQUIRED)
include(UseCython)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

cython_add_module(cyquad 
    cyquad.pyx
    )

add_subdirectory(Fortran)
