#include "Labirint.h"
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <sstream>




/**
 * Конструктор класса Labirint.
 * Инициализирует лабиринт с заданными размерами и количеством предметов.
 * После инициализации сразу же генерирует лабиринт и определяет позицию выхода.
 *
 * Аргументы:
 * - rows: количество строк в лабиринте.
 * - cols: количество столбцов в лабиринте.
 * - numItems: количество предметов для размещения в лабиринте.
 */
/**
 * @brief Constructor of the Labirint class.
 *
 * Initializes the labyrinth with the specified dimensions and number of items.
 * Immediately after initialization, it generates the maze and determines the exit position.
 *
 * @param rows     Number of rows in the labyrinth.
 * @param cols     Number of columns in the labyrinth.
 * @param numItems Number of items to be placed in the labyrinth.
 */

Labirint::Labirint(int rows, int cols, int numItems)
        : rows(rows), cols(cols), numItems(numItems)
{
    std::srand(static_cast<unsigned int>(std::time(nullptr)));
    grid.resize(rows, std::vector<char>(cols, '#'));
    generate();
    auto [exitRow, exitCol] = getExit();
}

void Labirint::generate() {
    /**
 * Генерирует лабиринт с использованием алгоритма Эллера и других вспомогательных методов.
 * В процессе создаются вход и выход, а также проверяется наличие связанного пути между ними.
 * При неудачной генерации выводится сообщение об ошибке.
 *
 * Аргументы: Нет.
 * Возвращаемое значение: Нет.
 * Исключения: std::runtime_error, если лабиринт не удается сгенерировать
     * за пределенное количество попыток.
 */

    /**
* @brief Generates the labyrinth using the Eller algorithm and other helper methods.
*
* During generation, the entrance and exit are created, and the existence of a connected
* path between them is verified. If generation fails within the allowed number of attempts,
* an error message is displayed.
*
* @exception std::runtime_error Thrown if the labyrinth cannot be generated within the
*                              specified number of attempts.
*/

        bool success = false;
        unsigned attempt = 0;

        while (!success) {
            ++attempt;

            // Полная очистка сетки
            for (int r = 0; r < rows; ++r)
                for (int c = 0; c < cols; ++c)
                    grid[r][c] = '#';

            // Случайный вход/выход
            unsigned enterCol = 1 + std::rand() % (cols - 2);
            unsigned exitCol  = 1 + std::rand() % (cols - 2);
            grid[0][enterCol]       = 'U';
            grid[rows - 1][exitCol] = 'I';

            // Алгоритм Эллера + полукруги
            generateWithEller();
            createSemicircle(1,       enterCol, 3, true);
            createSemicircle(rows - 2, exitCol,  3, false);

            // Проверка пути
            if (isPathExists(1, enterCol, rows - 2, exitCol)) {
                success = true;
            }
            else if (attempt % 50 == 0) {
                std::cerr << "Warning: уже " << attempt
                          << " попыток, а пути нет. Повторяем...\n";
            }
        }
        placeItems(numItems);
    }




/**
 * Реализует алгоритм Эллера для генерации горизонтальных и вертикальных путей в лабиринте.
 * Этот метод вызывается внутри метода generate().
 *
 * Аргументы: Нет.
 * Возвращаемое значение: Нет.
 */
/**
 * @brief Implements the Eller algorithm for generating horizontal and vertical passages in the labyrinth.
 *
 * This method is called within the generate() function.
 *
 * @exception none
 */

void Labirint::generateWithEller() {
    // Реализация алгоритма Эллера
    std::vector<int> currentSet(cols - 2, 0);
    int uniqueSetId = 1;

    auto mergeSets = [&](int from, int to) {
        for (auto& id : currentSet) {
            if (id == from) id = to;
        }
    };

    for (int row = 1; row < rows - 1; row += 2) {
        for (int col = 1; col < cols - 1; col++) {
            if (currentSet[col - 1] == 0) {
                currentSet[col - 1] = uniqueSetId++;
            }

            if (col < cols - 2 && rand() % 2 == 0) {
                mergeSets(currentSet[col - 1], currentSet[col]);
                grid[row][col] = '.';
                grid[row][col + 1] = '.';
            }
        }

        if (row < rows - 2) {
            for (int col = 1; col < cols - 1; col++) {
                if (rand() % 2 == 0) {
                    grid[row + 1][col] = '.';
                }
            }
        }
    }
}

/**
 * Создает полукруг в лабиринте вокруг заданного центра.
 * Может создавать как верхнюю, так и нижнюю половину полукруга.
 *
 * Аргументы:
 * - centerRow: центральная строка полукруга.
 * - centerCol: центральный столбец полукруга.
 * - radius: радиус полукруга.
 * - topHalf: если true, создает верхнюю половину, иначе нижнюю.
 * Возвращаемое значение: Нет.
 */
/**
 * Creates a semicircle in the labyrinth around a specified center.
 * Can generate either the upper or lower half of the semicircle.
 *
 * Arguments:
 * - centerRow: the center row of the semicircle.
 * - centerCol: the center column of the semicircle.
 * - radius: the radius of the semicircle.
 * - topHalf: if true, generates the upper half; otherwise, the lower half.
 * Returns: none.
 */

