# 1) Theory Questions
1) What is a program?
   - A program is a set of instructions or orders typically in the form of a code that tells a computer what to do. 
   - A computer is able to execute those commands and translate it to source code.
2) What is the process?
   - Is when a program is being executed on a computer. Usually, one process is associated with one program.
   - But there can be one or more threads in a process.
3) What is cache?
   - Is a chip-based temporary memory storage of a computer.
   - It particularly useful when we don't want to access the main hard-dive of the computer and want to easily store data.
4) What is thread and multithreading?
    - A thread has a single sequential flow in a program whereas a multi-thread has more than one sequential flow. 
    - Multi-threading is parallel programming and can cause memory leaking therefore it's not as ideal as single threading.
    - In python, multithreading is not possible because there's a GIL. 
5) What is GIL and how does it work? 
   - GIL is global interpreter lock. It's used to prevent parallel programming and many threads running at the same time. 
   - This is because having more multi-threads will affect the memory of the program. 
   - GIL works by preventing many threads from parallel running in order to protect python objects.
6) What is Concurrency and Parallelism and what are the differences?
7) What do these stand for in programming: DRY, KISS, BDUF
   - DRY:Don’t repeat yourself
   - KISS:Keep It Simple,Stupid
   - BDUF:Big Design Up Front
8) What is Garbage collector? How does it work?
   - Garbage collector is an effecient tool in python that frees up memory storage. It works by removing/deleting unused objects.
   - The freed memory space is then re-used for new objects.
9) What are ‘deadlock’ and ‘livelock’ in a relational database?
   - A deadlock is when more than one transaction cannot progress because it relys on another to release a lock.
   - A livelock is the opposite. It does not rely on another and continues to request for access and has it denied because 
many locks are overlapping.
10) What is Flask and what can we use it for?
    - Flask is a web framework that is used in python to build web applications. Flask is generally used for backend purposes.
    - It can provide you with tools and libraries.

# 2) Discuss the difference between Python2 and Python 3?
One of the differences between python 2 and python 3 is that python 2 uses an older syntax. For example,
python 2 treat the print function as a statement whereas python 3 treats it as a function.
Another difference is the integer division function. In python 2, the dividing two integers gave an integer even when the answer was
a float. For example, in python 2, 5/4 would be 1 whereas in python 3 it would be 1.25. Another difference between the 
two pythons are the strings. In python 2, there were two string types, unicode and non-unicode.
Python 3's strings are now all unicodes by default. In conclusion, Python 3 is a more reliable and accurate version of python.
It also supports many newer libaries.

# Q5: Agile methodology, Scrum: name at least 3 types of meetings that are exercised by Agile teams and describe the 
# objective of each meeting. 
1) Scrum daily meetings
   1) These meetings are held daily, usually in the morning. The objective of these meetings is to see what the team members
   accomplised the day before and what they will be working on that day.
2) Scrum sprint meeting
   1) These happen in the beginning of a sprint and everyone involved is present. The scrum master will set the ojectives,
   sprint backlogs and ensure that everyone has a task and knows what they are doing. 
3) Scrum retrospective meeting
   1) These take place after a sprint and it's used to assess what when wrong/right during the sprint. The aim is to
   improve the performance the next time a spint happens.
   
# Q6: Exception handling in Python, explain what each of the following blocks means in the program flow:
1) Try: A block of code is ran using try. This could be anything.
2) Except: when the block of code runs into an error, except lets you handle it by preventing an error from occuring.
3) Else: if the block of code does not run into an error, it will continue to execute the code.
4) Finally: this part of the code will run regardless if the code result. 

# Q7:How can we connect a Python program (process) with a database? Explain how it works and how do we fetch / insert data 
# into DB tables from a python program.
On python professional, we can use the big data tool to connect python with mySQL databases. However, for community 
python, we manually connect to mySQL. This is done by creating a new file and importing mysql.connector. For example the 
below function is used. In a new file, add your user, password and host. Once this is done, python is then connected to 
mySQL. Any database that is stored on mySQL can be fetched once this is done.
def connect_to_db(db_name=str):
    cnx = mysql.connector.connect(host=HOST,
                              user=USER,
                              PASSWORD=PASSWORD,
                              auth_plugin='mysql_native_password',
                              database='tests')
    return cnx
   
