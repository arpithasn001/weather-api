# def create_db(cursor,dataBaseName):
#     db=f"create database {dataBaseName}"
#     cursor.execute(db)

# def create_table(cursor,customer_comments):
#     tb=f"CREATE TABLE IF NOT EXISTS {customer_comments} (Current_Temperature varchar(1000),Current_Pressure varchar(100),Current_Humidity varchar(30),Weather_Description varchar(400),Date_Time varchar(200));"
#     cursor.execute(tb)

# def insert_table(cursor,customer_comments,lst):
#     insert_query=f"INSERT INTO {customer_comments}(Current_Temperature,Current_Pressure,Current_Humidity,Weather_Description,Date_Time) VALUES (%(Current_Temperature)s, %(Current_Pressure)s, %(Current_Humidity)s, %(Weather_Description)s, %(Date_Time)s);"  
#     cursor.executemany(insert_query,lst)
