/*=======================================================
Your Name: Jagger Collins
Your Purdue Email: colli576@purdue.edu
Lab Section: In_Lab06
Lab Number: 6
Program Description: In this lab I will utilize if else statements and for loops to display a menu that a user can give multiple options to do computations.
==========================================================*/

// Pre-processor Directives 
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <conio.h>

// main function 
int main() {

    int choice = 0;
    int num;

    printf(" ******************************** \n");
    printf(" * In_Lab 06                    * \n");
    printf(" * By: Jagger Collins           * \n");
    printf(" * Email: colli576@purdue.edu   * \n");
    printf(" ******************************** \n");

    // Main loop for menu choices
    while (choice != 5) {
        printf("\t For Loops Lab \n");
        printf("\t============================  \n");
        printf("\t 1. Display and Add natural numbers from 1 to N \n");
        printf("\t 2. Multiplication table of N \n");
        printf("\t 3. Display an inverted triangle of stars \n");
        printf("\t 4. Display a triangle of numbers \n");
        printf("\t 5. Exit \n");

        printf("\t Enter your choice: ");
        scanf("%d", &choice);

        // Option 1
        if (choice == 1) {
            int summation = 0;
            printf("Enter a natural number for N: ");
            scanf("%d", &num);

            printf("Displaying natural numbers from 1 to %d:\n", num);
            for (int i = 1; i <= num; i++) {
                printf("%d\n", i);
                summation += i;
            }
            printf("The sum of the natural numbers from 1 to %d is %d\n", num, summation);
        }

        // Option 2
        else if (choice == 2) {
            printf("Enter a natural number for N:\n");
            scanf("%d", &num);

            printf("Displaying the multiplication table of %d:\n", num);
            for (int i = 1; i <= 10; i++) {
                printf("%d * %d = %d\n", num, i, num * i);
            }
        }

        // Option 3
        else if (choice == 3) {
            printf("Enter the amount of lines you want to display:\n");
            scanf("%d", &num);

            for (int i = num; i >= 1; i--) {
                for (int j = 1; j <= i; j++) {
                    printf("*");
                }
                printf("\n");
            }
        }

        // Option 4
        else if (choice == 4) {
            printf("Enter the amount of rows of numbers you want to display:\n");
            scanf("%d", &num);

            for (int i = 1; i <= num; i++) {
                for (int j = 1; j <= i; j++) {
                    printf("%d", j);
                }
                printf("\n");
            }
        }

        // Option 5
        else if (choice == 5) {
            printf("Goodbye!\n");
        }

        // Invalid input
        else {
            printf("Invalid input!\n");
            printf("Enter a number between 1-5.\n");
        }
    }

    _getch();
    return 0;
}