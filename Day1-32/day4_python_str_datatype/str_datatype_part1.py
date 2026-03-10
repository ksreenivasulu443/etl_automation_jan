""" Document strings
This str_datatype_part1.py is created to practice python str datatype
created by: Sreeni
created date : 19th January 2026
updated by:
updated date:
version: v1
"""

''' Document strings
This str_datatype_part1.py is created to practice python str datatype
created by: Sreeni
created date : 19th January 2026
updated by:
updated date:
version: v1
'''

str1 = 'ETL Automation labs'

print("str1 is", str1)
print("type of str1 is", type(str1))
print("size of of str1 is", str1.__sizeof__())
print("methods of str type is", dir(str1))
print("id of str1  is", id(str1))


str2 = "ETL Automation labs"

print("str2 is", str2)
print("type of str2 is", type(str2))
print("size of of str2 is", str2.__sizeof__())
print("methods of str type is", dir(str2))
print("id of str2  is", id(str2))


str3 = '''ETL Automation labs'''

print("str3 is", str3)
print("type of str3 is", type(str3))
print("size of of str3 is", str3.__sizeof__())
print("methods of str type is", dir(str3))
print("id of str3  is", id(str3))

str4 = """ETL Automation labs"""

print("str4 is", str4)
print("type of str4 is", type(str4))
print("size of of str4 is", str4.__sizeof__())
print("methods of str type is", dir(str4))
print("id of str4  is", id(str4))


# str5 = str("ETL Automation labs")

str6 =  " It's raning outside " # when to use double quote - when you are string has single quote in it

str7 =  "I don't care "

sql1 = " select * from customer where name = 'sreenivas'  "

str8 =  ' Reena said "She palys cricket" '

str9 = 'I don\'t care '

print(str7, str9, id(str7), id(str9))


str10 = '''Reena said "She palys cricket" and I don't care '''

str10 = """Reena said "She palys cricket" and I don't care """

str11 =  """SELECT employee_id, name, department
FROM employees
WHERE name LIKE 'A%'
  AND status = 'ACTIVE';"""

str12 =  '''SELECT employee_id, name, department
FROM employees
WHERE name LIKE 'A%'
  AND status = 'ACTIVE';'''

print(str11)

print(str12)

str13 = '''select * from customer 
            where name = 'sreenivas' '''

email = 'etlautomationlabs@ymail.com'

print('upper format of email', email.upper())
print('lower format of email', email.lower())


print("email is ending with gmail.com Y/N", email.endswith('gmail.com')) # DQE, GE, SODA, Pydeequ


def dqe_is_gmail(email):
    """
    Check if the given email ends with '@gmail.com'
    Returns True or False
    """
    if email is None:
        return False

    return str(email).strip().lower().endswith("@gmail.com")
