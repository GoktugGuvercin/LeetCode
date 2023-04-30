### Question: 509. Fibonacci Number
### Given n, calculate f(n), referring to nth item in fibonacci series
### f(0) = 0, f(1) = 1, f(2) = f(1) + f(0)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
