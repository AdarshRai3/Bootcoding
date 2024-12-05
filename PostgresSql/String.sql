-- concat(first_column,second_column) , concat_ws('Seperator',first_column,second_column)
-- concat() is used to join two or more strings into a single string.  
-- concat_ws() is used to join two or more strings into a single string with a separator.
Select emp_id , concat_ws(' ',fname,lname)as full_name, dept , salary, hire_date from employees;

-- Substr(column_name,start_index,end_index);indexing starts from one.

left() , right()