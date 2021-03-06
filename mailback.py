#!/usr/bin/python3


"""
To use, create a file ~/.mailback with settings:

    [mailback]
    myself = Your Name <your.address@example.com>
    sendmail = /usr/sbin/sendmail-or-equivalent -x with -y arguments

Then pipe in the body and use the arguments as the subject:

    cat mydata | mailback This is the data
"""


import os
import shlex
import subprocess
import sys

from configparser import ConfigParser
from email.message import Message
from email.utils import formatdate


class Emailer:

    use_local_timezone = True

    def __init__(self, path=None):
        if path is None:
            path = os.path.join(os.environ['HOME'], ".mailback")
        if not os.path.exists(path):
            raise Exception("Missing config file: %r" % path)
        self.load_config_from(path)

    def load_config_from(self, filepath):
        parser = ConfigParser()
        parser.read(filepath)
        self.myself = parser.get("mailback", "myself")
        self.sendmail = parser.get("mailback", "sendmail")

    def build_message(self, subject=None, body=None):
        email = Message()
        email.add_header("From", self.myself)
        email.add_header("To", self.myself)
        email.add_header("Date", formatdate(None, self.use_local_timezone))
        if subject is not None:
            email.add_header("Subject", subject)
        if body is not None:
            email.set_payload(body)
        return email

    def send_message(self, email):
        args = shlex.split(self.sendmail)
        args.append(self.myself)
        sendmail = subprocess.Popen(args, stdin=subprocess.PIPE)
        sendmail.communicate(email.as_string().encode())

    def main(self):
        body = sys.stdin.read()
        if len(body) == 0:
            body = "(no body text received from pipeline)"
        subject = " ".join(sys.argv[1:])
        if len(subject) == 0:
            subject = "(no subject given on command line)"
        email = self.build_message(subject=subject, body=body)
        self.send_message(email)


if __name__ == '__main__':
    Emailer().main()
