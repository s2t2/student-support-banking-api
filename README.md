# Narmi Banking API - Investigation

Student project support. Programmatic banking!

## Installation

```sh
conda create -n narmi-env
conda activate narmi-env
```

```sh
pip install -r requirements.txt
```

## Setup

Create a new file called .env in the root directory of this repository, and set some environment variables there.

Set environment variables: `NARMI_TOKEN`, and `NARMI_SECRET` to match your Narmi API credentials.

Run the following commands in the terminal once (first time only), then store the results in environment variables `NARMI_DATE` and `NARMI_SIG`, respectively. TODO: make this process more dynamic!

```sh
secret='________________' # use your NARMI_SECRET here

date=`date -u +'%Y-%m-%dT%H:%M:%SZ'`
#> set the result as NARMI_DATE environment variable

signature=`echo -n "date: $date" | openssl dgst -sha256 -binary -hmac "$secret" | base64`
#> set the result as NARMI_SIG environment variable
```

## Usage

```sh
python narmi_requests.py
```

## [Credits](/CREDITS.md)

## [License](/LICENSE.md)
