include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

add_library(gfunc SHARED
    gfunc.f90
    pygfunc.h
    pygfunc.f90
    )
cython_add_module(pygfunc 
    pygfunc.pyx
    )
target_link_libraries(pygfunc
    gfunc
    )

add_executable(fun.bin
    main.f90
    )
target_link_libraries(fun.bin
    gfunc
    )

configure_file(test.py ${CMAKE_BINARY_DIR}/test.py)
execute_process(COMMAND chmod 755 ${CMAKE_BINARY_DIR}/test.py)
