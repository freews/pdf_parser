import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_report():
    # --- Configuration ---
    # 보안을 위해 비밀번호는 환경변수에서 가져오거나 실행 시 입력받는 것이 좋습니다.
    # Gmail의 경우 '앱 비밀번호'를 사용해야 합니다.
    # https://myaccount.google.com/apppasswords
    
    sender_email = input("Enter your email address (e.g., your@gmail.com): ")
    sender_password = input("Enter your email password (or App Password): ")
    receiver_email = input("Enter receiver email address: ")
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    subject = "[Report] DeepSeek OCR vs Qwen VL Comparison Results"
    report_file = "comparison_report_kr.md"
    
    # --- Create Email ---
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    body = "Please find the attached comparison report.\n\nBest regards,\nLLM Assistant"
    msg.attach(MIMEText(body, 'plain'))
    
    # --- Attach File ---
    try:
        if os.path.exists(report_file):
            with open(report_file, "r", encoding="utf-8") as f:
                # 본문에 내용을 추가할 수도 있습니다.
                content = f.read()
                # msg.attach(MIMEText(content, 'plain')) # 본문에 추가하려면 주석 해제
                
            # 파일 첨부
            attachment = open(report_file, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {report_file}")
            msg.attach(part)
            attachment.close()
        else:
            print(f"Error: Report file '{report_file}' not found.")
            return

        # --- Send Email ---
        print("Connecting to server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        print("\n✅ Email sent successfully!")
        
    except Exception as e:
        print(f"\n❌ Failed to send email: {e}")
        print("Tip: If using Gmail, make sure you are using an 'App Password', not your login password.")

if __name__ == "__main__":
    send_email_with_report()
