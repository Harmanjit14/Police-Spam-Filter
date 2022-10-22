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

    resp.record(timeout=10,transcribe=True)
    # Read a message aloud to the caller
    resp.say("hello world!", voice='alice')

    return HttpResponse(str(resp))