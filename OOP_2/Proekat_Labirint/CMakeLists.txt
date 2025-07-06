cmake_minimum_required(VERSION 3.25)
project(Progect_Labirint)

set(CMAKE_CXX_STANDARD 17)
enable_testing()
# --- Основная игра ---
add_executable(Progect_Labirint
        main.cpp
        Labirint.cpp
        Game.cpp
        Character.cpp
        Robot.cpp
        Minotaur.cpp
        FileManager.cpp
        )
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)
target_link_libraries(Progect_Labirint PRIVATE sfml-graphics sfml-window sfml-system)

# --- CppUnit ---
find_path(CPPUNIT_INCLUDE_DIR cppunit/TestFixture.h
        HINTS /opt/homebrew/opt/cppunit/include /usr/local/include /usr/include
        )
find_library(CPPUNIT_LIBRARY NAMES cppunit libcppunit
        HINTS /opt/homebrew/opt/cppunit/lib /usr/local/lib /usr/lib
        )
if(NOT CPPUNIT_INCLUDE_DIR OR NOT CPPUNIT_LIBRARY)
    message(FATAL_ERROR "CppUnit not found")
endif()

# --- Тесты для Labirint ---
add_executable(labirint_tests
        Labirint.cpp
        LabirintTest.cpp
        test_main.cpp
        )
target_include_directories(labirint_tests PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CPPUNIT_INCLUDE_DIR}
        )
target_link_libraries(labirint_tests PRIVATE
        ${CPPUNIT_LIBRARY}
        )
add_test(NAME LabirintTests COMMAND labirint_tests)

# --- Тесты для Game ---
add_executable(game_tests
        Labirint.cpp
        Game.cpp
        Character.cpp

        Robot.cpp
        Minotaur.cpp
        FileManager.cpp
        GameTest.cpp
        gameTest_main.cpp
        )
target_include_directories(game_tests PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CPPUNIT_INCLUDE_DIR}
        )
target_link_libraries(game_tests PRIVATE
        ${CPPUNIT_LIBRARY}
        )
add_test(NAME GameTests COMMAND game_tests)


# --- Интеграционные тесты ---
add_executable(integration_tests
        Labirint.cpp
        Game.cpp
        Character.cpp
        Robot.cpp
        Minotaur.cpp
        FileManager.cpp

        GameIntegrationTest.cpp
        test_main.cpp
        )
target_include_directories(integration_tests PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CPPUNIT_INCLUDE_DIR}
        )
target_link_libraries(integration_tests PRIVATE
        ${CPPUNIT_LIBRARY}
        )
add_test(NAME IntegrationTests COMMAND integration_tests)
