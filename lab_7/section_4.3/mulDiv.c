/*
Name: Bethany Hampton
Class: SENG2220
Assignemnt: lab 7 - Section 4.3

Details: Getting user input in the form of an integer.
         Then prompting user to enter a power of 2 to multiply
         the integer by. Then the same is done for division.
 */

#include <stdio.h>

int main(void)
{
  int x;
  int leftShift, rightShift;

  // prompting user
  // saving value as signed decimal
  printf("Enter an integer: ");
  scanf("%d", &x);

  // prompting to get power of 2
  printf("Multiply by two raised to the power: ");
  scanf("%d", &leftShift);
  // shifting to the left to multiply by the value stored in x
  // will at least multiply by 1
  printf("%d x %d = %d\n", x, 1 << leftShift, x << leftShift);

  // prmopting to get two power to divide by
  printf("Divide by two raised to the power: ");
  scanf("%d", &rightShift);
  // outputing this value by shifting a to the right to divide
  printf("%d / %d = %d\n", x, 1 << rightShift, x >> rightShift);

  return 0;
}
