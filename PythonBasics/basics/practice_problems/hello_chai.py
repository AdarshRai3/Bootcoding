print("chai & code")

def serve_chai(n):
    print(n)

serve_chai("lemon tea")

chai_one = "masala chai"
chai_two = "mint chai"

''' Inner working of python : 
  1.Compiled to bytecode(low level & platform independent)
  -Bytecode run faster

  .pyc -> compiled python(frozen Binaries)
  
  __pycache__ : folder where python stores the compiled bytecode 
  this folder has two uses : Source change and Python versioning 

  As we can see in the name of the file,
  i.e. : hello_chai.cpython-310.pyc
  - cpython : implementation of python
  -313 : version of python
  -pyc : compiled python 
  
  for source changes python uses the diffing algorithm to check the changes in the source code and then it only compiles the changed code to bytecode.

  -pyc files are for imported files only not for the top level file 
  
  -> Python -Virtual Machine(PVM): Code loop to iterate byte code
  -run time engine
  -PVM is also know as python intrepreter

  ByteCode is Not machine code
  
  -Python specific interpreteion

  -cpython is the default implementation of python

  -Other implementationof python are jython, ironpython, pypy, micropython, stackless python, etc.
   
 '''