from keyboard import input_string, input_integer, input_real, input_boolean

def main():
    first_name = input_string('Enter first name: ')
    last_name = input_string('Enter last name: ')
    age = input_integer('Enter age: ')
    salary = input_real('Enter salary: ')
    is_salary_hidden = input_boolean('Hide salary? (y/n): ')

    print('DATA RECORD')
    print('===========')
    print('Name:', first_name, last_name)
    print('Age:', age)
    
    if is_salary_hidden:
        print('Salary: [HIDDEN]')
    else:
        print('Salary:', salary)

if __name__ == "__main__":
    main()