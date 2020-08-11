"""
Research Paper by: Javier Cilleruelo, Florian Luca, Lewis Baxter

The research paper states that every positive integer in base g >= 5 can always
be expressed as a sum of three palindromes in the same base.

Palindrome Number: A number which is same when read from left to right or right to left is a Palindrome number.
                e.g. 121 is a Palindrome number.

In this program, we will try to implement the Algorithms in that 42 page research paper and try to find the 3 palindrome numbers
that will make the number given by user as input when added.
"""

# Helper Functions
def D(number, g=10):
    '''Returns the mod(remainder) when number is divided by g(base). 
        For g=10 returns the digit at unit place'''
    result = number % g
    if result < 0:
        result += g
    return result

# Count number of digits and convert number to array of digits:
def find_digits_and_convert_to_list(n):
    num_digits = 0
    num_array = []
    while n:
        num_digits += 1
        num_array.append(n % 10)
        n = n // 10

    return (num_digits, num_array)


def find_palindromes(n, g=10):
    num_digits, d = find_digits_and_convert_to_list(n)

    # Initializing all palindromes to 0.
    p1 = [0]*num_digits
    p2 = [0]*num_digits
    p3 = [0]*num_digits


    # ------------------------------------------------------------------------------------------------ #
    def sum_two_digits(d, p1, p2, p3):

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
    def sum_three_digits(d, p1, p2, p3):

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
    def sum_four_digits(d, p1, p2, p3):
        
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
                d = 1
                for i in range(1, g-1):
                    if m == [0, 0, i+1, i]:
                        d = i
                        break
                if d[3] + d == d[0]:
                    if d[3] != 1:
                        p1 = [d[3]-1, g-2, g-2, d[3]-1]
                        p2 = [0, 1, 3, 1][::-1]
                        p3 = [0, 0, d, d][::-1]
                    else:
                        p1 = [0, g-1, g-1, g-1][::-1]
                        p2 = [0, 0, d+1, d+1][::-1]
                        p3 = [0, 0, 0, 1][::-1]

                elif d[3] + d == g + d[0]:
                    p1 = [d[3]-1, g-2, g-2, d[3]-1]
                    p2 = [0, 1, 3, 1][::-1]
                    p3 = [0, 0, d, d][::-1]
            
        elif (d[0] <= d[3] - 1) and d[3] != 1:
            p1 = [d[3]-1, g-1, g-1, d[3]-1]
            p2 = [0, 0, 0, g+d[0]-d[3]][::-1]
            p3 = [0, 0, 0, 1][::-1]
        
        elif d[::-1] == [1, 0, 0, 0]:
            p1 = [0, g-1, g-1, g-1][::-1]
            p2 = [0, 0, 0, 1][::-1]
        
        return (p1, p2, p3)
                

    # ------------------------------------------------------------------------------------------------ #

    # All positive integers which have less than 7 digits:
    if num_digits < 7:

        # Base Case: First palindrome is number itself, Other two are 0.
        if num_digits == 1:
            p1[0] = d[0]

        elif num_digits == 2:
            # Lemma 4.2: All positive integers with 2 digits are sum of 2 palindromes in base g >= 5
            # except those of form n = (d+1)d, 1 <= d <= g-2 which are sum of 3 palindromes.
            p1, p2, p3 = sum_two_digits(d, p1, p2, p3)
            

        elif num_digits == 3:
            # Lemma 4.3: All positive integers with 3 digits are sum of 2 palindromes in base g >= 5
            # except n = 201(in any base g) which is sum of three palindromes.
            p1, p2, p3 = sum_three_digits(d, p1, p2, p3)
        

        elif num_digits == 4:
            # Lemma 4.4: All positive integers with four digits are sum of 3 palindromes 
            # in base g >= 5.
            p1, p2, p3 = sum_four_digits(d, p1, p2, p3)



    else:
        # Number of digits are greater than 7. So, we use general algorithm.
        pass

    # We print the numbers in appropriate format. e.g. [1, 4, 5] will represent number 541 and not 145.
    def print_palindromes():
        print("-------------------------------------------")
        print("First Palindrome: \t" ,   *p1[::-1],  sep='')
        print("Second Palindrome:\t" ,   *p2[::-1],  sep='')
        print("Third Palindrome: \t" ,   *p3[::-1],  sep='')
        print("-------------------------------------------")

    print_palindromes()



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

    print(f"You entered: {n}")

    find_palindromes(n, g)



if __name__ == "__main__":
    main()
