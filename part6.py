"""
SCI 33 Project 1
Part6:  Implement a custom iterator with the ability to peek at the next item
        without advancing the iterator
"""


class PeekableIterator:
    """
    Implement a custom iterator in Python that extends the functionality of a
    standard iterator by allowing us to peek at the next item without
    advancing the iterator. This class also includes a method to check if
    there are more items to iterate.
    """

    def __init__(self, iterable):
        """
        Create a list for items of the iterable
        Set the pointer to the start of the list
        :param iterable: an iterable object
        """
        self._iter_lst = list(iterable)
        self._pointer = 0

    def __iter__(self):
        """
        Return the iterator object
        """
        return self

    def __next__(self):
        """
        Return the current item in the iterable and advance the pointer
        to the next item. If the pointer has reached the end of the iterable,
        raise a StopIteration exception.
        """
        # Check if the pointer has reached the end of the iterable
        if self._pointer >= len(self._iter_lst):
            raise StopIteration("End of the iterable")
        # Return the current item and advance the current pointer to next item
        item = self._iter_lst[self._pointer]
        self._pointer += 1
        return item

    def peek(self):
        """
        Peek at the current item without advancing the pointer.
        If the pointer has reached the end of the iterable, raise a
        StopIteration exception.
        """
        # Check if the pointer has reached the end of the iterable
        if self._pointer >= len(self._iter_lst):
            raise StopIteration("End of the iterable")
        return self._iter_lst[self._pointer]

    def has_next(self) -> bool:
        """
        Check if there are more items to iterate.
        :return: True if there are more items to iterate, otherwise False
        """
        return self._pointer < len(self._iter_lst)


def main():
    """
    Main function to test the PeekableIterator class
    """
    my_iterable = "abcd"
    iter_obj = PeekableIterator(my_iterable)
    print(next(iter_obj))  # a
    print(iter_obj.peek())  # b
    print(next(iter_obj))  # b
    print(iter_obj.has_next())  # True
    print(next(iter_obj))  # c
    print(next(iter_obj))  # d
    print(iter_obj.has_next())  # False
    try:
        print(next(iter_obj))  # Raises a StopIteration exception
    except StopIteration as e:
        print(f"next StopIteration: {e}")
    try:
        print(iter_obj.peek())  # Raises a StopIteration exception
    except StopIteration as e:
        print(f"peek StopIteration: {e}")


if __name__ == "__main__":
    main()
