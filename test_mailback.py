

import unittest

import mailback


class TestWithExample(unittest.TestCase):

    def setUp(self):
        self.emailer = mailback.Emailer(path="./mailback.example")
        self.email_to_send = self.emailer.build_message(
                    body="body-w4K45v", subject="subject-hEd4ki")

    def test_from(self):
        self.assertEqual(self.email_to_send["From"], "Your Name <your.address@example.com>")

    def test_subject(self):
        self.assertEqual(self.email_to_send["Subject"], "subject-hEd4ki")

    def test_body(self):
        self.assertEqual(self.email_to_send.get_payload(), "body-w4K45v")
