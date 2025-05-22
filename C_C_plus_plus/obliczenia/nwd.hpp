#include <iostream>

int nwd(int a, int b){
    if (b == 0) return a;
    return nwd(b , a % b);
}
