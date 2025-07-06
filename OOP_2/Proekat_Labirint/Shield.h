//
// Created by Виктория Аванесова on 21.01.2025.
//

#ifndef PROGECT_LABIRINT_SHIELD_H
#define PROGECT_LABIRINT_SHIELD_H

#include "Item.h"
#include <string>

class Shield : public Item {
public:
    virtual ItemEffect activateEffect() override {
        ItemEffect effect;
        effect.shieldTurns = 4;
        effect.message = "\033[34m[Shield] You are protected from Minotaur! (" + std::to_string(effect.shieldTurns) + " turns left)\033[0m";
        return effect;
    }
};

#endif // PROGECT_LABIRINT_SHIELD_H
