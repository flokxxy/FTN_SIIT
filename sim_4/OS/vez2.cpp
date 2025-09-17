/*
* 1
 * Sabrati korespodentne elemente vektora a i b, a zbirove smestiti na
 * odgovarajuce pozicije vektora c. Obezbediti da svako sabiranje obavlja
 * posebna nit.
 * 
 * 2
 * Napraviti konkurentni program koji pita korisnika koliko niti da stvori, a
 * zatim stvara zadati broj niti. Pri instanciranju nit dobija redni broj pod
 * kojim je stvorena. Svaka nit ispisuje svoj redni broj i svoj identifikator.
 * 
 * 3
 * Napraviti konkurentni program koji stvara jednu nit. Nit ima 2 parametra.
 * Jedan je referenca na ulaznu listu a drugi referenca na izlaznu. Nit treba da
 * elemente ulazne liste prebaci u izlaznu tako da stoje u obrnutom redosledu.
 * Ispisati izgled izlazne liste nakon rada niti.
 * 
 * 4
 * Napraviti konkurentni program koji pronalazi element najblizi 0 iz zadatog
 * niza brojeva. Posao podeliti tako da ga izvrsavaju 3 niti. Duzina niza
 * brojeva treba da je deljiva sa 3.
 * 
 * 5
 * Napraviti konkurentni program koji pravi srpsko engleski recnik iz englesko
 * srpskog recnika. Recnik ima proizvoljan broj reci (bitno je da bude vise od
 * jedne). Posao treba obaviti u jednoj niti. Ispisati englesko srpski i srpsko
 * engleski recnik na kraju programa.
 *
 * Napomena: ispis prevedenih reci ne mora biti u redosledu unesenih reci
 * prilikom formiranja recnika, ali prevod mora biti tacan.
 * 
 * 6
 * Napraviti konkurentni program za ispis identifikatora niti sa odredjenim
 * rednim brojem. Na pocetku programa potrebno je pitati korisnika da unese
 * redni broj niti. Program pokrece 10 niti. Svaka nit pri izvrsavanju ispisuje
 * "Pozdrav iz niti X", pri cemu je X redni broj niti. Main funkcija treba da
 * ispise identifikator niti ciji je redni broj korisnik uneo.
 * 
 * 7
 * Napraviti program za evidenciju identifikatora niti. U programu definisati
 * STL kontejner sa 5 elemenata (isto toliko ce biti i niti). Elementi
 * kontejnera su objekti koji predstavljaju identifikatore niti. Svaka nit treba
 * u dati STL kontejner da upise svoj identifikator i to u odgovarajuci element.
 *
 * Dakle, prva nit upisuje svoj identifikator u prvi element vektora, druga nit
 * u drugi element i tako redom. Kada se sve niti zavrse, potrebno je ispisati
 * identifikatore uskladistene u STL kontejneru.
 * 
 * //8 json
 * Napraviti konkurentni program koji simulira serijalizaciju objekata u JSON
 * format pri slanju podataka sa veb servera na klijent. JSON objekti se sastoje
 * od parova <kljuc,vrednost>.
 *
 * U main funkciji, koriscenjem odgovarajuceg STL kontejnera, definisati JSON
 * objekat Korisnik koji ima sledece parove:
 *
 *     <id,1>
 *     <ime,Marko>
 *     <prezime,Markovic>
 *     <email,marko.markovic@gmail.com>
 *
 * Zatim napraviti posebnu nit koja ispisuje sadrzaj JSON objekta u JSON
 * formatu.
 *
 * Ispis u JSON formatu izgleda ovako:
 *
 *     {"email":"marko.markovic@gmail.com","id":"1","ime":"Marko","prezime":"Markovic"}
 *
 * Pri ispisu nije vazan redosled parova.
 * 
 * //9 krug
 * Napisati program koji proverava koje se od zadatih tacaka nalaze u/na 
 * kruznici, a koje su van kruznice.
 * Tacke se nalaze u vektoru points:
 * 
 * struct Point { double x, y; };
 * vector<Point> points;
 * 
 * Definisati klasu:
 * 
 * class Circle {
 *   ...
 * public:
 *   Circle(const Point& t, const double r_);
 *   void check(const vector<Point> p, vector<bool>& belong);
 * };
 * 
 * Objekt tipa Circle, za svaku tacku iz vektora, izracunava da li se ona nalazi:
 *     - u krugu (ili na kruznici)
 *         + korespodentni element vektora belong dobija vrednost true ili
 *     - van kruga
 *         + korespodentni element vektora belong dobija vrednost false.
 * 
 * Stvoriti nit koja poziva funkciju check nad objektom klase Circle.
 * 
 * 10 logovanje
 * Napraviti konkurentni program za simulaciju logovanja na udaljeni racunar.
 *
 * Da bi se logovao, u glavnom programu korisnik redom treba da unese:
 *
 *     login <enter>
 *     <korisnicko_ime> <enter>
 *     <lozinka> <enter>
 *
 * Nakon toga posebna nit treba da utvrdi da li korisnik moze da se uloguje.
 *
 * Provera ispravnosti logovanja vrsi se na osnovu evidencije korisnika. U
 * glavnom programu, koriscenjem STL kontejnera, evidentirati sledece korisnike:
 *
 *     1. korisnicko_ime: milan, lozinka: 12345
 *     2. korisnicko_ime: marko, lozinka: xyz
 *     3. korisnicko_ime: admin, lozinka: 4dm1n
 *
 * Nit treba da utvrdi da li je najpre unesena rec "login". Ako jeste, korisnik
 * se moze ulogovati ako postoji evidentiran korisnik sa unesenim  korisnickim
 * imenom i lozinkom.
 *
 * Ako je logovanje uspesno, nit ispisuje:
 *
 *     Korisnik uspesno prijavljen.
 *
 * U slucaju neuspesnog logovanja, nit ispisuje:
 *
 *     Neuspesna prijava!
 * 
 * //11 evidencija studenata
 * Napraviti konkurentni program koji radi formiranje evidencije studenata.
 * Studentska sluzba (glavni program) salje 2 kontejnera niti koja formira
 * evidenciju. Prvi kontejner sadrzi indekse studenata, dok drugi kontejner
 * sadrzi ime i prezime studenta (kao jedan element kontejnera). Podrazumeva se
 * da indeks na i-toj poziciji prvog kontejnera odgovara imenu i prezimenu na
 * i-toj poziciji drugog kontejnera.
 *
 * Zadatak niti je da formira novi kontejner koji sadrzi parove
 * <kljuc, vrednost> uz pomoc prethodno opisanih kontenjera brojeva indeksa
 * (kljuc) i imena sa prezimenima (vrednost).
 *
 * Nakon zavrsetka rada niti u glavnom programu ispisati sadrzaj novoformiranog
 * kontejnera sa parovima <kljuc, vrednost>.
 *
 * Ispis bi trebao da izgleda ovako:
 *
 *     Indeks: RA 111/2012 Ime i prezime: Petar Petrovic
 *     Indeks: RA 222/2012 Ime i prezime: Stefan Stefanovic
 *     Indeks: RA 333/2012 Ime i prezime: Milica Micic
 *
 * U programu postoji samo jedna nit koja kreira evidenciju studenata.
 * 
 * //12
 * Napisati konkurentni program koji koristi STL kontejner <map>. U main-u
 * inicijalizovati mapu tako da sadrzi 10 elemenata pri cemu je kljuc broj od
 * 1-10 a vrednost id niti main.
 * 
 * Kreirati 10 niti klasom thread. Svakoj niti se prosleduje njen redni broj
 * prilikom stvaranja i referenca na mapu. Svaka nit u mapi treba upise svoj id
 * na element kojem je kljuc redni broj date niti (1-10).
 * 
 * Na kraju programa iz mape ispisati id-eve niti u obrnutom redosledu rednog
 * broja niti.
*/

