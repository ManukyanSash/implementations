#ifndef VECTOR
#define VECTOR

#include <iostream>
#include <initializer_list>

template <typename T>
class Vector{
    private:
        size_t m_size {0};
        size_t m_cap {1};
        T* m_arr {nullptr};
        class iterator{
            private:
                T* m_ptr {nullptr};
            public:
                iterator(T*);
                ~iterator();

                T& operator*() const;
                bool operator==(const iterator&) const;
                bool operator!=(const iterator&) const;

                iterator& operator++();
                iterator operator++(int);
        };
    public:
        Vector();
        Vector(const Vector&);
        Vector(Vector&&);
        Vector(size_t, T);
        Vector(size_t);
        Vector(std::initializer_list<T>);
        ~Vector();
    
        Vector& operator=(const Vector&);
        Vector& operator=(Vector&&);
        const T& operator[](size_t pos) const;
        T& operator[](size_t pos);

        void push_back(T el);
        void pop_back();
        void insert(size_t pos, T el);
        void erase(size_t pos);
        size_t find(T val) const;

        size_t size() const;

        iterator begin();
        iterator end();
        T& at(size_t);
}; 

#include "Vector.hpp"

#endif