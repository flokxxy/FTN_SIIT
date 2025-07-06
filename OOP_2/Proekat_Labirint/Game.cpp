#include "Game.h"
#include "FileManager.h"
#include "Item.h"
#include "Sword.h"
#include "Shield.h"
#include "Hammer.h"
#include "Fog.h"

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <sstream>
#include <thread>
#include <fstream>


#include <termios.h>
#include <unistd.h>

using namespace std;

/**
 * @file Game.h
 * @brief Заголовочный файл для класса Game, который управляет логикой игры.
 *
 * Этот файл содержит определение класса Game, который отвечает за инициализацию
 * лабиринта, управление состоянием игры и обработку пользовательского ввода.
 * Включает функции для движения робота и Минотавра, обработки столкновений, победы и других аспектов игры.
 *
 * @author Viktorija Avanesova
 * @date Последнее изменение: 17 января 2025 года
 */


/**
 * @file Game.h
 * @brief Header file for the Game class that controls game logic.
 *
 * This file contains the definition of the Game class, which is responsible for
 * initializing the labyrinth, managing the game state, and handling user input.
 * It includes functions for moving the Robot and Minotaur, handling collisions,
 * victory conditions, and other aspects of the game.
 *
 * @author Viktorija Avanesova
 * @date Last modified: January 17, 2025
 */




std::vector<std::string> activeEffects; // For convenient display of active items
std::vector<std::string> errorMessages; // For convenient display of error messages
std::vector<std::string> gameMessages; // For convenient display of messages

std::ostringstream gameHistory; // Stores the entire game history
bool won;



char getCharInput() {
    /**
 * @brief Получает символ ввода без необходимости нажимать Enter.
 *
 * Эта функция позволяет пользователю ввести один символ без необходимости
 * нажимать клавишу Enter. Используется для удобства обработки ввода.
 *
 * @return char Символ, введённый пользователем.
 *
 * @exception нет
 */

    /**
 * @brief Reads a single input character without requiring the Enter key.
 *
 * This function allows the user to input one character without
 * having to press the Enter key. It is used to facilitate input handling.
 *
 * @return char The character entered by the user.
 *
 * @exception none
 */


    struct termios oldt, newt;
    char ch;
    tcgetattr(STDIN_FILENO, &oldt);          // Получаем текущие настройки терминала
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);        // Отключаем канонический ввод и эхо
    tcsetattr(STDIN_FILENO, TCSANOW, &newt); // Устанавливаем новые настройки
    ch = getchar();                          // Считываем символ
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt); // Восстанавливаем старые настройки
    return ch;
}



/**
 * @brief Constructor of the Game class.
 *
 * Initializes game parameters such as the labyrinth, positions of the Robot and Minotaur,
 * and settings for active items.
 *
 * @param rows    Number of rows in the labyrinth.
 * @param cols    Number of columns in the labyrinth.
 * @param numItems Number of items to place in the labyrinth.
 */
Game::Game(int rows, int cols, int numItems)
        : labirint(rows, cols, numItems),
          robot(1, labirint.getEntranceColumn()), // Робот инициализируется и стартует под входом
          minotaur(0, 0), // Минотавр инициализируется
          shieldTurns(0),
          hammerTurns(0),
          swordTurns(0),
          fogTurns(0),
          swordActive(false),
          won(false),
          numItems(numItems) {
    auto [exitRow, exitCol] = labirint.getExit(); // Устанавливаем позицию Минотавра
    exitX = exitRow;
    exitY = exitCol;

    /*
    if (exitX != -1 && exitY != -1) {
        std::cout << "Exit initialized at: (" << exitX << ", " << exitY << ")\n"; // Диагностика
    } else {
        std::cerr << "Failed to initialize exit coordinates.\n"; // Диагностика
    }
     */

    // Initialization of the Minotaur
    srand(time(nullptr));
    do {
        int randomX = rand() % rows;
        int randomY = rand() % cols;
        if (!labirint.isWall(randomX, randomY)) {
            minotaur.setPosition(randomX, randomY);
            break;
        }
    } while (true);
}

