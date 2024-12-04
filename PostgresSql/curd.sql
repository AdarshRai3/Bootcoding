-- Create 
Create Database test;
Create Table Student(
    id int primary key,
    name varchar(100),
    rollnos int,
);
Insert into Student values(1,'Mayur',101);
Insert into Student values(2,'Shreyas',102);
Insert into Student values(3,'Adarsh',103);

Insert into Student (id,name,rollNos) values(4,'Raj',104);

-- Read
Select * from Student;
Select name from Student;
Select name,rollnos from Student;

-- Update
Update Student set rollNos=101 where id=1;
Update Student set name = 'Akash' where id=3;

--Delete 
Delete from Student where id=2;
Delete from Student where id=3;
