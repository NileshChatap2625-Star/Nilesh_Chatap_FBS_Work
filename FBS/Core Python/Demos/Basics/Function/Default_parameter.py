#1. to make parameter optional to use default para
#2. Assign value to parameter in function defination
#3. if we pass value to default parameter it tskes passed value   or  if we dont pass to default para, it takes default value
#4. flow it takes left to right




def emp(id, name, sal, dept='Backoffice'):

    print('ID', id)
    print('NAME', name)
    print('SALARY', sal)
    print('DEPARTMENT', dept)

emp(101, 'Nilesh', 75000, 'Ai')

emp(101, 'rohit', 50000)