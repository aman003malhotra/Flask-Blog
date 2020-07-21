import os

db_mail = os.environ.get('EMAIL_USER')
db_pass = os.environ.get('EMAIL_PASS')

print(db_mail)
print(db_pass)