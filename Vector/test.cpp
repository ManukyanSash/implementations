#include "Vector.h"

void testVector() {
    // Create an empty vector
    Vector<int> vec1;

    // Add elements to the vector
    vec1.push_back(10);
    vec1.push_back(20);
    vec1.push_back(30);

    // Print the vector elements
    std::cout << "Vector elements: ";
    for (size_t i = 0; i < vec1.size(); ++i) {
        std::cout << vec1[i] << " ";
    }
    std::cout << std::endl;

    // Insert an element at position 1
    vec1.insert(1, 15);

    // Print the vector elements after insertion
    std::cout << "Vector elements after insertion: ";
    for (size_t i = 0; i < vec1.size(); ++i) {
        std::cout << vec1[i] << " ";
    }
    std::cout << std::endl;

    // Remove the last element
    vec1.pop_back();

    // Print the vector elements after removal
    std::cout << "Vector elements after removal: ";
    for (size_t i = 0; i < vec1.size(); ++i) {
        std::cout << vec1[i] << " ";
    }
    std::cout << std::endl;

    // Find the value 20 in the vector
    int val = vec1.find(20);
    if (val != -1) {
        std::cout << "Value 20 found at index: " << val << std::endl;
    } else {
        std::cout << "Value 20 not found in the vector" << std::endl;
    }

    // Test operator overloads
    Vector<int> vec2 = vec1; // Copy constructor
    Vector<int> vec3;
    vec3 = vec1; // Copy assignment operator

    // Print the vector elements of vec2
    std::cout << "Vector elements of vec2: ";
    for (size_t i = 0; i < vec2.size(); ++i) {
        std::cout << vec2[i] << " ";
    }
    std::cout << std::endl;

    // Print the vector elements of vec3
    std::cout << "Vector elements of vec3: ";
    for (size_t i = 0; i < vec3.size(); ++i) {
        std::cout << vec3[i] << " ";
    }
    std::cout << std::endl;

    // Test move constructor
    Vector<int> vec4(std::move(vec1));

    // Print the vector elements of vec4
    std::cout << "Vector elements of vec4: ";
    for (size_t i = 0; i < vec4.size(); ++i) {
        std::cout << vec4[i] << " ";
    }
    std::cout << std::endl;

    // Test move assignment operator
    Vector<int> vec5;
    vec5 = std::move(vec4);

    // Print the vector elements of vec5
    std::cout << "Vector elements of vec5: ";
    for (size_t i = 0; i < vec5.size(); ++i) {
        std::cout << vec5[i] << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void testVectorIterator() {
    Vector<T> vec {10, 20, 30};

    // Print vector elements using iterator
    std::cout << "Vector elements: ";
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // Access elements using at() method
    try {
        std::cout << "Element at index 1: " << vec.at(1) << std::endl;
        std::cout << "Element at index 3: " << vec.at(3) << std::endl;  // Out of range
    } catch (const std::out_of_range& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    // Modify elements using iterator
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        *it += 5;
    }

    // Print vector elements after modification
    std::cout << "Vector elements after modification: ";
    for (const auto& element : vec) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}