/* Data je klasa Message_box koja predstavlja sanduce za poruke bilo kojeg tipa.
 * Message_box sadrzi dve metode:
 * 1. send(const MESSAGE* message) - za ubacivanje poruke u sanduce i
 * 2. receive() - za preuzimanje poruke iz sanduceta
 *
 * Date su niti proizvodjac i potrosac. Nit proizvodjac ubacuje tri poruke u
 * sanduce, a nit potrosac ih preuzima i ispisuje.
 *
 * Prepraviti klasu tako da bude implementirana u skladu sa sledecim pravilima:
 *  - Nit proizvodjac ne sme da upise novu poruku, dok nit potrosac ne preuzme
 *    prethodno upisan polozaj.
 *  - Nit potrosac ne sme da preuzme polozaj kursora pre nego sto ga nit
 *    proizvodjac upise.
 *  - Nit potrosac ne sme dva puta da preuzme isti polozaj kursora.
 * (Alternativno, koriscenjem stanja:
 *      Nit proizvodjac ne sme da pise u punu deljenu promenljivu.
 *      Nit potrosac ne sme da cita iz prazne deljene promenljive.)
 *
 * Ako program ispravno radi, sve tri poruke trebaju biti preuzete i ispisane,
 * tako da ispis bude:
 *
 *     2
 *     9
 *     7
 */
#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

using namespace std;

template<class MESSAGE> //класс шаблон. Может принимать любой тип для одного из своих полей. 
class Message_box {
    mutex m;
	enum Message_box_states { EMPTY, FULL }; // состояния ящика.
	Message_box_states state; // текущее состояние ящика.
	condition_variable full; // условная переменная, которая используется для синхронизации при заполнении ящика.
    condition_variable empty; // условная переменная, которая используется для синхронизации при опустошении ящика.
    MESSAGE content;
public:
	Message_box() : state(EMPTY) {}; // в начале ящик пуст.
    void send(const MESSAGE* message);
    MESSAGE receive();
};

template<class MESSAGE>
void Message_box<MESSAGE>::send(const MESSAGE* message)
{
	unique_lock<mutex> lock(m);
    while (state == FULL)
        empty.wait(lock);// Пока состояние ящика FULL (полный) ничего не может быть отправлено, т.е. сначала он должен быть опустошен.
    content = *message;
	state = FULL; // состояние теперь полное (FULL).
	full.notify_one(); // уведомляются потоки, которые ждали заполнения ящика (потребители).
}

template<class MESSAGE>
MESSAGE Message_box<MESSAGE>::receive()
{
	unique_lock<mutex> lock(m);
    while (state == EMPTY)
		full.wait(lock); // Пока состояние ящика EMPTY (пустой) ничего не может быть прочитано, т.е. сначала он должен быть заполнен.
	state = EMPTY; // состояние теперь пустое (EMPTY).
	empty.notify_one(); // уведомляются потоки, которые ждали опустошения ящика (производители).
    return content;
}

void proizvodjac(Message_box<int>& mb) {
    int a = 2;
    mb.send(&a);
    a = 9;
    mb.send(&a);
    a = 7;
    mb.send(&a);
}

void potrosac(Message_box<int>& mb) {
    cout << "Preuzeto: " << mb.receive() << endl;
    cout << "Preuzeto: " << mb.receive() << endl;
    cout << "Preuzeto: " << mb.receive() << endl;
}

int main() {
    Message_box<int> mb;

    thread t1(proizvodjac, ref(mb));
    thread t2(potrosac, ref(mb));

    t1.join();
    t2.join();

    return 0;
}
