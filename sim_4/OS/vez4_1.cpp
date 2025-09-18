/* 1
Napraviti konkurentni program sa dve niti.
 * Nit a ispisuje: "Ja sam nit a."
 * Nit b ispisuje: "Ja sam nit b."
 * Obezbediti da se uvek izvrsi prvo nit a.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class kordinator {
	enum red{prvi,drugi};
	red na_redu_je;
	mutex m;
	condition_variable c; //позволяет усыпить поток до определенного сигнала

public:
	kordinator(): na_redu_je(prvi){}

	void prva_zavrsila() {
		unique_lock<mutex> lock(m);//"умный замок", берет управление захвата/освобождения мьютекса
		c.notify_one();//будит один ожидающий поток 
		na_redu_je = drugi; //переключение на второй поток
	}
	void driga_cheka() {
		unique_lock<mutex> lock(m);
		while (!(na_redu_je == drugi))
			c.wait(lock);
	}
	};

kordinator kord;

void niti1() {
	
	cout << "Ja sam nit a" << endl;
	kord.prva_zavrsila();
}
void niti2() {
	kord.driga_cheka();
	cout << "Ja sam nit b" << endl;
	
}


int main() {

	thread t1(niti1);
	thread t2(niti2);

	t1.join();
	t2.join();

	return 0;
}
