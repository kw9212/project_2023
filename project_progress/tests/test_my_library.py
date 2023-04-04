import my_library

my_library.send_email("example@gmail.com", "example subject", "example message")
my_library.attach_file("example@gmail.com", "example subject", "example message", "path/to/file.txt")
my_library.read_email_content()
my_library.read_email_title()
my_library.send_notification()
my_library.sendSlackWebhook("example message")