from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


def send_access_code(rsvp, access_code):
    subject = "RSVP Access Code"
    from_email = settings.EMAIL_HOST_USER
    to_email = rsvp.email
    context = {
        "domain": settings.DOMAIN,
        "rsvp": rsvp,
        "access_code": access_code,
    }

    text_content = render_to_string("email/password.txt", context=context)
    html_content = render_to_string("email/password.html", context=context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_confirmation_email(rsvp, guests):
    subject = "Regina & George's Wedding"
    from_email = settings.EMAIL_HOST_USER
    to_email = rsvp.email
    context = {
        "domain": settings.DOMAIN,
        "rsvp": rsvp,
        "guests": guests
    }

    text_content = render_to_string("email/receipt.txt", context=context)
    html_content = render_to_string("email/receipt.html", context=context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
