from flask import Flask, render_template, request
import pandas as pds

app = Flask(__name__)

#home page route
@app.route("/", methods=['POST','GET'])
def home():
    return render_template("index.html")

#page for the form
@app.route('/data', methods=['POST'])
def data():
    #get the response from the form and format strings for response
    err = ""
    response = ""
    city = request.form['city']
    date = request.form['date']

    if city == "NONE" :
        err = "אנא בחר עיר מהרשימה" 
        return render_template("error.html", error=err)
    
    formatted_city = ""
    if city == 'BSH':
        formatted_city = "באר שבע"
    elif city == 'ELT':
        formatted_city = "אילת"
    elif city == 'JER':
        formatted_city = "ירושלים"
    elif city == 'ROP':
        formatted_city = "ראש פינה"
    elif city == 'TLV':
        formatted_city = "תל אביב"
    
    if date == '':
        err = "אנא בחר תאריך בפורמט הנכון"
        return render_template("error.html", error=err)
        
    year = date[0:4]
    formatted_date = date[6:8]+ "/"+ date[4:6]+ "/"+ year
    
    #get the correct data file
    
    filename = "data/"+ city + ".txt"
    df = pds.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    
    #handle 2 type of requests: daily or yearly avarge temp
    temp = ""
    temp_type = ""
    if len(date) > 4:
        temp_by_day  = df.loc[df['    DATE'] == date]["   TG"].squeeze() / 10
        temp_type = "daily"
        temp =  temp_by_day
    else:
        df["    DATE"] = df["    DATE"].astype(str)
        res_from_file = df[df["    DATE"].str.startswith(str(year))]
        if res_from_file.empty:
            err = "אין מידע בנוגע לשנה זו בעיר זו"
            return render_template("error.html", error=err)
        avg_temp = res_from_file.loc[df["   TG"] != -9999]["   TG"].mean() /10
        temp_year_avg = round(avg_temp, 2)
        temp_type = "yearly"
        temp=temp_year_avg
        
    response = {
        "city": formatted_city,
        "date" : formatted_date,
        "temp": temp,
        "year": year
    }

    if temp_type == "daily":
        return render_template("res_daily.html", result = response)
    else:
        return render_template("res_yearly.html", result = response)

if __name__ == "__main__":
    app.run(debug=True)