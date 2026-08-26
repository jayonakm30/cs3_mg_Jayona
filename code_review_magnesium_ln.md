# INSTRUCTIONS

| Activity 2: Code Quality Assessment  Instructions: This activity will be done in pairs.  Find your partner or work with your seatmate The activity could be found in Annex C: Code Quality Assessment Form Create a copy of the Code Quality Assessment Form in your Github portfolio and name it as code\_review\_section\_ln[.md](http://codereviewSectionLN.md)             Here are the short guides on how to use Markdown:              [https://www.markdowntutorial.com/](https://www.markdowntutorial.com/)             [https://daringfireball.net/projects/markdown/basics](https://daringfireball.net/projects/markdown/basics)             [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)             [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/) Both of you will create the .md file, but identify in the .md file who is your partner. Given two algorithms, use this worksheet to select the better solution to the problem of Searching for a Number in a Sorted List by answering the questions from 1 to 5\.  Note: Divide the assessment between your partner and then agree on the final answer on which of the two algorithms is the best. A checklist for each number is given to guide you in answering each question.   Create a [README.md](http://README.md) file (to be also uploaded in your GitHub) to have the link to your file and submit the live server link  and the .git repository link in the submission bin found in KhuB. |
| :---- |

**NOTE:** 

1. If, due to time constraints, you are unable to create and finish your Markdown file, please make a copy of this document, enter your answers, and submit it to the Activity \#2 submission bin in Khub.

2. However, I would appreciate it if you would submit a Markdown file uploaded to your GitHub repository.

# Annex C

### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: 9 Magnesium	                                                                Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name: \#23, \#26 | Jayona, Penafiel 	                                          Date: Aug. 26, 2026**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

Implementation 2 would be faster since it uses binary search. This makes it faster if ever the list is very large since it divides the list by half after each search, not needing to test every single element. Implementation 1 would require it to test each element 1 by 1, while implementation 2 is able to narrow it down to fewer options.


**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | How many elements might the algorithm need to check?  A small number of elements Does the algorithm reduce the search area as it runs?  yes Does the algorithm still work efficiently with a very large list? yes |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

Implementation 1, because its logic is simple (it starts at the beginning of the list and checks each number until it finds the target using variable i  to keep track). It also utilizes less conditions which make it simpler to look at. 

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? They clearly describe their purposes and uses. How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Implementation 1 would be slightly easier to update because linear search has a more straightforward structure. The search process is contained in a simple loop with one main condition, so the changes can be made without having to understand or modify the code and adjusting it too much.
**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?
Implementation 1 would be slightly easier to update because linear search has a more straightforward structure. The search process is contained in a simple loop with one main condition, so the changes can be made without having to understand or modify the code and adjusting it too much.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?
It should check if the given list is empty or if the input is in a valid format. Since the input involves a sorted list, it should also verify that the list is sorted before using the search algorithm. The given implementations do not include these input-validation checks, so validation would need to be added.


**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

I would personally choose Implementation 2 / Binary search for the problem of searching for a number in a sorted list since it is more efficient for a larger list because it divides the data in half with every single comparison. It jumps straight to the middle of a sorted list and discards the half that cannot contain the target.
Implementation 1 / Linear search would be more suitable with smaller lists when simplicity  and readability are more important, or when the list is guaranteed to not be sorted. Since the question is about a sorted list, binary search is the better choice especially with the larger amount of data.
