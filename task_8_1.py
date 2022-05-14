import re


def email_parser(email_address: str):
    re_email = r'^\s*(?P<username>[^\.][a-z0-9!.]*[a-z0-9!])@(?P<domain>[a-z0-9]+\.[a-z]{1,63})$'
    email_match = re.match(re_email, email_address)

    if email_match:
        return email_match.groupdict()
    else:
        raise ValueError(f'wrong email: {email_address}')


if __name__=='__main__':

    print(email_parser('gb@gmail.com'))
    print(email_parser('gb!@gmail.com'))
    print(email_parser('gb-@gmail.com'))
