from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_confirmation_email(user):
    context = {
        "email_text_detail": """Thanks for creating account.
                            Please verify your account""",
        "email": user.email,
        "activation_code": user.activation_code
    }

    msg_html = render_to_string("email.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Account activation"
    to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        "maviboncuaika@gmail.com",
        [to_emails],
        html_message= msg_html
    )