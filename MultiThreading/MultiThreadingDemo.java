public class MultiThreadingDemo {
    //Program is set of Intructions writen in a programming language that tells computer how to perform a task
    //Process is an instance of program that is being executed.
    //Thread executable unit of process is called a process, a single process can have multiple thread which can share the same resources but can run idependently.
    //Multitaking allows a operating system to run multiple processes simantaneousl. 
    //On single core CPU that has done through rapid time sharing between task.
    //On a multiple core CPU true parallel excution occurs, where is task is distributed over multiple cores.
    //Os Scheduelar Balanace the load, ensuring effecient and responsive system performance.
    //Example of MultiTasking : We can browse the  internet, listen to music while downloading a file.
    //Multitaksing basically utilize the capability of the CPU and its cores. In Multiasking assigne multiple task to multiple core this more effecient of then assigning single task to single core.
    //Multithreading is a ability to process multiple threads within a single process concurrently.\
    //A web browser can use mutithreading by assigning seperate threads for rendering the page 
    //Multithreading enhances the effeciency of Multitasking by breaking the main task into smaller sub task or threads can be processed concurrently, making the better use of CPU capabilities
    //In a single threaded ecosystem,both processes and Threads are managed by the OS Scedular through context switching and time slicing whih give the illusion of parallelism
    //In a multi-core system, both threads and process can run in true parallelism with oS Schedular distributing task among multiple core for effecient processing.
    //Time silicing divides the CPU time into smaller intervals of time called quanta or time slice
    //Function : OS schedular allocates allocates these time slice to different processes ,ensuring that each process get a fair share of CPU time.
    //Context Switching is the process of storing and restoring the state of a process or thread so that execution can be resumed from the same point at a later time.
    //Context switching is saving the state of currently running process and loading the state of another process.
    //Function the process thread slice get expires OS schedular save the state of that process and load the state of another process to be executed.
    //Purpose this allows multiple process and threads to share the CPU giving us the appearance of multithreading 

}