void Game::startGame() {
/**
 * @brief Запускает игровой цикл и обрабатывает ввод пользователя.
 *
 * Эта функция инициализирует лабиринт с указанными пользователем размерами,
 * запускает основной цикл игры, обрабатывает ввод пользователя и проверяет
 * условие победы. В случае достижения условий победы или поражения вызывает метод endGame.
 *
 * @exception нет
 */

/**
 * @brief Starts the game loop and handles user input.
 *
 * This function initializes the labyrinth with the dimensions specified by the user,
 * starts the main game loop, processes user input, and checks the victory condition.
 * If victory or defeat conditions are met, it calls the endGame method.
 *
 * @exception none
 */
        // Prompting the user for parameters to create the labyrinth
        int rows, cols, items;
        cout << "Enter the number of rows for the labirint: ";
        cin >> rows;
        cout << "Enter the number of columns for the labirint: ";
        cin >> cols;
        cout << "Enter the number of items in the labirint: ";
        cin >> items;

    // Checking the validity of the entered data
    if (rows < 15 || cols < 15) {
            cout << "Dimensions must be at least 15x15. Exiting.\n";
            return;
        }
        if (items < 3) {
            cout << "Number of items must be at least 3. Exiting.\n";
            return;
        }

    // Creates a new labyrinth using the specified parameters
    labirint = Labirint(rows, cols, items);
        numItems = items;

        auto [exitRow, exitCol] = labirint.getExit();
        exitX = exitRow;
        exitY = exitCol;

        if (exitX != -1 && exitY != -1) {
            std::cout << "Exit initialized at: (" << exitX << ", " << exitY << ")\n"; // Диагностика
        } else {
            std::cerr << "Failed to initialize exit coordinates.\n"; // Диагностика
        }

        // Initialize the positions of the Robot and the Minotaur
        robotX = 1; // The Robot is always positioned directly below the entrance
        robotY = labirint.getEntranceColumn();
        labirint.setCell(robotX, robotY, 'R'); // Place the robot

    do {
            minotaurX = rand() % rows;
            minotaurY = rand() % cols;
        } while (labirint.isWall(minotaurX, minotaurY) || (minotaurX == robotX && minotaurY == robotY));
        labirint.setCell(minotaurX, minotaurY, 'M'); // Place the Minotavr

        // Основной игровой цикл  Main game loop
        char input;
        while (true) {
            system("clear");
            updateGameState(); // Обновляем состояние игры
            cout << "Enter command (W/A/S/D to move, Q to quit): ";
            //cin >> input; //ввод с использованием Enter

            input = getCharInput(); // Read input without requiring the Enter

            if (input == 'Q' || input == 'q') {
                std::string exitMessage = "There was a way out of the game";
                gameMessages.push_back(exitMessage);
                gameHistory << exitMessage << "\n";

                // Update the last state of the labyrinth
                lastLabState = labirint.getState();

                cout << "Exiting the game. Goodbye!\n";
                endGame(false); break;
            }

            processInput(input); // Processes user input
            //updateGameState();
            //checkWinCondition(); // Проверяем условие победы
            bool winCond = checkWinCondition();
            bool collision = checkCollision(); // вызываем один раз

            if (winCond) {
                won = true;
                std::cout << "DEBUG: before endGame, won = " << (won ? "true" : "false") << std::endl;
                endGame(won);
                break;
            } else if (collision) {
                std::cout << "DEBUG: before endGame, won = " << (won ? "true" : "false") << std::endl;
                endGame(won);
                break;
            }
            //updateGameState();
        }
}


