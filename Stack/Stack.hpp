template <typename T>
Stack<T>::Stack() : m_arr {} {}

template <typename T>
void Stack<T>::push(const T& el) { m_arr.push_back(el); }

template <typename T>
void Stack<T>::push(T&& el) { m_arr.push_back(el); }

template <typename T>
void Stack<T>::pop() { m_arr.pop_back(); }

template <typename T>
T Stack<T>::top() const {
    return m_arr[m_arr.size()-1];
}

template <typename T>
bool Stack<T>::empty() const {
    return m_arr.size() == 0;
}

template <typename T>
void Stack<T>::swap(Stack<T>& rhs) {
    this->m_arr.swap(rhs.m_arr); 
}

template <typename T>
Stack<T>::~Stack() {
    
}