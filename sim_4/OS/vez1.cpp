/* 1
   Napraviti program koji kreira jednu nit i u okviru nje ispisuje proizvoljnu
 * recenicu.
 * 
 * 2
 * Napraviti program koji kreira jednu nit kojoj se prosledjuju dva cela broja
 * a i b. U okviru niti sabrati brojeve i ispisati njihov zbir
 * 
 * 3
 * Napisati konkurentni program koji stvara jednu nit.
 * Nit od glavnog programa kao parametar dobija ceo broj i ima zadatak da uveca
 * vrednost broja za 1.
 *
 * Ispisati vrednost broja nakon zavrsetka rada niti
 * 
 * 4
 *  Napraviti konkurentni program koji kreira 5 niti od kojih svaka izvrsava isti
 * kod (svaka nit ima isto telo niti).
 * Svaka nit dobija svoj redni broj prilikom kreiranja.
 * U telu niti svaka nit treba da ispise svoj redni broj.
 * 
 * 5
 * Napraviti sekvencijalni program koji izračunava sumu svih elemenata vektora
 * sekvencijalno, koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 * 
 * 6
 * Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na 2 dela tako da prvu polovinu vektora sumira prva
 * nit, a drugu polovinu druga nit.
 *
 * Napomena: ovakva optimizacija sumiranja je znacajna kada se radi na
 * dvojezgarnom procesoru za vektore velike duzine.
 * 
 * 7
 * Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na N delova tako svaka nit sabira duzina vektora/broj
 * niti elemenata vektora.
 * 
 * 8
 * Napraviti konkurentni program  (koristeći funkciju f()) koji sabira
 * korespodentne elemente kontejnera  a i b, a rezultat smešta u vektor zbir.
 *
 * Dato je telo niti:
 *
 * void f(ci a_begin, ci a_end, ci b_begin, vector<double>::iterator sum_begin);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Program optimizovati za procesor sa 2 jezgra.
 *
 * Napomene: Podrazumeva se da su kontejneri a i b iste dužine.
 */

 
#include <iostream>
#include <thread>
#include <vector>
using namespace std;

typedef vector<double>::const_iterator ci;


void niti1() {
	// Funkcija koja ce biti izvrsena u okviru niti
	cout << "niit pisite" << endl;
}
void niti2(int a, int b) {
	// Funkcija koja ce biti izvrsena u okviru niti
	cout << "Zbir brojeva " << a << "+" << b << " = " << a + b << endl;
}
void niti3(int& c) {
	c++;
}

void niti4(int id) {
	cout << "Nit sa rednim brojem: " << id << " je pokrenuta." << endl;
}

void f1(ci begin, ci end, double& zbir) {// Racuna sumu elemenata vektora u opsegu [begin, end)
	zbir = 0;
	for (auto it = begin; it != end; ++it) {
		zbir += *it;
	}
}

void f2(ci begin, ci end, double& zbir) {// Racuna sumu elemenata vektora u opsegu [begin, end) koristeci 2 niti
	thread t(f1, begin, end, ref(zbir));
	t.join();
}
void f3(ci begin, ci end, double& zbir) {// Racuna sumu elemenata vektora u opsegu [begin, end) koristeci N niti
	zbir = 0;
	for (auto it = begin; it != end; ++it) {
		zbir += *it;
	}
}
void f(ci a_begin, ci a_end, ci b_begin, vector<double>::iterator sum_begin) {
    // Sabira korespodentne(соответствующие) elemente vektora a i b i smesta rezultat u vektor sum
    for (auto it = sum_begin; a_begin != a_end; ++a_begin, ++b_begin, ++it) {
        *it = *a_begin + *b_begin;
    }
}


int main() {
	//1
	// Kreiranje niti
	//thread t1(niti1);// Prosledjivanje funkcije niti kao argumenta
	//t1.join();// Cekanje da se nit zavrsi

	//2
	//int a, b;
	//cin >> a >> b;
	//thread t2(niti2, a, b);
	//t2.join();

	//3
	//int c;
	//cin >> c;
	//thread t3(niti3, ref(c));
	//t3.join();
	//cout << "Vrednost broja nakon zavrsetka niti je: " << c << endl;

	//4
	//const int n = 5;// Broj niti
	//thread niti[n];
	//for (int i = 0; i < n; i++) {
	//	niti[i] = thread(niti4, i + 1);
	//}
	//for (int i = 0; i < n; i++) {
	//	niti[i].join();
	//}

	//5
	//vector<double> v;
	//int m;
	//cout << "Unesite broj elemenata vektora: ";
	//std::cin >> m;
	//v.resize(m);
	//cout << "Unesite elemente vektora: ";
	//for (int i = 0; i < m; i++) {
	//	cin >> v[i];
	//}
		
	//double zbir; 
	//f1(v.begin(), v.end(), zbir);
	//cout << "Suma elemenata vektora je: " << zbir << endl;


	//6
	/*vector<double> v;
	int num_elements;
	cout << "Unesite broj elemenata vektora: ";
	std::cin >> num_elements;
	v.resize(num_elements);
	cout << "Unesite elemente vektora: ";
	for (int i = 0; i < num_elements; i++) {
		cin >> v[i];
	}
	double zbir1, zbir2;
	thread t1(f2, v.begin(), v.begin() + v.size() / 2, ref(zbir1));
	thread t2(f2, v.begin() + v.size() / 2, v.end(), ref(zbir2));
	t1.join();
	t2.join();
	cout << "Suma elemenata vektora je: " << zbir1 + zbir2 << endl;
	*/

	//7
	/*vector<double> v;
	int num_elements;
	int broj_niti;
	cout << "Unesite broj elemenata vektora: ";
	std::cin >> num_elements;
	v.resize(num_elements);
	cout << "Unesite elemente vektora: ";
	for (int i = 0; i < num_elements; i++) {
		cin >> v[i];
	}
	cout << "Unesite broj niti: ";
	cin >> broj_niti;

	vector<double> zbir(broj_niti);
	vector<thread> niti(broj_niti);
	int chunk_size = v.size() / broj_niti;
	for (int i = 0; i < broj_niti; i++) {
		ci begin = v.begin() + i * chunk_size;
		ci end = (i == broj_niti - 1) ? v.end()
			: begin + chunk_size;
		niti[i] = thread(f3, begin, end, ref(zbir[i]));
	}
	for (int i = 0; i < broj_niti; i++) {
		niti[i].join();
	}
	double total_sum = 0;
	for (const auto& part_sum : zbir) {
		total_sum += part_sum;
	}
	cout << "Suma elemenata vektora je: " << total_sum << endl;
	*/

	//8
	vector<double> a, b;
	int num_elements;
	cout << "Unesite broj elemenata vektora: ";
	std::cin >> num_elements;
	a.resize(num_elements);
	b.resize(num_elements);
	cout << "Unesite elemente prvog vektora: ";
	for (int i = 0; i < num_elements; i++) {
		cin >> a[i];
	}
	cout << "Unesite elemente drugog vektora: ";
	for (int i = 0; i < num_elements; i++) {
		cin >> b[i];
	}
	vector<double> zbir(num_elements);
	thread t1(f, a.begin(), a.begin() + a.size() / 2,
		b.begin(), zbir.begin());
	thread t2(f, a.begin() + a.size() / 2, a.end(),
		b.begin() + b.size() / 2, zbir.begin() + zbir.size()
		/ 2);
	t1.join();
	t2.join();
	cout << "Zbir korespodentnih elemenata vektora je: ";
	for (const auto& elem : zbir) {
		cout << elem << " ";
	}
	cout << endl;




		



	return 0;
}
