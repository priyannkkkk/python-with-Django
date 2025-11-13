from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
import random
import string
import time
import json
from django.utils import timezone
from datetime import datetime


# -----------------------------------
# Strong OTP Generator (optimized)
# -----------------------------------
def generate_custom_otp():
    start = time.time()

    digits = random.choices(string.digits, k=2)
    specials = random.choices("!@#$%^&*()-_=+<>?", k=2)
    upper = random.choices(string.ascii_uppercase, k=2)

    otp_list = digits + specials + upper
    random.shuffle(otp_list)

    otp = ''.join(otp_list)

    end = time.time()
    print(f"OTP generation time: {end - start:.8f} seconds")

    return otp


# -----------------------------------
# Generate OTP Page View
# -----------------------------------
def generate_otp(request):
    otp = generate_custom_otp()

    request.session['otp'] = otp
    request.session['otp_time'] = timezone.now().isoformat()  # save as string
    request.session['attempts'] = 0                           # reset attempts

    sent = False

    if request.method == "POST":
        email = request.POST.get('email')

        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            'yourgmail@gmail.com',
            [email],
            fail_silently=False,
        )
        sent = True

    return render(request, 'generator/otp.html', {
        "otp": otp,
        "sent": sent
    })


# -----------------------------------
# Verify OTP (AJAX)
# -----------------------------------
def verify_otp(request):
    if request.method == "POST":
        body = json.loads(request.body)
        entered = body.get('entered_otp')

        original = request.session.get('otp')
        attempts = request.session.get('attempts', 0)
        otp_time_str = request.session.get('otp_time')

        # Convert session string back to datetime
        otp_time = None
        if otp_time_str:
            otp_time = datetime.fromisoformat(otp_time_str)

        # ----------------------------
        # 1. Check OTP expiration
        # ----------------------------
        if otp_time and (timezone.now() - otp_time).total_seconds() > 60:
            new_otp = generate_custom_otp()
            request.session['otp'] = new_otp
            request.session['otp_time'] = timezone.now().isoformat()
            request.session['attempts'] = 0

            return JsonResponse({
                "message": "⏳ OTP expired — Generate New OTP"
            })

        # ----------------------------
        # 2. Wrong OTP
        # ----------------------------
        if entered != original:
            attempts += 1
            request.session['attempts'] = attempts

            # More than 3 wrong attempts → new OTP
            if attempts >= 3:
                new_otp = generate_custom_otp()
                request.session['otp'] = new_otp
                request.session['otp_time'] = timezone.now().isoformat()
                request.session['attempts'] = 0

                return JsonResponse({
                    "message": "❌ Incorrect! 3 failed attempts — Generate New OTP"
                })


            return JsonResponse({
                "message": f"❌ Incorrect OTP! Attempts left: {3 - attempts}"
            })

        # ----------------------------
        # 3. Correct OTP
        # ----------------------------
        request.session['attempts'] = 0
        return JsonResponse({
            "message": "🎉 Correct OTP! Welcome!"
        })
