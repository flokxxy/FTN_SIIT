// Napraviti konkurentni program koji modeluje kreditno poslovanje banke.
// Banka odobrava kredite u dinarima i u evrima.

// Klijent trazi kredit pozivanjem operacije uzmi_kredit(), 
// kojoj prosledjuje svotu koju zeli da pozajmi od banke 
// i valutu u kojoj zeli da pozajmi.
// Klijent neko vreme koristi pozajmljena sredstva, pa ih vrati banci
// pozivanjem operacije vrati_kredit().

// Banka inicijalno poseduje odredjene svote dinara 
// i evra na dva razlicita racuna, koje pozajmljuje.
// Banka odobrava kredite dok ima sredstava. 
// Kada vise nema sredstava, banka ceka da klijenti vrate 
// pretodno odobrene kredite pre nego sto odobri sledeci kredit.
// Banka odobrava kredite u proizvoljnom redosledu.

// Banka tezi tome da klijent ciji je zahtev moguce ispunitini 
// (postoje sredstva) ne ceka na kredit.

// Komentari su obavezni


#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class banka {
    mutex m;
	int din_saldo, ev_saldo; //баланс динар и евро
    condition_variable din_likvidan, ev_likvidan;
public:
    enum valute { DINAR = 0, EVRO };
    
	banka(int inicijalni_dsaldo, int inicijalni_esaldo) :din_saldo(inicijalni_dsaldo), ev_saldo(inicijalni_esaldo) {}
    int uzmi_kredit(int svota, valute valuta);
    int vrati_kredit(int svota, valute valuta);
};



int banka::uzmi_kredit(int svota, valute valuta) {//функция взятия кредита
    int saldo; //balance

    unique_lock<mutex> l(m); //

    if (valuta == DINAR) {
        while (din_saldo < svota) // svota - сумма которую берут/отдают
        {//пока нет всего кол-ва динаров в банке, клиент ждет
            din_likvidan.wait(l);
        }
        din_saldo -= svota;// денег достаточно, списывается из банка
        saldo = din_saldo;//возвращает остаток средств банка
    }
    else {
        while (ev_saldo < svota) {
            ev_likvidan.wait(l);
        }
        ev_saldo -= svota;
        saldo = ev_saldo;
    }

    return saldo;
}

int banka::vrati_kredit(int svota, valute valuta) {
    int saldo;
    unique_lock<mutex> l(m);

    if (valuta == DINAR) {
        din_saldo += svota;
        din_likvidan.notify_all();
        saldo = din_saldo;
    }
    else {
        ev_saldo += svota;
        ev_likvidan.notify_all();
        saldo = ev_saldo;
    }
    return saldo;
}

string naziv_valute(banka::valute valuta) {
    if (valuta == banka::DINAR)  return "dinar";
    else return "evro";
}

void klijent(banka& b, int svota, banka::valute valuta) {
    static mutex term_m;
    thread::id id = this_thread::get_id();
    int saldo;
    {
        unique_lock<mutex> l(term_m);
        cout << "Klijent: " << id << " trazi na zajam " << svota
            << ", valuta: " << naziv_valute(valuta) << endl;
    }
    saldo = b.uzmi_kredit(svota, valuta);
    {
        unique_lock<mutex> l(term_m);
        cout << "Klijent: " << id << " dobio " << svota
            << ", u banci ostalo: " << saldo
            << ", valuta: " << naziv_valute(valuta) << endl;
    }
    // klijent koristi pozajmljeni novac
    this_thread::sleep_for(chrono::seconds(1));
    saldo = b.vrati_kredit(svota, valuta);
    unique_lock<mutex> l(term_m);
    cout << "Klijent: " << id << " vratio " << svota
        << ", u banci ostalo: " << saldo
        << ", valuta: " << naziv_valute(valuta) << endl;
}

int main() {
   int svota_din = 20;
   int svota_ev = 30;
   const int klienti = 10;

   banka b{ svota_din,svota_ev };
   thread t[klienti];

   for (int i = 0; i < klienti; i++) {
       t[i] = thread(klijent, ref(b), 1 + i * 3 % (svota_din < svota_ev ? svota_din : svota_ev), (banka::valute)(i % 2));
   }
   for (int i = 0; i < klienti; i++) {
       t[i].join();
   }
}

