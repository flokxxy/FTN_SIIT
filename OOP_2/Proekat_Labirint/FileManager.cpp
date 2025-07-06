//
// Created by Виктория Аванесова on 20.01.2025.
//

#include "FileManager.h"
#include <fstream>
#include <string>
#include <iostream>

/**
 * @brief Класс FileManager отвечает за операции записи результатов игры в файл.
 *
 * Содержит метод для сохранения итогового состояния игры, включающего историю состояний лабиринта,
 * сообщения игровых событий и итоговый результат (победа или поражение).
 */
/**
 * @brief The FileManager class is responsible for writing game results to a file.
 *
 * It includes a method to save the final game state, encompassing the labyrinth history,
 * game event messages, and the final outcome (victory or defeat).
 */



    /**
     * @brief Сохраняет результаты игры в заданный файл.
     *
     * Метод записывает в файл итоговую историю игры, включая состояния лабиринта,
     * игровые сообщения и итоговый результат.
     *
     * @param filename Путь к файлу, в который будут сохранены результаты.
     * @param gameHistory Строка, содержащая накопленную историю игры.
     * @param won Булевый флаг: true, если игрок победил, false – если проиграл.
     */
/**
 * @brief Saves the game results to the specified file.
 *
 * This method writes the final game history to the file, including the labyrinth states,
 * game messages, and the final outcome.
 *
 * @param filename    Path to the file where the results will be saved.
 * @param gameHistory A string containing the accumulated game history.
 * @param won         Boolean flag: true if the player won, false if the player lost.
 */

void FileManager::saveGameResults(const std::string &filename,
                                  const std::string &gameHistory,
                                  bool won,
                                  const std::string &lastLabState,
                                  const std::string &resultReason,
                                  int labyrinthRows,
                                  int labyrinthCols,
                                  int numItems) {
    std::ofstream file(filename, std::ios::out);
    if (file.is_open()) {
        // Write the accumulated game history (e.g., all iterations)
        file << "Game History:\n" << gameHistory << "\n\n";

        // Write labyrinth information
        file << "Labyrinth Size: " << labyrinthRows << " rows x " << labyrinthCols << " cols\n";
        file << "Number of items: " << numItems << "\n";

        // Write the last iteration of the labyrinth
        file << "Last Iteration of the Labyrinth:\n" << lastLabState << "\n\n";

        // Write the final game result and its reason
        file << "Result: " << (won ? "Victory" : "Defeat") << "\n";
        file << "Reason: " << resultReason << "\n\n";

        file.close();
        std::cout << "Game results saved to '" << filename << "'.\n";
    } else {
        std::cerr << "Unable to open file " << filename << ".\n";
    }
}
