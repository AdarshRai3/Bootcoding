 Basically the difference between container and virual machine is that each virtual machine has its own operating system with it own kernel and resources are carved out from the host machine but in Docker Container resorces can be dynamically allocated and all contianers can share a common kernal.
---------------------------------------------------------------
 Kernal is the core of the operating system and it has 3 core responsibilites: 
 -Resource Management: The kernel is responsible for managing the computer's resources. This includes:   

CPU Scheduling: Deciding which programs get to use the CPU and for how long.   
Memory Management: Allocating and managing the computer's memory, ensuring that different programs don't interfere with each other's memory.   
Device Management: Communicating with and controlling hardware devices through device drivers.   
File System Management: Organizing and managing files and directories on storage devices.
Networking: Handling network communication.
 
 System Calls: The kernel provides a set of system calls, which are like special functions that user-level programs can use to request services from the kernel. For example, when you want to open a file, your application makes a system call to the kernel, and the kernel handles the interaction with the storage device.   

Security: The kernel implements security features to protect the system from unauthorized access and to ensure the integrity of data.
-------------------------------------------------------------