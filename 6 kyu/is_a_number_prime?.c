#include <stdbool.h>
#include <math.h>

// Square root optimization to find if num is prime

bool is_prime(int num) {
    if (num > 1) {
        for (int i = 2; i < (int)sqrt(num)+1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    return false;
}