void Game::processInput(char input) {
/**
 * @brief Обрабатывает ввод пользователя и перемещает робота.
 *
 * Эта функция принимает символ, представляющий направление, и перемещает робота
 * в указанное направление. Если ввод неверный, выводится сообщение об ошибке.
 *
 * @param input Символ, представляющий направление ('W', 'A', 'S', 'D').
 *
 * @exception нет
 */

/**
 * @brief Processes user input and moves the robot.
 *
 * This function takes a character representing the direction and moves
 * the robot accordingly. If the input is invalid, an error message is displayed.
 *
 * @param input Character representing the direction ('W', 'A', 'S', 'D').
 *
 * @exception none
 */
    switch (input) {
            case 'W':
            case 'w':
                moveRobot('W');
                break;
            case 'A':
            case 'a':
                moveRobot('A');
                break;
            case 'S':
            case 's':
                moveRobot('S');
                break;
            case 'D':
            case 'd':
                moveRobot('D');
                break;
            default:
                std::cout << "Invalid input! Use W/A/S/D for movement.\n";
    }
    std::cout << "Robot position: (" << robotX << ", " << robotY << ")\n"; // Диагностика
}

void Game::moveRobot(char direction) {
    /**
 * @brief Перемещает робота в указанном направлении.
 *
 * Эта функция обновляет позицию робота в лабиринте в зависимости от введённого
 * направления. Если новая позиция является стеной, проверяется, можно ли разрушить стену
 * с помощью молота.
 *
 * @param direction Направление движения робота ('W', 'A', 'S', 'D').
 *
 * @exception нет
 */

    /**
 * @brief Moves the robot in the specified direction.
 *
 * This function updates the robot's position in the labyrinth based on the
 * provided direction. If the new position is a wall, it checks whether the wall
 * can be destroyed using the hammer.
 *
 * @param direction Direction of movement ('W', 'A', 'S', 'D').
 *
 * @exception none
 */

    int newX = robotX;
    int newY = robotY;

    switch (direction) {
        case 'W': newX--; break;
        case 'A': newY--; break;
        case 'S': newX++; break;
        case 'D': newY++; break;
    }

    if (!labirint.isWall(newX, newY) || hammerTurns > 0) {
        if (labirint.isWall(newX, newY)) {
            gameMessages.push_back ("\033[33mYou used the hammer to break through the wall!\033[0m\n");
            hammerTurns--;
        }
        labirint.setCell(robotX, robotY, '.'); // Убираем старую позицию
        robotX = newX;
        robotY = newY;
        char cell = labirint.getCell(robotX, robotY);

        if (cell == 'P') {
            handleItem(robotX, robotY);
        }

        labirint.setCell(robotX, robotY, 'R'); // Обновляем новую позицию
    } else {
        errorMessages.push_back("\033[31m[ERROR] You hit a wall?????!\033[0m");
    }
}

void Game::moveMinotaur() {

    /**
     *  @brief Перемещает Минотавра в зависимости от положения робота.
     * Если робот находится в радиусе 3 клеток, Минотавр движется к нему.
     * Если робот далеко, Минотавр перемещается случайным образом.
     * @exception нет
     */

    /**
 * @brief Moves the Minotaur based on the Robot's position.
 *
 * If the robot is within a radius of 3 cells, the Minotaur moves toward it.
 * Otherwise, the Minotaur moves randomly.
 *
 * @exception none
 */


    int dx = robotX - minotaurX;  // Разница по X
    int dy = robotY - minotaurY;  // Разница по Y
    int absDx = abs(dx);
    int absDy = abs(dy);

    // Если робот в радиусе 3 клеток, идем к нему
    // If the robot is within a 3-cell radius, move towards it
    if (absDx <= 3 && absDy <= 3) {
        if (absDx > absDy) { // Move in the direction with the greatest difference
            if (dx > 0 && !labirint.isWall(minotaurX + 1, minotaurY)) {
                minotaurX++;
            } else if (dx < 0 && !labirint.isWall(minotaurX - 1, minotaurY)) {
                minotaurX--;
            }
        } else {
            if (dy > 0 && !labirint.isWall(minotaurX, minotaurY + 1)) {
                minotaurY++;
            } else if (dy < 0 && !labirint.isWall(minotaurX, minotaurY - 1)) {
                minotaurY--;
            }
        }
    }
        //If the robot is far away, move randomly
    else {
        int direction = rand() % 4;
        int newX = minotaurX, newY = minotaurY;

        switch (direction) {
            case 0: newX--; break; // Вверх
            case 1: newX++; break; // Вниз
            case 2: newY--; break; // Влево
            case 3: newY++; break; // Вправо
        }

        if (!labirint.isWall(newX, newY)) {
            minotaurX = newX;
            minotaurY = newY;
        }
    }
}

