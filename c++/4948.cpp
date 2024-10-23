#include <iostream>
#include <cmath>
#include <vector>

bool is_prime(int n){
    if (n == 0 || n == 1){
        return false;
    }

    for (int i = 2; i < static_cast<int>(std::sqrt(n)) + 1; i ++){
        if (n%i == 0){
            return false;
        }
    }
    return true;
}

int main(void){
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    
    int n;
    std::cin >> n;
    int ans = 0;
    
    while(n != 0){
        ans = 0;
        for (n; n < (2*n) + 1; n++){
            if(is_prime(n)){
                ans ++;
            }
        }
        std::cout << n;
        std::cin >> n;
    }
    
    
    return 0;
}