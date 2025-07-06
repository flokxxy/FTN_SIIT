//
// Created by Виктория Аванесова on 21.01.2025.
//

#ifndef PROGECT_LABIRINT_HAMMER_H
#define PROGECT_LABIRINT_HAMMER_H

#include "Item.h"
#include <string>

class Hammer : public Item {
public:
    virtual ItemEffect activateEffect() override {
        ItemEffect effect;
        effect.hammerTurns = 4;
        effect.message = "\033[35m[Hammer] You can break walls! (" + std::to_string(effect.hammerTurns) + " turns left)\033[0m";
        return effect;
    }
};

#endif // PROGECT_LABIRINT_HAMMER_H
