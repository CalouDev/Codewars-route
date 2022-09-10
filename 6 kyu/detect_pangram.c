#include <string.h>
#include <stdbool.h>

bool is_pangram(char *str_in) {
    bool isCharIn = false;

    for (int i = 0; i <= 25; i++) {
        for (unsigned long j = 0; j < strlen(str_in); j++) {
            if (((char)(i + 97) == str_in[j] || (char)(i + 65) == str_in[j]) && isCharIn == false)
                isCharIn = true;
        }

        if (!isCharIn)
            return false;

        isCharIn = false;
    }

    return true;
}
