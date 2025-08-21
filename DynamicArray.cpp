#include <iostream>

class DynamicArray
{
private:
    int *array;
    int size;
    int capacity;

public:
    DynamicArray(int cap)
    {
        capacity = cap;
        array = new int[capacity];
        size = 0;
    }

    int get(int i)
    {
        return array[i];
    }

    void set(int i, int n)
    {
        array[i] = n;
    }

    void pushback(int n)
    {
        if (size == capacity){
            resize();
        }
        array[size++] = n;
    }

    int popback()
    {
        if (size == 0){
            return false;
        }
        int val = array[size - 1];
        size--;
        return val;
    }

    void resize()
    {
        capacity = capacity * 2;
        int* new_array = new int[capacity];
        for (int i = 0; i < size; i++)
        {
            new_array[i] = array[i];
        }
        delete[] array;
        array = new_array;
    }

    int getSize()
    {
        return size;
    }

    int getCapacity()
    {
        return capacity;
    }

    ~DynamicArray(){
        delete[] array;
    }
};

int main()
{
    DynamicArray arr(5);

    // Push elements 0 to 6 (will trigger resize)
    for (int i = 0; i < 7; i++)
    {
        arr.pushback(i);
        std::cout << "Pushed " << i << ": size=" << arr.getSize() << ", capacity=" << arr.getCapacity() << std::endl;
    }

    // Print all elements
    std::cout << "Array contents: ";
    for (int i = 0; i < arr.getSize(); i++)
    {
        std::cout << arr.get(i) << " ";
    }
    std::cout << std::endl;

    // Set element at index 3 to 99
    arr.set(3, 88);
    std::cout << "After set(3, 88): ";
    for (int i = 0; i < arr.getSize(); i++)
    {
        std::cout << arr.get(i) << " ";
    }
    std::cout << std::endl;

    // Pop last element
    int popped = arr.popback();
    std::cout << "Popped value: " << popped << std::endl;
    std::cout << "After popback: ";
    for (int i = 0; i < arr.getSize(); i++)
    {
        std::cout << arr.get(i) << " ";
    }
    std::cout << std::endl;

    return 0;
}