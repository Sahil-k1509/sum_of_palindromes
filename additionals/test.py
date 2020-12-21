from ..three_palindrome import find_palindromes, is_palindrome
from ..naive_sum import naive_palindromes
import matplotlib.pyplot as plt


# Initialized arrays for recording values
time_naive = []
time_algo  = []
numbers = []

for i in range(1, 100000000):
    
    p1_a, p2_a, p3_a, time_a = find_palindromes(i, g=10, print_pal=False)
    #p1_n, p2_n, p3_n, time_n = naive_palindromes(i, print_pal=False)
    
    
    if is_palindrome(p1_a) and is_palindrome(p2_a) and is_palindrome(p3_a) and p1_a + p2_a + p3_a == i:
        time_algo.append(time_a)
    else:
        time_algo.append(-1)
    
    
    #if is_palindrome(p1_n) and is_palindrome(p2_n) and is_palindrome(p3_n) and p1_n + p2_n + p3_n == i:
    #    time_naive.append(time_n)
    #else:
    #    time_naive.append(-1)
        
    numbers.append(i)
    print(i)
    if time_a == -1: break
    # print(i)

    
plt.xlabel('number')
plt.ylabel('time(ms)')
    
plt.plot(numbers, time_algo, label='Algorithm')
#plt.plot(numbers, time_naive, label='Brute Force')

plt.legend()
plt.show()