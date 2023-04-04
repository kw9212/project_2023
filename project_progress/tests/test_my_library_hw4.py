import unittest
import my_library

class TestMyLibrary(unittest.TestCase):
    # Unit test 1
    def test_send_email(self):
        # Test sending an email to a valid email address
        result = my_library.send_email("example@gmail.com", "test subject", "test message")
        self.assertTrue(result)

        # Test sending an email to an invalid email address
        result = my_library.send_email("invalidemail", "test subject", "test message")
        self.assertFalse(result)

    # Unit test 2
    def test_attach_file(self):
        # Test attaching a file to an email
        result = my_library.attach_file("example@gmail.com", "test subject", "test message", "sample_file.txt")
        self.assertTrue(result)

        # Test attaching a non-existent file to an email
        result = my_library.attach_file("example@gmail.com", "test subject", "test message", "non_existent_file.txt")
        self.assertFalse(result)

    # Unit test 3
    def test_read_email_content(self):
        # Test reading email content from a valid email address
        result = my_library.read_email_content("example@gmail.com")
        self.assertIsNotNone(result)

        # Test reading email content from an invalid email address
        result = my_library.read_email_content("invalidemail")
        self.assertIsNone(result)

    # Unit test 4
    def test_read_email_title(self):
        # Test reading email title from a valid email address
        result = my_library.read_email_title("example@gmail.com")
        self.assertIsNotNone(result)

        # Test reading email title from an invalid email address
        result = my_library.read_email_title("invalidemail")
        self.assertIsNone(result)

    # Unit test 5
    def test_send_notification(self):
        # Test sending a notification
        result = my_library.send_notification()
        self.assertTrue(result)

    # Unit test 6
    def test_sendSlackWebhook(self):
        # Test sending a Slack webhook
        result = my_library.sendSlackWebhook("test message")
        self.assertTrue(result)

    # An integration Test between sending an email and attaching a file.
    def test_send_email_with_attachment(self):
        # Test sending an email with an attachment
        email_address = "example@gmail.com"
        subject = "test subject"
        message = "test message"
        file_path = "sample_file.txt"

        # Send the email with attachment
        result = my_library.send_email_with_attachment(email_address, subject, message, file_path)

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()