#include <iostream>
#include <vector>
#include <map>
#include <thread>

using namespace std;



struct Point { double x, y; };
class Circle {
	Point center;
	double radius;
public:
	Circle(const Point& t, const double r_) : center(t), radius(r_) {}
	void check(const vector<Point> p, vector<bool>& belong) {
		for (size_t i = 0; i < p.size(); ++i) {
			double dist = sqrt((p[i].x - center.x) * (p[i].x - center.x) + (p[i].y - center.y) * (p[i].y - center.y));
			if (dist <= radius) {
				belong[i] = true;
			}
			else {
				belong[i] = false;
			}
		}
	}

};

void konkurentno_logovanje(const map<string, string>& korisnici, const string& komanda, const string& korisnicko_ime, const string& lozinka) {
	if (komanda != "login") {
		cout << "Neuspesna prijava!" << endl;
		return;
	}
	auto it = korisnici.find(korisnicko_ime);
	if (it != korisnici.end() && it->second == lozinka) {
		cout << "Korisnik uspesno prijavljen." << endl;
	}
	else {
		cout << "Neuspesna prijava!" << endl;
	}
}



int main() {

	//1
	/*
	vector<int> a = {1, 2, 3, 4, 5};
	vector<int> b = {10, 20, 30, 40, 50};
	vector<int> c(a.size());
	vector<thread> threads;
	for (size_t i = 0; i < a.size(); ++i) {
		threads.emplace_back([&, i]() {
			c[i] = a[i] + b[i];
		});
	}
	for (auto& t : threads) {
		t.join();
	}
	cout << "Result vector c: ";
	for (const auto& val : c) {
		cout << val << " ";
	}
	cout << endl;*/

	//2
	/*int broj_niti;
	cout << "Unesite broj niti: ";
	cin >> broj_niti;
	vector<thread> threads;
	for (int i = 0; i < broj_niti; ++i) {
		threads.emplace_back([i]() {
			cout << "Nit rednog broja: " << i << ", ID: " << this_thread::get_id() << endl;
		});
	}
	for (auto& t : threads) {
		t.join();
	}*/

	//3
	/*vector<int> ulazna_lista = {1, 2, 3, 4, 5};
	vector<int> izlazna_lista;
	thread t([&ulazna_lista, &izlazna_lista]() {
		for (auto it = ulazna_lista.rbegin(); it != ulazna_lista.rend(); ++it) {
			izlazna_lista.push_back(*it);
		}
		});
	t.join();
	cout << "Izlazna lista u obrnutom redosledu: ";
	for (const auto& val : izlazna_lista) {
		cout << val << " ";
	}
	cout << endl;
	*/

	//4
	/*vector<double> niz = {3.5, -1.2, 0.4, -0.6, 2.1, -0.3, -0.1};
	double najblizi_nuli = niz[0];
	size_t velicina = niz.size();
	auto pronadji_najblizi = [&](size_t start, size_t end) {
		double lokalni_najblizi = niz[start];
		for (size_t i = start; i < end; ++i) {
			if (abs(niz[i]) < abs(lokalni_najblizi)) {
				lokalni_najblizi = niz[i];
			}
		}
		if (abs(lokalni_najblizi) < abs(najblizi_nuli)) {
			najblizi_nuli = lokalni_najblizi;
		}
		};
	thread t1(pronadji_najblizi, 0, velicina / 3);
	thread t2(pronadji_najblizi, velicina / 3, 2 * velicina / 3);
	thread t3(pronadji_najblizi, 2 * velicina / 3, velicina);
	t1.join();
	t2.join();
	t3.join();	
	cout << "Element najblizi nuli je: " << najblizi_nuli << endl;*/

	//5
	/*setlocale(LC_ALL, "rus");

	map<string, string> englesko_srpski = {
		{"hello", "zdravo"},
		{"world", "svet"},
		{"computer", "racunar"},
		{"programming", "programiranje"}
	};
	map<string, string> englesko_rus = {
		{"hello", "привет"},
		{"world", "мир"},
		{"computer", "компьютер"},
		{"programming", "прграммирование"}
	};
	map<string, string> rus_engleski;
	map<string, string> srpsko_engleski;
	thread t([&englesko_srpski, &srpsko_engleski]() {
		for (const auto& par : englesko_srpski) {
			srpsko_engleski[par.second] = par.first;
		}
		});
	t.join();

	thread t2([&englesko_rus, &rus_engleski]() {
		for (const auto& par : englesko_rus) {
			rus_engleski[par.second] = par.first;
		}
		});
	t2.join();

	cout << "Englesko-Srpski recnik:" << endl;
	for (const auto& par : englesko_srpski) {
		cout << par.first << " -> " << par.second << endl;
	}
	cout << endl;
	cout << "Srpsko-Engleski recnik:" << endl;
	for (const auto& par : srpsko_engleski) {
		cout << par.first << " -> " << par.second << endl;
	}
	cout << endl;
	cout << "Englesko-Ruski recnik:" << endl;
	for(const auto& par : englesko_rus) {
		cout << par.first << " -> " << par.second << endl;
	}
	cout << endl;
	cout << "Rusko-Engleski recnik:" << endl;
	for (const auto& par : rus_engleski) {
		cout << par.first << " -> " << par.second << endl;
	}*/


	//6
	/*int redni_broj;
	cout << "Unesite redni broj niti (0-9): ";
	cin >> redni_broj;
	vector<thread> threads;
	for (int i = 0; i < 10; ++i) {
		threads.emplace_back([i]() {
			cout << "Pozdrav iz niti " << i << endl;
		});
	}
	for (auto& t : threads) {
		t.join();
	}
	cout << "ID niti sa rednim brojem " << redni_broj << " je: " << threads[redni_broj].get_id() << endl;*/

	//7
    /*
	vector<thread::id> ids(5);
	vector<thread> threads;
	for (int i = 0; i < 5; ++i) {
		threads.emplace_back(identifikatori_niti, ref(ids), i);
	}
	for (auto& t : threads) {
		t.join();
	}
	cout << "Identifikatori niti:" << endl;
	for (const auto& id : ids) {
		cout << id << endl;
	}
	*/

	//8
    /*
	map<string, string> korisnik = {
		{"id", "1"},
		{"ime", "Marko"},
		{"prezime", "Markovic"},
		{"email", "marko.markovic@gmail.com"}
	};
	thread t([&korisnik]() {
		cout << "{";
		bool prvo = true;
		for (const auto& par : korisnik) {
			if (!prvo) {
				cout << ",";
			}
			cout << "\"" << par.first << "\":\"" << par.second << "\"";
			prvo = false;
		}
		cout << "}" << endl;
		});
	t.join();*/

	//9
    /*
	vector<Point> points = { {1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}, {7.0, 8.0} };
	vector<bool> belong(points.size());
	Circle circle({ 4.0, 4.0 }, 3.0);
	thread t2([&circle, &points, &belong]() {
		circle.check(points, belong);
		});
	t2.join();
	cout << "Centar kruga: (4.0, 4.0), poluprecnik: 3.0" << endl;
	cout << "Tacke i njihova pripadnost krugu:" << endl;
	for (size_t i = 0; i < points.size(); ++i) {
		cout << "Tacka (" << points[i].x << ", " << points[i].y << ") je ";
		if (belong[i]) {
			cout << "u krugu ili na kruznici." << endl;
		}
		else {
			cout << "van kruga." << endl;
		}
	}
	*/

	//10 logovanje
	/*
	map<string, string> korisnici = {
	{"milan", "12345"},
	{"marko", "xyz"},
	{"admin", "4dm1n"}
	};
	string komanda, korisnicko_ime, lozinka;
	cout << "Unesite komandu: ";
	cin >> komanda;
	cout << "Unesite korisnicko ime: ";
	cin >> korisnicko_ime;
	cout << "Unesite lozinku: ";
	cin >> lozinka;
	thread t3(konkurentno_logovanje, ref(korisnici), komanda, korisnicko_ime, lozinka);
	t3.join();
	*/

	//11 evidencija studenata
	vector<string> indeksi = {"RA 111/2012", "RA 222/2012", "RA 333/2012"};
	vector<string> imena_prezimena = { "Petar Petrovic", "Stefan Stefanovic", "Milica Micic" };
	map<string, string> evidencija;
	thread t4([&indeksi, &imena_prezimena, &evidencija]() {
		for (size_t i = 0; i < indeksi.size(); ++i) {
			evidencija[indeksi[i]] = imena_prezimena[i];
		}
		});
	t4.join();
	cout << "Evidencija studenata:" << endl;
	for (const auto& par : evidencija) {
		cout << "Indeks: " << par.first << " Ime i prezime: " << par.second << endl;
	}

	//12
	/*
	map<int, thread::id> mapa;
	vector<thread> threads;
	for (int i = 1; i <= 10; ++i) {
		threads.emplace_back([i, &mapa]() {
			mapa[i] = this_thread::get_id();
			});
	}
	for (auto& t : threads) {
		t.join();
	}
	cout << "ID-evi niti u obrnutom redosledu:" << endl;
	for (int i = 10; i >= 1; --i) {
		cout << "Nit " << i << ": " << mapa[i] << endl;
	}*/

	

	return 0;
}
