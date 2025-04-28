 Docker is plaform that use containerization technology to package applications and their dependencies into a single unit called a container.This allows developers to build,ship and run applications in a consistant environment, regardless of the underlying infrastructure. Docker containers are lightweight, virual isolated environments that share the host operating system's kernel. 
 --------------------------------------------------------------
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
VM and Docker Container:
VM :Encapsulate the whole operating system
Docker Container: Encapsulate the application and its dependencies
-------------------------------------------------------------
Dockerfile : It is simple text file that contains all the commands and instructions required to build a Docker Image. It is a blueprint for creating Docker Imagaes.
Docker Image : Single read-only file that contains all the dependencies and libraries required to run an application. It is a snapshot of a Docker Container at a specific point in time. It is used to create Docker Containers.
Docker Container : It is a running instance of a Docker Image. It is an isolated environment that contains everything needed to run an application. It is created from a Docker Image and can be started, stopped, and deleted.
Docker Registry : It is a repository for storing and sharing Docker Images. 
--------------------------------------------------------------


