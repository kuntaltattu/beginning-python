
>>> words = ["balls","cricket","football"]
>>> for i in words:
	print(words[i])

Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    print(words[i])
TypeError: list indices must be integers or slices, not str
>>> words = ["balls","cricket","football"]
>>> print (words[2])
football
>>> file = open('workfile','w')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    file = open('workfile','w')
PermissionError: [Errno 13] Permission denied: 'workfile'
>>> import math
>>> print(pi)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(pi)
NameError: name 'pi' is not defined
>>> import math'
SyntaxError: EOL while scanning string literal
>>> import math
>>> print (math.pi)
3.141592653589793
>>> print (math.delta)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (math.delta)
AttributeError: module 'math' has no attribute 'delta'
>>> import random
>>> print (random.randint(1,8))
3
>>> print (random.randit(1,1))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (random.randit(1,1))
AttributeError: module 'random' has no attribute 'randit'
>>> 
=============================== RESTART: Shell ===============================
>>> try:
	print (1/0)
	except;
	
SyntaxError: invalid syntax
>>> try:
	print (1/0)
	except:
		
SyntaxError: invalid syntax
>>> try:
	print(1/0)
   except:
	   
SyntaxError: unindent does not match any outer indentation level
>>> try:
	print (1/0)
    except:
	    
SyntaxError: unindent does not match any outer indentation level
>>> try:print(1/0)
except ZeroDivisionError:
	print ("Division by zero not possible")

	
Division by zero not possible
>>> try:
	print ("Initial line")
	print(1/0)
	print ("Line after possible error")
	print ("10"+2)
except ZeroDivisionError:
	print("Division by zzero not possible")
except:
	print ("Another error found")
finally:
	print ("This will always be printed")

	
Initial line
Division by zzero not possible
This will always be printed
>>> try:
	print ("Initial line")
	print(1/1)
	print ("Line after possible error")
	print ("10"+2)
except ZeroDivisionError:
	print("Division by zero not possible")
except:
	print ("Another error found")
finally:
	print ("This will always be printed")

	
Initial line
1.0
Line after possible error
Another error found
This will always be printed
>>> 
