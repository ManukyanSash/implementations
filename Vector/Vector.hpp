template <typename T>
Vector<T>::Vector() : m_size {0}, m_cap {1}, m_arr {new T[m_cap]} {}

template <typename T>
Vector<T>::Vector(const Vector<T>& src) : m_size {src.m_size}, m_cap {src.m_cap}{
    m_arr = new T[m_cap];
    std::copy(src.m_arr, src.m_arr + m_size, m_arr);
} 

template <typename T>
Vector<T>::Vector(Vector<T>&& src) : m_arr {nullptr} {
    std::swap(this->m_size, src.m_size);
    std::swap(this->m_cap, src.m_cap);
    std::swap(this->m_arr, src.m_arr);
}

template <typename T>
Vector<T>::Vector(size_t size, T val) : m_size {size}, m_cap {size+1}, m_arr{new T[size](val)} {}

template <typename T>
Vector<T>::Vector(size_t size) : m_size {size}, m_cap {size+1}, m_arr {new T[size]} {}

template <typename T>
Vector<T>::Vector(std::initializer_list<T> init_list) : m_size {init_list.size()}, m_cap {init_list.size()}, m_arr {new T[m_cap]} {
    std::copy(init_list.begin(), init_list.end(), m_arr);
}
    
template <typename T>
Vector<T>::~Vector(){
    if (m_arr != nullptr) {
        delete [] m_arr;
        m_arr = nullptr;
    }
}

template <typename T>
Vector<T>& Vector<T>::operator=(const Vector<T>& rhs){
    if (this == &rhs) return *this;
    this->m_cap = rhs.m_cap;
    this->m_size = rhs.m_size;
    delete [] this->m_arr;
    m_arr = new T[m_cap];
    std::copy(rhs.m_arr, rhs.m_arr + m_size, m_arr);
    return *this;
}

template <typename T>
Vector<T>& Vector<T>::operator=(Vector<T>&& rhs){
    if (this == &rhs) return *this;
    std::swap(this->m_size, rhs.m_size);
    std::swap(this->m_cap, rhs.m_cap);
    std::swap(this->m_arr, rhs.m_arr);
    return *this;
}

template <typename T>
const T& Vector<T>::operator[](size_t pos) const {
    return m_arr[pos];
}

template <typename T>
T& Vector<T>::operator[](size_t pos) {
    return m_arr[pos];
}

template <typename T>
void Vector<T>::push_back(T val){
    if (m_size == m_cap) {
        m_cap *= 2;
        T* tmp = new T[m_cap];
        for (int i = 0; i < m_size; ++i) {
            tmp[i] = m_arr[i];
        } 
        tmp[m_size] = val;
    }
    m_arr[m_size] = val;
    ++m_size;
}

template <typename T>
void Vector<T>::pop_back() {
    --m_size;
}

template <typename T>
void Vector<T>::insert(size_t pos, T val) {
    if (pos == m_size) {
        m_arr[pos] = val;
        ++m_size;
        return;
    } 
    push_back(val);
    for(int i = size()-1; i > pos; --i) {
        std::swap(m_arr[i], m_arr[i-1]);
    }
}

template <typename T>
void Vector<T>::erase(size_t pos) {
    for (int i = pos; i < m_size - 1; ++i) {
        std::swap(m_arr[i], m_arr[i+1]);
    }
    --m_size;
}

template <typename T>
size_t Vector<T>::find(T val) const {
    for (int i = 0; i < m_size; ++i) {
        if(val == m_arr[i]) return i;
    }
    return -1;
}

template <typename T>
size_t Vector<T>::size() const {
    return m_size;
}

template <typename T>
Vector<T>::iterator::iterator(T* ptr) : m_ptr {ptr} {} 

template <typename T>
T& Vector<T>::iterator::operator*() const {
    return *m_ptr;
}

template <typename T>
bool Vector<T>::iterator::operator==(const iterator& rhs) const {
    return m_ptr == rhs.m_ptr;
}
                
template <typename T>
bool Vector<T>::iterator::operator!=(const iterator& rhs) const {
    return !(m_ptr == rhs.m_ptr);
}  

template <typename T>
Vector<T>::iterator& Vector<T>::iterator::operator++() {
    ++m_ptr;
    return *this;
}

template <typename T>
Vector<T>::iterator Vector<T>::iterator::operator++(int) {
    iterator temp = *this;
    ++(*this);
    return temp;
}

template <typename T>
Vector<T>::iterator Vector<T>::begin() {
    return iterator(m_arr);
}

template <typename T>
Vector<T>::iterator Vector<T>::end() {
    return iterator(m_arr + m_size);
}

template <typename T>
T& Vector<T>::at(size_t index) {
    if (index >= m_size) {
        throw std::out_of_range("Index out of range");
    }
    return m_arr[index];
}

template<typename T>
Vector<T>::iterator::~iterator() {
    m_ptr = nullptr;
}