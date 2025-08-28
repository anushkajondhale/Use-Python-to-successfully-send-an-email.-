# Python Email Sender 

This project demonstrates how to send an email using Python via SMTP.

## Steps
1. Copy `.env.example` to `.env` and fill in your credentials.
2. Load environment variables:
   ```bash
   source load_env.sh
   ```
3. Run the script:
   ```bash
   python3 send_email.py
   ```

## Notes
- If using Gmail, enable 2FA and create an App Password.
- Works with any SMTP server (e.g., Gmail, Outlook, custom).
