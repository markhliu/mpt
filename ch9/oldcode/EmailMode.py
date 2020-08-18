# import the needed modules
import smtplib

# make sure you put mySAY.py and mysr.py in the same folder as this program
from mySAY import printAndSAY
from mysr import VTT

# define the Email() function
def Email():
    #build a dictionary of names and emails
    emails = {'mark':'mark.liu@uky.edu',
             'sarah':'Sarah email address here',
             'chris':'Chris email address here'}
    #different email providers have different domain name and port number
    mysmt = smtplib.SMTP('smtp.gmail.com', 587)
    mysmt.ehlo()
    mysmt.starttls()
    #use your own login info; you may need an app password
    mysmt.login('ukmarkliu@gmail.com', 'udguvodbyyayroai')
    #voice input the name of of the recipeint
    printAndSAY('who do you want to send the email to?')
    name=VTT().lower()
    email=emails[name]
    printAndSAY(f"you just said {name}.")
    #voice input the subject line
    printAndSAY('what is the subject line?')
    subline=VTT()
    printAndSAY(f"you just said {subline}.")
    #voice input the email content
    printAndSAY ('what is the email content?')
    content=VTT()
    printAndSAY(f"you just said {content}.")
    #send the actual email
    mysmt.sendmail('ukmarkliu@gmail.com', email, 
                   f'Subject: {subline}.\nHello, {content}.')
    {}
    printAndSAY('ok, email sent')
    mysmt.quit()
