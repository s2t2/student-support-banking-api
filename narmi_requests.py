

from datetime import datetime
import os
#import subprocess

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("NARMI_TOKEN", "OOPS")
SECRET = os.environ.get("NARMI_SECRET", "OOPS")
HOST = os.environ.get("NARMI_HOST", "https://api.demo.narmitech.com/v1")
ACCOUNTS_URL = os.path.join(HOST, "accounts")

#def parsed_output(my_output):
#    return my_output.decode().strip()
#
#def system_command(my_command="whoami"):
#    process = subprocess.Popen(my_command.split(), stdout=subprocess.PIPE)
#    output, error = process.communicate()
#    return output, error


date = os.environ.get("NARMI_DATE", datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")) #> "2019-04-09T17:02:26Z"
sig = os.environ.get("NARMI_SIG", "OOPS")

signature = f"keyId='{TOKEN}',algorithm='hmac-sha256',headers='date',signature={sig}"
#> Signature: keyId="_____",algorithm="hmac-sha256",headers="date",signature="_________"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Date": date,
    "Signature": signature
}
print(headers)

response = requests.get(ACCOUNTS_URL, headers=headers)

print("-------------------")
print("RESPONSE:", type(response))
print(response.status_code) #> 401
print(response.text) #> {"message":"No signature provided","id":"authentication_failed"}
