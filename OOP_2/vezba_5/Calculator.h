//
// Created by Виктория Аванесова on 28.10.2024.
//

#ifndef CALCULATOR_H
#define CALCULATOR_H

#include "myComplex.h"
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class Calculator {
public:
    // Функция для обработки нескольких входных файлов
    void processFile(const string& inputFile, const string& outputFile);

private:
    // Функция для обработки одного входного файла
    void processFile(const string& inputFile);
    // Вспомогательные функции для парсинга данных и выполнения операций
    Complex parseOperand(const string& str);
    string parseOperation(const string& operation);
};

#endif // CALCULATOR_H
