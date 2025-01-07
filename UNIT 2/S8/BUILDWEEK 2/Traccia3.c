#include <stdio.h>
#include <stdlib.h>

int main() {
    int vector[10], i, j, k;
    int swap_var;
    int scelta;

    printf("Seleziona un'opzione:\n");
    printf("1. Esegui il programma corretto\n");
    printf("2. Esegui il programma con errore (buffer overflow)\n");
    printf("Scelta: ");
    if (scanf("%d", &scelta) != 1 || (scelta != 1 && scelta != 2)) {
        printf("Errore: Selezione non valida. Inserire 1 o 2.\n");
        return 1;
    }

    if (scelta == 1) {
        // Programma corretto
        printf("Hai selezionato il programma corretto.\n");
        printf("Inserire 10 numeri interi:\n");
        for (i = 0; i < 10; i++) {
            printf("[%d]: ", i + 1);
            if (scanf("%d", &vector[i]) != 1) {
                printf("Errore: Inserire un numero intero valido.\n");
                return 1;
            }
        }

        printf("\nIl vettore inserito è:\n");
        for (i = 0; i < 10; i++) {
            printf("[%d]: %d\n", i + 1, vector[i]);
        }

        // Ordinamento Bubble Sort
        for (j = 0; j < 10 - 1; j++) {
            for (k = 0; k < 10 - j - 1; k++) {
                if (vector[k] > vector[k + 1]) {
                    swap_var = vector[k];
                    vector[k] = vector[k + 1];
                    vector[k + 1] = swap_var;
                }
            }
        }

        printf("\nIl vettore ordinato è:\n");
        for (i = 0; i < 10; i++) {
            printf("[%d]: %d\n", i + 1, vector[i]);
        }

    } else if (scelta == 2) {
        // Programma con errore
        printf("Hai selezionato il programma con errore (buffer overflow).\n");
        printf("Inserire 15 numeri interi:\n");

        for (i = 0; i < 15; i++) { // Accede oltre i limiti di vector[10]
            if (i >= 10) {
                printf("\n[!] ERRORE CRITICO: BUFFER OVERFLOW RILEVATO! (Scrittura oltre i limiti)\n");
            }

            // Forza un vero errore di segmentazione
            printf("[%d]: ", i + 1);
            scanf("%d", &vector[i]); // Scrittura oltre i limiti di vector[10]
        }

        printf("Questo messaggio non dovrebbe mai apparire!\n");
    }

    return 0;
}
