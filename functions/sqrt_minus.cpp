#include "math.h"

double sqrt_minus(double x) {
    if (x < 1) {
        return -11111111;
    }
    return sqrt(x) - sqrt(x - 1);
}

int main() {
    sqrt_minus(10);
}