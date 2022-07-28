add_executable(kie_context_test kie_context_test.cpp)
target_link_libraries(kie_context_test PUBLIC kie_context)
target_compile_options(kie_context_test PRIVATE -fsanitize=address -g --coverage -Wall -Wextra -Werror)
target_link_options(kie_context_test PRIVATE -fsanitize=address --coverage)

add_test(kie_context_test kie_context_test)