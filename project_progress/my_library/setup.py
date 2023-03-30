from setuptools import setup

setup(
    name='my_library',
    version='0.1.0',
    description='A library for sending and reading emails, attaching files, and sending Slack notifications',
    packages=['my_library'],
    install_requires=[
        'requests',
        'imaplib',
        'email'
    ],
    # Your name, your email address
    author='KeunWoo Song',
    author_email='ks3651@columbia.edu',
    url='https://github.com/kw9212/my_library',
)