// Java is a versatile, object-oriented programming language that is popular for building a wide range of applications, including web, mobile, desktop, and enterprise-level software.

// Class Declaration:
// In Java, everything is defined within classes. Classes are blueprints for objects, encapsulating data and behavior.
public class HelloWorld {

    // Method Declaration:
    // Methods are functions defined within classes. They define the behavior of objects.
    public static void main(String[] args) {

        // Print Statement:
        // The System.out.println() method is used to print output to the console.
        System.out.println("Hello, world!"); // This prints "Hello, world!" to the console.

        // Variable Declaration and Initialization:
        // Variables are containers for storing data values. In Java, variables must be declared with a specific data type.
        int num1 = 10; // This declares an integer variable named num1 and initializes it with the value 10.
        double num2 = 5.5; // This declares a double variable named num2 and initializes it with the value 5.5.
        String message = "Java is fun!"; // This declares a String variable named message and initializes it with the value "Java is fun!".

        // Conditional Statement:
        // Conditional statements allow the program to make decisions based on certain conditions.
        if (num1 > num2) {
            System.out.println("num1 is greater than num2.");
        } else {
            System.out.println("num2 is greater than or equal to num1.");
        }

        // Looping Statement:
        // Loops are used to execute a block of code repeatedly until a certain condition is met.
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteration " + (i + 1));
        }

        // Object Instantiation:
        // Objects are instances of classes that encapsulate data and behavior.
        // Here, we instantiate an object of the Scanner class to read input from the user.
        Scanner scanner = new Scanner(System.in);

        // Reading Input:
        // We use the Scanner object to read input from the user.
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // Exception Handling:
        // Exception handling is used to handle runtime errors gracefully.
        try {
            int result = num1 / 0; // This will throw an ArithmeticException.
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        }

        // Array Declaration and Initialization:
        // Arrays are used to store multiple values of the same data type.
        int[] numbers = {1, 2, 3, 4, 5}; // This declares and initializes an array of integers.

        // Enhanced for Loop (foreach loop):
        // The enhanced for loop is used to iterate over elements in an array or collection.
        for (int number : numbers) {
            System.out.println(number);
        }
    }
}
