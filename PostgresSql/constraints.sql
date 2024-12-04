Create Table employees(
    emp_id serial primary key not null,
    fname varchar(100) not null,
    lname varchar(100) not null,
    email varchar(100) unique not null,
    salary decimal(10,2) not null,
    dept varchar(100) not null,
    hire_date date not null Default CURRENT_DATE
);

Insert into employees values(1,'Mayur','Sharma','RyH2a@example.com',10000,'IT',now());
Insert into employees(fname,lname,email,salary,hire_date) values ('Abhishek','Sharma','RyH2a@example.com',10000,now());

