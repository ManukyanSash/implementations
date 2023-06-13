#include <iostream>
#include "Stack.h"

template <typename T>
void testStack() {
    Stack<T> stack;

    // Push elements onto the stack
    stack.push(10);
    stack.push(20);
    stack.push(30);

    // Print the top element
    std::cout << "Top element: " << stack.top() << std::endl;

    // Pop elements from the stack
    stack.pop();
    stack.pop();

    // Check if the stack is empty
    std::cout << "Is stack empty? " << (stack.empty() ? "Yes" : "No") << std::endl;

    // Push a new element onto the stack
    stack.push(40);

    // Print the top element again
    std::cout << "Top element: " << stack.top() << std::endl;

    // Swap the stack with another stack
    Stack<int> stack2;
    stack2.push(100);
    stack2.push(200);
    stack.swap(stack2);

    // Print the elements of the stack after swapping
    std::cout << "Elements of stack after swapping: ";
    while (!stack.empty()) {
        std::cout << stack.top() << " ";
        stack.pop();
    }
    std::cout << std::endl;

    // Print the elements of the other stack after swapping
    std::cout << "Elements of stack2 after swapping: ";
    while (!stack2.empty()) {
        std::cout << stack2.top() << " ";
        stack2.pop();
    }
    std::cout << std::endl;
}


