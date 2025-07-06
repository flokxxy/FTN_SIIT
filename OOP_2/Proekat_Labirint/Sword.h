#ifndef PROGECT_LABIRINT_SWORD_H
#define PROGECT_LABIRINT_SWORD_H

#include "Item.h"
#include <string>

class Sword : public Item {
public:
    virtual ItemEffect activateEffect() override {
        ItemEffect effect;
        effect.swordActive = true;
        effect.swordTurns = 4;
        effect.message = "\033[33m[Sword] You can destroy the Minotaur! (" + std::to_string(effect.swordTurns) + " turns left)\033[0m";
        return effect;
    }
};

#endif // PROGECT_LABIRINT_SWORD_H
