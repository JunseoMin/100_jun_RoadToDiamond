#include <iostream>
#include <string>
#include <vector>

int is_group(const std::string& instr){
  if (instr.length() == 1)
  {
    return 1;
  }
  std::vector<char> cvec;
  cvec.push_back(instr[0]);

  for(const auto& c : instr){
    if(cvec.back() == c){
      continue;
    }

    
  }
}

int main(void){
    int N;
    std::cin >> N;
    std::string instr;
    int ans = 0;
    
    for(int i = 0; i < N; i++){
        instr.clear();
        ans += is_group(instr);
    }
    
    std::cout<<ans;
    return 0;
}