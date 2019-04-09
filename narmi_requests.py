

from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("NARMI_TOKEN", "OOPS")
SECRET = os.environ.get("NARMI_SECRET", "OOPS")
HOST = os.environ.get("NARMI_HOST", "https://api.demo.narmitech.com/v1")
ACCOUNTS_URL = os.path.join(HOST, "accounts")

timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ") #> "2019-04-09T17:02:26Z"
print("DATE:", timestamp)

#signature = `echo -n "date: $date" | openssl dgst -sha256 -binary -hmac "$secret" | base64`
signature = "TODO"

#sig_header = f"keyId={TOKEN},algorithm=hmac-sha256,headers={timestamp},signature={signature}"

headers = {
    "Authorization": f"Bearer {token}",
    "Date": timestamp,
    "Signature": f"keyId={TOKEN},algorithm=hmac-sha256,headers={timestamp},signature={signature}"
}
print(headers)

response = requests.get(ACCOUNTS_URL, headers=headers)

print("-------------------")
print("RESPONSE:", type(response))
print(response.status_code)
print(response.text)
