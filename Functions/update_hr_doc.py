# 2. For the contents of this list: 
# ∗ Mark just reported a name change. Update Mark’s last name to Blick-Hawley. 
# ∗ Jim has accepted a new account manager role in another department. Change Jim’s 
# department code from OPS to CS and update his salary to 60000. 
# 3. Display the updated contents on multiple lines in the following format, using the pipe 
# symbol | to separate each value and formatting the salary to use a comma: 
# Employee# | DeptCode | Name | NN,NNN 
# ∗ Formatting that last value can be deceptively tricky! Consider that you might have to 
# cast it as another data type when using the format function…


hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'),
           ('0121', 'IT', 'Mark Blick', '67000'), 
           ('0068', 'IT', 'Kahna Larsen', '112000'),
           ('0234', 'OPS', 'Jim Smith', '54000')] 

mark_change = list(hr_list[1])
mark_change[2] = 'Mark Blick-Hawley'
hr_list[1] = tuple(mark_change)

jim_change = list(hr_list[3])
jim_change[1] = 'cs'
jim_change[3] = '60000'
hr_list[3] = tuple(jim_change)


for i in hr_list:
    employee_number, dept_code, name, salary = i
    salary = f"{int(salary):,}"
    print(f"{employee_number} | {dept_code} | {name} | {salary}")