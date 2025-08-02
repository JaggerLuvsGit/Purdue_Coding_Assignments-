/*=======================================================
Your Name:Jagger Collins
Your Purdue Email: colli576@purdue.edu
Lab Section: In_Lab05
Lab Number: 5
Program Description: In this lab I will utilize if else statements and while loops to display a menu that a user can give multiple options to manupulate a list of numbers. 
==========================================================*/

//Pre-processor Directives 
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<conio.h>
#include<math.h> 

//main function 
int main() {

    int choice = 0;
    int naturalN;
    int loop_count = 1;
    int loop_sum = 1;
    int loop_squared = 1;
    int loop_cubed = 1;
    int square_sum = 0;
    int cubed = 0;
    int summation = 0;
    int naturalN_sum;
    int naturalN_squared;
    int naturalN_average;



    printf(" ******************************** \n");
    printf(" * In_Lab 05                    * \n");
    printf(" * By: Jagger Collins           * \n");
    printf(" * Email: colli576@purdue.edu  * \n");
    printf(" ******************************** \n");

    while (choice != 5)
    {
        printf("\t While Loops Lab \n");
        printf("\t============================  \n");
        printf("\t 1. Print natural numbers from 1 to N \n");
        printf("\t 2. Add natural numbers from 1 to N \n");
        printf("\t 3. Compute the sum of the square of numbers from 1 to N  \n");
        printf("\t 4. Compute the sum and average of the cubes of numbers from 1 to N  \n");
        printf("\t 5. Exit \n");

        printf("\t Enter your choice:");
        scanf("%d", &choice);

        //=====================================================

        if (choice == 1) // choice 1, printing N values 
        {
            printf("Enter a natural number for N:\n");
            scanf("%d", &naturalN);
            printf("Displaying natural numbers from 1 to %d \n", naturalN);

            while (loop_count <= naturalN)
            {
                printf("%d \n", loop_count);
                loop_count++;
            }
        }

        //=====================================================

        if (choice == 2) // choice 2, printing and adding N values
        {
            printf("Enter a natural number for N: \n");
            scanf("%d", &naturalN);
            printf("Displaying natural numbers from 1 to %d \n", naturalN);

            while (loop_sum <= naturalN)
            {
                printf("%d \n", loop_sum);
                summation += loop_sum;
                loop_sum++;
            }

            printf("The sum of the numbers from 1 to %d is %d \n", naturalN, summation);
        }

        //================================================


        if (choice == 3) // choice 3, computing the sum of the squares of N values
        {
            printf("Enter a natural number for N: \n");
            scanf("%d", &naturalN);
            printf("Displaying the squares of numbers from 1 to %d \n", naturalN);

            while (loop_squared <= naturalN)
            {

                printf("%d \n", (loop_squared * loop_squared));
                square_sum += loop_squared * loop_squared;
                loop_squared++;
            }

            printf("The sum of the squares of numbers from 1 to %d is %d \n", naturalN, square_sum);
        }
        //=================================================


        if (choice == 4) // choice 4, computing the sum and average of the cubes of N values
        {
            printf("Enter a natural number for N: \n");
            scanf("%d", &naturalN);
            printf("Displaying the cubes of numbers from 1 to %d \n", naturalN);

            while (loop_cubed <= naturalN)
            {

                printf("%d \n", (loop_cubed * loop_cubed * loop_cubed));
                cubed += loop_cubed * loop_cubed * loop_cubed;
                loop_cubed++;
            }


            printf("The sum of the cubes of numbers from 1 to %d is %d \n", naturalN, cubed);
            printf("The average of the cubes of numbers from 1 to %d is %.2f \n", naturalN, (float)cubed / naturalN);

        }

        //====================================================================
        else if (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5) // Choice 6 for alternate response .
        {
            printf("Invalid input!\n");
            printf("Enter a number between 1-5.\n");
        }





        //====================================================================
        else if (choice == 5)    // Choice 5 to exit menu.
           printf("Goodbye!\n");
        

    }




 _getch();
 return 0;

 }