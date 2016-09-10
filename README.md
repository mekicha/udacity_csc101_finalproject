# udacity_csc101_finalproject
I just copied the instructions for the project from the udacity site:
https://www.udacity.com/course/viewer#!/c-cs101/l-652789146/e-714268688/m-726408569
and they are as below:

 --------------------------- 
## Intro to CS Final Project   
## Gaming Social Network       
 --------------------------- 

## Background
 ==========
 You and your friend have decided to start a company that hosts a gaming
 social network site. Your friend will handle the website creation (they know 
 what they are doing, having taken our web development class). However, it is 
 up to you to create a data structure that manages the game-network information 
 and to define several procedures that operate on the network. 

 In a website, the data is stored in a database. In our case, however, all the 
 information comes in a big string of text. Each pair of sentences in the text 
 is formatted as follows: 
 
 <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.

 For example:
 
 John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
 
 Note that each sentence will be separated from the next by only a period. There will 
 not be whitespace or new lines between sentences.
 
 Your friend records the information in that string based on user activity on 
 the website and gives it to you to manage. You can think of every pair of
 sentences as defining a user's profile.

 Consider the data structures that we have used in class - lists, dictionaries,
 and combinations of the two (e.g. lists of dictionaries). Pick one that
 will allow you to manage the data above and implement the procedures below. 

 You may assume that <user> is a unique identifier for a user. For example, there
can be at most one 'John' in the network. Furthermore, connections are not 
 symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
 connected to 'Bob'.

## Project Description
 ====================
 Your task is to complete the procedures according to the specifications below
 as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
 to define any additional helper procedures that can assist you in accomplishing 
 a task. You are encouraged to test your code by using print statements and the 
 Test Run button. 
 ----------------------------------------------------------------------------- 
