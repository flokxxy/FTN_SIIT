#include <iostream>
#include <complex>
#include "myComplex.h"


using namespace std;


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
