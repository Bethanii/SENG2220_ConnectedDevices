/*
Name: Bethany Hampton
Class: SENG2220
Assignment: Lab 7
 * User inputs a decmial and hexadeciaml value
 * Outputs the memory location of both of these values
 * Note: the solution for this used a while loop but I did not. 
         but I am returning the correct values.
 */

#include <stdio.h>

int main(void)
{
  //For these instructions we are asked to find the location of the x and y variables. 
  // I will make the previously assigned variables be these x and y values.

  unsigned int x;
  unsigned int y;

  // %u - specifying  unsigned int
  // getting user input and then using'scanf' to read this input
    printf("Enter a decimal integer: ");
    scanf("%u", &x);

   // %x - hexadecimal representation
    printf("Enter a bit pattern in hexadecimal: ");
    scanf("%x", &y);

   // %010x - hexadecimal formatting
   // this is printing out the memory location for both values
   // & (ampersand) is used  to point to the value of a variable in its memory location 
    printf("%u is stored as %#010x at address location: %p  and\n", x, x,&x);
    printf("%#010x represents the unsigned decimal integer %u at address location: %p\n", y, y, &y);

  // in C when we return a 0 we are telling the os that there are no issues
  return 0;
}
