"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


#####################
# This is my first pass - just to establish the correct answer
# Answer: 4613732
#####################
def answer1(term_max):
    _sum = 0
    previous = 1
    current = 2
    while current <= term_max:
        if current % 2 == 0:
            _sum += current
        new_current = previous + current
        previous = current
        current = new_current
    print(_sum)


def answer2():
    _sum = 0
    tuple = (1, 2)


class Fib:
    """Iterator for looping over a fibonacci sequence until max_term(inclusive)."""
    def __init__(self, max_term):
        self.max_term = max_term
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        new_current = self.previous + self.current

        if new_current > self.max_term:
            raise StopIteration

        self.previous = self.current
        self.current = new_current
        return new_current





if __name__ == '__main__':
    answer1(4000000)
    answer2(4000000)