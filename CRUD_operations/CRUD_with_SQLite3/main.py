from generate_data import create_data
from utils import Data

if __name__ == "__main__":
    create_data()
    data = Data('data.db')
    data.insert_college('Harvard')
    data.insert_college('Oxford')
    data.insert_college('USP')
    data.insert_college('UFBA')
    data.insert_occupation('Student')
    data.insert_one_customer('Yun', 25, '+0000000', 1, 1)
    data.insert_customers([
        ('Chang', 27, '+8888888', 1, 2),
        ('Ping', 21, '+11111111', 1, 3)])
    data.list_colleges()
    data.list_customers()
    data.list_occupations()
    data.del_customer_by_id(1)


    data.close_connection()



