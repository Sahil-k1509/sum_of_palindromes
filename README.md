# sum_of_palindromes


### Structure and Contents: 
1) naive_sum.py: Contains the brute force approach to calculate three palindromes such that their sum is equal to number given by user.
                  Program uses 3 nested loops to iterate over all triplets of numbers from (0,0,0) to (n,n,n) and stop when it finds the triplet such that all numbers are     
                  palindromes and sum is n. The time complexity is O(n^3) which is not very efficient. You can see the time taken by program to find triplets in comparision.png.
                  Orange line represents the time taken to find triplet for given n. It increases to great extend after n=1000.
                  We Can increase the efficiency by exploiting the fact that sum is constant by following code.        
                  ```
                  for num1 in range(n):     
                      for num2 in range(n):       
                          num3 = n - (num1 + num2)        
                          if ispalindrome(num1) and ispalindrome(num2) and ispalindromenum3):       
                              return (num1, num2, num3)
                  ```
                  
2) three_palindrom.py: It is the algorithmic implementation of _**'research_paper_3_palindrome.pdf'**_. The algorithm first classifies the given sum into cases.
                        If number given is from 2 to 6 digits, we have specific algorithms and for bigger numbers we follow a general algorithm by further breaking it
                        into different cases. Numbers are broken into 13 categories (A1-A7, B1-B6) and depending on category, One(or more) of the five algorithms are used on it.
                        We first identify the corner digits and iterate towards the center digits to get the complete number. The actual calculations can be read in research paper
                        or the program. 
                        The time complexity of program is O(k) where k is the number of digits. You can see the comparision.png to see runtime as compared to naive approach.
                        
                        
3) test.py: It imports both naive and algorithmic program and compare their runtimes and accuracy over a range of n from 1-1100.


requirements: For test.py, You would want to install matplotlib but as it plots the graph for runtime vs n. But there are no requirements to run algorithm
