//
// Created by Виктория Аванесова on 28.10.2024.
//

#ifndef OOP2_VEZB5_MYCOMPLEX_H
#define OOP2_VEZB5_MYCOMPLEX_H

#include <iostream>

using namespace std;

//этот файл где объявлены/инициализированны функции/методы которые будут вызваны для этого класса
class Complex{
private:
    double x;
    double y;

public:

    Complex();
    Complex(double real,double imag);
    Complex(const Complex& other);

    void setReal(double real);
    void setImag(double imag);
    double getReal();
    double getImag();

    Complex add(Complex num);
    Complex sub(Complex num);
    Complex mul(Complex num);
    Complex conj(Complex num);

    Complex operator+(Complex num);
    Complex operator-(Complex num);
    Complex operator*(Complex num);
    Complex operator~();

    friend istream& operator>>(istream& in, Complex& num);
    friend ostream& operator<<(ostream& os, const Complex& num);

    string to_string();
};


#endif //OOP2_VEZB5_MYCOMPLEX_H
