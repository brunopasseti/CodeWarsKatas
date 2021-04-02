#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

typedef unsigned long long ull;
class SumFct {
   public:
	static ull perimeter(int n);
};

ull SumFct::perimeter(int n) {
	ull current = 1, last = 1, next = 0, sperimeter = 1;
	for (int i = 0; i < n; i++) {
		sperimeter += current;
		next = current + last;
		last = current;
		current = next;
	}
	sperimeter *= 4;
	return sperimeter;
}

void testequal(ull ans, ull sol) {
	assert(ans == sol);
}

void dotest(int n, ull expected) {
	testequal(SumFct::perimeter(n), expected);
}

void test() {
	dotest(5, 80);
	dotest(7, 216);
	dotest(20, 114624);
	dotest(30, 14098308);
}

int main() {
	test();
	return 0;
}