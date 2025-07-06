// GameTest.cpp
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include "Game.h"

#include <fstream>
#include <iostream>

class GameTest : public CppUnit::TestFixture {
CPPUNIT_TEST_SUITE(GameTest);
        CPPUNIT_TEST(testConstructor);
        CPPUNIT_TEST(testEndGame);
        CPPUNIT_TEST(testCheckWinCondition);
        CPPUNIT_TEST(testCheckCollision);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp() override {
        // Перенаправляем все выводы в /dev/null
        nullStream.open("/dev/null");
        origCout = std::cout.rdbuf(nullStream.rdbuf());
        origCerr = std::cerr.rdbuf(nullStream.rdbuf());

        game = new Game(5, 5, 0);
    }

    void tearDown() override {
        delete game;

        // Восстанавливаем потоки
        std::cout.rdbuf(origCout);
        std::cerr.rdbuf(origCerr);
        nullStream.close();
    }

    void testConstructor() {
        CPPUNIT_ASSERT(!game->won);
    }

    void testEndGame() {
        game->endGame(true);
        CPPUNIT_ASSERT(game->won);

        game->endGame(false);
        CPPUNIT_ASSERT(!game->won);
    }

    void testCheckWinCondition() {
        game->robotX = game->exitX = 2;
        game->robotY = game->exitY = 3;
        CPPUNIT_ASSERT(game->checkWinCondition());

        game->robotX = 0; game->robotY = 0;
        CPPUNIT_ASSERT(!game->checkWinCondition());
    }

    void testCheckCollision() {
        game->robotX = game->minotaurX = 1;
        game->robotY = game->minotaurY = 1;
        CPPUNIT_ASSERT(game->checkCollision());

        game->minotaurX = 2; game->minotaurY = 2;
        CPPUNIT_ASSERT(!game->checkCollision());
    }

private:
    Game* game;
    std::ofstream nullStream;
    std::streambuf* origCout;
    std::streambuf* origCerr;
};

// Регистрация фикстуры в реестре
CPPUNIT_TEST_SUITE_REGISTRATION(GameTest);
