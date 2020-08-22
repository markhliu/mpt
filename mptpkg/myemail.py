import smtplib

from mptpkg import voice_to_text, print_say

# Define the email() function
def email():
    # Build a dictionary of names and emails
    emails = {'mark':'mark.liu@uky.edu',
             'sarah':'Sarah email address here',
             'chris':'Chris email address here'}
    # Different email providers have different domain name and port number
    mysmt = smtplib.SMTP('smtp.gmail.com', 587)
    mysmt.ehlo()
    mysmt.starttls()
    # Use your own login info; you may need an app password
    mysmt.login('{your email here}', '{your password here}')
    # Voice input the name of the recipient
    print_say('Who do you want to send the email to?')
    name = voice_to_text().lower()
    email = emails[name]
    print_say(f"You just said {name}.")
    # Voice input the subject line
    print_say('What is the subject line?')
    subline = voice_to_text()
    print_say(f"You just said {subline}.")
    # Voice input the email content
    print_say('What is the email content?')
    content = voice_to_text()
    print_say(f"You just said {content}.")
    # Send the actual email
    mysmt.sendmail('ukmarkliu@gmail.com', email, 
                   f'Subject: {subline}.\nHello, {content}.')
    {}
    print_say('Ok, email sent.')
    mysmt.quit()