bool Game::checkCollision() {

    /**
 * @brief Проверяет столкновение робота с Минотавром.
 *
 * Эта функция проверяет, находится ли робот в одной клетке с Минотавром.
 * В случае столкновения выполняются различные действия в зависимости от состояния эффектов:
 * - Если у робота есть активированный щит, то он блокирует атаку Минотавра.
 * - Если у робота есть меч, то он побеждает Минотавра.
 * - В случае отсутствия щита и меча, Минотавр ловит робота, и игра заканчивается.
 *
 * @return bool Возвращает `false`, так как функция не требует возвращаемого значения для других операций.
 *
 * @exception При столкновении с Минотавром игра заканчивается, и программа завершает выполнение.
 */

    /**
 * @brief Checks for a collision between the Robot and the Minotaur.
 *
 * This function determines whether the Robot occupies the same cell as the Minotaur.
 * In case of a collision, it performs actions based on active effects:
 * - If the Robot has an active shield, it blocks the Minotaur’s attack.
 * - If the Robot has a sword, it defeats the Minotaur.
 * - If neither shield nor sword is active, the Minotaur catches the Robot and the game ends.
 *
 * @return bool Always returns `false` since collision handling is performed internally.
 *
 * @exception On collision without protection, the game ends and execution terminates.
 */

    if (robotX == minotaurX && robotY == minotaurY) {
        if (shieldTurns > 0) { // Если у робота есть щит, он защищает от атаки Минотавра
            gameMessages.push_back("\033[34m[SHIELD] The Minotaur attacked, but your shield protected you!\033[0m");
            shieldTurns--;
            return false;
        } else if (swordActive) { // Если у робота есть меч, он побеждает Минотавра
            std::cout << "DEBUG: Sword active - minotaur destroyed.\n";
            gameMessages.push_back("\033[33m[VICTORY] You used the sword to destroy the Minotaur!\033[0m\n");
            // Вывод сообщения перед завершением игры
            std::cout << "\n\033[33m[VICTORY] You used the sword to destroy the Minotaur!\033[0m\n";
            std::this_thread::sleep_for(std::chrono::seconds(2)); // Даем 2 секунды на отображение
            won = true;
            return true;
        } else { // В случае, если у робота нет защиты и оружия, Минотавр ловит его, и игра заканчивается
            gameMessages.push_back("\033[31m[DEATH] Game over! The Minotaur caught you.\033[0m");
            // Вывод сообщения перед завершением игры
            won = false;
            std::cout << "\n\033[31m[DEATH] Game over! The Minotaur caught you.\033[0m\n";
            std::this_thread::sleep_for(std::chrono::seconds(2)); // Даем 2 секунды на отображение
            endGame(won);
            exit(0);
            //return true;
        }
    }
    return false;
}


