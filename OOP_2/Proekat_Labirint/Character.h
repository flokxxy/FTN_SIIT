//
// Created by Виктория Аванесова on 20.12.2024.
//

#ifndef PROGECT_LABIRINT_CHARACTER_H
#define PROGECT_LABIRINT_CHARACTER_H

/*
 * Класс Character служит базовым классом для всех персонажей в лабиринте.
 * Он содержит основные атрибуты и функции, необходимые для управления позиционированием персонажей.
 */

class Character {
protected:
    int posX, posY; // Позиции персонажа на карте лабиринта по осям X и Y.

public:
    Character(int x, int y);
    /*
     * Конструктор класса Character.
     * Инициализирует персонажа в начальной позиции (x, y) на карте.
     *
     * Аргументы:
     * - x: начальная позиция персонажа по оси x.
     * - y: начальная позиция персонажа по оси y.
     */

    virtual ~Character() = default;
    /*
     * Виртуальный деструктор для класса Character.
     * Обеспечивает корректное уничтожение объектов производных классов.
     */

    int getX() const;// Возвращает текущую позицию персонажа по оси X.
    int getY() const;//Возвращает текущую позицию персонажа по оси Y.

    void setPosition(int x, int y);
    /*
     * Устанавливает новую позицию для персонажа.
     * Используется для обновления координат персонажа на карте.
     *
     * Аргументы:
     * - x: новая позиция по оси x.
     * - y: новая позиция по оси y.
     */

    virtual void move(int deltaX, int deltaY) = 0; // Pure virtual method

};


#endif //PROGECT_LABIRINT_CHARACTER_H
