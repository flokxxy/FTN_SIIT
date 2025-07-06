//
// Created by Виктория Аванесова on 21.01.2025.
//

#ifndef PROGECT_LABIRINT_FOG_H
#define PROGECT_LABIRINT_FOG_H

#include "Item.h"
#include <string>

class Fog : public Item {
public:
    virtual ItemEffect activateEffect() override {
        ItemEffect effect;
        effect.fogTurns = 3;
        effect.message = "\033[36m[Fog] Visibility reduced to 3x3! (" + std::to_string(effect.fogTurns) + " turns left)\033[0m";
        return effect;
    }
};

#endif // PROGECT_LABIRINT_FOG_H
