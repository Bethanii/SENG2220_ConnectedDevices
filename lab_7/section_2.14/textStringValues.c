/*
Name: Bethany Hampton
Class: SENG2220
Assignment: Lab 7 - Section 2.14

Details: Gets the memory address where the characters in
a text string are located and also displays the corresponding
hexadecmial value.
*/

#include <stdio.h>

int main(void)
{
  // Setting a pointer variable to access characters
  char *stringPtr = "Hello from Dunwoody :) \n";

  printf("Address  Contents\n");
 // While loop to print out the hex value
 //  and memory location of the above string
 // placing the dereferencing operator (*) to point to the memory location
  while (*stringPtr != '\0')
  {
    // %p is to point to this memory location value
    printf("%p:  ", stringPtr);
    // below is formatting the coresponding hex value
    printf("0x%02x\n", *stringPtr);
    stringPtr++;
  }
  printf("%p:  ", stringPtr);
  printf("0x%02x\n", *stringPtr);

 // 0 = telling the os that there is no issue
  return 0;
}
