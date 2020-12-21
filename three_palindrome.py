# About the Program

"""
Research Paper by: Javier Cilleruelo, Florian Luca, Lewis Baxter

The research paper states that every positive integer in base g >= 5 can always
be expressed as a sum of three palindromes in the same base.


Palindrome Number: A number which is same when read from left to right or right to left is a Palindrome number.
                e.g. 121 is a Palindrome number.


In this program, we will try to implement the Algorithms in that 42 page research paper and try to find the 3 palindrome numbers
that will make the number given by user as input when added. The algorithm holds for any base but we will only consider base 10 
for now and extend it to other bases once we have method to check if number is of certain base or not to catch invalid inputs.


Algorithm implementation by: Sahil Bairagi
Dated: 12 August 2020
"""


# INDEX:

# 1)    imports:                  line 49
# 2)    Helper functions:         line 56   -   112
# 3)    sum_two_digits:           line 117  -   132
# 4)    sum_three_digits:         line 138  -   169
# 5)    sum_four_digits:          line 173  -   246
# 6)    sum_five_digits:          line 252  -   333
# 7)    sum_six_digits:           line 339  -   740
# 8)    Decide_type:              line 753  -   848
# 9)    Algorithm_1:              line 856  -   937
# 10)   Algorithm_2:              line 943  -   1041
# 11)   Algorithm_3:              line 1047 -   1142
# 12)   Algorithm_4:              line 1148 -   1432
# 13)   Algorithm_5:              line 1438 -   1498
# 14)   Main_algorithm:           line 1505 -   1576
# 15)   find_palindrome:          line 1583 -   1697
# 16)   main:                     line 1702 -   1735
# 17)   calling main function:    line 1740 


# Main Code Starts
# ------------------------------------------------------------------------------------------------ #

# Import modules
from time import perf_counter
from math import floor



# Helper Functions
# ------------------------------------------------------------------------------------------------ #
def D(number, g=10):
    '''Returns the mod(remainder) when number is divided by g(base). 
        For g=10 returns the digit at unit place.'''
        
    result = number % g
    
    if result < 0:
        result += g
    
    return result


def find_digits_and_convert_to_list(n):
    '''Count number of digits and convert number to array of digits.'''
    
    num_digits = 0
    num_array = []
    
    while n>0:
        num_digits += 1
        num_array.append(n % 10)
        n = n // 10
    
    return (num_digits, num_array)


def list_to_int(n):
    '''Converts a list of integers into equivalent integer. We reverse array because 
        by convention our numbers are reversed. e.g. 100 is represented by [0,0,1] '''
    
    return int(''.join(list(map(str, n[::-1]))))


def is_palindrome(number):
    '''Checks if a number is a palindrome or not.'''
    
    if type(number)!=int:
        raise ValueError("You can't give any other argument other than integers(not even strings/arrays).")
    
    return str(number) == str(number)[::-1]