bool Game::checkWinCondition() {

    /**
 * @brief Проверяет условие победы.
 *
 * Если робот находится на выходе, игра считается выигранной.
 *
 * @exception нет
 */

    /**
 * @brief Checks the victory condition.
 *
 * The game is considered won if the robot is at the exit location.
 *
 * @exception none
 */

    /*
   std::cout << "Checking win condition...\n"; // Диагностика
   std::cout << "Robot position: (" << robotX << ", " << robotY << ")\n"; // Диагностика
   std::cout << "Exit position: (" << exitX << ", " << exitY << ")\n"; // Диагностика
    */


    if (robotX == exitX && robotY == exitY) {
        gameMessages.push_back("\033[32m[GAME OVER] Congratulations! You successfully escaped the labyrinth!\033[0m");
        std::cout << "\n\033[32m[GAME OVER] Congratulations! You successfully escaped the labyrinth!\033[0m\n";
        std::this_thread::sleep_for(std::chrono::seconds(2)); // Даем 2 секунды на отображение
        return true;
    }
    return false;
}

void Game::handleItem(int x, int y) {
    /**
     * @brief Обрабатывает найденный предмет, используя наследование.
     *
     * Выбирает случайный тип предмета (меч, щит, молот или туман),
     * активирует его эффект и обновляет игровые параметры.
     *
     * @param x Строка, в которой находится предмет.
     * @param y Столбец, в котором находится предмет.
     */

    /**
 * @brief Processes a discovered item using inheritance.
 *
 * Selects a random item type (sword, shield, hammer, or fog),
 * activates its effect, and updates the game parameters.
 *
 * @param x The row where the item is located.
 * @param y The column where the item is located.
 */

    // Определяем случайный выбор предмета
    // Determine a random item selection
    int randomEffect = rand() % 4;
    Item* item = nullptr;
    switch (randomEffect) {
        case 0:
            item = new Sword();
            break;
        case 1:
            item = new Shield();
            break;
        case 2:
            item = new Hammer();
            break;
        case 3:
            item = new Fog();
            break;
        default:
            break;
    }

    if (item) {
        Item::ItemEffect effect = item->activateEffect();

        // Добавляем сообщение об эффекте в активные эффекты и игровые сообщения
        activeEffects.push_back(effect.message);

        //отладка
        /*
        std::cout << "DEBUG: Effect applied: " << effect.message << std::endl;
        std::cout << "DEBUG: swordTurns = " << swordTurns << ", shieldTurns = " << shieldTurns
                  << ", hammerTurns = " << hammerTurns << ", fogTurns = " << fogTurns << std::endl;
        */

        gameMessages.push_back(effect.message);
        gameHistory << effect.message << "\n"; // Добавляем сообщение в историю игры

        // Обновляем игровые параметры на основе эффекта
        swordActive = effect.swordActive;
        swordTurns = effect.swordTurns;
        shieldTurns = effect.shieldTurns;
        hammerTurns = effect.hammerTurns;
        fogTurns = effect.fogTurns;

        // Удаляем предмет с карты
        labirint.setCell(x, y, '.');

        // Освобождаем память
        delete item;
    }
}


