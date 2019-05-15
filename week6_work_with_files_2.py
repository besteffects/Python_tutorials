Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> filename='\Self-eduction\Python_Coursera\week6_sample_text.txt'
>>> file=open(filename, 'r')
>>> line=file.readline
>>> line= file.readline()
>>> line=file.readline()
>>> line
'1) Equivalence Partitioning\n'
>>> #while line != '\n':
	#print(line)
	#line= file.readline()
>>> #prints only what is needed and allows to stop processing when we want it
>>> # to read every line in the file do the following:
>>> for line in file:
	print(line, end = '')

2) Boundary Value Analysis (BVA)
3) Cause-Effect Graph / Decision Table
4) Error Guessing
Error guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.
5) Statement Coverage
6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)
Decision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.
That is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.
7) Condition Coverage
Condition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.
8) Combination of Decision & Condition Coverage
9) Multiple Condition Coverage
>>> #for small files use file.read() Example:
>>> print(file.read())

>>> file.close()
>>> file-open(filename, 'r')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    file-open(filename, 'r')
TypeError: unsupported operand type(s) for -: '_io.TextIOWrapper' and '_io.TextIOWrapper'
>>> file=open(filename, 'r')
>>> print(file.read())
Test methodologies:
1) Equivalence Partitioning
2) Boundary Value Analysis (BVA)
3) Cause-Effect Graph / Decision Table
4) Error Guessing
Error guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.
5) Statement Coverage
6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)
Decision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.
That is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.
7) Condition Coverage
Condition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.
8) Combination of Decision & Condition Coverage
9) Multiple Condition Coverage

>>> file.close()
>>> file=open(filename, 'r')
>>> file.readlines()
['Test methodologies:\n', '1) Equivalence Partitioning\n', '2) Boundary Value Analysis (BVA)\n', '3) Cause-Effect Graph / Decision Table\n', '4) Error Guessing\n', "Error guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.\n", '5) Statement Coverage\n', '6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)\n', 'Decision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.\n', 'That is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.\n', '7) Condition Coverage\n', 'Condition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.\n', '8) Combination of Decision & Condition Coverage\n', '9) Multiple Condition Coverage\n']
>>> #above returns a list of all the lines in the file
>>> file.close()
>>> file= open (filename, 'r')
>>> lines = file.readlines()
>>> for line in lines:
	print(line, end='')

	
Test methodologies:
1) Equivalence Partitioning
2) Boundary Value Analysis (BVA)
3) Cause-Effect Graph / Decision Table
4) Error Guessing
Error guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.
5) Statement Coverage
6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)
Decision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.
That is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.
7) Condition Coverage
Condition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.
8) Combination of Decision & Condition Coverage
9) Multiple Condition Coverage
>>> #this approach is useful if we want to keep a list around, so we can access elements of it later
>>> lines[0]
'Test methodologies:\n'
>>> 
