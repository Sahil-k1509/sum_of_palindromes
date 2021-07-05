from three_palindrome import find_palindromes, is_palindrome, check_base
from naive_sum import naive_palindromes, naive_palindromes_n3 
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
    

    
def test_naive_n3(n):
    p1, p2, p3, t = naive_palindromes_n3(n, print_pal=False)
    
    assert is_palindrome(p1), f"{p1} is not a palindrome. ({n})" 
    assert is_palindrome(p2), f"{p2} is not a palindrome. ({n})" 
    assert is_palindrome(p3), f"{p3} is not a palindrome. ({n})" 
    assert p1 + p2 + p3 == n, f"{p1} {p2} {p3} don't add upto {n}" 
    
    return (p1, p2, p3, t)
    
    
def test_compare(start, end):
    nums = list(range(start, end+1))
    time_a = []
    time_n = []
    time_n3 = []

    for n in range(start, end+1):
        p1a, p2a, p3a, ta = test_algo(n)
        p1n, p2n, p3n, tn = test_naive(n)
        
        time_a.append(ta)
        time_n.append(tn)
        
    for n in range(1, 1100):
        p1n3, p2n3, p3n3, tn3 = test_naive_n3(n)
        time_n3.append(tn3)
        
    plt.xlabel('number')
    plt.ylabel('time(ms)')
    
    plt.scatter(nums, time_a, s=10, label='Algorithm')

    plt.legend()
    plt.show()
    
    plt.scatter(list(range(1, 1100)), time_n3, s=10, label='Brute Force(O(n^3))')

    plt.legend()
    plt.show()

    plt.scatter(nums, time_n, s=10, label='Brute Force(O(n^2))')
    
    plt.legend()
    plt.show()
        
test_compare(3000, 10000)