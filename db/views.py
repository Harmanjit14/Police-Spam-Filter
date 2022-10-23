from http.client import HTTPResponse
from django.shortcuts import render
from twilio.twiml.voice_response import VoiceResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
# Create your views here.


@csrf_exempt
def voice(request):
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    resp.record(max_length=30, play_beep=True, recording_status_callback="recording-complete",
                recording_status_callback_event="completed")
    resp.hangup()

    return HttpResponse("Not for consumer use")


@csrf_exempt
def recording_complete(request):
    response = VoiceResponse()
    # print(request)
    # The recording url will return a wav file by default, or an mp3 if you add .mp3
    # recording_url = request.values['RecordingUrl'] + '.mp3'

    # filename = request.values['RecordingSid'] + '.mp3'

    # with open('{}/{}'.format("static/recordings/", filename), 'wb') as f:
    #     f.write(requests.get(recording_url).content)
    response.hangup()

    return HttpResponse("Not for consumer use")
