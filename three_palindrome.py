"""
Research Paper by: Javier Cilleruelo, Florian Luca, Lewis Baxter

The research paper states that every positive integer in base g >= 5 can always
be expressed as a sum of three palindromes in the same base.

Palindrome Number: A number which is same when read from left to right or right to left is a Palindrome number.
                e.g. 121 is a Palindrome number.

In this program, we will try to implement the Algorithms in that 42 page research paper and try to find the 3 palindrome numbers
that will make the number given by user as input when added. The algorithm holds for any base but we will only consider base 10 
for now and extend it to other bases once we have method to check if number is of certain base or not to catch
"""



# Import modules
from time import perf_counter



# Helper Functions
# ------------------------------------------------------------------------------------------------ #
def D(number, g=10):
    '''Returns the mod(remainder) when number is divided by g(base). 
        For g=10 returns the digit at unit place'''
    result = number % g
    if result < 0:
        result += g
    return result


def find_digits_and_convert_to_list(n):
    '''Count number of digits and convert number to array of digits.'''
    num_digits = 0
    num_array = []
    while n:
        num_digits += 1
        num_array.append(n % 10)
        n = n // 10

    return (num_digits, num_array)


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

        elif any([(m == [0, 0, x+1, x]) for x in range(1, g-1)]):
            d0 = 1
            for i in range(1, g-1):
                if m == [0, 0, i+1, i]:
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



# ALGORITHMS TO FIND PALINDROME OF GENERAL NUMBERS (LARGER THAN 6 DIGITS)

# ------------------------------------------------------------------------------------------------ #
# Decide the type of number and initialize values
def decide_type(d, p1, p2, p3, g=10):
    '''Returns the category of number and initializes p1, p2, p3(last and first digits) based on that.'''
    l = len(d)
    n_type = None
    
    if d[l-2] not in [0, 1, 2] and (z1 := D(d[0]-d[l-1]-d[l-2]+1, g))!=0:
        n_type = 'A1'
        p1[l-1] = p1[0] = d[l-1]
        p2[l-2] = p2[0] = d[l-2] - 1
        p3[l-3] = p3[0] = z1
    
    elif d[l-2] not in [0, 1, 2] and D(d[0]-d[l-1]-d[l-2]+1, g) == 0:
        n_type = 'A2'
        p1[l-1] = p1[0] = d[l-1]
        p2[l-2] = p2[0] = d[l-2] - 2
        p3[l-3] = p3[0] = 1
        
    elif d[l-2] in [0, 1, 2] and (d[l-1] != 1) and (z1 := D(d[0]-d[l-1]+2, g))!=0:
        n_type = 'A3'
        p1[l-1] = p1[0] = d[l-1]-1
        p2[l-2] = p2[0] = g-1
        p3[l-3] = p3[0] = z1
    
    elif d[l-2] in [0, 1, 2] and (d[l-1] != 1) and D(d[0]-d[l-1]+2, g)==0:
        n_type = 'A4'
        p1[l-1] = p1[0] = d[l-1]-1
        p2[l-2] = p2[0] = g-2
        p3[l-3] = p3[0] = 1
    
    elif d[l-1]==1 and d[l-2]==0 and d[l-3]<=3 and (z1:= D(d[0]-d[l-3], g))!=0:
        n_type = 'A5'
        p1[l-2] = p1[0] = g-1
        p2[l-3] = p2[0] = d[l-3] + 1
        p3[l-4] = p3[0] = z1

    elif d[l-1]==1 and d[l-2]==0 and d[l-3]<=2 and D(d[0]-d[l-3], g)==0:
        n_type = 'A6'
        p1[l-2] = p1[0] = g-1
        p2[l-3] = p2[0] = d[l-3] + 2
        p3[l-4] = p3[0] = g-1
    
    
    elif d[l-1] == 1 and d[l-2]<=2 and d[l-3]>=4 and (z1:= D(d[0]-d[l-3], g)!=0):
        n_type = 'B1'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = d[l-3]-1
        p3[l-4] = p3[0] = z1
    
    elif d[l-1] == 1 and d[l-2]<=2 and d[l-3]>=3 and D(d[0]-d[l-3], g)==0:
        n_type = 'B2'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = d[l-3]-2
        p3[l-4] = p3[0] = 1
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [0, 1] and d[0] == 0:
        n_type = 'B3'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2] - 1
        p2[l-3] = p2[0] = g - 2
        p3[l-4] = p3[0] = 1
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [2, 3] and d[0] == 0:
        n_type = 'B4'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = 1
        p3[l-4] = p3[0] = g - 2  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3] in [0, 1, 2] and (z1 := d[0]) != 0:
        n_type = 'B5'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2] - 1
        p2[l-3] = p2[0] = g - 1
        p3[l-4] = p3[0] = z1  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3]==3 and (z1 := D(d[0]-3, g)) != 0:
        n_type = 'B6'
        p1[l-1] = p1[0] = 1
        p1[l-2] = p1[1] = d[l-2]
        p2[l-3] = p2[0] = 2
        p3[l-4] = p3[0] = z1  
    
    elif d[l-1] == 1 and  d[l-2] in [1, 2] and d[l-3]==3 and d[0]==3:
        n_type = 'B7'
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
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-2
def algorithm_2(d, p1, p2, p3, m, l, g=10):
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-3
def algorithm_3(d, p1, p2, p3, m, l, g=10):
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-4
def algorithm_4(d, p1, p2, p3, m, l, g=10):
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Algorithm-5
def algorithm_5(d, p1, p2, p3, m, l, g=10):
    return (p1, p2, p3)
# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# main algorithm to break number into subcases and call Algorithm 1-5 accordingly
def main_algorithm(d, p1, p2, p3, g=10):
    n_type, p1, p2, p3 = decide_type(d, p1, p2, p3, g)
    
    l = len(d)
    odd = (l%2==1)
    m = l >> 1
    special = ((d[m]==0 or d[m-1]==0) and (l == 2*m))

    # Determining the Algorithm to use according to n_type, odd and special properties
    if n_type in ['A1', 'A2', 'A3', 'A4']:
        if odd:
            p1, p2, p3 = algorithm_1(d, p1, p2, p3, m, l, g)
            
        elif not special:
            p1, p2, p3 = algorithm_2(d, p1, p2, p3, m, l, g)
            
        else:
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
      
            
    elif n_type in ['A5', 'A6']:
        if not odd:
            p1, p2, p3 = algorithm_1(d, p1, p2, p3, m-1, l, g)
            
        elif not special:
            p1, p2, p3 = algorithm_2(d, p1, p2, p3, m, l, g)
            
        else:
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
            
            
    elif n_type in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']:
        if odd:
            p1, p2, p3 = algorithm_3(d, p1, p2, p3, m, l, g)
            
        elif not special:
            p1, p2, p3 = algorithm_4(d, p1, p2, p3, m, l, g)
            
        else:
            p1, p2, p3 = algorithm_5(d, p1, p2, p3, m, l, g)
    
    
    else:
        # Number is not of any type which is solvable
        raise ValueError("The number was not categorized in any of the present distributions which could be broken to find a solution. We might need to yet consider some extreme cases.")
    
    return (p1, p2, p3)

# ------------------------------------------------------------------------------------------------ #



# MAIN FUNCTION API TO CALCULATE PALINDROMES, ESTIMATING THE RUNTIME AND PRINT THEM IN FORMATTED WAY USING ABOVE ALGORITHMS
def find_palindromes(n, g=10, print_pal=True):
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



    else:
        # Number of digits are greater than 7. So, we use general algorithm.
        p1, p2, p3 = main_algorithm(d, p1, p2, p3, g)
        

    # end the timer
    end_time = perf_counter()
    time_elapsed = end_time - start_time 
    
    # We print the numbers in appropriate format. e.g. [1, 4, 5] will represent number 541 and not 145.
    def print_palindromes():
        
        # Remove the zeroes that are not of any value
        p1_c = remove_trailing_zeros(p1)
        p2_c = remove_trailing_zeros(p2)
        p3_c = remove_trailing_zeros(p3)
        
        print("-------------------------------------------")
        print("First Palindrome: \t" ,   *p1_c[::-1] if len(p1_c) > 0 else [0],  sep='')
        print("Second Palindrome:\t" ,   *p2_c[::-1] if len(p2_c) > 0 else [0],  sep='')
        print("Third Palindrome: \t" ,   *p3_c[::-1] if len(p3_c) > 0 else [0],  sep='')
        print("-------------------------------------------")
        print(f"Total Time Elapsed:  {time_elapsed*1000:.5f} ms")

    if print_pal:
        print_palindromes()
    
    # Convert palindrome list to integers and return the time elapsed and palindromes.
    try:
        pal1 = int( ''.join( list( map( str, p1[::-1] ) ) ) )
    except Exception:
        pal1 = 0
    
    try:
        pal2 = int( ''.join( list( map( str, p2[::-1] ) ) ) )
    except Exception:
        pal2 = 0
        
    try:
        pal3 = int( ''.join( list( map( str, p3[::-1] ) ) ) )
    except Exception:
        pal3 = 0
        
        
    return (pal1, pal2, pal3, time_elapsed*1000)




# DRIVER FUNCTION
def main():
    # Set the base.
    g = 10

    # Take input from user
    print("Note: If you enter decimal number, it will be truncated to an integer.")
    print("Please enter the number you would like to break into palindromes: ", end=' ')

    input_successful = False
    while not input_successful:
        try:
            n = int(input())

            if n < 0:
                # User entered negative number
                print("Please enter a positive integer: ", end=' ')
            else:
                input_successful = True

        except ValueError:
            # User entered Alphabets 
            print("Invalid Input. Please enter an integer: ", end=' ')

    print(f"\nYou entered: {n}")

    # This will return a tuple of (pal1, pal2, pal3, time). 
    # We can store and perform calculations on it if we don't
    # want to print it in standard inbuilt way.
    find_palindromes(n, g, print_pal=True)
    
    


# CALL DRIVER ONLY IF THIS FILE IS RAN OTHERWISE WE PERFORM AUTOMATED TESTING BY CALLING find_palindromes directly.
if __name__ == "__main__":
    main()
