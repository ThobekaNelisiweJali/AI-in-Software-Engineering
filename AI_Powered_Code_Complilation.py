#-------------Manual Implimentation of a function to sort a list of dictionaries by a specific key-------------------#

def sort_dicts_by_key(data_list, sort_key):
    return sorted(data_list, key=lambda x: x[sort_key])

#Example of usage 

     # Sample data: list of dictionaries

employees = [
    {'name': 'Alice', 'age': 30, 'department': 'HR'},
    {'name': 'Bob', 'age': 25, 'department': 'Engineering'},
    {'name': 'Charlie', 'age': 35, 'department': 'Marketing'}
]

# Sort employees by 'age'
sorted_employees = sort_dicts_by_key(employees, 'age')

# Print the sorted list
print(sorted_employees)

#Expected Output:

[
    {'name': 'Bob', 'age': 25, 'department': 'Engineering'},
    {'name': 'Alice', 'age': 30, 'department': 'HR'},
    {'name': 'Charlie', 'age': 35, 'department': 'Marketing'}
]


#---------------- AI Implimentation of a function to sort a list of dictionaries by a specific key------------------#

def sort_records(records, sort_key, reverse=False, missing_value=None):
    """
    Sort a list of dictionaries (records) by a specified key.
    
    Parameters:
    - records: List of dictionaries to sort.
    - sort_key: Key to sort the dictionaries by.
    - reverse: Whether to sort in descending order.
    - missing_value: Fallback if key is missing (default None raises error).
    """
    if missing_value is None:
        return sorted(records, key=lambda d: d[sort_key], reverse=reverse)
    else:
        return sorted(records, key=lambda d: d.get(sort_key, missing_value), reverse=reverse)
    
 #Example of usage:   
    
    # Sample data for AI-powered sorting function


employees = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25},  # Missing 'salary'
    {'name': 'Charlie', 'age': 35, 'salary': 80000},
    {'name': 'Diana', 'age': 28, 'salary': 65000},
    {'name': 'Eve', 'age': 40}  # Missing 'salary'
]


# Sort by salary, descending order, use 0 as fallback salary if missing
sorted_by_salary = sort_records(employees, 'salary', reverse=True, missing_value=0)

print(sorted_by_salary)

# Expected Output:

[
    {'name': 'Charlie', 'age': 35, 'salary': 80000},
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Diana', 'age': 28, 'salary': 65000},
    {'name': 'Bob', 'age': 25},        # Treated as salary = 0
    {'name': 'Eve', 'age': 40}         # Treated as salary = 0
]

#This shows how the function gracefully handles missing keys by using the fallback value provided.