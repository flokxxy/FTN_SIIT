/*
 * 1
 * Napraviti konkurentni program koji sadrzi main funkciju i 2 niti. Obe niti
 * pristupaju istoj celobrojnoj promenljivoj brojac, koja inicijalno ima
 * vrednost 0.
 * Prva nit 1000000 puta uvecava vrednost brojaca.
 * Druga nit isti broj puta smanjuje vrednost brojaca.
 *
 * Ukoliko je program ispravno napisan, na kraju programa vrednost brojaca mora
 * biti 0.
 * 
 * 2
 * Napraviti konkurentni program sa 2 niti koje imaju isto telo niti. Svaka nit
 * najpre trazi od korisnika da unese svoju visinu. Nakon unosa, nit ispisuje
 * unetu vrednost na terminal.
 *
 * Sinhronizovati pristup terminalu kao deljenom resursu. Kada jedna nit stupi u
 * interakciju sa korisnikom, ne sme biti prekinuta dok se ne zavrsi kompletna
 * interakcija (i unos i ispis).
 * 
 * 3
 * Napraviti konkurentni program koji modeluje klasu brojača.
 * Interfejs klase sadrži sledeće metode:
 *
 * class brojac {
 * public:
 *     void inc();
 *     void dec();
 *     friend ostream& operator<<(ostream& , brojac& );
 * };
 *
 * Metode inc i dec povećavaju, odnosno smanjuju vrednost brojača za 1. Operator
 * << služi za ispis brojača na ekran. Klasa mora biti thread-safe (da garantuje
 * ispravan rad i ako se objektu klase pristupa iz razlicitih niti).
 *
 * Kreirati jednu instancu date klase kojoj pristupaju 2 niti.
 *
 * Jedna nit poziva metodu uvećavanja brojača 1000000 puta, a druga metodu
 * smanjivanja brojača 1000000 puta.
 *
 * Na kraju programa ispisati konačnu vrednost brojača.
 * 
 * 4
*/

#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

using namespace std;


class brojac {
	int broj = 0; // vrednost brojaca
	mutex m;      // propusnica pripada klasi i obezbedjuje sprecavanje stetnog preplitanja pri vrsenju operacija nad objektima klase
public:
	brojac() : broj(0) {} // inicijalno je brojac nula
	void inc() {
		unique_lock<mutex> l(m);
		++broj;
	}
	void dec() {
		unique_lock<mutex> l(m);
		--broj;
	}
	friend ostream& operator<<(ostream& os, brojac&b) {
		unique_lock<mutex> l(b.m);
		os << b.broj << endl;
		return os;
	}
	
};

brojac br; // da bi obe niti menjale isti brojac, on je definisan kao globalna promenljiva
const int iter = 1000000;
int brojac1 = 0;
mutex m; // globalna propusnica za sprecavanje stetnog preplitanja pri pristupu brojacu
//глобальный проход для предотвращения вредоносного запутывания при доступе к счетчику


void povecaj() {
	for (int i = 0; i <iter; ++i) {
		m.lock(); // zakljuca se propusnica pre pristupa deljenoj promenljivoj
		//проход блокируется перед доступом к общей переменной
		++brojac1;
		m.unlock();
	}
}
void smanji() {
	for (int i = 0; i < iter; ++i) {
		m.lock(); // zakljuca se propusnica pre pristupa deljenoj promenljivoj
		--brojac1;
		m.unlock();
	}
}

void visina() {
	int v;
	m.lock();
	cout << "Unesite visinu: ";
	cin >> v;
	cout << "Uneta visina je: " << v << endl;
	m.unlock();
}

void inkrement() {
	// specificirani broj puta se zatrazi povecavanje brojaca.
	// Pozivalac ne vodi racuna o stetnom preplitanju, to je odgovornost klase
	for (int i = 0; i < iter; ++i)
		br.inc();
}
void dekrement() {
	for (int i = 0; i < iter; ++i) // specificirani broj puta se zatrazi smanjivanje brojaca
		br.dec();
}


int main() {
	
	//1
	thread t1(povecaj);
	thread t2(smanji);
	t1.join();
	t2.join();
	//cout << brojac << endl;


	//2
	thread t3(visina);
	thread t4(visina);
	t3.join();
	t4.join();

	//3
	thread t5(inkrement);
	thread t6(dekrement);
	t5.join();
	t6.join();
	cout << br << endl;


	


	return 0;
}
