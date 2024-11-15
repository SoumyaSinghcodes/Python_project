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
    ID = input("Enter Employee Id: ")

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
            


        


