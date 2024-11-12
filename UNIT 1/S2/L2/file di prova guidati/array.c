#include <stdio.h>

int main(){
    int numeri[3];
    numeri[0]=1;
    numeri[1]=4;
    numeri[2]=89;
    printf("0x%x = %d\n", &numeri[2], numeri[2]);
    int anum[] = {1,4,3,57,6,3};
    printf("0x%x = %d\n", &anum[3], anum[3]);
    return 0;
}