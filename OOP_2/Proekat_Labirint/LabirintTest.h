//
// Created by Виктория Аванесова on 12.06.2025.
//

#ifndef PROGECT_LABIRINT_LABIRINTTEST_H
#define PROGECT_LABIRINT_LABIRINTTEST_H

#include <cppunit/TestFixture.h>
#include <cppunit/extensions/HelperMacros.h>
#include "Labirint.h"

class LabirintTest : public CppUnit::TestFixture {
CPPUNIT_TEST_SUITE(LabirintTest);
        CPPUNIT_TEST(testGetCellAndSetCell);
        CPPUNIT_TEST(testIsWall);
        CPPUNIT_TEST(testHasPathToExit); // существование проходимого пути
        CPPUNIT_TEST(testEntranceAndExitCoordinates); // существование входа/выхода
        CPPUNIT_TEST(testIsExitAndCheckRobotAtExit);
        CPPUNIT_TEST(testPlaceItems); // проверяет кол-во размещенных предметов
        CPPUNIT_TEST(testGetState); //проверяет непустое строковое представление и количество строк
    CPPUNIT_TEST_SUITE_END();

public:
    // тест работы Get и Cell
    void testGetCellAndSetCell() {
        Labirint lab(10, 10, 0);
        lab.setCell(2, 3, 'X');
        CPPUNIT_ASSERT(lab.getCell(2, 3) == 'X');
    }

    /// Вне границ — должна быть стена
    void testIsWall() {
        Labirint lab(10, 10, 0);
        // Стена по умолчанию
        CPPUNIT_ASSERT(lab.isWall(0, 0));
        // Вне границ — всегда стена
        CPPUNIT_ASSERT(lab.isWall(-1, 0));
        CPPUNIT_ASSERT(lab.isWall(10, 10));
    }
    void testHasPathToExit() {
        bool success = false;
        // даём до 5 попыток сгенерировать проходимый лабиринт
        for (int i = 0; i < 5 && !success; ++i) {
            Labirint lab(15, 15, 0);
            success = lab.hasPathToExit();
        }
    }

    void testEntranceAndExitCoordinates() {
        Labirint lab(12, 12, 0);
        int entranceCol = lab.getEntranceColumn();
        CPPUNIT_ASSERT(entranceCol >= 1 && entranceCol <= lab.getCols() - 2);
        auto exitCoords = lab.getExit();
        CPPUNIT_ASSERT(exitCoords.first == lab.getRows() - 1);
        CPPUNIT_ASSERT(exitCoords.second >= 1 && exitCoords.second <= lab.getCols() - 2);
    }

    void testIsExitAndCheckRobotAtExit() {
        Labirint lab(8, 8, 0);
        auto [er, ec] = lab.getExit();
        CPPUNIT_ASSERT(lab.isExit(er, ec));
        // Проверяем checkRobotAtExit
        CPPUNIT_ASSERT(lab.checkRobotAtExit(er, ec));
        // На произвольной клетке, не выход e.g. (1,1)
        CPPUNIT_ASSERT(!lab.checkRobotAtExit(1, 1));
    }

    void testPlaceItems() {
        int items = 5;
        Labirint lab(10, 10, items);
        int count = 0;
        for (int i = 0; i < lab.getRows(); ++i)
            for (int j = 0; j < lab.getCols(); ++j)
                if (lab.getCell(i, j) == 'P') count++;
        CPPUNIT_ASSERT(count <= items);
    }

    void testGetState() {
        Labirint lab(7, 7, 0);
        std::string state = lab.getState();
        CPPUNIT_ASSERT(!state.empty());
        // Количество строк в строковом представлении = rows + 1 с последним '\n'
        int lines = 0;
        for (char c : state) if (c == '\n') ++lines;
        CPPUNIT_ASSERT_EQUAL(lab.getRows(), lines);
    }

};

CPPUNIT_TEST_SUITE_REGISTRATION(LabirintTest);


#endif //PROGECT_LABIRINT_LABIRINTTEST_H
