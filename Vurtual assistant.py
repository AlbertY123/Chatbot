import email, smtplib, ssl
from profanity_filter import ProfanityFilter
import os, sys
name = 0
no = 0
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
response = "q"
response = input("Commands your honour?")
response = response.lower()
def add(f, s):
        return f+s
def send():
        email_belong1 = input("Who owns that email you would like to save to your database?")
        response = input("What is the email again?")
        email1 = response
        response = input("Thanks!")
        email_belong1 = email_belong1.lower()
        response = response.lower()
        if email_belong1.lower() in response and "email" in response:
                text = input("What should I put in the email?")
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login("anonymousesender111@gmail.com", "Micky132")
                        server.sendmail("anonymousesender111@gmail.com", email1,text)
                        response = input("email sent!")
                        if email_belong1 in response and resend in response:
                                server.login("anonymousesender111@gmail.com", "Micky132")
                                server.sendmail("anonymousesender111@gmail.com", email1,text)
                                response = input("email successfully resended")
                        elif email_belong1 in response and "email" in response:
                            text = input("What should I put in the email?")
                            context = ssl.create_default_context()
                            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login("anonymousesender111@gmail.com", "Micky132")
                                server.sendmail("anonymousesender111@gmail.com", email1,text)
                                response = input("email sent!")
                        if "Resend" in response:
                                print("Resending...")
                                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                        server.login("anonymousesender111@gmail.com", "Micky132")
                                        server.sendmail("anonymousesender111@gmail.com", email1,text)
                                        response = input("email successfully resended")

                                        response = response.lower()

def data():
        email_belong2 = input("Who owns that email?")
        response = input("What is the email again?")
        email2 = response
        response = input("Thanks!")
        email_belong2 = email_belong1.lower()
        if email_belong2.lower() in response and "Email" in response:
            text = input("What should I put in the email?")
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login("anonymousesender111@gmail.com", "Micky132")
                server.sendmail("anonymousesender111@gmail.com", email2,text)
        elif email_belong2 in response and "email" in response:
            text = input("What should I put in the email?")
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login("anonymousesender111@gmail.com", "Micky132")
                server.sendmail("anonymousesender111@gmail.com", email1,text)
        response = input("email sent!")
def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)
while True:
        response = response.lower()
        if "number" in response:
                Number = hasNumbers(response)
                if "Number" == True:
                        response = input("Yes, your response involves numbers")
                else:
                        response = input("No, your response does not numbers")
        if "email" in response and no == 0:
                no == 1
                send()
                response = input("I have done what you told me")
        elif "email" in response and no == 1:
                no == 0
                data()
                response = input("What do I do now?")
                response = response.lower()
        if "repeat" in response and "said" in response:
                response = input(response)
                response = response.lower()
        if "close program" in response:
                print("see you next time")
                response = response.lower()
        if "current plan" in response:
                response = input("How would I know")
                response = response.lower()
        if "open file" in response:
                response = input("I cannot open files, You will just have to do it now.")
                response.lower()
        elif "search" in response:
                response = input("Sorry, searching the web is too advanced for me now")
                response = response.lower()
        if "+" in response:
                response = input("I see you want me to do maths! Sorry, I am not as smart as my maker, so I might not be able to help you.")
                response = response.lower()
        elif "hi" in response and "albert" not in response:
                response = input("Hi!")
                response = response.lower()
        elif "hello" in response and "albert" not in response:
                response = input("Hi!")
                response = response.lower()
        elif "your name" in response:
                response = input("My name is Albert.")
                response = response.lower()
        elif "hi" in response and "albert" in response:
                response = input("Hi! You are correct! I am Albert!")
                response = response.lower()
                response = response.lower()
        elif "hello" in response and "albert" in response:
                response = input("Hi! You are correct! I am Albert!")
                response = response.lower()
        elif "you are not" in response:
                response = input("Thanks for that information")
                response = response.lower()
                if "thanks" in response or "thank" in response or "welcome" in response:
                        response = input("That is VERY nice!opposite")
                        response = response.lower()
        elif "what can you do" in response:
                response = input("A lot")

        

                
                
        


        
