/* Definisati klasu parking koja modeluje parking prostor kapaciteta N mesta.
 * Kapacitet parkinga proslediti kao argument konstruktoru, pri instanciranju
 * deljene promenljive.
 *
 * Klasa parking ima operacije:
 *
 *     void parking::udji();
 *     void parking::izadji();
 *
 * Automobili koji dolaze na parking su predstavljeni nitima. Za ulazak na
 * parking, automobil poziva metodu udji(). Za izlazak sa parkinga, automobil
 * poziva metodu izadji(). Automobil se na parkingu zadrzava 3 sekunde.
 *
 * Pri ulasku, ukoliko su sva parking mesta zauzeta, automobil mora da saceka da
 * se neko parking mesto oslobodi.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
using namespace std;

class parking {
	
	int broj_mesta;
	mutex evidencija;
	condition_variable kolona;


public:
	parking(int N) :broj_mesta(N) {};//конструктор
	void udji() {
		unique_lock<mutex>ev(evidencija);
		//uslov ulaska
		while (!broj_mesta) {
			kolona.wait(ev);
		}
		broj_mesta--;

	}
	void izadji() {
		unique_lock<mutex>ev(evidencija);
		broj_mesta++;
		ev.unlock();
		//теперь надо продолжить выполнение других потоков
		kolona.notify_one(); //оповещаем что место освободилось
		}
};

mutex m;
void automobil(parking& p) {
	p.udji();
	{
		unique_lock<mutex> l(m);
		cout << "Automobil " << this_thread::get_id() << " usao na parking." << endl;
	}
	this_thread::sleep_for(chrono::seconds(3));
	p.izadji();
	{
		unique_lock<mutex> l(m);
		cout << "Automobil " << this_thread::get_id() << " izasao sa parkinga." << endl;
	}
}

const int broj_auto = 7;

int main() {
	parking ispred_zgrade(5);
	thread automobili[broj_auto];

	for (thread& autic : automobili) {
		autic = thread(automobil, ref(ispred_zgrade));
	}

	for (thread& autic : automobili) {
		autic.join();
	}

	return 0;
}
