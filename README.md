# sum_of_palindromes

## How to run
**To run the console app**    
> Clone the repository or download zip.    
> Run the three_palindrome.py file using `python three_palindrome.py` command. Make sure you have python installed.    
> If you want to see the comparision. Head towards **additionals** folder and open images...    
**For running the test.py**    
> Install matplotlib module using `pip install matplotlib`    
> Run test.py using `python test.py`     
**For web version**    
> Install the required modules with `pip install -r requirements.txt`    
> Run the app.py file using `python app.py`     
> Go to browser and search `localhost:5000` or `127.0.0.1:5000`    

## Web version:
After creating the console version, I created a flask based website to give a more GUI based look to the website.
In the web version, You have to fill the input box and submit. The program will make a post request and receive the three palindromes if the input given was correct.



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
                        The time complexity of program is O(k) where k is the number of digits.

3) Static: Static folder contains the cascading style sheets and the javascript code for the web version of program. I have used SCSS and JQuery in place of vanilla JS and CSS.

4) templates: It contains the html code for the web version.

5) Additionals:
      - test.py: it imports the naive and research algorithm code and runs for n=1 to 1000 and plots the time taken by both codes. After seeing the comparision images, it is                         obvious that our algorithm is much more efficient than the brute force approach.
      - research paper.pdf : It is the research paper based on which the whole code is written

requirements: For test.py, You would want to install matplotlib but as it plots the graph for runtime vs n. But there are no requirements to run algorithm
