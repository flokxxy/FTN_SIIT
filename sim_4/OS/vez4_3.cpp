/* Napraviti konkurentni program sa tri niti.
 * Nit a ispisuje: "Ja sam nit a."
 * Nit b ispisuje: "Ja sam nit b."
 * Nit c ispisuje: "Ja sam nit c."
 * Obezbediti da se niti a i b, uvek izvrse pre niti c.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include<condition_variable>

using namespace std;

class koordinator {
	enum steps { prvi, drugi, treci };
	steps step;
	mutex m;
	condition_variable c;

public:
	koordinator() :step(prvi) {}
	void prvi_zavrsi() {
		unique_lock<mutex> lock(m);
		c.notify_one();
		step = drugi;
	}
	void drugi_zavrsi() {
		unique_lock<mutex> lock(m);
		c.notify_one();
		step = treci;
	}
	void treci_ceka() {
		unique_lock<mutex> lock(m);
		while(!(step == treci))
			c.wait(lock);
	}
};

koordinator k;

void a() {
	cout << "Ja sam nit a." << endl;
	k.prvi_zavrsi();
}
void b() {
	cout << "Ja sam nit b." << endl;
	k.drugi_zavrsi();
}
void c() {
	k.treci_ceka();
	cout << "Ja sam nit c." << endl;
}

int main() {
	thread ta(a);
	thread tb(b);
	thread tc(c);
	ta.join();
	tb.join();
	tc.join();
	return 0;
}
