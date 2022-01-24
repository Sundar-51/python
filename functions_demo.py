import json
work_hours = [('adam', 100), ('eve', 790), ('james', 200)]
#print (work_hours)
def employee_check(work_hours):
    #work_hours = [('adam', 100), ('eve', 790), ('james', 200)]
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)
    #print('helloo')
result= (employee_check(work_hours))
print (result)
employee, hours = result
print (hours,employee)