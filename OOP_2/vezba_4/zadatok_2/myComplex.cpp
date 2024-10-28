#include "myComplex.h"
#include <iostream>

//тут описана работа функций для класса

using namespace std;

Complex::Complex():x(0.0),y(0.0) {};
Complex::Complex(double real, double imag) :x(real), y(imag)  {};

Complex::Complex(const Complex &other):x(other.x), y(other.y) {};

//Complex::~Complex() {};

void Complex::setReal(double real) {
    (*this).x=real;
};
void Complex::setImag(double imag) {
    (*this).y=imag;
}

double Complex::getReal() {
    return  (*this).x;
}
double Complex::getImag() {
    return  (*this).y;
}

string Complex::to_string() {
    string s;
    s=std::to_string(x)+"+"+std::to_string(y)+"i";
    return s;
}

Complex Complex::operator+(Complex num) {
    return Complex((*this).x+num.getReal(),(*this).y+num.getImag());
}
Complex Complex::operator-(Complex num) {
    return Complex((*this).x-num.getReal(),(*this).y-num.getImag());
}

Complex Complex::operator*(Complex num) {
    return Complex(
            (*this).x * num.getReal() - (*this).y * num.getImag(),    // Реальная часть
            (*this).x * num.getImag() + (*this).y * num.getReal()     // Мнимая часть
    );
}

Complex Complex::operator~() {
    return Complex((*this).x, -(*this).y);  // Сопряжение меняет знак у мнимой части
}


// Реализация дружественного оператора ввода
istream& operator>>(istream& in, Complex& num) {
    cout << "Введите действительную часть: ";
    in >> num.x;
    cout << "Введите мнимую часть: ";
    in >> num.y;
    return in;
}

// Реализация дружественного оператора вывода
ostream& operator<<(ostream& os, const Complex& num) {
    os << "(" << num.x<< ", " << num.y << "i)";
    return os;
    //вывод должен быть константен
}


Complex Complex::sub(Complex num) {
    return Complex(x - num.getReal(), y - num.getImag());
}
Complex Complex::add(Complex num) {
    return Complex(x + num.getReal(), y + num.getImag());
}

Complex Complex::mul(Complex num) {
    return Complex(
            x * num.getReal() - y * num.getImag(),
            x * num.getImag() + y * num.getReal()
    );
}

Complex Complex::conj(Complex num) {
    return Complex(x, -y);
}

