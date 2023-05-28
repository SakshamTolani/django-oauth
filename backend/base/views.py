from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

CLIENT_SECRETS_FILE = "D:/Django OAuth Test/backend/base/credentials.json"

SCOPES = ['openid', 'https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
REDIRECT_URL = 'http://127.0.0.1:8000/rest/v1/calendar/redirect'
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'


@api_view(['GET'])
def google_calendar_init_view(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)

    flow.redirect_uri = REDIRECT_URL

    authorization_url, state = flow.authorization_url(

        access_type='offline',

        include_granted_scopes='true')

    request.session['state'] = state

    return Response({"authorization_url": authorization_url})


@api_view(['GET'])
def google_calendar_redirect_view(request):
    state = request.session['state']
    if state is None:
        return Response({"detail": "Some error occured"})

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URL

    authorization_response = request.get_full_path()
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = {'token': credentials.token,
                                      'refresh_token': credentials.refresh_token,
                                      'token_uri': credentials.token_uri,
                                      'client_id': credentials.client_id,
                                      'client_secret': credentials.client_secret,
                                      'scopes': credentials.scopes}

    if 'credentials' not in request.session:
        return redirect('v1/calendar/init')

    credentials = google.oauth2.credentials.Credentials(
        **request.session['credentials'])

    service = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Returns the calendars on the user's calendar list
    events_list = service.calendarList().list().execute()

    # Getting user ID which is his/her email address
    calendar_id = events_list['items'][0]['id']

    # Getting all events associated with a user ID (email address)
    events = service.events().list(calendarId=calendar_id).execute()

    events_list_append = []
    if not events['items']:
        return Response({"message": "No events have happened"})
    else:
        for events_list in events['items']:
            events_list_append.append(events_list)

    # return Response({"error": "calendar event aren't here"})
    return Response({"events": events_list_append})
