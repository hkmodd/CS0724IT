#include <stdio.h>
#include <stdlib.h>

void run_classic_mode();
void run_broken_mode();

int main() {
    int choice;

    printf("Benvenuto! Scegli una modalit\u00e0:\n");
    printf("1: Modalit\u00e0 classica\n");
    printf("2: Modalit\u00e0 rotta (simula segmentation fault)\n");
    printf("Inserisci la tua scelta (1 o 2): ");

    if (scanf("%d", &choice) != 1 || (choice != 1 && choice != 2)) {
        printf("Errore: Selezione non valida. Inserire 1 o 2.\n");
        return 1;
    }

    if (choice == 1) {
        run_classic_mode();
    } else if (choice == 2) {
        run_broken_mode();
    }

    return 0;
}

void run_classic_mode() {
    int vector[10], i, j, k;
    int swap_var;

    printf("Inserire 10 numeri interi:\n");

    for (i = 0; i < 10; i++) {
        printf("[%d]: ", i + 1);
        scanf("%d", &vector[i]);
    }

    printf("\nIl vettore inserito \u00e8:\n");
    for (i = 0; i < 10; i++) {
        printf("[%d]: %d\n", i + 1, vector[i]);
    }

    for (j = 0; j < 10 - 1; j++) {
        for (k = 0; k < 10 - j - 1; k++) {
            if (vector[k] > vector[k + 1]) {
                swap_var = vector[k];
                vector[k] = vector[k + 1];
                vector[k + 1] = swap_var;
            }
        }
    }

    printf("\nIl vettore ordinato \u00e8:\n");
    for (i = 0; i < 10; i++) {
        printf("[%d]: %d\n", i + 1, vector[i]);
    }
}

void run_broken_mode() {
    int vector[10], i;
    int *ptr = NULL; // Puntatore nullo

    printf("Inserire 10 numeri interi:\n");

    for (i = 0; i < 10; i++) {
        printf("[%d]: ", i + 1);
        scanf("%d", &vector[i]);
    }

    printf("\nIl vettore inserito \u00e8:\n");
    for (i = 0; i < 10; i++) {
        printf("[%d]: %d\n", i + 1, vector[i]);
    }

    printf("\nErrore...\n");

    // Generazione intenzionale del segmentation fault
    printf("Valore in *ptr: %d\n", *ptr);
}
