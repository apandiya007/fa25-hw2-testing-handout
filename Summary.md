# SUMMARY
Answer all the questions. Please put your answers *after* the italicized instructions.

## Privacy Analysis

The following table discusses the data being tested: 311 service requests. We will dive further into data analysis next week, but we can discuss the privacy of any people whose data might be in those calls. Please fill out the table. Some answers have been filled out for you.

| Question | Answer |
| -------- | ------ |
| What type of information is shared? | Personal details (names, phone numbers, emails, address), location, timestamps and descriptions of service issues. Additionally, sensitive info might be included if requesters type it in the field.|
| Who is the subject of the information? | Anybody who gives personal info while making a 311 service request |
| Who is the sender of the information? | The person whose details are included, but also the public 311 dataset publisher |
| Who are the potential recipients of the information? | Intended recipient: 311 service workers<br />Unintended recipient(s): Researchers, the general public, companies, and potentially bad actors who might misuse identifiable data |
| What principles govern the collection and transmission of the information? | 311 service requests are often the most efficient way to access necessary services, and it is possible to unintentionally leak personal info while making a request. |

[10 points]  
*Answer:*

---

## Citations 

### Who did you work with and how?   
*Discussing the assignment with people not on your team is fine as long as you don't share code.*   
*Please include any people or other sources who helped you, and any students whom you helped.*   
*For each source, make sure to include how they helped you (or how you helped them).*    
I didn't work with anyone in class at all I mostly worked by myself and if I had trouble trying to debug some code I would either watch a youtube video on it or try to google how to solve it. So Google and Youtube were my main sources of solutions. Additionally I also used Geeks for Geeks.org for simple solutions.

[1 point] 
* *"I had no idea how to approach Question 3 until classmate Alice Smith explained how I could break it down into separate functions."*   
* *"I showed Bob Lee my test-mocking approach for calculate_score; he gave me feedback on ordering the decorators."*   
* *If you did not talk to anybody about the assignment, please state that.*  

---  

### What resources did you use?   
*Please give specific URLs (not "Stack Overflow" or "Google") and state which ones were particularly helpful.*    https://www.geeksforgeeks.org/pandas/python-pandas-dataframe/ - learned how to use DataFrame for pandas correctly

[1 point] 
* *https://docs.python.org/3/library/unittest.html – for learning about `unittest.mock.patch`.*   
* *https://realpython.com/python-mock-library/ – example patterns for mocking user input.*  

---  

## Logistics 

### Did you successfully implement everything that was requested?   
*Answer "Yes", or state here which parts did not work or which tests did not pass. Be specific about any methods or test cases that are incomplete.*    

[1 point]   
*Answer:*  

### How long did the assignment take?   
*Rather than giving a range, if you are unsure, give the average of the range. Break down time spent on different parts (writing tests, implementation, debugging, documentation).*    

[1 point]   
*Answer:*  
This homework took me approximately 6 hours to complete.
- Writing and debugging Dataloader implementation ~ 2 hours
- Writing and debugging CaseSorter implementation ~ 2 hours
- Writing tests ~ 1.5 hours
- Debugging/cleanup ~ 0.5 hour
---  

## Reflections   
*Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:*   
* What was the most difficult part of the assignment?   
* What was the most rewarding part of the assignment?   
* What did you learn from this assignment?
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.    

[8 points]   
*Answer:*  
The most difficult part of this assignment was carefully debugging and writing tests for the provided buggy functions, since some of the errors were subtle and required me to have a great understanding in both the Dataloader and Casesorter logic. The most rewarding part of this assignment was seeing my test that I wrote catch some of the issues and confirming that the implementations passed most of the cases I wrote. I learned a lot about test-driven development, the importance of clear type annotations, and unit testing makes you think about edge cases like missing column and empty ranking. One suggestion I have for improving the assignment is to make Pawtograder have clear instructions on how it wants submissions to be structured, since pushing the repository has proven difficult for me and sometimes it doesn't even go through.

---

Then, please answer these two questions:
1. Who is one potential unintended recipient of this data?
One potential unintended recipient is the general public, since 311 datasets are often published openly online and can be accessed by researchers, bad actors, and even corporations.
2. How might this housing application be redesigned to minimize the number of unintended recipients of that information?
The housing application could be redesigned to automatically strip any personally identifiable information before requests are published in public datasets. It could also provide warnings about what information is necessary and what is optional.