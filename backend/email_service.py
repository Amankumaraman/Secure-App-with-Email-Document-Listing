import imaplib
import email
from email.header import decode_header
from config import IMAP_SERVER

def decode_mime_header(value):
    decoded_parts = decode_header(value)
    result = []
    for part, encoding in decoded_parts:
        try:
            if encoding:
                result.append(part.decode(encoding, errors="ignore"))
            else:
                result.append(part if isinstance(part, str) else part.decode("utf-8", errors="ignore"))
        except Exception as e:
            result.append("[Decoding Error]")
    return " ".join(result)

def fetch_emails(user_email, app_password):
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(user_email, app_password)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()
        emails = []

        for num in email_ids[-10:]:  # Get last 10 emails
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    sender = msg.get("From")
                    date = msg.get("Date")
                    
                    subject = msg.get("Subject") or "No Subject"
                    subject = decode_mime_header(subject)  

                    attachments = []
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_disposition = part.get("Content-Disposition")
                            if content_disposition and "attachment" in content_disposition:
                                filename = part.get_filename()
                                if filename:
                                    attachments.append(decode_mime_header(filename))  

                    emails.append({
                        "sender": sender or "Unknown",
                        "subject": subject,
                        "date": date or "No Date",
                        "attachments": attachments
                    })

        return emails  
    except Exception as e:
        return {"error": str(e)}  