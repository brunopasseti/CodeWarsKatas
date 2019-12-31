#include <vector>
#include <cassert>
#include <iostream>
#include <algorithm>

int square_sum(const std::vector<int>& numbers)
{
	int acc = 0;
  std::for_each(numbers.begin(), numbers.end(), [&acc](int element)
	{
			acc += (element*element);
			return;
	});
	return acc;
}

void test(){
	assert((square_sum({1, 2})) == 5);
	assert((square_sum({1, 2, 2})) == 9);
	assert(square_sum({0, 3, 4, 5}) == 50);
}

int main(){
	test();
	return 0;
}