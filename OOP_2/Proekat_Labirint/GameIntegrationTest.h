// GameIntegrationTest.cpp
#include <cppunit/extensions/HelperMacros.h>
#include "Game.h"
#include "Labirint.h"

#include <fstream>
#include <iostream>

class GameIntegrationTest : public CppUnit::TestFixture {
CPPUNIT_TEST_SUITE(GameIntegrationTest);
        CPPUNIT_TEST(testInitialization);
        CPPUNIT_TEST(testDefeatScenario);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp() override {
        // Перенаправляем всё в /dev/null
        nullStream.open("/dev/null");
        origCout = std::cout.rdbuf(nullStream.rdbuf());
        origCerr = std::cerr.rdbuf(nullStream.rdbuf());

        game = new Game(3, 3, 0);
    }

    void tearDown() override {
        delete game;

        // Восстанавливаем потоки
        std::cout.rdbuf(origCout);
        std::cerr.rdbuf(origCerr);
        nullStream.close();
    }

    void testInitialization() {
        // Робот должен быть в начале (входе)
        int entranceCol = game->labirint.getEntranceColumn();
        CPPUNIT_ASSERT_EQUAL(entranceCol, game->robotX);
        CPPUNIT_ASSERT_EQUAL(0, game->robotY);
        CPPUNIT_ASSERT(!game->won);
    }


    void testDefeatScenario() {
        // Ставим минотавра на робота «в лоб»
        game->minotaurX = game->robotX;
        game->minotaurY = game->robotY;
        game->updateGameState();
        CPPUNIT_ASSERT(!game->won);
    }

private:
    Game* game;
    std::ofstream nullStream;
    std::streambuf* origCout;
    std::streambuf* origCerr;
};

CPPUNIT_TEST_SUITE_REGISTRATION(GameIntegrationTest);
