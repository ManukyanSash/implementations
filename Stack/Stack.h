#ifndef STACK
#define STACK

#include <iostream>
#include <vector>

template <typename T>
class Stack {
    private:
        std::vector<T> m_arr;
    public:
        Stack();

        void push(const T&);
        void push(T&&);
        void pop();
        T top() const;
        bool empty() const;
        void swap(Stack<T>&);

        ~Stack();
};

#include "Stack.hpp"

#endif