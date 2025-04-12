//Para compilar gcc -Iheaders/ -shared -o libconversion.so -fPIC conversion.c
#include "conversion.h"
#include <stdio.h>
#include "cdecl.h"

void PRE_CDECL suma_uno(int, int * ) POST_CDECL;

int main(void){
    float num = 3.5;
    convert_and_increment(num);
    return 0;
}

int convert_and_increment(float value) {
    int ivalue = (int)value;    // truncamiento hacia cero
    printf("%d\n", ivalue);
            suma_uno(value, &ivalue);
            printf("%d\n", ivalue);
    return ivalue;  
}
