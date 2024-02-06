import asyncio
import imaplib
import email
import re

from block import lock


email_user = ""
email_pass = ""
mail_server = "" # imap.rambler.ru

async def main():
    mail = imaplib.IMAP4_SSL(mail_server)
    mail.login(email_user, email_pass)
    mail.select("inbox")

    while True:
        status, messages = mail.search(None, "(UNSEEN)")
        message_ids = messages[0].split()

        for message_id in message_ids:
            result, message_data = mail.fetch(message_id, "(RFC822)")
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)
            from_mail = re.findall('<(.*?)>', msg.get("From"))[0]
            print(from_mail)
            res = await lock(from_mail)
            print(f'{res}\n')
            
        await asyncio.sleep(5)

asyncio.run(main())
