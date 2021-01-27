from three_palindrome import find_palindromes, is_palindrome, check_base
from naive_sum import naive_palindromes
import matplotlib.pyplot as plt


def test_algo(n):
    p1, p2, p3, t = find_palindromes(n, g=10, print_pal=False)
    
    assert is_palindrome(p1), f"{p1} is not a palindrome. ({n})" 
    assert is_palindrome(p2), f"{p2} is not a palindrome. ({n})" 
    assert is_palindrome(p3), f"{p3} is not a palindrome. ({n})" 
    assert p1 + p2 + p3 == n, f"{p1} {p2} {p3} don't add upto {n}"
    
    return (p1, p2, p3, t) 
    
    
def test_naive(n):
    p1, p2, p3, t = naive_palindromes(n, print_pal=False)
    
    assert is_palindrome(p1), f"{p1} is not a palindrome. ({n})" 
    assert is_palindrome(p2), f"{p2} is not a palindrome. ({n})" 
    assert is_palindrome(p3), f"{p3} is not a palindrome. ({n})" 
    assert p1 + p2 + p3 == n, f"{p1} {p2} {p3} don't add upto {n}" 
    
    return (p1, p2, p3, t)
    
    
def test_compare(start, end):
    nums = list(range(start, end+1))
    time_a = []
    time_n = []

    for n in range(start, end+1):
        p1a, p2a, p3a, ta = test_algo(n)
        p1n, p2n, p3n, tn = test_naive(n)
        
        time_a.append(ta)
        time_n.append(tn)
        
    plt.xlabel('number')
    plt.ylabel('time(ms)')
    
    plt.plot(nums, time_a, label='Algorithm')
    plt.plot(nums, time_n, label='Brute Force')
    
    plt.legend()
    plt.show()
        
test_compare(10, 3000)