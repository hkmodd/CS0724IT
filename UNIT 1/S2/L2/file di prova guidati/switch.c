#include <stdio.h>

int main()
{
    int scelta;  // Dichiariamo la variabile scelta
    
    printf("\nBuongiorno, qui il manicomio!\n1 Se sei schizofrenico\n2 Se sei paranoico\n3 Se hai bassa autostima\n");
    scanf("%d", &scelta);  // Aggiungi & per l’indirizzo e punto e virgola
    
    switch(scelta)
    {
        case 1:
            printf("\nVorremmo parlare con un'altra tua personalità");
            break;
        case 2:
            printf("\nTi avvisiamo che questa chiamata è condivisa con i poteri forti");
            break;
        case 3:
            printf("\nI nostri operatori stanno parlando con persone più importanti di te");
            break;
        default:
            printf("\nGrazie Arthur per averci contattato");
            break;
    }
    
    return 0;
}