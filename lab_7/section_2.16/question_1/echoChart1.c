/*
Name: Bethany Hampton
Class: SENG2220
Assignment: lab 7 - Section 2.16

Details: Promts user for input and echos this character back.
*/

#include <unistd.h>
#include <string.h>

int main(void)
{
  // intializing variables
  // creating one to be an array
  // stringPtr will point to characters
  char aString[200];
  char *stringPtr = aString;

  //stdout = program to user
  //stdout_fileno = prompting user for input
  write(STDOUT_FILENO, "Enter a text string: ",
        strlen("Enter a text string: "));

  // stdin = user to program
  // getting the first character of user input
  read(STDIN_FILENO, stringPtr, 1);

  // while loop to continue until the end of user input line
  while (*stringPtr != '\n')
  {
    // moving to the next value
    stringPtr++;
    // now reading this value
    read(STDIN_FILENO, stringPtr, 1);
  }

  // echoing to user
  write(STDOUT_FILENO, "You entered:\n",
        strlen("You entered:\n"));
  stringPtr = aString;

 // final loop to echo back complete string to user
 // also runs until reaching the end of the user input
 do
  {
    write(STDOUT_FILENO, stringPtr, 1);
    stringPtr++;
  } while (*stringPtr != '\n');
  write(STDOUT_FILENO, stringPtr, 1);

  return 0;
}
