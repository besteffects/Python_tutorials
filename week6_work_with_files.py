Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> filename='\Self-eduction\Python_Coursera\week6_sample_text.txt'
>>> file=open(filename, 'r')
>>> file.readline()
'Test methodologies:\n'
>>> file.close()
>>> filename='\Self-eduction\Python_Coursera\week6_sample_text.txt'
>>> file=open(filename, 'r')
>>> while line!='':
	print(line)
	line.file.readline()

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    while line!='':
NameError: name 'line' is not defined
>>> line=file.readline()
>>> while line!='':
	print(line)
	line.file.readline()

	
Test methodologies:

Traceback (most recent call last):
  File "<pyshell#12>", line 3, in <module>
    line.file.readline()
AttributeError: 'str' object has no attribute 'file'
>>> while line !='':
	print(line)
	line.file.readline()

	
Test methodologies:

Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    line.file.readline()
AttributeError: 'str' object has no attribute 'file'
>>> file.close()
>>> file=open(filename, 'r')
>>> line = file.readline()
>>> while line !='':
	print(line)
	line=file.readline()

	
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
>>> line=file.readline()
>>> while line != '':
	print(line, end = '')
	line=file.readline()

	
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
>>> line = file.readline()
>>> line=
SyntaxError: invalid syntax
>>> line
'Test methodologies:\n'
>>> 
