/*=======================================================
Your Name: Jagger Collins
Your Purdue Email: colli576@purdue.edu
Lab Section: In_Lab07
Lab Number: 7
Program Description: In this lab I will utilize functions to help build a right triangle by modeling my code from the starter code provided. 
==========================================================*/

// Pre-processor Directives 
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <conio.h>
#include <math.h>


// function 1 for printing box of stars
void displayMyInfo() {
    printf(" ******************************** \n");
    printf(" * In_Lab 07                    * \n");
    printf(" * By: Jagger Collins           * \n");
    printf(" * Email: colli576@purdue.edu   * \n");
    printf(" ******************************** \n");
}

// function 2 Maxmimum function 
float maximum(float a, float b, float c) {
    if (a >= b && a >= c)
        return a;
    else if (b >= a && b >= c)
        return b;
    return c;
}

// function 3 minimum function 
float minimum(float a, float b, float c) {
    if (a <= b && a <= c)
        return a;
    else if (b <= a && b <= c)
        return b;
    return c;
}

// function 4 triangle validation

int validate(float a , float b , float c) {
    if ((a + b > c) && (a + c > b) && (b + c > a)) {
        return 1;
    }
    return 0;

    }


// function 5 computing the area

float computeArea(float a, float b , float c) {
    float s;
    s = (a + b + c) / 2;

    float area;
    area = sqrt(s * (s - a) * (s - b) * (s - c));
    return area;
    
}

// function 6 PYTHAGOREAN 

int pythagorean(float a, float b, float c) {
    float hyp = maximum(a, b, c);
    float min = minimum(a, b, c);
    float mid;

    if ((a != hyp) && (a != min)) {
        mid = a;
    }
    else if ((b != hyp) && (b != min)) {
        mid = b;
    }
    else {
        mid = c;
    }

    float lhs = hyp * hyp;
    float rhs = mid * mid + min * min;

    if ((int)(lhs + 0.5) == (int)(rhs + 0.5)) {
        return 1;
    }
    else {
        return 0;
    }
}


// main function 
int main() {

    float sideA;
    float sideB;
    float sideC;
    int valid;
    int right_angle;
    float area;
    int choice;

    /// calling the box of stars function 
    displayMyInfo();
    // while loop to get sides for triangle  PRE VALIDATION
    while (1) {
        printf("Enter the length of side A of a triangle:\n");
        scanf("%f", &sideA);
        if (sideA == -1) break;
        printf("Enter the length of side B of a triangle:\n");
        scanf("%f", &sideB);
        if (sideB == -1) break;
        printf("Enter the length of side C of a triangle:\n");
        scanf("%f", &sideC);
        if (sideC == -1) break;

        // validation stages 
        printf("Validating the triangle...\n");
        valid = validate(sideA, sideB, sideC);

        if (!valid) {
            printf("Inputs do not form a triangle. Please enter diferent numbers.\n");
            continue;
        }


        // area computation stage 
        area = computeArea(sideA, sideB, sideC);
        printf("This is a valid triangle.\n");
        printf("The area of the triangle is %.2f \n", area);

        printf("Checking if this is a right triangle....\n");
        right_angle = pythagorean(sideA, sideB, sideC);

        if (right_angle) {
            printf("This is a right triangle. \n");

            // trig computations 
            float min = minimum(sideA, sideB, sideC);
            float hyp = maximum(sideA, sideB, sideC);
            float sine = min / hyp;
            float cos = sqrt(1 - sine * sine);
            float tan = sine / cos;

            printf("The sine of the smallest angle is %.2f\n", sine);
            printf("The cosine of the smallest angle is %.2f\n", cos);
            printf("The tangent of the smallest angle is %.2f\n", tan);
        }
        else {
            printf("This is not a right triangle.\n");
        }

        printf("\n");
    }





    printf("Goodbye!\n");


    _getch();
    return 0;
}


