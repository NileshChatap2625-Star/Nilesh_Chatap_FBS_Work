# 1. to pass multiple para with meaning
# 2. mention 2 asterisk symbol brfore para name in function defination
# 3. passed data will be store in dictionary formate
## 4. Use for loop to iterate value from tuple
def emp(**data):
    for key, val in data.items():
        print(key, ':', val)


emp(id = 121, name = 'nilesh', sal = 20000, dept = 'ai')