void Labirint::createSemicircle(unsigned int centerRow, unsigned int centerCol,
                                unsigned int radius, bool topHalf) {
    for (int dr = -radius; dr <= (int)radius; dr++) {
        for (int dc = -radius; dc <= (int)radius; dc++) {
            int rr = centerRow + dr;
            int cc = centerCol + dc;

            if (rr > 0 && rr < rows - 1 && cc > 0 && cc < cols - 1 &&
                std::sqrt(dr * dr + dc * dc) <= radius) {
                if (topHalf && dr >= 0) {
                    grid[rr][cc] = '.';
                }
                if (!topHalf && dr <= 0) {
                    grid[rr][cc] = '.';
                }
            }
        }
    }
}


/**
 * Проверяет, существует ли путь от заданной начальной точки (sr, sc) до конечной точки (er, ec).
 * Использует алгоритм поиска в ширину (BFS) для определения пути.
 *
 * Аргументы:
 * - sr: начальная строка.
 * - sc: начальный столбец.
 * - er: конечная строка.
 * - ec: конечный столбец.
 * Возвращаемое значение: true, если путь существует, иначе false.
 */
/**
 * Checks whether a path exists from the specified starting point (sr, sc) to the ending point (er, ec).
 * Uses the Breadth-First Search (BFS) algorithm to determine the path.
 *
 * Arguments:
 * - sr: starting row.
 * - sc: starting column.
 * - er: ending row.
 * - ec: ending column.
 * @return true if a path exists; otherwise false.
 */

bool Labirint::isPathExists(unsigned int sr, unsigned int sc, unsigned int er, unsigned int ec) {
    std::queue<std::pair<int, int>> q;
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    q.push({sr, sc});
    visited[sr][sc] = true;

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == (int)er && c == (int)ec) return true;

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                !visited[nr][nc] && grid[nr][nc] == '.') {
                visited[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }

    return false;
}

/**
 * Возвращает колонку, в которой расположен вход в лабиринт.
 * Проверяет первую строку на наличие символа 'U'.
 *
 * Аргументы: Нет.
 * Возвращаемое значение: Колонка входа или -1, если вход не найден.
 */
/**
 * Returns the column index where the labyrinth entrance is located.
 * Scans the first row for the 'U' character.
 *
 * Arguments: None.
 * @return The entrance column index, or -1 if the entrance is not found.
 */

int Labirint::getEntranceColumn() const {
    for (int col = 0; col < cols; ++col) {
        if (grid[0][col] == 'U') {
            return col; // Колонка, где расположен вход
        }
    }
    return -1; // Если вход не найден
}


/**
 * Определяет, является ли клетка по заданным координатам стеной.
 *
 * Аргументы:
 * - x: строка клетки.
 * - y: столбец клетки.
 * Возвращаемое значение: true, если клетка является стеной, иначе false.
 */
/**
 * Determines whether the cell at the specified coordinates is a wall.
 *
 * Arguments:
 * - x: the row index of the cell.
 * - y: the column index of the cell.
 * @return true if the cell is a wall; otherwise false.
 */

bool Labirint::isWall(int x, int y) const {
    if (x < 0 || x >= rows || y < 0 || y >= cols) {
        return true; // Клетки вне границ считаются стенами
    }
    return grid[x][y] == '#';
}


/**
 * Возвращает координаты выхода из лабиринта.
 * Проверяет последнюю строку на наличие символа 'I'.
 *
 * Аргументы: Нет.
 * Возвращаемое значение: Пара координат выхода, или {-1, -1}, если выход не найден.
 */
/**
 * Returns the coordinates of the labyrinth exit.
 * Scans the last row for the 'I' character.
 *
 * @return A pair of exit coordinates {row, col}, or {-1, -1} if the exit is not found.
 */

std::pair<int, int> Labirint::getExit() const {
    for (int col = 0; col < cols; ++col) {
        if (grid[rows - 1][col] == 'I') {
            return {rows - 1, col}; // Координаты выхода
        }
    }
    std::cerr << "Exit not found!\n";
    return {-1, -1}; // Если выход не найден
}


/**
 * Устанавливает значение в клетку лабиринта по заданным координатам.
 *
 * Аргументы:
 * - x: строка клетки.
 * - y: столбец клетки.
 * - value: значение для установки.
 * Возвращаемое значение: Нет.
 */
/**
 * Sets the value of a labyrinth cell at the specified coordinates.
 *
 * @param x     Row index of the cell.
 * @param y     Column index of the cell.
 * @param value The value to set in the cell.
 */

void Labirint::setCell(int x, int y, char value) {
    if (x >= 0 && x < rows && y >= 0 && y < cols) {
        grid[x][y] = value;
    }
}



/**
 * Возвращает значение клетки по заданным координатам.
 *
 * Аргументы:
 * - x: строка клетки.
 * - y: столбец клетки.
 * Возвращаемое значение: Символ, находящийся в клетке.
 */
