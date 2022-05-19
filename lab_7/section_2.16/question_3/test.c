
/*
Name: Bethany Hampton
Class: SENG2220
Assignment Lab 7 - Section 2.16 - Question 3

Details: Echoing a user input string by using a read and write method.
*/
#include <unistd.h.>

//outputs to the user
//pointint to the correct value within the varaible
int writeStr(char *stringAddr) {
	int count = 0;
	while (*stringAddr != '\0') {
		write(STDOUT_FILENO, stringAddr, 1);
		count++;
		stringAddr++;
	}
	return count;
}

//reading line with standard input
int readLn(char *stringAddr, int maxLength) {
	int count = 0;
	maxLength--;
	read(STDIN_FILENO, stringAddr, 1);
       // reading until new line is made
	while (*stringAddr != '\n') {
		if (count < maxLength) {
			count++;
			stringAddr++;
		}
		read(STDIN_FILENO, stringAddr, 1);
	}
	*stringAddr = '\0';
	return count;
}
//main loop to output results
int main(void) {
	char aString[200];
	writeStr("Enter a text string: ");
	readLn(aString, 200);
	writeStr("You entered: ");
	writeStr(aString);
	writeStr("\n");
	return 0;
}
