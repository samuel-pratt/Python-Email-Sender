import Sender

sender_one = sender()

email_from = input("Your email: ")
email_to = input("Their email: ")
title = input("What you want your name to appear as: ")
subject = input("Subject Line: ")

sender_one.send_mail(email_from, email_to, title, subject)
