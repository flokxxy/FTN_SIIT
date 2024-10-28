#include <iostream>
#include <complex>
#include "myComplex.h"

//1 
using namespace std;

class Complex{
private:
    double real;
    double imag;

public:

    double getReal() const {
        return real;
    }
    double getImag() const {
        return imag;
    }

    // Конструктор
    Complex(double r = 0.0, double i = 0.0) : real(r), imag(i) {}


    // Операции над комплексными числами
    Complex add(const Complex& other) const;
    Complex sub(const Complex& other) const;
    Complex mul(const Complex& other) const;
    Complex conj() const;


    // Метод для сложения двух комплексных чисел
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    Complex operator-(const Complex& other) const {
        return Complex(real - other.real, imag - other.imag);
    }

    // Умножение двух комплексных чисел
    Complex operator*(const Complex& other) const {
        return Complex(real * other.real - imag * other.imag,
                       real * other.imag + imag * other.real);
    }

    // Умножение на действительное число
    Complex operator*(double scalar) const {
        return Complex(real * scalar, imag * scalar);
    }
    
    // Конъюгация
    Complex operator~() const {
        return Complex(real, -imag);
    }

    void print() const {
        cout << "(" << real << ", " << imag << "i)";
    }
};


int main(int argc, char** argv) {
    Complex a(3.0, 4.0);   // Инициализация (3, 4i)
    Complex b(5.0, 7.0);   // Инициализация (5, 7i)
    Complex c;

    cout << "a (" << a.getReal() << ", " << a.getImag() << "i) " << endl;
    cout << "b (" << b.getReal() << ", " << b.getImag() << "i) " << endl;

    c = a.operator+(b);
    cout << "a + b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;

    c = a.operator-(b);
    cout << "a - b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;

    c = a.operator*(b);
    cout << "a * b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;

    c = a.operator~();
    cout << "~a = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;

    cout << "Done!" << endl;

    return 0;
}
