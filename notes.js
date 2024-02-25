// Variables (var): Variables are containers for storing data values.
// In this code, we declare a variable named 'message' using the 'var' keyword
// and assign it the value "Hello, world!".
var message = "Hello, world!";

// Comments (//): Comments are ignored by the JavaScript engine
// and are used to add explanations or notes to the code for better understanding.

// console.log(): This method is used to output data to the console.
// It's often used for debugging purposes to print values of variables or messages.
// Here, we use it to log the value of the 'message' variable and a greeting message inside the 'sayHello' function.
console.log(message); // This prints "Hello, world!" to the console.

// Functions (function): Functions are blocks of reusable code that perform a specific task.
// In this code, we declare a function named 'sayHello' using the 'function' keyword.
// Inside the function body, we use console.log() to print the greeting message.
function sayHello() {
    // Function body starts here.
    console.log("Hello there!"); // This prints "Hello there!" to the console.
    // Function body ends here.
}

// Function Call: After defining the 'sayHello' function,
// we call it by simply writing its name followed by parentheses ().
// This causes the function to execute, printing "Hello there!" to the console.
sayHello(); // This invokes the 'sayHello' function, causing "Hello there!" to be printed to the console.
// Conditional Statements (if...else): Conditional statements are used to make decisions in code.
// Here's an example:
var x = 10;
if (x > 5) {
    console.log("x is greater than 5"); // This prints "x is greater than 5" to the console.
} else {
    console.log("x is less than or equal to 5");
}
// Conditional Statements:

// 1. If Statement:
// The if statement is used to execute a block of code if a specified condition evaluates to true.
// If the condition is false, the code block is skipped.
var age = 20;
if (age >= 18) {
    console.log("You are an adult.");
}

// 2. Else If Statement:
// The else if statement allows you to specify a new condition to test if the first condition in the if statement is false.
// If the condition in the else if statement is true, the corresponding block of code is executed.
// You can have multiple else if statements in a chain.
var time = 14;
if (time < 12) {
    console.log("Good morning!");
} else if (time < 18) {
    console.log("Good afternoon!");
} else {
    console.log("Good evening!");
}

// 3. Else Statement:
// The else statement is used to execute a block of code if the condition in the if statement is false
// and no else if conditions are true. It comes at the end of an if statement.
var age = 15;
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}


// Loops (for): Loops are used to repeat a block of code until a condition is met.
// Here's an example:
for (var i = 0; i < 5; i++) {
    console.log("Count: " + i); // This prints "Count: 0", "Count: 1", ..., "Count: 4" to the console.
}

// Arrays: Arrays are used to store multiple values in a single variable.
// Here's an example:
var colors = ["Red", "Green", "Blue"];
console.log(colors[0]); // This prints "Red" to the console.

// Objects: Objects are used to store key-value pairs.
// Here's an example:
var person = {
    name: "John",
    age: 30,
    city: "New York"
};
console.log(person.name); // This prints "John" to the console.