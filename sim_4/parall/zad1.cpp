#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include <iostream>

using namespace tbb;
using namespace std;

//TODO: Create a class/structure for paralelization
struct Average{
	// Структура описывает параллельную работу для части массива input
	const double* input;
	double* output;

	void operator()(const blocked_range<int>& r) const { // оператор (используеться для обработки диапазона)
		// blocked_range управляет, какой кусок обрабатывает каждый поток
		for (int i = r.begin(); i < r.end(); i++)
			output[i] = (input[i] + input[i + 1] + input[i + 2]) * (1 / 3.0f);
	}

};

// Note: The input must be padded such that input[-1] and 
// input[n] can be used to calculate the first and last 
// output values.

//TODO: Create a funcion for paralelization
void ParalAverage(double* output, const double* input, size_t n) {
	//Создаёт экземпляр Average и запускает его параллельно через parallel_for
	Average avg;
	avg.input = input;
	avg.output = output;

	parallel_for(blocked_range<int>(0, n, 12), avg);
}


// Sets output[i] to the average of input[i-1], input[i] and input[i+1]
int main() {
	double input[1002], output_serial[1000], output_parallel[1000];
	int test = 0;

	input[0] = 0;
	input[1001] = 0;
	for (int i = 1; i < 1001; i++) {
		input[i] = i * 3.14;
	}

	for (int i = 0; i < 1000; i++) {
		output_serial[i] = (input[i] + input[i + 1] + input[i + 2]) * (1 / 3.0f);
	} //вычисляеться среднее

	//TODO: Paralell average
	ParalAverage(output_parallel, input, 1000);
	// паралельная версия вычисления
	 
	//TODO: Check if the results are equal

	bool are_equal = true; // флаг равенства
	const double e = 1e-9;

	for (int i = 0; i < 1000; i++) { // проверка на равенство
		if (fabs(output_serial[i] - output_parallel[i] > e)) {
			are_equal = false;
			cout << "Greska" << i << endl;
			break;
		}
	}
	if (are_equal) cout << "good";


	return 0;
}
