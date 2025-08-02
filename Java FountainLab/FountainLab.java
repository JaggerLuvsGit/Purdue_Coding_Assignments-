import java.text.NumberFormat;
import java.util.*;

public class FountainLab{
public static void main(String args[]) 

{
// Create a Scanner to read from user input
// TODO - ask for each of `radius`, `width1`, `width2`, `depth`. Remember to keep asking 
// if the value is out of range, and to tell the user that they've entered an invalid value.
Scanner in = new Scanner(System.in);

// Creating variables fo user input to be stored. 
double radius = 0.0;
double width1 = 0.0;
double width2 = 0.0;
double depth = 0.0; 

// input and validation while loop for radius to ensure correct info is entered.
while ( radius < 10.0 || radius > 15.0 ) {
    System.out.print("Enter a number between 10.0 and 15.0: ");
    radius = in.nextDouble();
    if ( radius < 10.0 || radius > 15.0 )
    {
        System.out.println("Invaid entry, Please enter a value between 10.0 and 15.0.");
    }
}

// input and validation while loop for width1 to ensure correct info is entered.
while ( width1 < 2.0 || width1 > 8.0 ) {
    System.out.print("Enter a number between 2.0 and 8.0: ");
    width1 = in.nextDouble();
    if ( width1 < 2.0 || width1 > 8.0 )
    {
        System.out.println("Invaid entry, Please enter a value between 2.0 and 8.0.");
    }
}

// input and validation while loop for width2 to ensure correct info is entered.
while ( width2 < 2.0 || width2 > 8.0 ) {
    System.out.print("Enter a second number between 2.0 and 8.0: ");
    width2 = in.nextDouble();
    if ( width2 < 2.0 || width2 > 8.0 )
    {
        System.out.println("Invaid entry, Please enter a value between 2.0 and 8.0.");
    }
}


// input and validation while loop for depth to ensure correct info is entered.
while( depth < 1.0 || depth > 3.0) {
    System.out.print("Enter a value for depth between 1.0 and 3.0: ");
    depth = in.nextDouble();
    if (depth < 1.0 || depth > 3.0 )
    {
        System.out.println("Invalid entry, Please enter a value between 1.0 and 3.o");
    }
}



//
// TODO - print the calculated statistics specified in "What To Do, And How"

// calculate the volume of the pool.

double poolVolume = Math.PI * Math.pow(radius, 2) * depth;

//Calculate the volume of the rectangular base 

double baseVolume = width1 * width2 * depth; 

// Calculate the volume of water in the pool.

double waterVolumeCubicFeet = poolVolume - baseVolume ; 

// Convert cubic feet to gallons

double waterVolumeGallon = waterVolumeCubicFeet * 7.481;


// Round up the gallons using Math.ceil

int roundedGal = (int) Math.ceil(waterVolumeGallon);

// Calculate the cost of water 

double cost = roundedGal * 0.10;



// You can print dollar amounts with the following code. Note that
// if you just print a double, it may not print two decimal places

// Output with results
System.out.println("The total volume of water needed: " + String.format("%.2f", waterVolumeCubicFeet) + " cubic feet");
System.out.println("The total volume of water needed: " + roundedGal + " gallons");
System.out.println("That amount of water will cost: " + NumberFormat.getCurrencyInstance().format(cost));

}
}