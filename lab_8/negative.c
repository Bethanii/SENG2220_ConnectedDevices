/*
Name: Bethany Hampton
Class: SENG2220 (Computer Organization)
Assignment: In-Class Follow-Along
*/
#include <stdio.h>

//structured- cause symbols give it structure
//strictly typed

int main()
{
    // unisgned = no sign, cant have negative number 
    unsigned int x = 15;
    int y = -15;

    printf("Value of x: %d\n", x);
    printf("Hex value of X: %X\n", x);

    // this is putting this value into twos complement
    // 8 * 4 = 32 bits are being used to store this in memory
    printf("Value of Y: %d\n", y);
    printf("Hex value of Y: %X\n", y);

    // variable has two values- the value and where its stored in memory
    // the output of this can change because it is using random access meemory 
    // random = could be different the next time
    // virtual memory - the memory that an operating system gives you
    //pointer = means a system can access the variable's location
    printf("Location of X: %X\n", &x);

    return 0;
}