-- employee data with employee number, last name, first name, gender, and salary
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees AS e
	LEFT JOIN salaries AS s ON e.emp_no=s.emp_no
ORDER BY emp_no;

-- employees hired in 1986
SELECT * FROM employees
WHERE EXTRACT(year FROM hire_date) = 1986
ORDER BY hire_date;

/*
manager data with  department number, department name, the manager's employee number,
last name, first name, and start and end employment dates
*/
SELECT m.dept_no, d.dept_name, m.emp_no,e.last_name,e.first_name,m.from_date,m.to_date 
FROM dept_manager AS m
	INNER JOIN departments AS d ON m.dept_no=d.dept_no
	INNER JOIN employees AS e ON m.emp_no=e.emp_no
ORDER BY dept_no;

-- department of each employee data with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name,e.first_name,d.dept_no
FROM employees AS e
	INNER JOIN dept_emp ON e.emp_no=dept_emp.emp_no
	INNER JOIN departments AS d ON dept_emp.dept_no=d.dept_no
ORDER BY emp_no;

-- employees whose first name is "Hercules" and last names begin with "B"
-- error?
SELECT *
FROM employees
	WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
ORDER BY last_name;

-- List all employees in the Sales department, 
-- including their employee number, last name, first name, and department name.
SELECT e.emp_no,e.first_name,e.last_name,d.dept_name
FROM employees AS e
	INNER JOIN dept_emp ON e.emp_no=dept_emp.emp_no
	INNER JOIN departments AS d ON dept_emp.dept_no=d.dept_no
WHERE dept_name='Sales'
ORDER BY emp_no;

-- List all employees in the Sales and Development departments,
-- including their employee number, last name, first name, and department name.
SELECT e.emp_no,e.first_name,e.last_name,d.dept_name
FROM employees AS e
	INNER JOIN dept_emp ON e.emp_no=dept_emp.emp_no
	INNER JOIN departments AS d ON dept_emp.dept_no=d.dept_no
	WHERE dept_name = 'Sales' OR dept_name = 'Development'
ORDER BY emp_no;

-- In descending order, list the frequency count of employee last names, i.e.,
-- how many employees share each last name.
SELECT last_name, COUNT (last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;
