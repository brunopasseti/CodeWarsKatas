#include <algorithm>
#include <string>
#include <iostream>

bool is_isogram(std::string str) {
  std::transform(str.begin(), str.end(), str.begin(), ::tolower);
  int *counterArray = new int[26];
  for(const char& l: str){
    counterArray[l-'a']++;
  }
  for(int i = 0; i < 26; i++){
    if(counterArray[i] > 1){
      return false;
    }
  }
  return true;
}

int main(){
  std::string str;
  while(1){
    std::cin >> str;
    std::cout << (is_isogram(str) ? "True" : "False") << std::endl;
  }
  return 0;
}