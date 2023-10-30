import openpyxl, warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category = UserWarning)
    wb = openpyxl.load_workbook('Personal_Budget.xlsx', data_only = True)
    wb = wb['Balance & Tracking']

def get_balance():

    # This function extract data from Personal_Budget.xlsx.
    annual_balance = wb['E4'].value
    current_balance = wb['E5'].value
    return f'The current balance is $ {current_balance}.'\
           f'The annual balance is $ {annual_balance}.' 
