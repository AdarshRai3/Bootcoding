-- concat(first_column,second_column) , concat_ws('Seperator',first_column,second_column)
-- concat() is used to join two or more strings into a single string.  
-- concat_ws() is used to join two or more strings into a single string with a separator.
Select emp_id , concat_ws(' ',fname,lname)as full_name, dept , salary, hire_date from employees;

-- Substr(column_name,start_index,end_index);indexing starts from one.
Select dept , substr(dept,1,2) as ID from employees;

Select replace(dept,'IT','Tech') from employees;

Select lname from employees where length(lname)>10;

Select lname from employees where lname like %a%;

Select left(lname,3) from employees;

Select right(lname,3) from employees;