/**
 * Returns the value of the cell at the specified coordinates.
 *
 * @param x Row index of the cell.
 * @param y Column index of the cell.
 * @return The character located in the cell.
 */

char Labirint::getCell(int x, int y) const {
    if (x >= 0 && x < rows && y >= 0 && y < cols) {
        return grid[x][y];
    }
    return '#';
}


/**
 * Проверяет, существует ли путь от входа до выхода в лабиринте.
 * Использует BFS для проверки наличия пути.
 *
 * Аргументы: Нет.
 * Возвращаемое значение: true, если путь существует, иначе false.
 */
/**
 * Checks whether a path exists from the entrance to the exit in the labyrinth.
 * Uses BFS to verify the presence of a path.
 *
 * Arguments: None.
 * @return true if a path exists; otherwise false.
 */

bool Labirint::hasPathToExit() const {
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    std::queue<std::pair<int, int>> queue;

    // Найдем вход
    int startRow = 0, startCol = getEntranceColumn();
    if (startCol == -1) return false; // Вход не найден

    // Найдем выход
    auto [endRow, endCol] = getExit();
    if (endRow == -1 || endCol == -1) return false; // Выход не найден

    // Инициализация BFS
    queue.push({startRow, startCol});
    visited[startRow][startCol] = true;

    // Направления {вверх, вниз, влево, вправо}
    const int dR[4] = {-1, 1, 0, 0};
    const int dC[4] = {0, 0, -1, 1};

    while (!queue.empty()) {
        auto [r, c] = queue.front();
        queue.pop();

        if (r == endRow && c == endCol) {
            return true; // Достигли выхода
        }

        for (int i = 0; i < 4; ++i) {
            int nr = r + dR[i];
            int nc = c + dC[i];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && grid[nr][nc] == '.') {
                visited[nr][nc] = true;
                queue.push({nr, nc});
            }
        }
    }

    return false; // Пути нет
}

bool Labirint::isExit(int x, int y) const {
    return getCell(x, y) == 'I';
}


/**
 * Проверяет, находится ли робот на выходе из лабиринта.
 * Выводит сообщение о успехе, если робот достиг выхода.
 *
 * Аргументы:
 * - robotX: строка, в которой находится робот.
 * - robotY: столбец, в котором находится робот.
 * Возвращаемое значение: true, если робот находится на выходе, иначе false.
 */
/**
 * Checks whether the robot is at the labyrinth exit.
 * Displays a success message if the robot has reached the exit.
 *
 * @param robotX The row index of the robot.
 * @param robotY The column index of the robot.
 * @return true if the robot is at the exit; otherwise false.
 */

bool Labirint::checkRobotAtExit(int robotX, int robotY) const {
    auto [exitRow, exitCol] = getExit();
    return (robotX == exitRow && robotY == exitCol);
}


/**
 * Размещает заданное количество предметов в лабиринте на случайных пустых клетках.
 *
 * Аргументы:
 * - numItems: количество предметов для размещения.
 * Возвращаемое значение: Нет.
 */
/**
 * Places the specified number of items in the labyrinth on random empty cells.
 *
 * @param numItems The number of items to place.
 * @return none
 */

void Labirint::placeItems(int numItems) {
    srand(time(nullptr));
    int placed = 0;
    while (placed < numItems) {
        int x = rand() % rows;
        int y = rand() % cols;
        if (grid[x][y] == '.') { // Только на пустые клетки
            grid[x][y] = 'P';
            placed++;
            //std::cout << "\033[34mItem placed at (" << x << ", " << y << ").\033[0m\n"; // Отладочное сообщение
        }
    }
}


/**
 * Отображает лабиринт в консоли, используя цветовую кодировку для особых объектов,
 * таких как робот или минотавр.
 *
 * Аргументы: Нет.
 * Возвращаемое значение: Нет.
 */
/**
 * Displays the labyrinth in the console using color coding for special objects,
 * such as the robot or the minotaur.
 *
 * Arguments: None.
 * @return none
 */

void Labirint::print() const {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            char cell = grid[i][j];
            if (cell == 'R') {
                std::cout << "\033[32mR\033[0m"; // Зеленый цвет для робота
            } else if (cell == 'M') {
                std::cout << "\033[31mM\033[0m"; // Красный цвет для минотавра
            } else {
                std::cout << cell; // Обычная печать для остальных клеток
            }
        }
        std::cout << '\n';
    }
}


/**
     * @brief Возвращает текущее состояние лабиринта в виде строки.
     *
     * Метод проходит по всей сетке лабиринта и формирует строку, представляющую лабиринт.
     *
     * @return std::string Строка с текущим видом лабиринта.
     */
/**
* @brief Returns the current state of the labyrinth as a string.
*
* This method traverses the entire labyrinth grid and constructs
* a string representing the labyrinth.
*
* @return std::string A string depicting the current view of the labyrinth.
*/

std::string Labirint::getState() const {
    std::ostringstream oss; //Создаётся поток для накопления строки.
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            oss << grid[i][j];
        }
        oss << "\n";
    }
    return oss.str();
}