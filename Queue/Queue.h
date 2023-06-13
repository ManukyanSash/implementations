#ifndef QUEUE
#define QUEUE

#include <iostream>
#include <stack>

template <typename T>
class Queue {
    private:
        std::stack<T> primaryStack;
        std::stack<T> secondaryStack;
    public:
        void push(const T&);
        T pop();
        T front();
        size_t size() const;
        bool empty() const;
};

#include "Queue.hpp"

#endif
