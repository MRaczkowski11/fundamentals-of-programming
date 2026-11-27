import re

def email_sender(email):
    pattern = r'From:.*<(.+)>'
    return re.search(pattern, email).group(1)


# Pobieramy adres odbiorcy
def email_recipient(email):
    pattern = r'To:.*<(.+)>'
    return re.search(pattern, email).group(1)


# Pobieramy temat wiadomości
def email_subject(email):
    pattern = r'Subject: (.+)'
    return re.search(pattern, email).group(1)


# Pobieramy treść wiadomości
def email_body(email):
    pattern = r'\n\n(.*)'
    return re.search(pattern, email, re.DOTALL).group(1)