void Game::updateGameState() {


/**
 * @brief Обновляет состояние игры (например, статус предметов).
 *
 * Эта функция обновляет активные эффекты и другие параметры игры, отображая
 * соответствующие сообщения.
 *
 * @exception нет
 */

/**
 * @brief Updates the game state (e.g., item statuses).
 *
 * This function updates active effects and other game parameters, displaying
 * the corresponding messages.
 *
 * @exception none
 */


    int oldMinotaurX = minotaurX;
    int oldMinotaurY = minotaurY;

    labirint.setCell(robotX, robotY, '.');
    labirint.setCell(minotaurX, minotaurY, '.');

    moveMinotaur();

    checkMinotaurCollisionWithShield(oldMinotaurX, oldMinotaurY);

    labirint.setCell(robotX, robotY, 'R');
    labirint.setCell(minotaurX, minotaurY, 'M');

    if (swordTurns > 0) swordTurns--;
    if (shieldTurns > 0) shieldTurns--;
    if (hammerTurns > 0) hammerTurns--;
    if (fogTurns > 0) {
        displayFog();
        fogTurns--;
    } else {
        labirint.print();
    }

    // Проверка: находится ли робот на выходе
    // Check if the robot is at the exit


    if (labirint.checkRobotAtExit(robotX, robotY)) {
        gameMessages.push_back("\033[33m[VICTORY]Congratulations! You successfully escaped the labyrinth!\033[0m");
        exit(0); // Завершаем игру
    }

    if (checkCollision()) {
        gameMessages.push_back("\033[31m[DEATH] The Minotaur caught you! You have been killed!\033[0m");
        won = false; // Если игра окончена, дальше ничего не делаем
        return;
    }

    // Вывод заголовка сообщений
    cout << "\n\033[32m===  MESSAGES  ===\033[0m\n";

    if (gameMessages.empty()) {
        std::cout << "No messages.\n";
    } else {
        for (const auto& msg : gameMessages) {
            std::cout << msg << "\n";
        }
    }
    gameMessages.clear();

    // Обновляем таймер эффектов и удаляем истекшие
    // Update effect timers and remove expired ones
    for (auto it = activeEffects.begin(); it != activeEffects.end(); ) {
        if (it->find("[Sword]") != std::string::npos && swordTurns <= 0) {
            it = activeEffects.erase(it);
        } else if (it->find("[Shield]") != std::string::npos && shieldTurns <= 0) {
            it = activeEffects.erase(it);
        } else if (it->find("[Hammer]") != std::string::npos && hammerTurns <= 0) {
            it = activeEffects.erase(it);
        } else if (it->find("[Fog]") != std::string::npos && fogTurns <= 0) {
            it = activeEffects.erase(it);
        } else {
            ++it;
        }
    }

    //отладка
    /*
    std::cout << "DEBUG: After update - swordTurns = " << swordTurns
              << ", shieldTurns = " << shieldTurns
              << ", hammerTurns = " << hammerTurns
              << ", fogTurns = " << fogTurns << std::endl;
    */

    // Выводим все активные эффекты
    std::cout << "\n\033[32m=== ACTIVE EFFECTS ===\033[0m\n";
    if (activeEffects.empty()) {
        std::cout << "No active effects.\n";
    } else {
        for (const auto& effect : activeEffects) {
            std::cout << effect << "\n";
        }
    }

    // Выводим ошибки
    if (!errorMessages.empty()) {
        std::cout << "\n\033[31m=== ERROR MESSAGES ===\033[0m\n";
        for (const auto& error : errorMessages) {
            std::cout << error << "\n";
        }
        errorMessages.clear(); // Очищаем ошибки перед следующим шагом
    }

    // Добавляем текущее состояние лабиринта в gameHistory
    // Add the current state of the labyrinth to gameHistory

    for (int i = 0; i < labirint.getRows(); ++i) {
        for (int j = 0; j < labirint.getCols(); ++j) {
            gameHistory << labirint.getCell(i, j);
        }
        gameHistory << '\n';
    }
    gameHistory << "\n---\n"; // Разделитель между состояниями



}

