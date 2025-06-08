Python Memory Management

Stack Memory: 
-Stores local variables and function calls(call frames).
-Managed by Python Intrepreter.
-Each function call creates a stack frame and when the funcion returns, the frame is destroyed.

Heap Memory:
-Managed by Python's memory manager and garbage collector.
-In python, all objects and data structres are stored in heap memory.
-In python we have two types of data types: mutable and immutable.
-Mutable data types: list, set, dict, bytearray, user-defined classes.
-Immutable data types: int, float, bool, str, tuple, frozenset, bytes.

-For optimization purpose, Python have concept of interning in which it stores the immutabe objects in a single memory and reuse them when it is needed.


