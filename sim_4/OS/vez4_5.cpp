/* Naparviti klasu mb (message_box) koja sadrzi n komunikacionih kanala. (n se
 * odredjuje u trenutku instanciranja objekta klase). Komunikacioni kanal
 * (sanduce) omogucava komunikaciju izmedju proizvodjaca i potrosaca nazavisnu
 * od ostalih komunikacija. Svaki kanal moze da sadrzi neogranicen broj poruka.
 *
 * mb ima dve operacije.
 * 1. mb::send() je neblokirajuca operacija sa dva parametra:
 *  - vrednosti (objekt) koja se salje i
 *  - indeksom kanala u koji se salje.
 *
 * 2. mb::receive() je blokirajuca operacija koja prihvata indeks kanala iz
 *  kojeg ocekuje poruku, a vraca objekt poruke.
 *
 * Jednu poruku je moguce preuzeti samo jednom (pri preuzimanju, poruka se i
 * izbacuje iz sanduceta). Ako u kanalu nema poruke, nit koja je pozvala
 * receive() ceka poruku. Niti koje pozovu receive moraju da dobiju poruke iz
 * odgovarajuceg kanala, ali ne moraju da dobiju poruke u redosledu u kojem su
 * one (poruke) poslate.
 *
 * Operacije send() i receive() bacaju izuzetak ako im se prosledi kanal koji ne
 * postoji.
 *
 * Operacije ove klase su thread safe.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>
#include <queue>
#include <condition_variable>
#include <stdexcept>
using namespace std;


template<typename T, int N>
class mb {
    vector<queue<T>> data_;
	vector<condition_variable*> cv_; //вектор для указателей на условные переменные
    mutex m_;
public:
    mb();
    ~mb();
    void send(T data, int channel);
    T receive(int channel);
};

template<typename T, int N> //консруктор класса 
mb<T, N>::mb() { // функция конструктора
    for (int i = 0; i < N; ++i) {// за каждый из N каналов сделать следующее:
        data_.push_back(queue<T>{}); // в соответствующий элемент вектора каналов вставить новую пустую очередь. Данная очередь должна
		// в будущем принимать сообщения, которые будут отправляться и приниматься.
		cv_.push_back(new condition_variable); // в соответствующий элемент вектора условных переменных поместить УКАЗАТЕЛЬ на
		// новосозданную условную переменную (операция new). Другими словами условные переменные создаются динамически на хипе, а в вектор
		// помещаются только УКАЗАТЕЛИ на них. Это сделано потому что условные переменные не могут
		// передаваться (копироваться) в вектор по значению. ЗАПРЕЩЕНО копирование условных переменных (оператор delete в классе) и мьютексов.
    }
}
template<typename T, int N>
mb<T, N>::~mb() { // функция деструктора
    for (int i = 0; i < N; ++i) { // за каждый из N каналов сделать следующее:
        data_.pop_back(); // из вектора каналов удалить очередь сообщений. Эффективно этим удаляются все сообщения в данном
        // канале. Затем удаляются все условные переменные на которые УКАЗЫВАЮТ указатели, 
        delete cv_.back(); // которые находятся в векторе cv_ (оператор delete). И в конце удаляются сами указатели
    }                    // из вектора cv_ с помощью векторной операции pop_back.
}

template<typename T, int N>
void mb<T, N>::send(T data, int channel) { // Функция отправки сообщения. Передается сообщение и канал.
    if (channel >= data_.size()) // Если канал больше чем количество каналов, выбрасывается (throw) ошибка.
        throw out_of_range("Invalid channel index.");

    unique_lock<mutex> l{ m_ }; // Вход в критическую секцию.
    data_[channel].push(data); // Помести сообщение в соответствующий канал
    cv_[channel]->notify_one(); // Разбуди потребителя соответствующего канала (если он есть).
}

template<typename T, int N>
T mb<T, N>::receive(int channel) { // Функция приема сообщения. Передается канал из которого желает принять сообщение.
    if (channel >= data_.size()) // Если канал больше чем количество каналов, выбрасывается (throw) ошибка.
        throw out_of_range("Invalid channel index.");
    unique_lock<mutex> l{ m_ }; // Вход в критическую секцию.
    while (data_[channel].empty()) { // Пока нет сообщения в канале -> жди
        cv_[channel]->wait(l);
    }
    T t = data_[channel].front(); // Сообщение пришло. Прими сообщение с вершины очереди в соответствующем канале (операция front).
    data_[channel].pop();         // После принятия удали сообщение с вершины очереди.
    return t;
}

mb<char, 3> mb3; //создание глобального объекта multi message boxa. Tip poruke je char, ima 3 kanala.

//proizvodjac salje tri uzastopna karaktera pocevsi od prosledjenog karaktera c
void producer(char c, int channel) {
    this_thread::sleep_for(chrono::seconds(1));
    mb3.send(c, channel);
    this_thread::sleep_for(chrono::seconds(1));
    mb3.send(c + 1, channel);
    this_thread::sleep_for(chrono::seconds(1));
    mb3.send(c + 2, channel);
}

void consumer(int channel) {
    static mutex mx;
    //   this_thread::sleep_for(chrono::seconds(1));
    char c = mb3.receive(channel);
    unique_lock<mutex> l(mx);
    cout << "[" << channel << "]= " << c << endl;
}

const int PROD = 3;
const int CONS = 9;

int main() {
    thread prod[PROD];
    thread cons[CONS];

    //posto svaki proizvodjac posalje tri uzastopna karaktera
    //pocevsi od prosledjenog, znaci da pri ispisu preuzeti karakteri
    //treba da budu (u proizvoljnom redosledu):
    //a,b,c, g,h,i, m,n,o
    char poruke[] = { 'a', 'g', 'm' };

    for (int i = 0; i < PROD; ++i)
        prod[i] = thread(producer, poruke[i], i % 3);
    for (int i = 0; i < CONS; ++i)
        cons[i] = thread(consumer, i % 3);
    for (int i = 0; i < PROD; ++i)
        prod[i].join();
    for (int i = 0; i < CONS; ++i)
        cons[i].join();

    return 0;
}
