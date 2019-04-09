

from datetime import datetime
import os
import subprocess

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("NARMI_TOKEN", "OOPS")
SECRET = os.environ.get("NARMI_SECRET", "OOPS")
HOST = os.environ.get("NARMI_HOST", "https://api.demo.narmitech.com/v1")
ACCOUNTS_URL = os.path.join(HOST, "accounts")

def parsed_output(my_output):
    return my_output.decode().strip()

def system_command(my_command="whoami"):
    process = subprocess.Popen(my_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

if __name__ == "__main__":
    #date, date_err = system_command("date -u +'%Y-%m-%dT%H:%M:%SZ'")
    #signature, sig_err = system_command(f'echo -n "date: {date}" | openssl dgst -sha256 -binary -hmac "{SECRET}" | base64')
    date = os.environ.get("NARMI_DATE", datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")) #> "2019-04-09T17:02:26Z"
    signature = os.environ.get("NARMI_SIG", "OOPS")

    curl_command = f'curl -H "Authorization: Bearer {TOKEN}" -H "Date: {date}" -H "Signature: keyId=\"{TOKEN}\",algorithm=\"hmac-sha256\",headers=\"date\",signature=\"{signature}\"" https://api.demo.narmitech.com/v1/accounts/'
    print("REQUEST", curl_command)
    print(curl_command)

    response, err = system_command(curl_command)
    print("-------------------")
    print("RESPONSE:", response)
    #> {"message":"Authentication credentials were not provided.","id":"not_authenticated"}'
