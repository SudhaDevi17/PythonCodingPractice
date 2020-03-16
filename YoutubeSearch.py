# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python


import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import os
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "D:/Google Interview Practice/Udemy Course Algorithms/Technical Break Section/Python-for-Algorithms--Data-Structures--and-Interviews-master/Time Series Forecast 3 months/Auth/client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="surfing"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()