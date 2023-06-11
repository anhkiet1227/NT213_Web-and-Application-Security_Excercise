#include <iostream>

int target = 1835996258;

int check(int value1, int value2);

int check1(int value1, int value2) {
    int j = 1;
    int i = value1;
    value1 = j;
    while (value1 < 100) {
        i += value1;
        value1 += 1;
    }
    return check(i, value2);
}

int check2(int value1, int value2) {
    if (value2 % 2 == 0) {
        int j = 1;
        int i = value1;
        value1 = j;
        while (value1 < 1000) {
            i += value1;
            value1 += 1;
        }
        return check(i, value2);
    }
    int j = 1;
    int i = value1;
    value1 = j;
    while (value1 < 1000) {
        i -= value1;
        value1 += 1;
    }
    return check(i, value2);
}

int check3(int value1, int value2) {
    int j = 1;
    int i = value1;
    value1 = j;
    while (value1 < 10000) {
        i += value1;
        value1 += 1;
    }
    return check(i, value2);
}

int check(int value1, int value2) {
    if (value2 <= 1) {
        return value1;
    }
    if ((2 * value2) % 3 == 0) {
        return check1(value1, value2 - 1);
    }
    else if ((2 * value2) % 3 == 1) {
        return check2(value1, value2 - 1);
    }
    else {
        return check3(value1, value2 - 1);
    }
}

int main() {
    for (int i = 1; i < 1000000000; i++) {
        if (check(i, 99) == target) {
            std::cout << i << std::endl;
            std::cout << "Done" << std::endl;
            break;
        }
        else {
            std::cout << i << std::endl;
            continue;
        }
    }
    std::cout << "END OF PROGRAM" << std::endl;
    return 0;
}
