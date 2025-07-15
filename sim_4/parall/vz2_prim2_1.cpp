#include <stdio.h>
#include <float.h>

#include "tbb\tbb.h"
#include "tbb\parallel_reduce.h"

using namespace tbb;
//поиск индекса минимального значения

float Foo(float a) {
	return a;
}

//TODO: Create a class called MinIndexFoo with constructors, operator() and the join method
//структура для парал нахождения минимума
class MinIndexFoo {
public:
	const float* arr; //входной массив
	float min_val;
	long min_index;


	MinIndexFoo(const float* a) : arr(a), min_val(FLT_MAX), min_index(-1) {}

	MinIndexFoo(MinIndexFoo& s, split) : arr(s.arr), min_val(FLT_MAX), min_index(-1) {}

	// Параллельная часть: поиск минимума в поддиапазоне
	void operator()(const blocked_range<size_t>& r) {
		for (size_t i = r.begin(); i < r.end(); ++i) {
			float val = Foo(arr[i]);
			if (val < min_val) {
				min_val = val;
				min_index = i;
			}
		}
	}

	// Объединение двух результатов
	void join(const MinIndexFoo& h) {
		if (h.min_val < min_val) {
			min_val = h.min_val;
			min_index = h.min_index;
		}
	}

};


//TODO: Create a function for parallel minimum
long ParallelMinIndexFoo(const float* a, int n) {
	MinIndexFoo result(a);
	parallel_reduce(blocked_range<size_t>(0, n), result);
	return result.min_index;

}

int main() {
	float a[100];

	for (int i = 0; i < 100; ++i) {
		a[i] = -i;
	}

	long ind = ParallelMinIndexFoo(a, 100);
	printf("%d\n", ind);

	return 0;
}
