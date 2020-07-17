import argparse
from math import log
from math import ceil


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)



calc_type = input(f'What do you want to calculate?\ntype "n" - for count of months,\n'
                  f'type "a" - for annuity monthly payment,\ntype "p" - for credit principal:\n')

if calc_type == 'n':
    credit_principal = int(input(f'Enter credit principal:\n'))
    monthly_payment = int(input(f'Enter monthly payment:\n'))
    credit_interest = float(input(f'Enter credit interest:\n'))
    nominal_interest_rate = credit_interest / (12 * 100)
    n_periods = ceil(log((monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal)),
                         1 + nominal_interest_rate))

    years = n_periods // 12
    months = n_periods % 12

    if years > 1 and months > 1:
        print(f'You need {years} years and {months} months to repay this credit!')
    elif (years == 1 and months > 1) or (years > 1 and months == 1):
        print(f'You need {years} years and {months} month to repay this credit!' if months == 1
              else f'You need {years} year and {months} months to repay this credit!')
    elif years == 1 and months == 1:
        print(f'You need {years} year and {months} month to repay this credit!')
    else:
        print(f'You need {months} months to repay this credit!' if years == 0
              else f'You need {years} years to repay this credit!')

elif calc_type == 'a':
    credit_principal = int(input(f'Enter credit principal:\n'))
    period_count = int(input(f'Enter count of periods:\n'))
    credit_interest = float(input(f'Enter credit interest:\n'))
    nominal_interest_rate = credit_interest / (12 * 100)
    annuity_payment = ceil(credit_principal * ((nominal_interest_rate * (1 + nominal_interest_rate) ** period_count) /
                                               ((1 + nominal_interest_rate) ** period_count - 1)))
    print(f'Your annuity payment = {annuity_payment}!')

elif calc_type == 'p':
    monthly_payment = float(input(f'Enter monthly payment:\n'))
    period_count = int(input(f'Enter count of periods:\n'))
    credit_interest = float(input(f'Enter credit interest:\n'))
    nominal_interest_rate = credit_interest / (12 * 100)

    credit_principal = round(monthly_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** period_count) /
                                                ((1 + nominal_interest_rate) ** period_count - 1)))
    print(f'Your credit principal = {credit_principal}!')

    # if credit_principal % count_months > 0:
    #     payment = (credit_principal // count_months) + 1
    #     last_payment = credit_principal % payment
    #     print(f'Your monthly payment = {payment} with last month payment = {last_payment}.')
    # else:
    #     payment = credit_principal / count_months
    #     print(f'Your monthly payment = {payment}')
