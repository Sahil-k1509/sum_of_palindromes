"""
In this program, We will find the three numbers whose sum is a number given by user
But, We will use exhaustive testing instead of any algorithms.

This program will have time complexity of O(n^3) which is much worse than the O(1) complexity of
the algorithm in research paper.

We will compare the results of both of them.
"""

# Import modules
from time import perf_counter


# function to check palindrome
def is_palindrome(number):
    return str(number) == str(number)[::-1]


# We define function only for base 10
def naive_palindromes(n, print_pal=True):
    
    def print_palindromes(p1, p2, p3, time_elapsed):
        print("-------------------------------------------")
        print("First Palindrome: \t" ,   p1,  sep='')
        print("Second Palindrome:\t" ,   p2,  sep='')
        print("Third Palindrome: \t" ,   p3,  sep='')
        print("-------------------------------------------")
        print(f"Total Time Elapsed:  {time_elapsed*1000:.5f} ms")

    start_time = perf_counter()
    for i in range(n+1):
        for j in range(n+1):
            k = n - (i+j)
            if k < 0: continue
            
            if is_palindrome(i) and is_palindrome(j) and is_palindrome(k):
                end_time = perf_counter()
                time_elapsed =  end_time - start_time
                pal1, pal2, pal3 = i, j, k
                
                if print_pal:
                    print_palindromes(pal1, pal2, pal3, time_elapsed)
                
                return (pal1, pal2, pal3, time_elapsed*1000)
                

def main():
    
    print("Enter the number you would like to break: ", end='')
    n = int(input())
    
    naive_palindromes(n, print_pal=True)
    
    
if __name__ == "__main__":
    main()