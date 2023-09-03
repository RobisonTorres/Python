import win32com.client as win32
import os
print('Sending Email.')

# Python-Outlook integration.
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

def send_email():

    mail.to = input('Please type in the recipient: ')
    mail.Subject = input('Enter the email subject: ')
    mail.HTMLBody = input('\nType in the massage' + 
    r'''

    ''')
    option_attach = input(f'\nPress 1 if you want to add an attachment' \
                          f'or anything else to continue: ')
    if option_attach == '1':
        try:
            attach = input('Please type in the name of the attachment: ')
            mail.Attachments.Add(os.path.join(os.getcwd(), attach))
            mail.Send()        
            return '\nThe email has sent with success.'
        except:
            return '\nFail to send the email. Check the attachment name first.' 
        
print(send_email())
