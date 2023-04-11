import unittest
from my_library import (
    send_email,
    attach_file,
    read_email_content,
    read_email_title,
    send_notification,
    sendSlackWebhook,
)


class TestMyLibrary(unittest.TestCase):
    # Unit test 1
    def test_send_email(self):
        # Test sending an email to a valid email address
        result = send_email("kwsong9212@naver.com", "test subject", "test message")
        self.assertTrue(result)

        # Test sending an email to an invalid email address
        result = send_email("invalidemail", "test subject", "test message")
        self.assertFalse(result)

    # Unit test 2
    def test_attach_file(self):
        # Test attaching a file to an email
        result = attach_file("kwsong9212@naver.com", "test subject", "test message", "sample_file.txt")
        self.assertTrue(result)

        # Test attaching a non-existent file to an email
        result = attach_file("example@naver.com", "test subject", "test message", "non_existent_file.txt")
        self.assertFalse(result)

    # Unit test 3
    def test_read_email_content(self):
        # Test reading email content from a valid email address
        result = read_email_content("kwsong9212@naver.com")
        self.assertIsNotNone(result)

        # Test reading email content from an invalid email address
        result = read_email_content("invalidemail")
        self.assertIsNone(result)

    # Unit test 4
    def test_read_email_title(self):
        # Test reading email title from a valid email address
        result = read_email_title("kwsong9212@naver.com")
        self.assertIsNotNone(result)

        # Test reading email title from an invalid email address
        result = read_email_title("invalidemail")
        self.assertIsNone(result)

    # Unit test 5
    def test_send_notification(self):
        # Test sending a notification
        result = send_notification("https://hooks.slack.com/services/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")
        self.assertTrue(result)

    # Unit test 6
    def test_sendSlackWebhook(self):
        # Test sending a Slack webhook
        result = sendSlackWebhook("test message")
        self.assertTrue(result)

    # An integration Test between sending an email and attaching a file.
    def test_send_email_with_attachment(self):
        # Test sending an email with an attachment
        email_address = "kwsong9212@naver.com"
        subject = "test subject"
        message = "test message"
        file_path = "/Users/keunwoo/project-proposals-s2023/project_2023/project_progress/my_library/sample_file.txt"

        # Send the email with attachment
        result = send_email_with_attachment(email_address, subject, message, file_path)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
