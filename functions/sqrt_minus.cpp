#include "math.h"
#include <iostream>
using namespace std;

double sqrt_minus(double x) {
    if (x < 1) {
        return -11111111;
    }
    return sqrt(x) - sqrt(x - 1);
}

int main() {
    double in[10];
    for(int i = 0; i < 10; i++) {
        in[i] = i * 0.1;
        cout << in[i] << endl;
    }

    cout << sqrt_minus(10);

}