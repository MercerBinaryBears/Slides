#include<stdio.h>

int main(void) {
    // we're going to keep doubling this number and print it as we go
    int N = 1;

    int i;

    for(i = 0; i < 50; i++) {
        // double the number
        N *= 2;

        // print i and our number out (using printf)
        printf("i = %d", i);
        printf(" N  = %d\n", N);
    }
}
