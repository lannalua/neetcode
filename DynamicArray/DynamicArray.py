class DynamicArray:

    # DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._array = [0]*capacity
        self._size = 0 

    # int get(int i) will return the element at index i. Assume that index i is valid.
    def get(self, i: int) -> int:
        return self._array[i]

    # void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    # void pushback(int n) will push the element n to the end of the array.
    # If we call void pushback(int n) but the array is full, we should resize the array first
    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1

    # int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        if self._size == 0:
            raise IndexError("popback from empty array")
        val = self._array[self._size - 1]
        self._size -= 1
        return val
    
    # void resize() will double the capacity of the array.
    def resize(self) -> None:
        self._capacity = self._capacity*2
        new_array = [0] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    # int getSize() will return the number of elements in the array.
    def getSize(self) -> int:
        return self._size

    # getCapacity() will return the capacity of the array.
    def getCapacity(self) -> int:
        return self._capacity


# ...existing code...

if __name__ == "__main__":
    # Create a DynamicArray with initial capacity 5
    array = DynamicArray(5)

    # Push elements 0 to 6 (will trigger resize)
    for i in range(7):
        array.pushback(i)
        print(
            f"Pushed {i}: size={array.getSize()}, capacity={array.getCapacity()}")

    # Print all elements
    print("Array contents:", [array.get(i) for i in range(array.getSize())])

    # Set element at index 3 to 99
    array.set(3, 99)
    print("After set(3, 99):", [array.get(i) for i in range(array.getSize())])

    # Pop last element
    popped = array.popback()
    print(f"Popped value: {popped}")
    print("After popback:", [array.get(i) for i in range(array.getSize())])
