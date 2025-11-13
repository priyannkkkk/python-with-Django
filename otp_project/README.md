# 📘 Django Learning Project — OTP Verification System

## 📌 Overview
This project was created as part of my learning journey to understand **Django**, a powerful Python web framework.

Instead of only reading theory, I built a **real working OTP Verification System** which helped me learn:

- Django views & URLs  
- Form handling (GET & POST)  
- Django sessions  
- Email sending  
- AJAX calls (no page reload)  
- Dynamic JavaScript timers  
- Frontend & backend communication  
- Timeout logic and attempt limiting  

This project is great for anyone trying to learn Django hands-on.

---

## 🎯 Features Implemented

### 🔐 **OTP Generation**
- Creates a **6-character OTP** containing:
  - 2 uppercase letters  
  - 2 digits  
  - 2 special characters  
- Randomized and secure

### 📧 **Email Delivery**
User enters email → OTP is sent using Django's SMTP backend.

The email **stays visible** in the box after sending (good UX).

### ⏱ **OTP Timer (60 seconds)**
- Timer starts **after OTP is sent**  
- Shown live on the webpage  
- After expiry:
  - OTP becomes invalid  
  - Button disables  
  - User must regenerate OTP  

### ❌ **Attempt Limiting**
User gets **3 attempts** to enter OTP.

After 3 failed attempts:
- Timer stops  
- Verify button disables & fades  
- Message shows: **"3 failed attempts — Generate New OTP"**

### ⚡ **AJAX Verification**
- OTP is checked **without page refresh**  
- Frontend dynamically displays:
  - Success  
  - Wrong OTP  
  - Attempts left  
  - Expired OTP  

---

## 🧠 Django Concepts Learned

### ✔ Project structure  
### ✔ Views & URL routing  
### ✔ Templates & rendering  
### ✔ POST form handling  
### ✔ JSON response with `JsonResponse`  
### ✔ JavaScript fetch API  
### ✔ Django session storage  
### ✔ Timer logic  
### ✔ UI state changes (enabled/disabled buttons)
