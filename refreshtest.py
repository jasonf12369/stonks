import json
import requests
from config import *
from td.client import TDClient

def auth(self):
    method = 'GET'
    url = 'https://auth.tdameritrade.com/auth?'


    code = "FbtouA8gFlhcwI3/iCUg47mN1/2rTCpohE+XVmJPnwfw6cfF5ZiLN7NZBTdznGedhZ1jatbgRF9ybXEjs4yR8JF6J7Fgwwxk28DAEReqw4c2gRNF7mqR5SJry+R+vtLeB4ktNe8+0hVjVjg+PAM6ut/n9ZL8b3j3zbu8hFcb+dtSX2F9wNUhn3APJVen0en3nUYbjZi6NxhNJE19vZJjPKZUZlbMei6wVp1CPd7GzIqrJEgtetzWrjZ+BDPyl7Z6VZ0GN0C63gZjutbe9cLIbNqgF7pR05MTuydxC8MvkhhGTJ2GU4GjJh2Ksx5XDisC/82mkfprBJb2dYKynoxVOZiyPBmiHX+LcFQSL5dNZ6P7waboCXAhDsf7N9L7yr/CKSJlVmehnylyJTFhplMgrTSb9JapwaZJ0mpLrMBzcurgnduVipEM3Xatrt5100MQuG4LYrgoVi/JHHvlY1m6z0I+3HXeOYNiP4TzTx3xNqLJzCvgjHrFyEvo7mNfV1VHsieF1PTHxWE5FFueqkPA51KqevEha4C9IEui2wkmcbP16YZEo06raI3vCzJjzDQeFUTdDC2Ga3TlZJgRdG5DuCRq5BJXxiD33e1yBCa35Sc3g+ariMaaKqw/4v/Muh3bQjfYI6S+dYqRwnGGTs/3HgWH3vdOYwnXdlkQoZ2iDvVTEyJE76PNIOQT7U7AHnp74pJlJSiqIRL9VtOMyFRFlgy5crqvXCAqRIbf8wP7sidepmMvQvHw7sut8F8/p/gyXV0LU1FA7yYf9O1CdO671mpU2icPsRRnS1zbrenYFUlZTBMgEaVeG9G7vzRF09V2a0wtBWMpFCBlMPs8EF9d1w+yRACSvQgWJ3+RhsHIcynQohav9EUHKgJk+rwEswjHiVdKCcxR8m0=212FD3x19z9sWBHDJACbC00B75E"

    headers = {"Content-Type":"application/x-www-form-urlencoded"}

    payload = {'grant_type': 'authorization_code', 
                'access_type': 'offline', 
                'code': code, 
                'client_id':TD_CLIENT_ID, 
                'redirect_uri':'http://192.168.0.12:8080/'}

    authReply = requests.post(r'https://api.tdameritrade.com/v1/oauth2/token', headers = headers, data=payload)
    decoded_content = authReply.json()
    access_token = decoded_content["access_token"]
    print("refresh_token")

