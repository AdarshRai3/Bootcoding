-- Joins : It is basically an operation to combine rows from two or more tables based on related columns beween them;

-- Types of Joins 

-- Cross Join : Every row of table 1 is basically combined with every other row of table 2;
-- (Helps us to get all possibe combinations(permutation) of the two table);

-- EX: We have table of 3*3 and 4*4 then cross join will be 
-- a table of 3*4 = 12 rows and 3+4=7 columns;

Select * from orders cross join customers;
------------------------------------------------------------------
-- Inner Join: Every row of table 1 is combined with every row of table 2 that matches the condition;
-- (Helps s to get the match between the columns of two tables);
 
-- EX : We have table of 3*3 and 4*4 then inner join will be
-- a table of row=max(3,4)=4 rows and 3+4=7 columns;
-- Intersection between the two tables;

Select * from orders o inner join customer c on o.cust_id = c.cust_id; 

-- here cust_id is treated a foreign key in the order table which is primary key in the customer table;
Select * from bill b inner join customer c on b.cust_id = c.cust_id inner join product p on b.prod_id = p.prod_id inner join store s on b.store_id = s.store_id;
Select cname , count(cname) from c inner join o on c.sid = s.sid group by cname;
-------------------------------------------------------------------
-- Views 

-- Instead of writing same query again and again we can use view .

Create view myview as Select * from bill b inner join customer c on b.cust_id = c.cust_id inner join product p on b.prod_id = p.prod_id inner join store s on b.store_id = s.store_id;

Select * from myview;
-------------------------------------------------------------------
-- Rollup ( will give us the perform aggregation on the basis of group by);

Select pname,sum(price) from bill b group by rollup(pname) order by pname;

Select coalesce(pname,'Total'), sum(price) from bill b group by rollup(pname) order by pname;

-------------------------------------------------------------------

Create table emp(
    id int primary key not null,
    name varchar(100) not null,
    email varchar(100) unique not null,
    salary decimal(10,2) not null,
    dept varchar(100) not null
)

Create table com(
    id serial primary key not null,
    name varchar(100) not null,
    email varchar(100) unique not null,
    salary decimal(10,2) not null
    eid int not null 
    FOREIGN key (eid) references emp(id)
)

Insert into emp values(1,'Mayur','RyH2a@example.com',10000,'IT');
Insert into com values(1,'Adarsh','ad@example.com',10000,'IT');

Select * from com c inner join emp e on c.eid = e.id;