void Game::displayFog() {

    /**
 * @brief Отображает лабиринт с эффектом тумана.
 *
 * Эта функция выводит лабиринт, скрывая клетки, находящиеся за пределами
 * видимости робота, с учётом эффекта тумана. Видимость ограничена радиусом,
 * который определяется переменной `fogRadius`. Все клетки, находящиеся
 * в пределах радиуса видимости, отображаются, остальные — скрыты.
 * В пределах видимости могут быть показаны разные объекты, такие как робот,
 * минотавр и предметы, с соответствующими цветами для лучшего восприятия.
 *
 * @note Эта функция также учитывает границы лабиринта, которые всегда отображаются.
 *
 * @exception нет
 */

    /**
 * @brief Displays the labyrinth with the fog effect.
 *
 * This function renders the labyrinth, hiding cells that are outside
 * the Robot’s visibility range due to the fog effect. Visibility is
 * limited by a radius defined by the `fogRadius` variable.
 * All cells within this visibility radius are shown, while the rest
 * are hidden. Within the visible area, objects such as the Robot,
 * the Minotaur, and items may be displayed using appropriate colors
 * for better clarity.
 *
 * @note This function also ensures that the labyrinth boundaries
 *       are always visible.
 *
 * @exception none
 */

    int fogRadius = 1;

    for (int i = 0; i < labirint.getRows(); ++i) {
        for (int j = 0; j < labirint.getCols(); ++j) {
            // Отображаем границы лабиринта
            if (i == 0 || i == labirint.getRows() - 1 || j == 0 || j == labirint.getCols() - 1) {
                std::cout << "#"; // Отображение стены
            }
            // Отображаем клетки внутри тумана
            else if (std::abs(i - robotX) <= fogRadius && std::abs(j - robotY) <= fogRadius) {
                char cell = labirint.getCell(i, j);

                if (cell == 'R') {
                    std::cout << "\033[32mR\033[0m"; // Зеленый робот
                } else if (cell == 'M') {
                    std::cout << "\033[31mM\033[0m"; // Красный минотавр
                } else if (cell == 'P') {
                    std::cout << "\033[34mP\033[0m"; // Синий предмет
                } else {
                    std::cout << cell;
                }
            }
                else {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
}

/**
 * @brief Обрабатывает столкновение Минотавра с Роботом при активном щите.
 *
 * Если Минотавр переместился в клетку Робота и у Робота есть оставшиеся
 * ходы щита, этот метод:
 *  - добавляет в gameMessages сообщение о том, что щит защитил от атаки,
 *  - уменьшает количество оставшихся ходов щита,
 *  - возвращает Минотавра на предыдущие координаты.
 *
 * @param oldMinotaurX Предыдущее значение X-координаты Минотавра.
 * @param oldMinotaurY Предыдущее значение Y-координаты Минотавра.
 */

/**
 * @brief Handles a collision between the Minotaur and the Robot when a shield is active.
 *
 * If the Minotaur moves into the Robot’s cell and the Robot has remaining shield turns,
 * this method:
 *  - Logs a message indicating the shield blocked the attack,
 *  - Decrements the shield’s remaining turns,
 *  - Moves the Minotaur back to its previous position.
 *
 * @param oldMinotaurX The Minotaur’s X-coordinate before its move.
 * @param oldMinotaurY The Minotaur’s Y-coordinate before its move.
 */
void Game::checkMinotaurCollisionWithShield(int oldMinotaurX, int oldMinotaurY) {
    // Если минотавр попадает на позицию робота
    if (minotaurX == robotX && minotaurY == robotY) {
        if (shieldTurns > 0) { // Если у робота есть щит
            gameMessages.push_back("\033[34m[SHIELD] The Minotaur attacked, but your shield protected you!\033[0m");
            shieldTurns--;

            // Возвращаем минотавра на старую позицию
            minotaurX = oldMinotaurX;
            minotaurY = oldMinotaurY;
        }
    }
}

void Game::endGame(bool won) {
    /**
     * @brief Завершает игру и сохраняет результаты в файл.
     *
     * Этот метод вызывает класс FileManager для записи итогового состояния игры,
     * включая историю состояний лабиринта, сообщения о событиях и конечный результат.
     *
     * @param won Булевый флаг, указывающий на победу (true) или поражение (false) игрока.
     */

    /**
 * @brief Ends the game and saves the results to a file.
 *
 * This method uses the FileManager class to write the final game state,
 * including the labyrinth history, event messages, and the outcome.
 *
 * @param won Boolean flag indicating whether the player won (true) or lost (false).
 */

    string file_name = "../game_result.txt";

    std::string finalMessage = (!gameMessages.empty() ? gameMessages.back() : "No final message.");

    if (lastLabState.empty()) {
        lastLabState = labirint.getState();
    }
    FileManager::saveGameResults(file_name,
                                 gameHistory.str(),
                                 won,
                                 lastLabState,
                                 finalMessage,
                                 labirint.getRows(),
                                 labirint.getCols(),
                                 numItems);

}

