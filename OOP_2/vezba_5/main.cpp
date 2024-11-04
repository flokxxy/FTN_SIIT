#include "Calculator.h"
#include <iostream>
#include <fstream>

using namespace std;

// Функция для создания входного файла с выражениями
void createInputFile(const string& inputFileName) {
    ofstream inputFile(inputFileName);
    if (!inputFile.is_open()) {
        cerr << "Ошибка создания входного файла: " << inputFileName << endl;
        return;
    }

    cout << "Введите выражения в формате (например, 4+3i ADD 2-1i)." << endl;
    cout << "Введите пустую строку для завершения ввода." << endl;

    string line;
    cout<<endl;
    for(int k=0;true;k++){
        cout << "выражение "<< k+1 <<": ";
        getline(cin, line);
        if (line.empty()) break;  // Завершаем ввод при пустой строке
        inputFile << line << endl;
    }

    inputFile.close();
    cout << "Входной файл " << inputFileName << " создан." << endl;
}
/* //main на один файл
int main() {
    // Создание объекта класса Calculator
    Calculator calculator;

    // Задание имен входного и выходного файлов
    string inputFileName = "input.txt";
    string outputFileName = "output.txt";

    // Создаем входной файл и записываем в него выражения
    createInputFile(inputFileName);

    // Обрабатываем входной файл и записываем результаты в выходной файл
    calculator.processFile(inputFileName, outputFileName);

    cout << "Обработка завершена. Результаты сохранены в " << outputFileName << endl;
    return 0;
}
*/

int main(){
    Calculator calculator;

    // Ввод количества файлов
    int numFiles;
    cout << "Введите количество файлов для создания и обработки: ";
    cin >> numFiles;
    cin.ignore();  // Игнорируем оставшийся символ новой строки

    vector<string> inputFiles(numFiles);
    vector<string> outputFiles(numFiles);

    // Создание и запись выражений в файлы
    for (int i = 0; i < numFiles; ++i) {
        inputFiles[i] = "input" + to_string(i + 1) + ".txt";
        outputFiles[i] = "output" + to_string(i + 1) + ".txt";

        cout << "Создание файла: " << inputFiles[i] << endl;
        createInputFile(inputFiles[i]);
    }

    // Обработка файла и запись результатов
    for (int i = 0; i < numFiles; ++i) {
        calculator.processFile(inputFiles[i], outputFiles[i]);
    }

    cout << "Обработка всех файлов завершена." << endl;
    return 0;
}