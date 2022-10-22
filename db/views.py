from http.client import HTTPResponse
from django.shortcuts import render
from twilio.twiml.voice_response import VoiceResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def voice(self):
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    resp.record(max_length=30,play_beep=True)
    # Read a message aloud to the caller
    resp.say("Done Thank You!", voice='alice')
    resp.hangup()

    return HttpResponse(str(resp))