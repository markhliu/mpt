import smtplib

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
# Ask for the name of of the recipeint
name = input('Who do you want to send the email to?\n')
email = emails[name]
print(f"You just said {name}.")
# Ask for the subject line
subline = input('What is the subject line?\n')
print(f"You just said {subline}.")
# Ask for the email content
content = input('What is the email content?\n')
print(f"You just said {content}.")
# Send the actual email
mysmt.sendmail('ukmarkliu@gmail.com', email, 
               f'Subject: {subline}.\nHello, {content}.')
{}
print('Ok, email sent')
mysmt.quit()
