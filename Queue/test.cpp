#include "Queue.h"

void testQueue() {
    Queue<int> q;

    q.push(10);
    q.push(20);
    q.push(30);

    std::cout << "Front element: " << q.front() << std::endl;

    while (!q.empty()) {
        std::cout << "Dequeued element: " << q.pop() << std::endl;
    }

    std::cout << "Is queue empty? " << (q.empty() ? "Yes" : "No") << std::endl;
}