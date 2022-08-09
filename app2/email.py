from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings


def send_review_email(name, email, review):

    context = {
        'name': name,
        'email': email,
        'review': review,
    }

    email_subject = 'Thank you for your review'
    # email_body = render_to_string('email_message.txt', context)
    email_body = context["name"] + "\n" + context["email"] + "\n" + context["review"]

    return mail.send_mail(
        email_subject, 
        email_body, 
        'from@example.com',
        ['yexari7943@chimpad.com'],
    )