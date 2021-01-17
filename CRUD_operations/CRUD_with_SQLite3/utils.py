import sqlite3

class Data():

    def __init__(self, data):
        
        self.conn = sqlite3.connect(data)
        self.cursor = self.conn.cursor()
        
    def check(cursor, conn):
        "Function to check changes in the database."
        if cursor.rowcount == 1:
            conn.commit()
            print('Operation performed successfully.')
        else:
            print('Not found or error.')
         
    def insert_college(self, college:str):
        "Function to insert university records in the database."
        try:
            sql = f"""INSERT INTO college(college_name) VALUES ('{college}') """
            self.cursor.execute(sql)
        except Exception as error:
            print(error)
            self.conn.rollback()
        else:
            self.conn.commit()
            print(f'The value {college} has been inserted into database.')
    
    def insert_occupation(self, occupation:str):
        "Function to insert occupation records in the database."
        try:
            sql = f"""INSERT INTO work(occupation) VALUES ('{occupation}') """
            self.cursor.execute(sql)
            
        except Exception as error:
            print(error)
            self.conn.rollback()
        else:
            self.conn.commit()
            print(f'The value {occupation} has been inserted into database.')
    
    def insert_one_customer(self, name:str, 
                            age:int, phone:str, 
                            id_occupation:int, 
                            id_college:int):
        "Function to insert one customer record in the database."
        try:
            sql = """INSERT INTO customer (name, age, phone, id_occupation, id_college) VALUES (?,?,?,?,?) """
            self.cursor.execute(sql, (name, age, phone, id_occupation, id_college))
        except Exception as error:
            print(error)
            self.conn.rollback()
        else:
            self.conn.commit()
            print('The values were inserted in the table.')

    def insert_customers(self,list_customers:list):
        "Function to insert more than one customer record in the database."
        if isinstance(list_customers,list):
            #check if the inserted value is a list
            try:
                sql = "INSERT INTO customer(name, age, phone, id_occupation, id_college) VALUES (?,?,?,?,?)"
                self.cursor.executemany(sql, list_customers)
            except Exception as error:
                print(f'Error: {error}')
                self.conn.rollback()
            else:
                print('The values were inserted in the table.')
                self.conn.commit()
        else:
            raise TypeError('Inappropriate argument type.')

    def update_college(self,row_id:int):
        "Updates university registration."
        try:
            new_college_name = input('New college name: ')
            sql = f"UPDATE college SET college_name = '{new_college_name}' WHERE id = {row_id}"
            self.cursor.execute(sql)
        except Exception as error:
            print(f'Error: {error}')
            self.conn.rollback()
        else:
            Data.check(self.cursor, self.conn)
    
    def update_occupation(self, row_id:int):
        "Updates occupation registration."
        try:
            new_occupation = input('New occupation name: ')
            sql = f"UPDATE work SET occupation='{new_occupation}' WHERE id = {row_id}"
            self.cursor.execute(sql)
        except Exception as error:
            print(f'Error:{error}')
            self.conn.rollback()
        else:
            Data.check(self.cursor, self.conn)
    
    def update_customer(self,id_customer:int):
        "Updates customer registration."
        try:
            new_age = input('New age: ')
            new_phone = input('New phone: ')
            new_occupation = input('New occupation: ')
            sql = f"""UPDATE customer SET age = {new_age},
            phone = '{new_phone}', id_occupation = {new_occupation} WHERE id = {id_customer} """
            self.cursor.execute(sql)
        except Exception as error:
            print(f'Error: {error}')
            self.conn.rollback()
        else:
            Data.check(self.cursor, self.conn)
    
    def del_college(self,id_college:int):
        "Deletes a college record."
        try:
            self.cursor.execute(
                f"""DELETE FROM college WHERE id = ?""", 
                (id_college,))
            
        except Exception as error:
            print(f'Error: {error}')
        else:
            Data.check(self.cursor, self.conn)
    
    def del_occupation(self, id_occupation:int):
        "Deletes an occupation record."
        try:
            self.cursor.execute(
                f"""DELETE FROM work WHERE id = ?""", 
                (id_occupation,))
            
        except Exception as error:
            print(f'Error: {error}')
        else:
            Data.check(self.cursor, self.conn)
    
    def del_customer_by_id(self, id_customer:int):
        "Deletes a customer record by id."
        try:
            self.cursor.execute(
                f"""DELETE FROM customer WHERE id = ?""", 
                (id_customer,)
            )
        except Excpetion as error:
            print(f'Error: {error}')
        else:
            Data.check(self.cursor, self.conn)
    
    def list_colleges(self):
        "Shows all colleges in the database."
        try:
            self.cursor.execute("SELECT * FROM college")
            results = self.cursor.fetchall()
            if len(results)>0:
                for row_id, value in results:
                    print(row_id, value)
            else:
                print('No values to show.')
                
        except Exception as error:
            print(f'Error: {error}')
    
    def list_occupations(self):
        "Shows all occupations in the database."
        try:
            self.cursor.execute("SELECT * FROM work")
            results = self.cursor.fetchall()
            if len(results)>0:
                for row_id, value in results:
                    print(row_id, value)
            else:
                print('No values to show.')
        except Exception as error:
            print(f'Error: {error}')
    
    def list_customers(self):
        "Shows all customers of the database."
        try:
            self.conn.row_factory = sqlite3.Row
            results = self.cursor.execute("SELECT * FROM customer")
 
            for record in results:
                print('_'*50)
                print(f'Record {record[0]}'.center(50,' '))
                print(f'\tName: {record[1]}')
                print(f'\tAge: {record[2]}')
                print(f'\tPhone: {record[3]}')
                print()
                print('_'*50)
                
        except Exception as error:
            print(f'Error: {error}')
    
    def search_customer(self, id_customer:int):
        "Fetch a customer by id."
        try:
            sql = f"""SELECT * FROM customer WHERE id = {id_customer}"""
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            
        except Exception as error:
            print(f'Error: {error}')
        else:
            if len(result)>0:
                return (f'Name: {result[1]}',
                        f'Age: {result[2]}',
                        f'Phone: {result[3]}',
                        f'Id Occupation:: {result[4]}',
                        f'Id college: {result[5]}')
            return 'Not found.'
                
    
    def close_connection(self):
        "Closes the connection to the server."
        self.cursor.close()
        self.conn.close()