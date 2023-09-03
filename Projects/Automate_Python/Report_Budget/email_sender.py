import take_report
import win32com.client as win32
import os
print('Sending Email.')

# Python-Outlook integration.
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

def send_email():

    # This function...
    take_report.hello()
    mail.to = input('Please type in the recipient: ')
    mail.Subject = 'Monthly Personal Budget Report.'
    mail.HTMLBody = r'''

    

    '''
    try:
        mail.Attachments.Add(os.path.join(os.getcwd(), "Relatório.png"))
        mail.Send()        
        return '\nThe email has sent with success.'
    except:
        return '\nSorry, something went wrong.' 
        
print(send_email())
