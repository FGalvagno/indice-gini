#include "conversion.h"

int converted_and_increment(float value) {
    int ivalue = (int)value;    // truncamiento hacia cero
    return ivalue + 1;
}