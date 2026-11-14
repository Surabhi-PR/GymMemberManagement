from mysql import connector
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
class DbConnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host = os.getenv("DB_HOST"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                database = os.getenv("DB_NAME")
            )
            return self.connection
        except Exception as e:
            print(e)
            return None


class GymMemberManager(DbConnect):
    
    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
        

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(e)
        

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = """insert into member(name, place, plan, mobile, fee, joining_date)
            values(%s, %s, %s, %s, %s, %s)"""
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("New member added successfully...!")
        except Exception as e:
            print(e)
        

    def retrieve(self, id=None):
        record = self.get_object(id=id)
        if record == None:
            print("No records found..!")
        print(record)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query = "delete from member where id = %s"
                self.cursor.execute(query, (id,))
                self.connect.commit()
                print("member deleted successfully..!")
            else:
                print("No members found..!")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                placeholder = " "
                for k in kwargs.keys():
                    placeholder += k + "= %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Member updated successfully...!")
            else:
                print("No member found..!")
        except Exception as e:
            print(e)
        

connection_instance = DbConnect()
print(connection_instance.get_connection())

member_instance = GymMemberManager()
member_instance.get()
#member_instance.post(name = "Anjana", place = "Kakkanadu", plan = "3 months", mobile = "9987564490", fee = 1000, joining_date = datetime.now().strftime("%Y-%m-%d"))
#member_instance.retrieve(id=1)
#member_instance.delete(id=2)
#member_instance.put(id = 1, name = "Anjana", place = "Kochi", plan = "3 months", mobile = "9087680932", fee = 1500, joining_date = datetime.now().strftime("%Y-%m-%d") )