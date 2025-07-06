#include <cppunit/ui/text/TestRunner.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
/*
int main() {
    CppUnit::TextUi::TestRunner runner;
    runner.addTest(CppUnit::TestFactoryRegistry::getRegistry().makeTest());
    return runner.run() ? 0 : 1;
}
 */

//#include "GameTest.h"    // включает реализацию тестов прямо в раннер

int main() {
    CppUnit::TextUi::TestRunner runner;
    // Подхватывает все тестовые фикстуры, которые попали в этот исполняемый файл
    runner.addTest( CppUnit::TestFactoryRegistry::getRegistry().makeTest() );
    return runner.run("", false) ? 0 : 1;
}
