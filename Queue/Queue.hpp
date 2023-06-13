template <typename T>
void Queue<T>::push(const T& el) {
    primaryStack.push(el);
}

template <typename T>
T Queue<T>::pop() { 
    for(size_t i = 0; i < primaryStack.size() - 1; ++i) {
        secondaryStack.push(primaryStack.top());
        primaryStack.pop();
    }
    T res = primaryStack.top();
    primaryStack.pop();
    for(size_t i = 0; i < secondaryStack.size(); ++i) {
        primaryStack.push(secondaryStack.top());
        secondaryStack.pop();
    }
    return res;
}

template <typename T>
T Queue<T>::front() {
    for(size_t i = 0; i < primaryStack.size(); ++i) {
        secondaryStack.push(primaryStack.top());
        primaryStack.pop();
    }
    T res = primaryStack.top();
    for(size_t i = 0; i < secondaryStack.size(); ++i) {
        primaryStack.push(secondaryStack.top());
        secondaryStack.pop();
    }
    return res;
}

template <typename T>
size_t Queue<T>::size() const {
    return primaryStack.size();
}

template <typename T>
bool Queue<T>::empty() const {
    return primaryStack.size() == 0;
}