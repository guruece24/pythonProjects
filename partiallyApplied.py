from functools import partial


def create_email(userName, domain):
    return f"{userName}@{domain}"

guru1 = partial(create_email, domain="gmail.com")
guru2 = partial(create_email, domain="gmail.com")

print(guru1("guruece24"))
print(guru2("gurublr"))