import requests
import csv

url = "https://reqres.in/api/users?page=1"

l1 = []

for page in range(1,3):
    response = requests.get(url + str(page)) # get request



