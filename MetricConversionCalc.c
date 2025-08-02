/*=======================================================
Programmer: Jagger Collins
Email: colli576@purdue.edu
CNIT 105, Assignment 02
Program Description: In this assignment I will utilize my skills in C and show the printf() function and scanf() function by converting integers into other metric types. 
Academic Honesty:
I attest that this is my original work.
I have not used unauthorized source code, either modified or unmodified.
I have not given other fellow student(s) access to my program.
==========================================================*/



//Pre-processor Directives 
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<conio.h>
#include<math.h>

//main function 
int main() {
	float pounds;
	float temp_celsius;
	float kilo;
	float temp_fahrenheit;
	float distance_miles;
	float distance_meters;
	float distance_yards;
	float distance_kilo;
	float centimeters;
	int height_feet;
	int height_inch;
	

	printf(" ********************************* \n");
	printf(" * Assignment 1                  * \n");
	printf(" * By: Jagger Collins            * \n");
	printf(" * Email: colli576@purdue.edu    * \n");
	printf(" ********************************* \n");


	printf("Conversion Calculator \n");
	printf(" ================================= \n");
	// pound to kilo conversion 
	printf("Converting weight: pounds to kilograms. \n");
	printf("Enter the weight in pounds: \n ");
	scanf("%f", &pounds);
	kilo = (pounds * 0.45359237);
	printf("The weight entered is %.2f lbs and it is equivalent to %.2f kg.\n", pounds,kilo);

	// celsius to fahrenehit conversion 
	printf("Converting degrees: Celsius to Fahrenhit. \n");
	printf("Enter the temperature in Celsius: \n ");
	scanf("%f", &temp_celsius);
	temp_fahrenheit = (temp_celsius * 9 / 5) + 32;
	printf("The temperature entered is %.2f C and it is equivalent to %.1f F.\n", temp_celsius, temp_fahrenheit);

	// feet to inches  conversion
	printf("Converting height: height to centimeters. \n");
	printf("Enter the height in feet: \n");
	scanf("%d", &height_feet);
	printf("Now enter the inches: \n");
	scanf("%d", &height_inch);
	int total_inches = height_feet * 12 + height_inch;
	centimeters = total_inches * 2.54;
	printf("The height entered is %d feet %d inches and is equivalent to %.2f cm\n", height_feet, height_inch, centimeters);

	// mile to kilo converion 
	printf("Converting distance: miles to kilometers. \n");
	printf("Enter the distance in miles: \n");
	scanf("%f", &distance_miles);
	distance_kilo = (distance_miles * 1.60934);
	printf("The distance entered is %.1f miles and is equivalent to %.1f km.\n", distance_miles, distance_kilo);


	// yars to meter converion
	printf("Converting distance: yards to meters. \n");
	printf("Enter the distance in yards: \n");
	scanf("%f", &distance_yards);
	distance_meters = (distance_yards * 0.9144);
	printf("The distance entered is %.1f yards and is equivalent to %.2f meters.\n", distance_yards, distance_meters);



	_getch();
	return 0;
}
