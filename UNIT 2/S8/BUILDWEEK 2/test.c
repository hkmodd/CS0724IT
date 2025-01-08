#include <stdio.h>
#include <stdlib.h>

void correct_version() {
    int vector[10], i, j, k;
    int swap_var;

    printf("Inserire fino a 10 interi (altri input verranno ignorati):\n");
    for (i = 0; i < 10; i++) {
        printf("[%d]: ", i + 1);
        if (scanf("%d", &vector[i]) != 1) {
            printf("Errore di input. Inserisci solo numeri interi.\n");
            return;
        }
    }

    printf("Il vettore inserito e':\n");
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

    printf("Il vettore ordinato e':\n");
    for (j = 0; j < 10; j++) {
        printf("[%d]: %d\n", j + 1, vector[j]);
    }
}

void vulnerable_version() {
    int vector[10];
    int i;

    printf("Inserire più di 10 interi. Il programma si romperà dopo il decimo input extra:\n");

    for (i = 0; i < 20; i++) { // Permettiamo fino a 20 input per simulare un BOF
        if (i < 10) {
            // Scriviamo normalmente nei limiti dell'array
            printf("[%d]: ", i + 1);
            scanf("%d", &vector[i]);
        } else {
            // Iniziamo a scrivere oltre i limiti
            printf("Stai scrivendo oltre i limiti! [%d]: ", i + 1);
            int *invalid_ptr = (int *)(vector + i); // Puntatore fuori dai limiti
            scanf("%d", invalid_ptr); // Scriviamo in memoria non valida
            if (i > 15) {
                // Provoca segmentation fault dopo pochi input fuori dai limiti
                int *crash_ptr = (int *)(vector + 1000);
                *crash_ptr = 12345; // Forziamo il segmentation fault
            }
        }
    }

    printf("Il programma non avrebbe mai dovuto arrivare qui.\n");
}

int main() {
    int choice;

    printf("Scegli quale versione eseguire:\n");
    printf("1. Versione corretta (con controlli di input)\n");
    printf("2. Versione vulnerabile (causa segmentation fault dopo il decimo numero extra)\n");
    printf("Scelta: ");
    if (scanf("%d", &choice) != 1) {
        printf("Errore di input. Riprova.\n");
        return 1;
    }

    switch (choice) {
        case 1:
            correct_version();
            break;
        case 2:
            vulnerable_version();
            break;
        default:
            printf("Scelta non valida.\n");
    }

    return 0;
}
