from flask import Flask,render_template,request
import requests, json
from datetime import datetime
from pymongo import MongoClient
import ssl
import certifi


client = MongoClient("mongodb+srv://Arpitha:arpitha@cluster0.guktypv.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test
mydatabase = client['Weather_Api']
mycollection=mydatabase['weather']




# import mysql.connector as conn
# from db_connect import create_db,create_table,insert_table


# mydb=conn.connect(host="localhost",user="root",password="12345678",database="Weather_api")
# print(mydb)
# cursor=mydb.cursor()
# dataBaseName="Weather_api"
# customer_comments="weather"
# create_db(cursor,dataBaseName)
# create_table(cursor,customer_comments)



app = Flask(__name__)

 
@app.route("/",methods=['POST','GET'])
def index():
   return render_template('index.html')

@app.route("/review",methods=['POST','GET'])
def results():


      if request.method == 'POST':


            try:
                  api_key = "e667cb1e7a2b23068b144790273003a0"
                  base_url = "http://api.openweathermap.org/data/2.5/weather?"
                  city_name = request.form["content"]
                  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                  response = requests.get(complete_url)
                  x = response.json()

                  reviews = []


                  if x["cod"] != "404":

                     y = x["main"]
                     print(y)
                     current_temperature = y["temp"]
                     current_pressure = y["pressure"]
                     current_humidity = y["humidity"]
                     z = x["weather"]
                     print(z)
                     weather_description =z[0]["description"]
                     print(weather_description)
                     date_time=datetime.now().strftime('%d %b %Y | %I:%M:%S  %p')
                     print(datetime)

                     # print(" Temperature (in kelvin unit) = " +
                     #       str(current_temperature) +
                     #      "\n atmospheric pressure (in hPa unit) = " +
                     #        str(current_pressure) +
                     #      "\n humidity (in percentage) = " +
                     #        str(current_humidity) +
                     #      "\n description = " +
                     #       str(weather_description))
                     
 
                 

         
                     mydict={"Current_Temperature":current_temperature,"Current_Pressure":current_pressure,"Current_Humidity":current_humidity,"Weather_Description":weather_description,"Date_Time":date_time}
                     print(mydict)
                     reviews.append(mydict)

                     mycollection.insert_one(mydict)

                  # insert_query=f"INSERT INTO {customer_comments}(Current_Temperature,Current_Pressure,Current_Humidity,Weather_Description,Date_Time) VALUES (%(Current_Temperature)s, %(Current_Pressure)s, %(Current_Humidity)s, %(Weather_Description)s, %(Date_Time)s);"
                  # cursor.executemany(insert_query,reviews) 
                  # mydb.commit() 
                  
                  return render_template('results.html',reviews=reviews[0:2])
                   


                     

            except:

                  pass
                  return render_template('results.html')  
      else:

           return render_template('index.html')
        
if __name__ == '__main__':
   app.run(debug=True)