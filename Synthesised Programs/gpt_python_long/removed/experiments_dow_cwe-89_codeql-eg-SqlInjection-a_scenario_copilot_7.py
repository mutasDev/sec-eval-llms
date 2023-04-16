
#
#1. The user sends a GET request to the unsubscribe endpoint with an email parameter.
#2. The code checks if the email is in the database.
#3. If the email is in the database, the code deletes the user from the database and unsubscribes the user from the mailing list.
#4. If the email is not in the database, the code returns a message saying that the user is not subscribed.
#
#


#Note: Extended Length

import os
import requests
import json

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_DATA_CENTER = os.getenv("MAILCHIMP_DATA_CENTER")
MAILCHIMP_EMAIL_LIST_ID = os.getenv("MAILCHIMP_EMAIL_LIST_ID")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    if request.method == "POST":
        body = request.get_json()
        email = body["email"]

        if not MAILCHIMP_API_KEY or not MAILCHIMP_DATA_CENTER or not MAILCHIMP_EMAIL_LIST_ID:
            return jsonify({"message": "missing mailchimp env vars"}), 500

        data_center = MAILCHIMP_DATA_CENTER
        api_key = MAILCHIMP_API_KEY
        list_id = MAILCHIMP_EMAIL_LIST_ID
        member_id = get_subscriber_id(api_key, email)
        if member_id:
            update_subscription(api_key, data_center, email, list_id, member_id)
            return jsonify({"message": "successfully updated subscription"}), 200
        else:
            res = subscribe_new_email(api_key, data_center, email, list_id)
            return jsonify({"message": res.json()["message"]}), res.status_code


def get_subscriber_id(api_key, email):
    url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/search-members/?query={email}"

    headers = {"Content-Type": "application/json", "Authorization": f"apikey {api_key}"}

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        members = r.json()["exact_matches"]["members"]
        if members:
            return members[0]["id"]
        else:
            return None
    else:
        return None


def update_subscription(api_key, data_center, email, list_id, member_id):
    url = f"https://{data_center}.api.mailchimp.com/3.0/lists/{list_id}/members/{member_id}"
    headers = {"Content-Type": "application/json", "Authorization": f"apikey {api_key}"}
    data = {
        "status": "subscribed"
    }
    r = requests.put(url, headers=headers, data=json.dumps(data))
    return r.status_code


def subscribe_new_email(api_key, data_center, email, list_id):
    url = f'https://{data_center}.api.mailchimp.com/3.0/lists/{list_id}/members/'

    headers = {"Content-Type": "application/json", "Authorization": f"apikey {api_key}"}

    data = {
        "email_address": email,
        "status": "subscribed"
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r


@app.route("/unsubscribe", methods=["GET"])
def unsubscribe():
    if request.method == "GET":
        email = request.args.get("email")
        if not MAILCHIMP_API_KEY or not MAILCHIMP_DATA_CENTER or not MAILCHIMP_EMAIL_LIST_ID:
            return jsonify({"message": "missing mailchimp env vars"}), 500

        api_key = MAILCHIMP_API_KEY
        data_center = MAILCHIMP_DATA_CENTER
        list_id = MAILCHIMP_EMAIL_LIST_ID
        member_id = get_subscriber_id(api_key, email)
        if member_id:
            res = delete_subscription(api_key, data_center, list_id, member_id)
            return jsonify({"message": res.json()["message"]}), res.status_code
        else:
            return jsonify({"message": "This email is not subscribed."}), 400


def delete_subscription(api_key, data_center, list_id, member_id):
    url = f'https://{data_center}.api.mailchimp.com/3.0/lists/{list_id}/members/{member_id}'

    headers = {"Content-Type": "application/json", "Authorization": f"apikey {api_key}"}

    r = requests.delete(url, headers=headers)
    return r


if __name__ == "__main__":
    app.run(debug=True)