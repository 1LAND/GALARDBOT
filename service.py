import requests
import donationalerts

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# import uvicorn

from config import CONFIG_DONATION_ALERT as CDA

api = donationalerts.DonationAlertsAPI("11909","E6eHCcBJTHAs5zd2PCSJFGZugLUZWJHYQu0XQLRe", "http://127.0.0.1:5000/login", donationalerts.Scopes.ALL_SCOPES)
app = FastAPI()

DEFAULT_URL = "https://www.donationalerts.com/oauth/"
DEFAULT_API_LINK = "https://www.donationalerts.com/api/v1/"


@app.get("/",response_class=RedirectResponse)
def index():
    return f"{DEFAULT_URL}authorize?client_id={CDA['client_id']}&redirect_uri={CDA['redirect_uri']}&response_type=code&"\
        "scope=oauth-user-show%20oauth-donation-subscribe%20oauth-donation-index%20oauth-custom_alert-store%20oauth-goal-subscribe%20oauth-poll-subscribe"

@app.get("/login", )
def login(code):
    token = requests.post(
        f"https://www.donationalerts.com/oauth/token",
        data={
            "grant_type":"authorization_code",
            "client_id":CDA['client_id'],
            "client_secret":CDA['client_secret'],
            "redirect_uri":CDA['redirect_uri'],
            "code":code
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
        ).json()
    user = api.user(token['access_token'])

    return user.objects
