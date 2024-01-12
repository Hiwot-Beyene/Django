from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Let's create a dictionary
monthly_challenge = {
    "january": "Study",
    "march": "Relax",
    "april": "Have fun"
}

def monthly_challenges_inNumber(request, month):
    try:
        # Try to convert the month to an integer
        month = int(month)
        months = list(monthly_challenge.keys())
        redirected_month = months[month - 1]
        challenge_text = monthly_challenge[redirected_month]
        return HttpResponseRedirect("/challenges/" + redirected_month)
    except (ValueError, IndexError, KeyError):
        return HttpResponseNotFound("This month is not found!")

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
    except KeyError:
        return HttpResponseNotFound("This month is not found!")
    return HttpResponse(challenge_text)
