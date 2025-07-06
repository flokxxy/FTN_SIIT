//
// Created by Виктория Аванесова on 21.01.2025.
//

#ifndef PROGECT_LABIRINT_ITEM_H
#define PROGECT_LABIRINT_ITEM_H


#include <string>

/**
 * @brief Класс Item отвечает за обработку предметов,
 * которые подбирает робот во время игры.
 *
 * Он определяет тип эффекта предмета и возвращает структуру с информацией
 * о том, какой эффект следует активировать (например, меч, щит, молот или туман),
 * а также соответствующее сообщение.
 */
/**
 * @brief The Item class handles items picked up by the robot during the game.
 *
 * It determines the type of item effect and returns a structure containing
 * information about which effect to activate (e.g., sword, shield, hammer, or fog),
 * along with the corresponding message.
 */

class Item {
public:
    /**
     * @brief Структура, содержащая параметры эффекта, активируемого предметом.
     */
    struct ItemEffect {
        bool swordActive; //Флаг активации меча
        int swordTurns;   //Количество ходов действия меча
        int shieldTurns;  //Количество ходов действия щита
        int hammerTurns;  //Количество ходов действия молота
        int fogTurns;     //Количество ходов действия тумана
        std::string message; //Сообщение, описывающее эффект

        ItemEffect()
            : swordActive(false), swordTurns(0), shieldTurns(0),
            hammerTurns(0), fogTurns(0), message("") {}
    };

    //ItemEffect processItem();

    virtual ~Item() {}

    virtual ItemEffect activateEffect() = 0;
};

#endif // PROGECT_LABIRINT_ITEM_H