def remove_trailing_zeros(n):
    '''Removes the unnecessary zeros from the number list before displaying it as output.'''
    
    done = False
    
    while not done:
        try:
            if n[-1] == 0:
                n.pop()
            else:
                break
        except IndexError:
            break
    
    return n
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def sum_two_digits(d, p1, p2, p3, g=10):

    if d[1] <= d[0]:
        p1[1], p1[0] = d[1], d[1]
        p2[0] = d[0] - d[1]

    elif d[1] > d[0] + 1:
        p1[1], p1[0] = d[1]-1, d[1]-1
        p2[0] = g + d[0] - d[1] + 1
    
    elif d[1] == d[0] + 1:
        p1[1], p1[0] = d[0], d[0]
        p2[0] = g-1
        p3[0] = 1

    return (p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def sum_three_digits(d, p1, p2, p3, g=10):

    if d[2] <= d[0]:
        p1[2], p1[1], p1[0] = d[2], d[1], d[2]
        p2[0] = d[0] - d[2]
    
    elif d[2] >= d[0] + 1 and d[1] != 0:
        p1[2], p1[1], p1[0] = d[2], d[1]-1, d[2]
        p2[0] = g + d[0] - d[2]

    elif (d[2] >= d[0] + 1) and (d[1] == 0) and (D(d[2]-d[0]-1, g)!=0):
        p1[2], p1[1], p1[0] = d[2]-1, g-1, d[2]-1
        p2[0] = g + d[0] - d[2] + 1

    elif (d[2] >= d[0] + 1) and (d[1] == 0) and (D(d[2]-d[0]-1, g)==0):
        
        if d[2] >= 3:
            p1[2], p1[1], p1[0] = d[2]-2, g-1, d[2]-2
            p2[2], p2[1], p2[0] = 1, 1, 1
        
        elif d[2] == 2:
            p1[2], p1[1], p1[0] = 1, 0, 1
            p2[1], p2[0] = g-1, g-1
            p3[0] = 1
        
        elif d[2] == 1:
            p1[1], p1[0] = g-1, g-1
            p2[0] = 1

    return (p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def sum_four_digits(d, p1, p2, p3, g=10):
    
    if (d[::-1] >= [d[3], 0, 0, d[3]]):
        m = [d[::-1][0] - d[3], d[::-1][1], d[::-1][2], d[::-1][3] - d[3]] 
        
        if ((m != [0, 2, 0, 1]) and all([(m != [0, 0, x+1, x]) for x in range(1, g-1)])):
            p1 = [d[3], 0, 0, d[3]]
            temp = m
            temp = temp[1:][::-1]
            
            if temp[2] != 0:
                # three digit
                p2, p3, p1 = sum_three_digits(temp, p2, p3, p1)
            
            else:
                # two digit
                temp = temp[:-1]
                p2, p3, p1 = sum_two_digits(temp, p2, p3, p1)
        
        elif m == [0, 2, 0, 1]:
            
            if d[3] != 1 and d[3] != g-1:
                p1 = [d[3]-1, g-1, g-1, d[3]-1]
                p2 = [0, 2, 1, 2][::-1]
            
            elif d[3]==1:
                p1 = [1, 1, 1, 1]
                p2 = [0, 0, g-2, g-2][::-1]
                p3 = [0, 0, 0, 3][::-1]
            
            elif d[3] == g-1:
                p1 = [g-1, 1, 1, g-1]
                p2 = [0, 0, g-2, g-2][::-1]
                p3 = [0, 0, 0, 3][::-1]

        elif any([(m == [0, 0, x + 1, x]) for x in range(1, g-1)]):
            
            d0 = 1
            
            for i in range(1, g-1):
                if m == [0, 0, i + 1, i]:
                    d0 = i
                    break
            
            if d[3] + d0 == d[0]:
            
                if d[3] != 1:
                    p1 = [d[3]-1, g-2, g-2, d[3]-1]
                    p2 = [0, 1, 3, 1][::-1]
                    p3 = [0, 0, d0, d0][::-1]
            
                else:
                    p1 = [0, g-1, g-1, g-1][::-1]
                    p2 = [0, 0, d0+1, d0+1][::-1]
                    p3 = [0, 0, 0, 1][::-1]

            elif d[3] + d0 == g + d[0]:
                p1 = [d[3]-1, g-2, g-2, d[3]-1]
                p2 = [0, 1, 3, 1][::-1]
                p3 = [0, 0, d0, d0][::-1]
        
        
    elif (d[0] <= d[3] - 1) and d[3] != 1:
        p1 = [d[3]-1, g-1, g-1, d[3]-1]
        p2 = [0, 0, 0, g+d[0]-d[3]][::-1]
        p3 = [0, 0, 0, 1][::-1]
    
    
    elif d[::-1] == [1, 0, 0, 0]:
        p1 = [0, g-1, g-1, g-1][::-1]
        p2 = [0, 0, 0, 1][::-1]
    
    
    return (p1, p2, p3)
            
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def sum_five_digits(d, p1, p2, p3, g=10):
    
    if d[4]!=1:
        p1, p2, p3 = main_algorithm(d, p1, p2, p3, g)
    
    else:
        r = [1, d[3], 0, d[3], 1]
        r_int = list_to_int(r)
        n_int = list_to_int(d)
        m_int = n_int - r_int
        _, m = find_digits_and_convert_to_list(m_int)
        
        if m_int >= 0:
    
            if m_int != 201 and all([(m != [x, x + 1]) for x in range(1, g-1)]):
                p2, p3, p1 = find_palindromes(m_int, g=10, print_pal=False, returnAs='list')
    
                if not any(p1): p1 = r[:]
                elif not any(p2): p2 = r[:]
                elif not any(p3): p3 = r[:]
                
            elif m_int == 201:
                p1 = [1, d[3], 1, d[3], 1]
                p2 = [0, 0, 1, 0, 1][::-1]
                
            else:
                
                d0 = 1
                
                for i in range(1, g-1):
                    if m == [0, 0, i + 1, i]:
                        d0 = i
                        break
                
                if d[3]!=0:
                
                    if d0 + 1 + d[3] <= g-1:
                        p1 = [1, d[3]-1, 1, d[3]-1, 1]
                        p2 = [0, 0, g-1, d0+1, g-1][::-1]
                        p3 = [0, 0, 0, 0, d0+1][::-1]
                
                    elif d[3]+1+d0==g+d[1]:
                        p1 = [1, d[3]-1, 1, d[3]-1, 1]
                        p2 = [0, 0, g-1, d0+1, g-1][::-1]
                        p3 = [0, 0, 0, 0, d0+1][::-1]
                
                else:
                    p1 = [0, g-1, g-1, g-1, g-1][::-1]
                    p2 = [0, 0, 0, d0+1, d0+1][::-1]
                    p3 = [0, 0, 0, 0, 1][::-1]
        
        else:
            n_2 = [1, d[3]-1, g-1, d[3]-1, 1]
            m_2_int = n_int - list_to_int(n_2)
            _, m_2 = find_digits_and_convert_to_list(m_2_int)
           
            if d[3]==0:
                p1 = [0, g-1, g-1, g-1, g-1][::-1]
                p2 = [0, 0, 0, 0, 1][::-1]
        
            elif d[3]!=0 and m_2_int!=201 and all([(m_2 != [x, x+1]) for x in range(1, g-1)]):
                p1, p2, p3 = find_palindromes(m_2_int, g=10, print_pal=False, returnAs='list')
        
                if not any(p1): p1 = n_2[:]
                elif not any(p2): p2 = n_2[:]
                elif not any(p3): p3 = n_2[:]
            
            else:
            
                d0 = 1
            
                for i in range(1, g-1):
                    if m == [0, 0, i+1, i]:
                        d0 = i
                        break
            
                p1 = [1, d[3]-1, g-2, d[3]-1, 1]
                p2 = [0, 0, 1, d0+1, 1][::-1]
                p3 = [0, 0, 0, 0, d0-1][::-1] 
                
        
    return (p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def sum_six_digits(d, p1, p2, p3, g=10):
    
    if d[5]!=1:
        # l = 6
        m = 3
        _, p1, p2, p3 = decide_type(d, p1, p2, p3, g)
        

        # Initialize the x, y, z arrays and carry over arrays.
        x, y, z = [None, p1[0]], [None, p2[0]], [None, p3[0]]
        c = [None, (x[1] + y[1] + z[1])//g]
        
        
        # Add the next value of x, y, z and carry
        if z[1] <= d[2*m - 3] - 1:  x.append(D(d[2*m - 2] - y[1], g))
        else:  x.append(D(d[2*m - 2] - y[1] - 1, g))
            
            
        y.append(D(d[2*m - 3] - z[1] - 1, g))
        z.append(D(d[1] - x[2] - y[2] - c[1], g))
        c.append( (x[2] + y[2] + z[2] + c[1] - d[1])//g)
       
        
        # Next all insertions are iterative
        for i in range(3, m):
            
            x.append(1 if (z[i-1] <= d[2*m - i - 1] - 1) else 0)
            y.append(D(d[2*m - i - 1] - z[i - 1] - 1, g))
            z.append(D(d[i - 1] - x[i] - y[i] - c[i - 1], g))
            
            c.append((x[i] + y[i] + z[i] + c[i - 1] - d[i - 1])//g)
        
        
        x.append(0)
        y.append(D(d[m - 1] - z[m - 1] - c[m - 1], g))
        c.append((x[m] + y[m] + z[m - 1] + c[m - 1] - d[m - 1])//g)
        
        # Adjustment Step
        if c[m] == 1: 
            # No adjustment is needed
            pass
        
        
        elif c[m] == 0:
            
            if y[m] != 0:
                
                x[m] = 1
                y[m] -= 1
            
            else:
            
                if y[m-1] != 0:
                    
                    x[m] = 1
                    y[m] = g - 2
                    y[m-1] -= 1
                    z[m-1] += 1 
            
                elif y[m-1] == 0 and z[m-1] != 0:
                    
                    y[m-1] = 1
                    y[m] = 1
                    z[m-1] -= 1
            
                elif y[m-1] == 0 and z[m-1] == 0:
            
                    if x[2] != 0:
                        
                        x[2] -= 1
                        x[3] = g - 1
                        y[2] = 1
                        y[3] = 1
            
                    else:
            
                        if x[1] == 1:
                            
                            p1 = [2, 0, 0, 0, 0, 2]
                            p2 = [0, 0, 0, 0, 1, 1][::-1]
                            p3 = [0, 0, 0, 0, 0, g-4][::-1]
                            
                            return (p1, p2, p3)
                        
                        elif x[1] != 1 and y[1] != g - 1:
                            
                            p1 = [x[1]-1, g-1, 0, 0, g-1, x[1]-1]
                            p2 = [0, y[1]+1, 0, g-2, 0, y[1]+1][::-1]
                            p3 = [0, 0, z[1], 1, 1, z[1]][::-1]
                            
                            return (p1, p2, p3)
                        
                        elif x[1] != g - 1 and z[1] == y[1] == g - 1:
                            
                            p1 = [x[1]+1, 0, 0, 0, 0, x[1]+1]
                            p2 = [0, 0, 0, 0, 1, 1][::-1]
                            p3 = [0, 0, 0, 0, 0, g-4][::-1]
                            
                            return (p1, p2, p3)
        
            
        elif c[m] == 2:
            
            y[m-1] -= 1
            y[m] = g - 2
            x[m] = 1
            z[m-1] = 0
        
        p1 = [x[1], x[2], x[3], x[3], x[2], x[1]]
        p2 = [0, y[1], y[2], y[3], y[2], y[1]][::-1]
        p3 = [0, 0, z[1], z[2], z[2], z[1]][::-1]
        
        
        return (p1, p2, p3)
            
    else:
        
        # Initialize all the parameters
        x, y, z = [None, None, None, None], [None, None, None, None], [None, None, None, None]
        c = [None, None, None, None, None, None]
        
        if D(d[0] - d[4] + 1, g) != 0 and D(d[0] - d[4] + 2, g) != 0:
            
            x[1] = floor( (g + d[4] - 1)/2 )
            y[1] = g + d[4] - 1 - x[1]
            z[1] = D( d[0] - d[4] + 1, g )
            
            c[1] = (x[1] + y[1] + z[1] - d[0])//g
            
            x[2] = floor( (g + d[3] - 1)/2 )
            y[2] = g + d[3] - 1 - x[2]
            z[2] = D(d[1] - x[2] - y[2] - c[1], g)
            
            c[2] = (x[2] + y[2] + z[2] + c[1] - d[1])//g
            
            x[3] = floor((g + d[2] - c[2] - z[1])/2)
            y[3] = g + d[2] - c[2] - z[1] - x[3]
            
            p1 = [0, x[1], x[2], x[3], x[2], x[1]][::-1]
            p2 = [0, y[1], y[2], y[3], y[2], y[1]][::-1]
            p3 = [0, 0, 0, z[1], z[2], z[1]][::-1]
            
            return (p1, p2, p3)
        
        
        elif D(d[0] - d[4] + 2,g) == 0 and d[2] != 0:
            x[1] = floor((g + d[4] - 1)/2)
            y[1] = g + d[4] - 1 - x[1]
            z[1] = g - 1
            
            c[1] = (x[1] + y[1] + z[1] - d[0])//g
            
            x[2] = floor((g + d[3] - 1)/2)
            y[2] = g + d[3] - 1 - x[2]
            z[2] = D(d[1] - x[2] - y[2] - c[1], g)
            
            c[2] = (x[2] + y[2] + z[2] + c[1] - d[1])//g
            
            x[3] = floor((1 + d[2] - c[2])/2)
            y[3] = 1 + d[2] - c[2] - x[3] 
            
            p1 = [0, x[1], x[2], x[3], x[2], x[1]][::-1]
            p2 = [0, y[1], y[2], y[3], y[2], y[1]][::-1]
            p3 = [0, 0, 0, z[1], z[2], z[1]][::-1]
            
            return (p1, p2, p3)
        
        
        elif D(d[0] - d[4] + 2,g) == 0 and d[2] == 0:
        
            if d[4] == 0: 
                x[2] = floor(d[3]/2)
                y[2] = d[3] - x[2]
                z[2] = D(d[1] - x[2] - y[2] - 1,g)
                c[2] = (x[2] + y[2] + z[2] + 1 - d[1])//g
                
                x[3] = floor((g - c[2] - z[2])/2)
                y[3] = g - c[2] - z[2] - x[3]
                
                p1 = [0, g-2, x[2], x[3], x[2], g-2][::-1]
                p2 = [0, 1, y[2], y[3], y[2], 1][::-1]
                p3 = [0, 0, g-1, z[2], z[2], g-1][::-1]
                
                return (p1, p2, p3)

            elif d[4] == 1:
                x[2] = floor(d[3]/2)
                y[2] = d[3] - x[2]
                z[2] = D(d[1] - x[2] - y[2] - 1,g)
                c[2] = (x[2] + y[2] + z[2] + 1 - d[1])//g
                
                x[3] = floor((g - c[2] - z[2])/2)
                y[3] = g - c[2] - z[2] - x[3]
            
                p1 = [0, g-1, x[2], x[3], x[2], g-1][::-1]
                p2 = [0, 1, y[2], y[3], y[2], 1][::-1]
                p3 = [0, 0, g-1, z[2], z[2], g-1][::-1]
                    
                return (p1, p2, p3)
                
            elif d[4] == 2:
                x[2] = floor(d[3]/2)
                y[2] = d[3] - x[2]
                z[2] = D(d[1] - x[2] - y[2] - 1,g)
                c[2] = (x[2] + y[2] + z[2] + 1 - d[1])//g
                
                if c[2] != 2:
                    x[3] = floor((g - c[2] - z[2])/2)
                    y[3] = g - c[2] - z[2] - x[3]
                
                    p1 = [0, g-1, x[2], x[3], x[2], g-1][::-1]
                    p2 = [0, 1, y[2], y[3], y[2], 1][::-1]
                    p3 = [0, 0, g-1, z[2], z[2], g-1][::-1]
                    
                    return (p1, p2, p3)
                
                else:
                    return ([1, 2, g-2, g-2, 2, 1], 
                            [1, g-3, 1, 0, 0, 0], 
                            [g-2, 0, 0, 0, 0, 0])
            
            elif d[4] >= 3:
                c[4] = (D(d[3] - 1, g) + 1 - d[3])//g
                c[1] = 1
                
                z = D(d[1] - d[3] - 1 + c[4], g)
                c[2] = (2 - c[4] + D(d[3] - 1, g) + z - d[1])//g
                
                p1 = [1, 1 - c[4], 0, 0, 1 - c[4], 1]
                p2 = [0, d[4] - 1, D(d[3] - 1, g), 2 - c[2], D(d[3] - 1, g), d[4] - 1][::-1]
                p3 = [0, 0, 0, g-2, z, g-2][::-1]
                
                return (p1, p2, p3)
       
        
        elif D(d[0] - d[4] + 1, g) == 0 and d[3] != 0:
            
            if d[4] != g - 1:
                x[1] = floor((g + d[4])/2)
                y[1] = g + d[4] - x[1]
                z[1] = g - 1
                
                c[1] = (x[1] + y[1] + z[1] - d[0])//g
                
                x[2] = floor((d[3] - 1)/2)
                y[2] = d[3] - 1 - x[2]
                z[2] = D(d[1] - x[2] - y[2] - c[1], g)
                
                c[2] = (x[2] + y[2] + z[2] + c[1] - d[1])//g
                
                x[3] = floor((1 + d[2] - c[2])/2)
                y[3] = 1 + d[2] - c[2] - x[3]
        
                p1 = [0, x[1], x[2], x[3], x[2], x[1]][::-1]
                p2 = [0, y[1], y[2], y[3], y[2], y[1]][::-1]
                p3 = [0, 0, 0, z[1], z[2], z[1]][::-1]
                
                return (p1, p2, p3)
            
            else:
                y = 3 if D(d[1] - 3 - 1, g) == g - 1 else 2 if D(d[1] - 3 - 1, g) == g - 2 else 1
                x = d[3] + g - y if d[3] < y else d[3] - y
                
                c[1] = (3 + y + D(d[1] - 3 - y, g) - d[1])//g
                u = 0
                c[2] = (x + D(d[2] - x - 1 - c[1] + u, g) + c[1] + 1 - d[2])//g
                
                if c[2] <= 1:
                    # Dont do anything
                    pass
                
                else:
                    c[2] = 1
                    u = 1
                
                c[3] = (x + y - d[3])//g
                
                p1 = [1, 3 - c[3], x - u, x - u, 3 - c[3], 1]
                p2 = [g - 4, y - c[2] + u, D(d[2] - x - 1 - c[1] + u, g), y - c[2] + u, g - 4, 0]
                p3 = [1, D(d[1] - 3 - y, g) + c[2] - u + c[3], 1, 0, 0, 0]
                
                return (p1, p2, p3)
        
        
        elif D(d[0] - d[4] + 1, g) == 0 and d[3] == 0:
            n = list_to_int(d)
            
            if d[4] == 0:
            
                if d[2] != 0:
                    s = n - 1 - g**5
                    p1, p2, p3 = find_palindromes(s, g, print_pal=False, returnAs='list')
            
                    if not any(p1): p1 = [1, 0, 0, 0, 0, 1]
                    elif not any(p2): p2 = [1, 0, 0, 0, 0, 1]
                    elif not any(p3): p3 = [1, 0, 0, 0, 0, 1]
                    
                    return (p1, p2, p3)
            
                elif d[1] != 0 and d[1] != g - 1:
                    s = n - 1 - g**5
                    p1, p2, p3 = find_palindromes(s, g, print_pal=False, returnAs='list')
            
                    if not any(p1): p1 = [1, 0, 0, 0, 0, 1]
                    elif not any(p2): p2 = [1, 0, 0, 0, 0, 1]
                    elif not any(p3): p3 = [1, 0, 0, 0, 0, 1]
                    
                    return (p1, p2, p3)
            
                elif d[1] == 0:
                    return ([1, 0, 0, 0, 0, 1], [g - 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])
            
                elif d[1] == g - 1:
                    return ([g-1, 0, 1, 0, g-1, 0], [g-1, g-2, g-2, g-1, 0, 0], [1, 0, 1, 0, 0, 0])
            
                
            elif d[4] == 1:
            
                if d[2] >= 2 or (d[2] == 1 and d[1] >= 2):
                    s = n - 1 - g - g**4 - g**5
                    p1, p2, p3 = find_palindromes(s, g, print_pal=False, returnAs='list')
            
                    if not any(p1): p1 = [1, 1, 0, 0, 1, 1]
                    elif not any(p2): p2 = [1, 1, 0, 0, 1, 1]
                    elif not any(p3): p3 = [1, 1, 0, 0, 1, 1]
                    
                    return (p1, p2, p3)
            
                elif d[2] == 1 and d[1] == 0:
                    return ([1, 0, g-1, g-1, 0, 1], [1, g-1, 1, 0,0,0], [g-2, 0,0,0,0,0])
            
                elif d[2] == d[1] == 1:
                    return ([1, 1, 0, 0, 1, 1], [g-1, g-1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] >= 2:
                    return ([1, 1, 0, 0, 1, 1], [d[1]-2, d[1]-2, 0, 0, 0, 0], [g-d[1]+1, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] == 1:
                    return ([1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0], [g-2, 0, 0, 0, 0, 0])
            
                elif d[2] == d[1] == 0:
                    return ([1, 0, 0, 0, 0, 1], [g-1, g-1, g-1, g-1, 0, 0], [0, 0, 0, 0, 0, 0])
            
            
            elif d[4] == 2:
            
                if d[2] >= 2 or (d[2] == 1 and d[1] >= 2):
                    s = n - 1 - 2*g - 2*g**4 - g**5
                    p1, p2, p3 = find_palindromes(s, g, print_pal=False, returnAs='list')
            
                    if not any(p1): p1 = [1, 2, 0, 0, 2, 1]
                    elif not any(p2): p2 = [1, 2, 0, 0, 2, 1]
                    elif not any(p3): p3 = [1, 2, 0, 0, 2, 1]
                    
                    return (p1, p2, p3)
                
                elif d[2] == 1 and d[1] == 0:
                    return ([1, 1, g-1, g-1, 1, 1], [1, g-2, 1, 0, 0, 0], [g-1, 0, 0, 0, 0, 0])
            
                elif d[2] == d[1] == 1:
                    return ([1, 1, g-1, g-1, 1, 1], [1, g-1, 1, 0, 0, 0], [g-1, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] == 3:
                    return ([1, 2, 0, 0, 2, 1], [g-1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] > 3:
                    return ([1, 2, 0, 0, 2, 1], [d[1]-3, d[1]-3, 0, 0, 0, 0], [g-d[1]+3, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] == 2:
                    return ([1, 1, g-1, g-1, 1, 1], [1, 0, 1, 0, 0, 0], [g-1, 0, 0, 0, 0, 0])
            
                elif d[2] == 0 and d[1] == 1:
                    return ([1, 0, 0, 0, 0, 1], [2, 0, 0, 0, 2, 0], [g-2, 0, 0, 0, 0, 0])
            
                elif d[2] == d[1] == 0:
                    return ([1, 1, g-1, g-1, 1, 1], [g-2, g-2, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0])
            
            
            elif d[4] == 3:
                y = 3 if D(d[1]- 1 - 1, g) == 0 else 2 if D(d[1] - 1 - 1, g) == g - 1 else 1
            
                c[1] = (2 + y - d[1] + D(d[1] - 1 - y, g))//g
                c[2] = (g - y + 1 + D(d[2] + y + 2, g) + g - 1 - d[2])//g
                
                p1 = [1, 0, g - y - c[1] - 1, g - y - c[1] - 1, 0, 1]
                p2 = [2, y - c[2] + 1 + c[1], D(d[2] + y + 2, g), y - c[2] + 1 + c[1], 2, 0]
                p3 = [g - 1, D(d[1] - 1 - y, g) + c[2] - 1 - c[1], g - 1, 0, 0 ,0]
                
                return (p1, p2, p3)
            
            
            elif d[4] >= 4:
                y = 3 if D(d[1] - 1 - 1, g) == 0 else 2 if D(d[1] - 1 - 1, g) == g - 1 else 1
            
                c[1] = (1 + y - d[1] + D(d[1] - 1 - y, g))//g
                c[2] = (g - y + 1 + D(d[2] + y - 1, g) - d[2])//g
                
                p1 = [1, 2, g - y - c[1], g - y - c[1], 2, 1]
                p2 = [d[4] - 3, y - c[2] + c[1], D(d[2] + y - 1, g), y - c[2] + c[1], d[4] - 3, 0]
                p3 = [1, D(d[1] - 2 - y, g) + c[2] - c[1], 1, 0, 0, 0]
                
                return (p1, p2, p3)
            
                


# ------------------------------------------------------------------------------------------------ #



# ALGORITHMS TO FIND PALINDROME OF GENERAL NUMBERS (LARGER THAN 6 DIGITS)

# ------------------------------------------------------------------------------------------------ #
# Decide the type of number and initialize values
def decide_type(d, p1, p2, p3, g=10):
    '''Returns the category of number and initializes p1, p2, p3(last and first digits) based on that.'''
    l = len(d)
    n_type = None
    
    if d[l-2] not in [0, 1, 2] and (z1 := D(d[0] - d[l-1] - d[l-2] + 1, g )) != 0:
        n_type  = 'A1'
        p1[l-1] = p1[0] = d[l-1]
        p2[l-2] = p2[0] = d[l-2] - 1
        p3[l-3] = p3[0] = z1
    
    elif d[l-2] not in [0, 1, 2] and D(d[0] - d[l-1] - d[l-2] + 1, g ) == 0:
        n_type  = 'A2'
        p1[l-1] = p1[0] = d[l-1]
        p2[l-2] = p2[0] = d[l-2] - 2
        p3[l-3] = p3[0] = 1
        
    elif d[l-2] in [0, 1, 2] and (d[l-1] != 1) and (z1 := D(d[0] - d[l-1] + 2, g )) != 0:
        n_type  = 'A3'
        p1[l-1] = p1[0] = d[l-1] - 1
        p2[l-2] = p2[0] = g - 1
        p3[l-3] = p3[0] = z1
    
    elif d[l-2] in [0, 1, 2] and (d[l-1] != 1) and D(d[0] - d[l-1] + 2, g) == 0:
        n_type  = 'A4'
        p1[l-1] = p1[0] = d[l-1] - 1
        p2[l-2] = p2[0] = g - 2
        p3[l-3] = p3[0] = 1
    
    elif d[l-1] == 1 and d[l-2] == 0 and d[l-3] <= 3 and (z1:= D(d[0] - d[l-3], g)) != 0:
        n_type  = 'A5'
        p1[l-2] = p1[0] = g - 1
        p2[l-3] = p2[0] = d[l-3] + 1
        p3[l-4] = p3[0] = z1

    elif d[l-1] == 1 and d[l-2] == 0 and d[l-3] <= 2 and D(d[0] - d[l-3], g) == 0:
        n_type  = 'A6'
        p1[l-2] = p1[0] = g - 1
        p2[l-3] = p2[0] = d[l-3] + 2
        p3[l-4] = p3[0] = g - 1
    
    
    elif d[l-1] == 1 and d[l-2] <= 2 and d[l-3] >= 4 and (z1:= D(d[0] - d[l-3], g)) != 0:
        n_type  = 'B1'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = d[l-3] - 1
        p3[l-4] = p3[0] = z1
    
    elif d[l-1] == 1 and d[l-2] <= 2 and d[l-3] >= 3 and D(d[0] - d[l-3], g) == 0:
        n_type  = 'B2'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = d[l-3] - 2
        p3[l-4] = p3[0] = 1
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [0, 1] and d[0] == 0:
        n_type  = 'B3'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2] - 1
        p2[l-3] = p2[0] = g - 2
        p3[l-4] = p3[0] = 1
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [2, 3] and d[0] == 0:
        n_type  = 'B4'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = 1
        p3[l-4] = p3[0] = g - 2  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [0, 1, 2] and (z1 := d[0]) != 0:
        n_type  = 'B5'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2] - 1
        p2[l-3] = p2[0] = g - 1
        p3[l-4] = p3[0] = z1  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] == 3 and (z1 := D(d[0]-3, g)) != 0:
        n_type  = 'B6'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = 2
        p3[l-4] = p3[0] = z1  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] == 3 and d[0] == 3:
        n_type  = 'B7'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = 1
        p3[l-4] = p3[0] = 1  
    
    
    if n_type == None:
        raise ValueError("Something unexpected happened. We might need to rectify code.")
    else:
        return (n_type, p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# Algorithm-1
def algorithm_1(d, p1, p2, p3, m, l, g=10):
    # Optional Prompt for algo stage.
    print("You are currently being processed through Algorithm 1")
    
    
    # Initialize the x, y, z arrays and carry over arrays.
    x, y, z = [None, p1[0]], [None, p2[0]], [None, p3[0]]
    c = [None, (x[1] + y[1] + z[1])//g]
    
    
    # Add the next value of x, y, z and carry
    if z[1] <= d[2*m - 2] - 1:
        x.append(D(d[2*m - 1] - y[1], g))
    elif z[1] >= d[2*m - 2]:
        x.append(D(d[2*m - 1] - y[1] - 1, g))
        
    y.append(D(d[2*m - 2] - z[1] - 1, g))
    z.append(D(d[1] - x[2] - y[2] - c[1], g))
    
    c.append((x[2] + y[2] + z[2] + c[1] - d[1])//g)
    
    # Next all insertions are iterative
    for i in range(3, m + 1):
        x.append(1 if (z[i - 1] <= d[2*m - i] - 1) else 0)
        y.append(D(d[2*m - i] - z[i - 1] - 1, g))
        z.append(D(d[i - 1] - x[i] - y[i] - c[i - 1], g))
        
        c.append((x[i] + y[i] + z[i] + c[i - 1] - d[i - 1])//g)
    
    
    x.append(0)
    
    # Adjustment Step
    if c[m] == 1: 
        # No adjustment is needed
        pass
    
    elif c[m] == 0:
        x[m + 1] = 1
        
    elif c[m] == 2:
        if z[m] != g - 1:
            y[m] -= 1
            z[m] += 1
        else:
            x[m + 1] = 1
            y[m] -= 1
            z[m] = 0
            
    # Put the values of x,y,z in p1, p2, p3 repectively
    for i in range(1, m + 1):
        p1[i - 1] = p1[2*m + 1 - i] = x[i]
        p2[i - 1] = p2[2*m - i] = y[i]
        p3[i - 1] = p3[2*m - 1 - i] = z[i]
        
        
    p1[m] = x[m + 1]
    
    
    # Note that: x, y, z are all arrays of size m while p1, p2, p3 are of size 2*m or 2*m+1. 
    # We can avoid the use of x,y,z in above function and directly assign to p1, p2, p3 but 
    # we will have to assign it to complement as well (i --> 2*m -i) which will make the code clumsy
    
    
    # Writing Results in File for analysis
    with open('./additionals/results.txt', 'a') as file:
        try:
            separator = '\n---------------------------\n'
            string = f'Algorithm: 1\nNumber array reversed: {d}\nActual Number: {d[::-1]}\nx: {x}\nP1: {p1}\ny: {y}\nP2: {p2}\nz: {z}\nP3: {p3}\nm(length of subarray x,y,z): {m}\t\tl(length of number): {l}\t\tbase: {g}'
            
            stringToAdd = separator + string + separator
            file.write(stringToAdd)
        
        except Exception:
            raise EOFError("File Doesn't exist")
            #raise ValueError("Something went wrong")

        finally:
            file.close()       
    
    
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-2
def algorithm_2(d, p1, p2, p3, m, l, g=10):
    # Optional Prompt for algo stage.
    print("You are currently being processed through Algorithm 2")
    
    
    # Initialize the x, y, z arrays and carry over arrays.
    x, y, z = [None, p1[0]], [None, p2[0]], [None, p3[0]]
    c = [None, (x[1] + y[1] + z[1])//g]
    
    # Add the next value of x, y, z and carry
    if z[1] <= d[2*m - 3] - 1:
        x.append(D(d[2*m - 2] - y[1], g))
    elif z[1] >= d[2*m - 3]:
        x.append(D(d[2*m - 2] - y[1] - 1, g))
        
    y.append(D(d[2*m - 3] - z[1] - 1, g))
    z.append(D(d[1] - x[2] - y[2] - c[1], g))
    
    c.append((x[2]+y[2]+z[2]+c[1]-d[1])//g)
    
    # Next all insertions are iterative
    for i in range(3, m):
        x.append(1 if (z[i - 1] <= d[2*m - i - 1] - 1) else 0)
        y.append(D(d[2*m - i - 1] - z[i - 1] - 1, g))
        z.append(D(d[i - 1] - x[i] - y[i] - c[i - 1], g))
        
        c.append((x[i] + y[i] + z[i] + c[i - 1] - d[i - 1])//g)
    
    x.append(0)
    y.append(D(d[m - 1] - z[m - 1] - c[m - 1], g))
    
    c.append((x[m] + y[m] + z[m - 1] + c[m - 1] - d[m - 1])//g)
    
    # Adjustment Step
    if c[m] == 1: 
        # No adjustment is needed
        pass
    
    elif c[m] == 0:
        if y[m] != 0:
            x[m] = 1
            y[m] -= 1
        
        else:
            if y[m - 1] != 0:
                x[m] = 1
                y[m] = g - 2
                y[m - 1] -= 1
                z[m - 1] += 1 
            
            elif y[m - 1] == 0 and z[m - 1] != 0:
                y[m - 1] = 1
                y[m] = 1
                z[m - 1] -= 1
            
            elif y[m - 1] == 0 and z[m - 1] == 0:
                x[m - 1] -= 1
                x[m] = 1
                y[m - 1] = g - 1
                y[m] = g - 4
                z[m - 1] = 2
        
    elif c[m] == 2:
        y[m - 1] -= 1
        y[m] = g - 2
        x[m] = 1
        z[m - 1] = 0
        
            
    # Put the values of x,y,z in p1, p2, p3 repectively
    for i in range(1, m):
        p1[i - 1] = p1[2*m - i] = x[i]
        p2[i - 1] = p2[2*m - i - 1] = y[i]
        p3[i - 1] = p3[2*m - i - 2] = z[i]
      
        
    p1[m] = x[m]
    p1[m - 1] = x[m]
    p2[m - 1] = y[m]
    
    
    # Writing Results in File for analysis
    with open('./additionals/results.txt', 'a') as file:
        try:
            separator = '\n---------------------------\n'
            string = f'Algorithm: 2\nNumber array reversed: {d}\nActual Number: {d[::-1]}\nx: {x}\nP1: {p1}\ny: {y}\nP2: {p2}\nz: {z}\nP3: {p3}\nm(length of subarray x,y,z): {m}\t\tl(length of number): {l}\t\tbase: {g}'
            
            stringToAdd = separator + string + separator
            file.write(stringToAdd)
        
        except Exception:
            raise EOFError("File Doesn't exist")
            #raise ValueError("Something went wrong")

        finally:
            file.close()    
    
    
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-3
def algorithm_3(d, p1, p2, p3, m, l, g=10):
    # Optional Prompt for algo stage.
    print("You are currently being processed through Algorithm 3")
    
    
    # Initialize the x, y, z arrays and carry over arrays.
    x, y, z = [None, p1[1]], [None, p2[0]], [None, p3[0]]
    c = [None, (1 + y[1] + z[1])//g]
    
    # Add the next value of x, y, z and carry
    if z[1] <= d[2*m - 3] - 1:  x.append(D(d[2*m - 2] - y[1], g))
    else:    x.append(D(d[2*m - 2] - y[1] - 1, g))
        
    y.append(D(d[2*m - 3] - z[1] - 1, g))
    z.append(D(d[1] - x[1] - y[2] - c[1], g))
    
    c.append((x[1] + y[2] + z[2] + c[1] - d[1])//g)
    
    # Next all insertions are iterative
    for i in range(3, m):
        x.append(1 if (z[i - 1] <= d[2*m - i - 1] - 1) else 0)
        y.append(D(d[2*m - i - 1] - z[i - 1] - 1, g))
        z.append(D(d[i - 1] - x[i - 1] - y[i] - c[i - 1], g))
        
        c.append((x[i - 1] + y[i] + z[i] + c[i - 1] - d[i - 1])//g)
    
    x.append(0)
    y.append(D(d[m - 1] - z[m - 1] - x[m - 1] - c[m - 1], g))
    
    c.append((x[m - 1] + y[m] + z[m - 1] + c[m - 1] - d[m - 1])//g)
    
    # Adjustment Step
    if c[m] == 1: 
        # No adjustment is needed
        pass
    
    
    elif c[m] == 0:
        x[m] = 1
      
        
    elif c[m] == 2:
        if y[m - 1] != 0 and z[m - 1] != g - 1:
            y[m - 1] -= 1
            y[m] -= 1
            m[m - 1] += 1
        
        elif y[m - 1] != 0 and z[m - 1] == g - 1:
            x[m] = 1
            y[m - 1] -= 1
            z[m - 1] = 0
        
        elif y[m - 1] == 0 and z[m - 1] != g - 1:
            x[m - 1] -= 1
            y[m - 1] = g - 1
            y[m] -= 1
            z[m - 1] += 1
            
        elif y[m - 1] == 0 and z[m - 1] == g - 1:
            x[m - 1] -= 1
            x[m] = 1
            y[m - 1] = g - 1
            z[m - 1] = 0
             
    # Put the values of x,y,z in p1, p2, p3 repectively
    for i in range(1, m):
        p1[i] = p1[2*m - i] = x[i]
        p2[i - 1] = p2[2*m - i - 1] = y[i]
        p3[i - 1] = p3[2*m - i - 2] = z[i]
        
    p1[m] = x[m]
    p2[m - 1] = y[m]
    
    
    # Writing Results in File for analysis
    with open('./additionals/results.txt', 'a') as file:
        try:
            separator = '\n---------------------------\n'
            string = f'Algorithm: 3\nNumber array reversed: {d}\nActual Number: {d[::-1]}\nx: {x}\nP1: {p1}\ny: {y}\nP2: {p2}\nz: {z}\nP3: {p3}\nm(length of subarray x,y,z): {m}\t\tl(length of number): {l}\t\tbase: {g}'
            
            stringToAdd = separator + string + separator
            file.write(stringToAdd)
        
        except Exception:
            raise EOFError("File Doesn't exist")
            #raise ValueError("Something went wrong")

        finally:
            file.close()    
    
        
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-4
def algorithm_4(d, p1, p2, p3, m, l, g=10):
    # Optional Prompt for algo stage.
    print("You are currently being processed through Algorithm 4")
    
    # Initialize the x, y, z arrays and carry over arrays.
    x, y, z = [None, p1[1]], [None, p2[0]], [None, p3[0]]
    c = [None, (1 + y[1] + z[1])//g]
    
    # Add the next value of x, y, z and carry
    if z[1] <= d[2*m - 4] - 1:  x.append(D(d[2*m - 3] - y[1], g))
    elif z[1] >= d[2*m - 4]:    x.append(D(d[2*m - 3] - y[1] - 1, g))
        
    y.append(D(d[2*m - 4] - z[1] - 1, g))
    z.append(D(d[1] - x[1] - y[2] - c[1], g))
    
    c.append((x[1] + y[2] + z[2] + c[1] - d[1])//g)
    
    
    # Next all insertions are iterative
    for i in range(3, m - 1):
        
        x.append(1 if (z[i - 1] <= d[2*m - i - 2] - 1) else 0)
        y.append(D(d[2*m - i - 2] - z[i - 1] - 1, g))
        z.append(D(d[i - 1] - x[i - 1] - y[i] - c[i - 1], g))
        
        c.append((x[i - 1] + y[i] + z[i] + c[i - 1] - d[i - 1])//g)
      
        
    x.append(1 if z[m - 2] <= d[m - 1] - 1 else 0)
    y.append(D(d[m - 1] - z[m - 2] - 1, g))
    z.append(D(d[m - 2] - x[m - 2] - y[m - 1] - c[m - 2], g))
    
    c.append((x[m - 2] + y[m - 1] + z[m - 1] + c[m - 2] - d[m - 2])//6)
    
    # Adjustment Step
    if x[m-1] + c[m-1] == 1:
        pass
        # We dont do anything
    
    elif x[m - 1] + c[m - 1] == 0 and y[m - 1] != g - 1:
        
        if z[m - 1] != 0:
            y[m - 1] += 1
            z[m - 1] -= 1
        
        elif z[m - 1] == 0 and y[m - 2] != 0:
            
            if y[m - 1] != 1 and z[m - 2] != g - 1:
                x[m - 1] = 1
                y[m - 2] -= 1
                y[m - 1] -= 1
                z[m - 2] += 1
                z[m - 1] = 1
            
            elif y[m - 1] != 1 and z[m - 2] == g - 1:
                x[m - 1] = 2
                y[m - 2] -= 1
                y[m - 1] -= 2
                z[m - 2] = 0
                z[m - 1] = 3
            
            elif y[m - 1] == 1:
                x[m - 1] = 1
                y[m - 2] -= 1
                y[m - 1] = g - 1
                z[m - 2] = 0
                z[m - 1] = 3
        
        elif z[m - 1] == 0 and y[m - 2] == 0:
            
            if z[m - 2] != g - 1:
                x[m - 2] -= 1
                x[m - 1] = 1
                y[m - 2] = g - 1 
                y[m - 1] -= 1
                z[m - 2] += 1
                z[m - 1] = 1
            
            elif z[m - 2] == g - 1 and y[m - 1] != 1:
                x[m - 2] -= 1
                x[m - 1] = 2
                y[m - 2] = g - 1
                y[m - 1] -= 2
                z[m - 2] = 0
                z[m - 1] = 3
            
            elif z[m - 2] == g - 1 and y[m - 1] == 1:
                x[m - 2] -= 1
                x[m - 1] = 1
                y[m - 2] = g - 1
                y[m - 1] = g - 1
                z[m - 2] = 0
                z[m - 1] = 3
    
    
    elif x[m - 1] + c[m - 1] == 0 and y[m - 1] == g - 1:
        x[m - 1] = 1
        y[m - 2] -= 1
        y[m - 1] = g - 2
        z[m - 2] += 1
        z[m - 1] = 1
    
    
    elif x[m - 1] + c[m - 1] == 2 and x[m - 1] == 0:
        
        if z[m - 1] != g - 1:
            y[m - 1] -= 1
            z[m - 1] += 1
        
        elif z[m - 1] == g - 1 and z[m - 2] != g - 1:
            
            if y[m - 2] != 0:
                x[m - 1] = 1
                y[m - 2] -= 1
                y[m - 1] -= 2
                z[m - 2] += 1
                z[m - 1] = 1
            
            else:
                x[m - 2] -= 1
                x[m - 1] = 1
                y[m - 2] = g - 2
                y[m - 1] -= 2
                z[m - 2] += 1
                z[m - 1] = 1
        
        elif x[m-1]==g-1 and z[m-2]==g-1:
            
            if y[m - 1] not in [g - 1, g - 2]:
                
                if y[m - 2] != g - 1:
                    x[m - 2] -= 1
                    x[m - 1] = g - 2
                    y[m - 2] += 1
                    y[m - 1] += 2
                    z[m - 2] = g - 2
                    z[m - 1] = g - 2
                
                else:
                    x[m - 1] = g - 2
                    y[m - 2] = 0
                    y[m - 1] += 2
                    z[m - 2] = g - 2
                    z[m - 1] = g - 2
            
            else:
                
                if y[m - 2] >= 1:
                    x[m - 1] = 2
                    y[m - 2] -= 1
                    y[m - 1] -= 3
                    z[m - 2] = 0
                    z[m - 1] = 3
                
                else:
                    x[m - 2] -= 1
                    x[m - 1] = 2
                    y[m - 2] = g - 1
                    y[m - 1] -= 3
                    z[m - 2] = 0
                    z[m - 1] = 3
                
                
    elif x[m - 1] + c[m - 1] == 2 and x[m - 1] == 1:
        
        if z[m-1]!=g-1 and y[m-1]!=0:
            y[m-1]-=1
            z[m-1]+=1
        
        
        elif z[m - 1] != g - 1 and y[m - 1] == 0:
            x[m - 1] = 1
            y[m - 1] = g - 1
            z[m - 1] += 1
        
        
        elif z[m - 1] == g - 1 and z[m - 2] != 0:
            
            if y[m - 2] != g - 1:
                x[m - 1] = 0
                y[m - 2] += 1
                y[m - 1] += 1
                z[m - 2] -= 1
                z[m - 1] = g - 2
            
            elif y[m - 2] == g - 1 and y[m - 1] not in [0, 1]:
                x[m - 1] = 2
                y[m - 2] = g - 2
                y[m - 1] -= 2
                z[m - 2] += 1
                z[m - 1] = 1
            
            elif y[m - 2] == g - 1 and y[m - 1] == 0:
                y[m - 2] = g - 2
                y[m - 1] = g - 2
                z[m - 2] += 1
                z[m - 1] = 1
            
            elif y[m - 2] == g - 1 and y[m - 1] == 1:
                y[m - 2] = g - 2
                y[m - 1] = g - 1
                z[m - 2] += 1
                z[m - 1] = 1
        
        
        elif z[m - 1] == g - 1 and z[m - 2] == 0 and y[m - 2] != 0:
            
            if y[m - 1] not in [0, 1]:
                x[m - 1] = 2
                y[m - 2] -= 1
                y[m - 1] -= 2
                z[m - 2] = 1
                z[m - 1] = 1
            
            elif y[m -1] == 0:
                y[m - 2] -= 1
                y[m - 1] = g - 2
                z[m - 2] = 1
                z[m - 1] = 1
            
            else:
                y[m - 2] -= 1
                y[m - 1] = g - 1
                z[m - 2] = 1
                z[m - 2] = 1
                
                
        elif z[m - 1] == g - 1 and z[m - 2] == 0 and y[m - 2] == 0:
            
            if y[m - 1] not in [0, 1]:
                x[m - 1] = 2
                x[m - 2] -= 1
                y[m - 2] = g - 1
                y[m - 1] -= 2
                z[m - 2] = 1
                z[m - 1] = 1
                
            elif y[m - 1] == 0:
                x[m - 2] -= 1
                y[m - 2] = g - 1
                y[m - 1] = g - 2
                z[m - 2] = 1 
                z[m - 1] = 1 
                
            else:
                x[m - 2] -= 1                
                y[m - 2] = g - 1
                y[m - 1] = g - 1
                z[m - 2] = 1
                z[m - 2] = 1
                
    
    elif x[m - 1] + c[m - 1] == 3:
        y[m - 1] -= 1
        z[m - 1] = 0
                    
        
    # Put the values of x,y,z in p1, p2, p3 repectively
    for i in range(1, m):
        
        p1[i]     = p1[2*m - i - 1] = x[i]
        p2[i - 1] = p2[2*m - i - 2] = y[i]
        p3[i - 1] = p3[2*m - i - 3] = z[i]
    
    
    # Writing Results in File for analysis
    with open('./additionals/results.txt', 'a') as file:
        try:
            separator = '\n---------------------------\n'
            string = f'Algorithm: 4\nNumber array reversed: {d}\nActual Number: {d[::-1]}\nx: {x}\nP1: {p1}\ny: {y}\nP2: {p2}\nz: {z}\nP3: {p3}\nm(length of subarray x,y,z): {m}\t\tl(length of number): {l}\t\tbase: {g}'
            
            stringToAdd = separator + string + separator
            file.write(stringToAdd)
        
        except Exception:
            raise EOFError("File Doesn't exist")
            #raise ValueError("Something went wrong")

        finally:
            file.close()    
    
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-5
def algorithm_5(d, p1, p2, p3, m, l, g=10):
    # Optional Prompt for algo stage.
    print("You are currently being processed through Algorithm 5")
    
    # Finding the value of n'
    s = g**m + g**(m - 1)
    sm = sm_1 = 1
    
    n = int(''.join(list(map(str, d[::-1]))))
    n_prime = n - s
    _, d_prime = find_digits_and_convert_to_list(n_prime)
    
    centre_zero = (d_prime[m]==0 or d_prime[m-1]==0)
    
    if centre_zero:
        n_prime = n - s
        sm = sm_1 = 2
        _, d_prime = find_digits_and_convert_to_list(n_prime)
    

    p1_pr, p2_pr, p3_pr = p1[:], p2[:], p3[:]
    _, p1_pr, p2_pr, p3_pr = decide_type(d_prime, p1_pr, p2_pr, p3_pr, g)
    
    even = p1_pr.__len__()%2 == 0
    
    if even:
        p1_pr, p2_pr, p3_pr = main_algorithm(d_prime, p1_pr, p2_pr, p3_pr, g)
    
    else:        
        p1_pr, p2_pr, p3_pr = algorithm_4(d_prime, p1_pr, p2_pr, p3_pr, m, l, g)
    
    
    # Actual answer is (p1'+k*s, p2', p3')
    p1_pr[m-1] += sm_1
    p1_pr[m] += sm
    
    
    # Reassign temporary variables to (p1, p2, p3)
    p1 = p1_pr[:]
    p2 = p2_pr[:]
    p3 = p3_pr[:]

    
    # Writing Results in File for analysis
    with open('./additionals/results.txt', 'a') as file:
        try:
            separator = '\n---------------------------\n'
            string = f'Algorithm: 5\nNumber array reversed: {d}\nActual Number: {d[::-1]}\nP1: {p1}\nP2: {p2}\nP3: {p3}\nm(length of subarray x,y,z): {m}\t\tl(length of number): {l}\t\tbase: {g}'
            
            stringToAdd = separator + string + separator
            file.write(stringToAdd)
        
        except Exception:
            raise EOFError("File Doesn't exist")
            #raise ValueError("Something went wrong")

        finally:
            file.close()    
    
        
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# main algorithm to break number into subcases and call Algorithm 1-5 accordingly
def main_algorithm(d, p1, p2, p3, g=10):
    
    # Decide  the type of d from [A1-A6 and B1-B7] to apply appropriate algorithm
    n_type, p1, p2, p3 = decide_type(d, p1, p2, p3, g)
    
    
    # Optional print statement for checking valid outputs
    print(f"We are considering", ''.join(list(map(str, d[::-1]))), 'for our calculations.')
    print("The subtype of your number is: ", n_type)
    
    l = len(d)
    odd = (l%2==1)
    m = l >> 1
    special = ((d[m]==0 or d[m-1]==0) and (l == 2*m))


    # Determining the Algorithm to use according to n_type, odd and special properties
    if n_type in ['A1', 'A2', 'A3', 'A4']:
        
        if odd:
            # d has odd number of digits
            p1, p2, p3 = algorithm_1(d, p1, p2, p3, m, l, g)
        
            
        elif not special:
            p1, p2, p3 = algorithm_2(d, p1, p2, p3, m, l, g)
        
            
        else:
            # d is a special number            
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
      
            
    elif n_type in ['A5', 'A6']:
        
        if not odd:
            # d has even number of digits
            p1, p2, p3 = algorithm_1(d, p1, p2, p3, m-1, l, g)
        
            
        elif not special:
            # d has odd number of digits, but is not special
            p1, p2, p3 = algorithm_2(d, p1, p2, p3, m, l, g)
        
            
        else:
            # d is a special number
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
            
            
    elif n_type in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']:
        
        if odd:
            # d has odd number of digits
            p1, p2, p3 = algorithm_3(d, p1, p2, p3, m, l, g)
        
            
        elif not special:
            # d has even digits but it is not special. (Special numbers have either of the centre digits as 0)
            p1, p2, p3 = algorithm_4(d, p1, p2, p3, m, l, g)
        
            
        else:
            # d is a special number
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
    
    
    else:
        # Number is not of any type which is solvable
        raise ValueError("The number was not categorized in any of the present distributions which could be broken to find a solution. We might need to yet consider some extreme cases.")
    
    return (p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #



# MAIN FUNCTION API TO CALCULATE PALINDROMES, ESTIMATING THE RUNTIME AND PRINT THEM IN FORMATTED WAY USING ABOVE ALGORITHMS
def find_palindromes(n, g=10, print_pal=True, returnAs='int'):

    # Calculate the number of digits and convert integer n to a list of digits
    num_digits, d = find_digits_and_convert_to_list(n)


    # Initializing all palindromes to 0.
    p1 = [0]*num_digits
    p2 = [0]*num_digits
    p3 = [0]*num_digits


    # Start the timer
    start_time = perf_counter()
    
    
    # All positive integers which have less than 7 digits:
    if num_digits < 7:

        # Base Case: First palindrome is number itself, Other two are 0.
        if num_digits == 1:
            p1[0] = d[0]


        elif num_digits == 2:
            # Lemma 4.2: All positive integers with 2 digits are sum of 2 palindromes in base g >= 5
            # except those of form n = (d+1)d, 1 <= d <= g-2 which are sum of 3 palindromes.
            p1, p2, p3 = sum_two_digits(d, p1, p2, p3, g)
            

        elif num_digits == 3:
            # Lemma 4.3: All positive integers with 3 digits are sum of 2 palindromes in base g >= 5
            # except n = 201(in any base g) which is sum of three palindromes.
            p1, p2, p3 = sum_three_digits(d, p1, p2, p3, g)
        

        elif num_digits == 4:
            # Lemma 4.4: All positive integers with four digits are sum of 3 palindromes 
            # in base g >= 5.
            p1, p2, p3 = sum_four_digits(d, p1, p2, p3, g)


        elif num_digits == 5:
            # Lemma 4.5: All positive integers with five digtis are sum of 3 palindromes.
            p1, p2, p3 = sum_five_digits(d, p1, p2, p3, g)


        elif num_digits == 6:
            # Lemma 4.6: All positive integers with six digtis are sum of 3 palindromes.
            p1, p2, p3 = sum_six_digits(d, p1, p2, p3, g)


    else:
        # Number of digits are greater than 7. So, we use general algorithm.
        p1, p2, p3 = main_algorithm(d, p1, p2, p3, g)
        

    # end the timer
    end_time = perf_counter()
    time_elapsed = end_time - start_time 
    
    
    # We print the numbers in appropriate format. e.g. [1, 4, 5] will represent number 541 and not 145.
    def print_palindromes():
        
        # Remove the zeroes that are not of any value
        p1_c = remove_trailing_zeros(p1[:])
        p2_c = remove_trailing_zeros(p2[:])
        p3_c = remove_trailing_zeros(p3[:])
        
        print()
        print("--------------------------------------------------------------------------------------")
        print("First Palindrome: \t" ,   *p1_c[::-1] if len(p1_c) > 0 else [0],  sep='')
        print("Second Palindrome:\t" ,   *p2_c[::-1] if len(p2_c) > 0 else [0],  sep='')
        print("Third Palindrome: \t" ,   *p3_c[::-1] if len(p3_c) > 0 else [0],  sep='')
        print("--------------------------------------------------------------------------------------")
        
        sumOfNum = list_to_int(p1) + list_to_int(p2) + list_to_int(p3)
        
        print("\nSum of these palindromes: ", sumOfNum)
        print("Is Sum equal to original number? Verdict: ", sumOfNum == n)
        
        print()
        
        print(f"Total Time Elapsed:  {time_elapsed*1000:.5f} ms")
        
        print()


    if print_pal:
        print_palindromes()
    
    
    # Convert palindrome list to integers and return the time elapsed and palindromes.
    if returnAs == 'int':
        try:
            pal1 = list_to_int(p1)
        except Exception:
            pal1 = 0
        
        try:
            pal2 = list_to_int(p2)
        except Exception:
            pal2 = 0
            
        try:
            pal3 = list_to_int(p3)
        except Exception:
            pal3 = 0
            
        return (pal1, pal2, pal3, time_elapsed*1000)
    
    
    else:
        return (p1, p2, p3)



# DRIVER FUNCTION
def main():
    # Set the base.
    g = 10
    
    # Take input from user
    print("Note: If you enter decimal number, it will be truncated to an integer.\n")
    print("Please enter the number you would like to break into palindromes: ", end=' ')

    input_successful = False
    while not input_successful:
        try:
            n = int(input())

            if n < 0:
                # User entered negative number
                print("\nPlease enter a positive integer: ", end=' ')
            else:
                input_successful = True

        except ValueError:
            # User entered Alphabets 
            print("\nInvalid Input. Please enter an integer: ", end=' ')


    print(f"\nYou entered: {n}\n")


    # This will return a tuple of (pal1, pal2, pal3, time). 
    # We can store and perform calculations on it if we don't
    # want to print it in standard inbuilt way.
    find_palindromes(n, g, print_pal=True)
    
    
    return
    


# CALL DRIVER ONLY IF THIS FILE IS RAN OTHERWISE WE PERFORM AUTOMATED TESTING BY CALLING find_palindromes directly.
if __name__ == "__main__":
    main()
