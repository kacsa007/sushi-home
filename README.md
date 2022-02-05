--- 0.008931398391723633 seconds ---
Although this time is not important -:> we are talking about time complexity importance when dealing with algorithms but as a reference to see

Woala I managed to do it. The avg(time) complexity is quite good. 
This app is brought to you by: Pycharm Professional with University License, and it's following strictly PEP8 ->aka OCD


The example from the PDF has a bug: 

Example 2:
• Calculate the optimized prize for the orders of Person A, B and C in Example 2 of user story 3.
Sum of per person optimized prices: 42.65 €
Optimized price: 41,65 €
Saved: 1,00 €

As you basically save nothing: 

Why? I'll explain this in the following lines
Accounting date and time: 2022-01-27 13:25
Sum of per person optimized prices: 42.65 Euro
Optimized price = 44.40 Euro
Paying together you saved: -1.75 Euro
Checking what you have ordered: {'Soup': 3, 'Grey': 4, 'Green': 6, 'Red': 5, 'Blue': 6, 'Yellow': 3}

Algorithm used to calculate the best price and the individual prices:

Split the dictionary to two dictionaries: 

{'Soup': 3,'Red': 5, 'Blue': 6} -> special dishes with menu
{'Grey': 4, 'Green': 6,'Yellow': 3} -> not so special dishes without a menu

Calculation:

In this case we know the following: we have 27 dishes - 14 menu dishes and 13 not so important dishes which can have a menu in order
We can have in this case 5 menus with 25 dishes this means the rest is 2 in our case we are going to have just 4 Blue dishes as the rests are going to be used for menu dishes

we calculate the following: 
4+6+3=>13 which is still not a multiplication of 25 the amount of dishes one can have -> so our not so important dictionary we all be 0 
we reach to the important dishes and we are using some while loops to find out how many dishes are going to be left

this can be calculated with =number of dishes-sum_of order in our case the sum of the orders from the not so important dishes 
25-13 will give us 12
And the sum of the important menu dishes is 14 and this will result in decreasing the values one by one until there's no more
not_used_this value so its zero and the program will stop at Blue and calculate 
{'Soup': 0,'Red': 0, 'Blue': 2} -> the sum accordingly -> this calculation can be optimized as I'm currently using the whole matrix sum
as I had no time to write separate sum functions for everything in particular

You can run this code: 

 python3 main.py input - where inputs are here: 
 
 1,2,2,0,2,1  -> one example

A group example where you actually save money:

1,2,2,0,2,1
0,2,2,2,2,0
2,2,2,3,2,0
Bill date and time: 2022-01-27 13:25
Sum of per person optimized prices: 48.65 Euro
Actually this is an Optimized price = 45.40 Euro
Paying together you really saved: 3.25 Euro
Checking what you have ordered: {'Soup': 3, 'Grey': 6, 'Green': 6, 'Red': 6, 'Blue': 1, 'Yellow': 5}


--- 0.009644269943237305 seconds ---


And the one where you actually dont save any money:
1,2,2,0,1,2
0,2,2,0,2,2
2,0,2,3,2,2



Bill date and time: 2022-01-27 13:25
Sum of per person optimized prices: 42.65 Euro
Actually this is not an Optimized price = 44.40 Euro
Paying together you saved NOTHING -> someone's greedy and this is a negative number: -1.75 Euro     
Checking what you have ordered: {'Soup': 3, 'Grey': 4, 'Green': 6, 'Red': 5, 'Blue': 6, 'Yellow': 3}

During my work I've encountered a lot of difficulties when solving this:
One was first I approached doing everything dynamically with one for so it will be efficient but I ended up having more complex code 
My experience with python is showing me that the more simple something is the better -> as python is not a strong OOP language using always classes should have a reason behind so 
thats why my approach is so easy rather than having abstract classes and OOP object modelling.