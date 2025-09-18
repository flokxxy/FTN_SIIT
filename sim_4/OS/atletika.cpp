/*
	Modelovati koriscenje zaletista na atletskom mitingu.
	Isto zaletiste koriste dve discipline: skok u dalj i bacanje koplja.
	Zaletiste ne mogu istovremeno da koriste dva takmicara.
	Discipline se naizmenicno smenjuju na zaletistu (jedan skakac u dalj, pa jedan bacac koplja i tako redom).

	Skok u dalj za jednog takmicara traje 1 sekundu. Bacanje koplja 2 sekunde.
	Metodu skaci poziva skakac u dalj. Metoda vraca duzinu u metrima koliko je takmicar skocio
	(izmedju 0 i 9 metara moze skociti) i koliko je ukupno trebalo vremena da zavrsi skok
	(koliko je zajedno trajalo cekanje i skakanje).
	Metodu baciKoplje poziva bacac koplja. Metoda vraca duzinu u metrima koliko je takmicar bacio koplje
	(izmedju 0 i 100 metara moze baciti) i koliko je ukupno trebalo vremena da zavrsi bacanje koplja
	(koliko je zajedno trajalo cekanje i bacanje koplja).
*/

#include <thread>
#include <iostream>
#include <map>
#include <mutex>
#include <condition_variable>
#include <chrono>

using namespace std;
using namespace chrono;



struct povratna_vrednost {
	int duzina;
	int metrika;
	duration<double, milli> trajanje;
};

class AtletskaStaza {
	mutex m;
	bool slobodno;  // свободно ли упражнение
	condition_variable skakanje, bacanje; // очередь ожидания для прыжков и метаний
	int skakaca, bacaca; // количество прыжков и метаний в очереди


public:
	AtletskaStaza() { // конструктор 
		slobodno = true; // упражнение свободно
		skakaca = 0; // нет прыжков в очереди
		bacaca = 0; // нет метаний в очереди
	}

	povratna_vrednost skaci() {// функция прыжков
		steady_clock::time_point dosao = steady_clock::now(); // фиксируем время прихода
		unique_lock<mutex> l(m);

		++skakaca; // увеличиваем количество прыжков в очереди
		while (!slobodno) // если упражнение не свободно, ждем свободного упражнения
			skakanje.wait(l);

		skakaca--; // уменьшаем количество прыжков в очереди, так как выходим из while и прыгаем
		slobodno = false; // занимаем упражнение

		l.unlock();
		this_thread::sleep_for(seconds(2)); // прыжок занимает 2 секунды
		
		steady_clock::time_point zavrsio = steady_clock::now(); // фиксируем время окончания прыжка
		l.lock();
		slobodno = true; // освобождаем упражнение

		// проверяем, есть ли метания в очереди. Если есть, уведомляем их, что они могут метать
		if (bacaca > 0) 
			bacanje.notify_one();
		else skakanje.notify_one(); // иначе уведомляем следующего прыгуна, что он может прыгать
		
		// формируем и возвращаем результат
		povratna_vrednost pv;
		pv.metrika = rand() % 10;
		pv.trajanje = zavrsio - dosao;
		return pv;
	}
	povratna_vrednost baciKoplje() {
		steady_clock::time_point dosao = steady_clock::now();
		unique_lock<mutex> l(m);
		++bacaca; // увеличиваем количество метаний в очереди

		while (!slobodno)
			bacanje.wait(l);
		bacaca--; // уменьшаем количество метаний в очереди, так как выходим из while и метаем
		slobodno = 0;

		l.unlock();
		this_thread::sleep_for(seconds(1)); // метание занимает 1 секунды
		steady_clock::time_point zavrsio = steady_clock::now();
		l.lock();
		slobodno = 1;

		if(skakaca>0)
			skakanje.notify_one();
		else bacanje.notify_one();

		// формируем и возвращаем результат
		povratna_vrednost pv;
		pv.metrika = rand() % 100;
		pv.trajanje = zavrsio - dosao;
		return pv;


	}
};

void skakac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.skaci();
	cout << "Takmicar sa brojem " << rbr << " skocio " << rez.duzina << " metara."
		<< ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

void bacac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.baciKoplje();
	cout << "Takmicar sa brojem " << rbr << " bacio koplje " << rez.duzina << " metara."
		<< ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}


const int br_sk = 5;
const int br_bk = 5;
int main() {
	AtletskaStaza st;
	thread skakaci[br_sk];
	thread bacaci[br_bk];

	for (int i = 0; i < 5; ++i) {
		skakaci[i] = thread(skakac, ref(st), i + 1);
		bacaci[i] = thread(bacac, ref(st), i + 1);

	}

	for (int i = 0; i < 5; i++) {
		skakaci[i].join();
	}
	for (int i = 0; i < 5; i++) {
		bacaci[i].join();
	}

}
