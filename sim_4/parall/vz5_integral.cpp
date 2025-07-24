#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>

#include "tbb/task_group.h"
#include <tbb/tick_count.h>


using namespace std;
using namespace tbb;

#define delta 0.000001
#define LOWER 0
#define UPPER 2*3.14

//wolfram alfa formula: (integrate exp(-1/x) cos(x) from x = 0 to 3.14)
//result -0.495667

double calculation(double x);
double incremental(double lowerBound, double upperBound);
double serial_integration(double lowerBound, double upperBound);
double parallel_integration(double lowerBound, double upperBound);

const double cutOff = 0.0001;

int main() {
	double serialResult = 0;
	double parallelResult = 0;



	cout << "Serial integral function..." << endl;
	tick_count startTime = tick_count::now();
	serialResult = serial_integration(LOWER, UPPER);
	tick_count endTime = tick_count::now();
	double serialTime = (endTime - startTime).seconds();

	cout << "Serial result: " << serialResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl << endl;

	cout << "Paralel integral function..." << endl;
	startTime = tick_count::now();
	parallelResult = parallel_integration(LOWER, UPPER);
	endTime = tick_count::now();
	double parallelTime = (endTime - startTime).seconds();

	cout << "Paralel result: " << parallelResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl;


	//часть с записью
	ofstream results("results.txt", ios::app);
	results << "Delta: " << delta << ", CutOff: " << cutOff
		<< ", Serial: " << serialResult
		<< ", Parallel: " << parallelResult
		<< ", Speedup: " << serialTime / parallelTime
		<< ", SerialTime: " << serialTime
		<< ", ParallelTime: " << parallelTime
		<< endl;
	results.close();

	return 0;
}

double calculation(double x) {
	return exp(-0.5 / x) * delta * cos(x);
}

double incremental(double lowerBound, double upperBound) {
	double res = 0;
	for (double iter = lowerBound; iter <= upperBound; iter += delta)
	{
		res += calculation(iter);
	}
	return res;
}

double serial_integration(double lowerBound, double upperBound) {

	if ((upperBound - lowerBound) <= cutOff) {
		return incremental(lowerBound, upperBound);
	}
	else {
		double mid = (lowerBound + upperBound) / 2.0;
		double left = serial_integration(lowerBound, mid);
		double right = serial_integration(mid, upperBound);
		return left + right;
	}
}

double parallel_integration(double lowerBound, double upperBound) {

	if ((upperBound - lowerBound) <= cutOff) {
		return incremental(lowerBound, upperBound);
	}
	else {
		double mid = (lowerBound + upperBound) / 2.0;
		double leftResult = 0, rightResult = 0;

		task_group tg;
		tg.run([&] { leftResult = parallel_integration(lowerBound, mid); });
		tg.run([&] { rightResult = parallel_integration(mid, upperBound); });
		tg.wait();

		return leftResult + rightResult;
	}
}

