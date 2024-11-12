#include <stdio.h>

int somma(int a, int b){
    int c = 0;
    c = a + b;
    return c;
}

int main(){
    printf("\nSomma: %d", somma(3, 4));
    return 0;
}