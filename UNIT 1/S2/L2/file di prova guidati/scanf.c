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

    risultato = primo + secondo;

    printf("\nLa somma %d + %d = %d\n", primo, secondo, risultato);
    printf("\nLa somma %d - %d = %d\n", primo, secondo, primo - secondo);
    printf("\nLa somma %d * %d = %d\n", primo, secondo, primo * secondo);
    printf("\nLa somma %d / %d = %d\n", primo, secondo, primo / secondo);
    printf("\nLa somma %d / %d ha resto %d\n", primo, secondo, primo % secondo);

    return 0;
}