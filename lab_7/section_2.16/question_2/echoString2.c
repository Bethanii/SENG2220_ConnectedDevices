/*
Name: Bethany Hampton
Class: SENG2220
Assignment: Lab 7 - Section 2.16 - Question 2

Details: Exploring existing code that echos a string back to the user.
This input is then converted to a C-style string.
*/

#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
  char aString[200];
  char *stringPtr = aString;

  // prompting user
  write(STDOUT_FILENO, "Enter a text string: ",
        strlen("Enter a text string: "));

  // getting first character of input
  read(STDIN_FILENO, stringPtr, 1);

  // while loop that will read input until end of line
  while (*stringPtr != '\n')
  {
    // going to the next character
    stringPtr++;
    // reading this value
    read(STDIN_FILENO, stringPtr, 1);
  }
   //converting this input into a C string
  *stringPtr = '\0';

  // echoing back a C-string
  printf("You entered:\n%s\n", aString);

  return 0;
}
