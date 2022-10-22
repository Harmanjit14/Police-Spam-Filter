from django.shortcuts import render
from twilio.twiml.voice_response import VoiceResponse

# Create your views here.

def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("hello world!", voice='alice')

    return str(resp)