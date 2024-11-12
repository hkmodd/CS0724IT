#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;

    printf("\nInserisci numero: ");
    scanf("%d", &primo);

    printf("\nInserisci secondo numero: ");
    scanf("%d", &secondo);

    // Somma
    risultato = primo + secondo;
    printf("\nLa somma %d + %d = %d\n", primo, secondo, risultato);

    // Differenza
    risultato = primo - secondo;
    printf("\nLa differenza %d - %d = %d\n", primo, secondo, risultato);

    // Prodotto
    risultato = primo * secondo;
    printf("\nIl prodotto %d * %d = %d\n", primo, secondo, risultato);

    // Divisione e Resto
    if (secondo != 0) {
        risultato = primo / secondo;
        printf("\nLa divisione %d / %d = %d\n", primo, secondo, risultato);

        risultato = primo % secondo;
        printf("\nIl resto della divisione %d %% %d = %d\n", primo, secondo, risultato);
    } else {
        printf("\nNon è possibile dividere per zero!\n");
    }

    return 0;
}