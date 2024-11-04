#include "Calculator.h"
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;

// Метод для обработки одного файла
void Calculator::processFile(const string& inputFile, const string& outputFile) {
    ifstream inFile(inputFile);
    if (!inFile.is_open()) {
        cerr << "Ошибка открытия входного файла: " << inputFile << endl;
        return;
    }

    ofstream outFile(outputFile);
    if (!outFile.is_open()) {
        cerr << "Ошибка создания выходного файла: " << outputFile << endl;
        return;
    }

    string line;
    while (getline(inFile, line)) {
        try {
            // Разделение строки на операнды и операцию
            size_t firstSpace = line.find(' ');
            size_t secondSpace = line.find(' ', firstSpace + 1);
            if (firstSpace == string::npos || secondSpace == string::npos) {
                throw runtime_error("Неверный формат строки: " + line);
            }

            string operand1Str = line.substr(0, firstSpace);
            string operationStr = line.substr(firstSpace + 1, secondSpace - firstSpace - 1);
            string operand2Str = line.substr(secondSpace + 1);

            Complex operand1 = parseOperand(operand1Str);
            Complex operand2 = parseOperand(operand2Str);
            Complex result;

            // Выполнение операции
            if (operationStr == "ADD"||operationStr == "+") {
                result = operand1 + operand2;
            } else if (operationStr == "SUB"||operationStr == "-") {
                result = operand1 - operand2;
            } else if (operationStr == "MUL"||operationStr == "*") {
                result = operand1 * operand2;
            } else {
                throw runtime_error("Неизвестная операция: " + operationStr);
            }

            // Запись результата в выходной файл
            outFile << "= " << result << endl;
        } catch (const exception& e) {
            cerr << "Ошибка: " << e.what() << endl;
            outFile << "Ошибка: " << e.what() << endl;
            return;
        }
    }

    inFile.close();
    outFile.close();
    cout << "Результаты вычислений сохранены в " << outputFile << endl;
}

// Метод для парсинга комплексного числа из строки
Complex Calculator::parseOperand(const string& str) {
    double real, imag;
    sscanf(str.c_str(), "%lf+%lfi", &real, &imag);
    return Complex(real, imag);
}
