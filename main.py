from flask import Flask,
import csv
import requests


app = Flask(__name__)

@app.route('/userdata', method='GET')
def userdata():
    main = {'content':'application/json'}
    users = []

    for user in range(1, 3):
        url = f"https://reqres.in/api/users?page={user}"
        response = requests.get(url,main=main)
        details = response.json()['details']
        for i in details:
            users.append(i)

    with open('userdetials.csv', mode='w') as csv_file:
        header = ['id','email','first_name', 'last_name', 'avatar']
        write_csv = csv.DictWriter(csv_file, header=header)
        write_csv.writeheader()
        for user_details in users:
            write_csv.writerow(user_details)

    return "csv file has created!"

## after fetching the users data, this program should create a CSV file name userdetails.csv
## The file output: *"TypeError: Session.request() got an unexpected keyword argument 'main'"*

if __name__ == '__main__':
    app.run()