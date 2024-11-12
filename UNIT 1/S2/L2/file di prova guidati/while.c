#include <stdio.h>

int main()
{
    int n = 5;
    int fattoriale = 1;

    while (n > 0) {  // Ciclo while per calcolare il fattoriale di n
        fattoriale = fattoriale * n;
        n--;
    }

    printf("\nFattoriale = %d\n", fattoriale);

    char carattere = 'a';

    while (carattere != 'V' && carattere != 'v') {  // Ciclo while che continua finché l'utente non inserisce 'V' o 'v'
        printf("\nPremi V: ");
        scanf(" %c", &carattere);

        if (carattere != 'V' && carattere != 'v') {
            printf("\nHo detto V!!!");
        }
    }

    return 0;
}