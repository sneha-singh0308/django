import sendgrid
from sendgrid.helpers.mail import *

def send_notification(user, comment_text):
    my_client = sendgrid.SendGridAPIClient(apikey='SG')
    # api_key : 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

    from_email = Email("snirmla@gmail.com")
    to_email = Email("snehasingh95@gmail.com")
    subject = "Post Notification"
    content = Content("text/plain", str(user) +"commented" +str(comment_text))
    mail = Mail(from_email, subject, to_email, content)
    response = my_client.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)