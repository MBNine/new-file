File Extension: HelloWorld.cs

Here's an expanded explanation of C# programming language with detailed comments:

```csharp
// C# is a versatile, object-oriented programming language developed by Microsoft. It is widely used for building a variety of applications, including web, desktop, mobile, and gaming.

// Namespace Declaration:
// Namespaces are used to organize code into logical groups and prevent naming conflicts. The 'HelloWorld' namespace contains the definition of the 'Program' class.
namespace HelloWorld {

    // Class Declaration:
    // Classes are the fundamental building blocks of C# programs. They encapsulate data and behavior.
    public class Program {

        // Method Declaration:
        // Methods define the behavior of objects. The 'Main' method is the entry point of a C# program.
        public static void Main(string[] args) {

            // Print Statement:
            // The 'Console.WriteLine()' method is used to print output to the console.
            Console.WriteLine("Hello, world!"); // This prints "Hello, world!" to the console.

            // Variable Declaration and Initialization:
            // Variables are containers for storing data values. In C#, variables must be declared with a specific data type.
            int num1 = 10; // This declares an integer variable named 'num1' and initializes it with the value 10.
            double num2 = 5.5; // This declares a double variable named 'num2' and initializes it with the value 5.5.
            string message = "C# is awesome!"; // This declares a string variable named 'message' and initializes it with the value "C# is awesome!".

            // Conditional Statement:
            // Conditional statements allow the program to make decisions based on certain conditions.
            if (num1 > num2) {
                Console.WriteLine("num1 is greater than num2.");
            } else {
                Console.WriteLine("num2 is greater than or equal to num1.");
            }

            // Looping Statement:
            // Loops are used to execute a block of code repeatedly until a certain condition is met.
            for (int i = 0; i < 5; i++) {
                Console.WriteLine("Iteration " + (i + 1));
            }

            // Object Instantiation:
            // Objects are instances of classes that encapsulate data and behavior.
            // Here, we instantiate an object of the Random class to generate random numbers.
            Random random = new Random();

            // Array Declaration and Initialization:
            // Arrays are used to store multiple values of the same data type.
            int[] numbers = {1, 2, 3, 4, 5}; // This declares and initializes an array of integers.

            // Enhanced for Loop (foreach loop):
            // The enhanced for loop is used to iterate over elements in an array or collection.
            foreach (int number in numbers) {
                Console.WriteLine("Number: " + number);
            }

            // Method Invocation:
            // Methods encapsulate behavior and can be invoked to perform specific tasks.
            // Here, we invoke a method named 'PrintMessage' to print a message to the console.
            PrintMessage("Welcome to C#!");

            // Exception Handling:
            // Exception handling is used to handle runtime errors gracefully.
            try {
                int result = num1 / 0; // This will throw a DivideByZeroException.
            } catch (DivideByZeroException e) {
                Console.WriteLine("Cannot divide by zero.");
            }
        }

        // Method Declaration:
        // Methods define the behavior of objects. Here, we define a method named 'PrintMessage' that takes a string parameter and prints it to the console.
        static void PrintMessage(string message) {
            Console.WriteLine(message);
        }
    }
}
