

# adapted from: https://github.com/narmitech/banking-client-python#getting-started

import banking_client
from banking_client.api_client import ApiClient
from banking_client.configuration import Configuration
from banking_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("NARMI_TOKEN", "OOPS")
SECRET = os.environ.get("NARMI_SECRET", "OOPS")
HOST = os.environ.get("NARMI_HOST", "https://api.demo.narmitech.com/v1")

config = Configuration()
config.host = HOST
config.access_token = TOKEN
config.secret = SECRET

client = banking_client.AccountApi(api_client=ApiClient(configuration=config))
print("CLIENT:", type(client))

try:
    response = client.list()
    print("RESPONSE:", type(response))
    pprint(response)
except ApiException as e:
    print("ERROR:", e)
