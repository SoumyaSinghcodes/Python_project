import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="som147", database="emp")

#Function to check if employee id exists or not

def check_employee(employee_id):
    #Query to select all rows from the employees table where id matches
    sql = 'SELECT*FROM employees WHERE id=%s'

    #Making cursor buffered to make rowcount method work properly
    cursor = con.cursor(buffered=True)
    data = (employee_id,)

    #Executing the SQL Query
    cursor.execute(sql, data)

    #Fetch the first row to check if employee exists
    employee = cursor.fetchone()

    #Closing the cursor
    cursor.close()

    #If employee is found, return True, else return False
    return employee is not None

#Add employee function will ask the employee id and uses the check employee function to check whether the employee to be added already exists in our record

def add_employee():
    Id = input("Enter Employee Id: ")

    #Checking if Employee with given Id already exits
    if check_employee(Id):
        print("Employee already exists. Please try again")
        return
    
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")

        #Inserting Employee details into the employees table
        sql = 'INSERT INTO employees(id, name, position, salary) VALUES(%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        cursor = con.cursor()

        try:
            #Executing the SQL Query
            cursor.execute(sql, data)

            #Committing the transaction
            con.commit()
            print("Employee Added Successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            #Closing the cursor
            cursor.close()

#Remove Employee Function which will simply ask for Id of the employee to be removed because Id is the primary key in our Employee details record as there can be two employees with same name

def remove_employee():
    Id = input("Enter Employee Id: ")

    #Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again")
        return
    
    else:
        #Query to delete employee from the employees table

        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()

        try:
            #Executing the SQL Query
            cursor.execute(sql, data)

            #Committing the transaction
            con.commit()
            print("Employee Removed Successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            #Closing the cursor
            cursor.close()


#Promote Employee Function will ask for the Employee Id and uses the check employee function to check whether the employee to be Promoted exist in our record or not if employee details exist then it will ask for the amount by which his salary is to be increased

def promote_employee():
    Id = input("Enter Employee's Id: ")

    #Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again")
        return
    
    else:
        try:
            Amount = float(input("Enter increase in Salary: "))

            #Query to fetch salary of Employee with given Id
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (Id,)
            cursor = con.cursor()

            #Executing the SQL Query 
            cursor.execute(sql_select, data)

            #Fetching salary of Employee with given Id
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            #Query to updateSalary of Employee with given Id
            sql_update = 'UPDATE employee SET salary=%s WHERE id=%s'
            data_update = (new_salary, Id)

            #Executing the SQL Query to update salary
            cursor.execute(sql_update, data_update)

            #Committing the transaction
            con.commit()
            print("Employee Promoted Successfully")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            con.rollback()

        finally:
            #Closing the cursor
            cursor.close()


#Display Employee Function to simply select query of SQL which fetches all the records stored in the employee details table and print them line by line

def display_employee():
    try:
        #Query to select all rows from the employee table
        sql = 'SELECT*FROM employees'
        cursor = con.cursor()

        #Executing the SQL Query
        cursor.execute(sql)

        #Fetching all details of all the Employees
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("----------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        #Closing the cursor
        cursor.close()


def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        #Taking choice from user
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employee()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")
    
            


        


