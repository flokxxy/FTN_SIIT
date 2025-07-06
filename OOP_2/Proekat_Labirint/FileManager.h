//
// Created by Виктория Аванесова on 20.01.2025.
//

#ifndef PROGECT_LABIRINT_FILEMANAGER_H
#define PROGECT_LABIRINT_FILEMANAGER_H

#include "iostream"
#include "Game.h"
using namespace std;

/**
     * @brief Сохраняет результаты игры в заданный файл.
     *
     * Метод записывает в файл последнюю итерацию лабиринта, итог игры с причиной,
     * а также информацию о размере лабиринта и количестве предметов.
     *
     * @param filename Путь к файлу для сохранения результатов.
     * @param gameHistory Строка, содержащая накопленную историю игры.
     * @param won Булевый флаг: true, если игрок победил, false – если проиграл.
     * @param lastLabState Строка с последним состоянием лабиринта.
     * @param resultReason Причина итогового результата (например, последнее сообщение).
     * @param labyrinthRows Количество строк в лабиринте.
     * @param labyrinthCols Количество столбцов в лабиринте.
     * @param numItems Количество предметов в лабиринте.
     */
/**
* @brief Saves the game results to the specified file.
*
* This method writes the final labyrinth state, the game outcome with its reason,
* and information about the labyrinth dimensions and number of items to a file.
*
* @param filename       Path to the file for saving results.
* @param gameHistory    A string containing the accumulated game history.
* @param won            Boolean flag: true if the player won, false if the player lost.
* @param lastLabState   A string with the last state of the labyrinth.
* @param resultReason   The reason for the final outcome (e.g., the last message).
* @param labyrinthRows  Number of rows in the labyrinth.
* @param labyrinthCols  Number of columns in the labyrinth.
* @param numItems       Number of items in the labyrinth.
*/


class FileManager {
public:
    static void saveGameResults(const std::string &filename,
                                const std::string &gameHistory,
                                bool won,
                                const std::string &lastLabState,
                                const std::string &resultReason,
                                int labyrinthRows,
                                int labyrinthCols,
                                int numItems);
};


#endif //PROGECT_LABIRINT_FILEMANAGER_H
