
#include <cppunit/ui/text/TestRunner.h>
#include "GameTest.h"
int main() {
    CppUnit::TextUi::TestRunner runner;
    // Явно добавляем тестовый набор из GameTest
    runner.addTest(GameTest::suite());
    bool ok = runner.run("", false);
    return ok ? 0 : 1;
}
