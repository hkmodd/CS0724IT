#include <stdio.h>

int main() {
    int num1, num2;
    printf("Inserisci due numeri: ");
    scanf("%d %d", &num1, &num2);
    printf("Il risultato della media è: %.2f\n", (num1 + num2) / 2.0);
    return 0;
}