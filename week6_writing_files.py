Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter.filedialog
>>> tkinter.filedialog.askopenfilename()
'C:/Self-eduction/Python_Coursera/week6_sample_text.txt'
>>> from_filename = tkinter.filedialog.askopenfilename()
>>> from_filename
'C:/Self-eduction/Python_Coursera/week6_sample_text.txt'
>>> to_filename = tkinter.filedialog.asksaveasfilename()
>>> to_filename
'C:/Self-eduction/Python_Coursera/week6_sample_text_copy.txt'
>>> from_file = open(from_filename, 'r')
>>> contents = from_file.read()
>>> from_file.close()
>>> contents
"Test methodologies:\n1) Equivalence Partitioning\n2) Boundary Value Analysis (BVA)\n3) Cause-Effect Graph / Decision Table\n4) Error Guessing\nError guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.\n5) Statement Coverage\n6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)\nDecision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.\nThat is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.\n7) Condition Coverage\nCondition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.\n8) Combination of Decision & Condition Coverage\n9) Multiple Condition Coverage\n"
>>> to_file = open(to_filename, 'w')
>>> to_file.write('Copy\n')
5
>>> to_file.write(contents)
1203
>>> to_file.close()
>>> to_file = open(to_filename, 'w')
>>> to_file.write("Copy\n")
5
>>> to_file.write(contents)
1203
>>> from_file.close()
>>> to_file.close()
>>> from_file=open(from_filename, 'r')
>>> contents=from_file.read()
>>> contents
"Test methodologies:\n1) Equivalence Partitioning\n2) Boundary Value Analysis (BVA)\n3) Cause-Effect Graph / Decision Table\n4) Error Guessing\nError guessing is a testing technique that makes use of a tester's skill, intuition and experience in testing similar applications to identify defects that may not be easy to capture by the more formal techniques. It is usually done after more formal techniques are completed.\n5) Statement Coverage\n6) Decision Coverage (https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm)\nDecision coverage or Branch coverage is a testing method, which aims to ensure that each one of the possible branch from each decision point is executed at least once and thereby ensuring that all reachable code is executed.\nThat is, every decision is taken each way, true and false. It helps in validating all the branches in the code making sure that no branch leads to abnormal behavior of the application.\n7) Condition Coverage\nCondition coverage is also known as Predicate Coverage in which each one of the Boolean expression have been evaluated to both TRUE and FALSE.\n8) Combination of Decision & Condition Coverage\n9) Multiple Condition Coverage\n"
>>> to_file=open(to_filename, 'w')
>>> to_file
<_io.TextIOWrapper name='C:/Self-eduction/Python_Coursera/week6_sample_text_copy.txt' mode='w' encoding='cp1252'>
>>> to_file.write('Copy\n')
5
>>> to_file
<_io.TextIOWrapper name='C:/Self-eduction/Python_Coursera/week6_sample_text_copy.txt' mode='w' encoding='cp1252'>
>>> to_file.write(contents)
1203
>>> to_filename
'C:/Self-eduction/Python_Coursera/week6_sample_text_copy.txt'
>>> to_filename.print
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    to_filename.print
AttributeError: 'str' object has no attribute 'print'
>>> to_filename.print()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    to_filename.print()
AttributeError: 'str' object has no attribute 'print'
>>> print(to_filename)
C:/Self-eduction/Python_Coursera/week6_sample_text_copy.txt
>>> to_file.write
<built-in method write of _io.TextIOWrapper object at 0x00000000045B93A8>
>>> to_file.write(contents)
1203
>>> from_file.readlines
<built-in method readlines of _io.TextIOWrapper object at 0x00000000045B9480>
