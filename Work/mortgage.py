# mortgage.py
#
# Exercise 1.7
mortgage = 500000
rate = 0.05
monthly_payment = 2684.11
years = 30
total_paid = 0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while mortgage > 0:
    months = months + 1
    if (months >= extra_payment_start_month) & (months <= extra_payment_end_month):
        extra_flag = 1
    else:
        extra_flag = 0

    mortgage = mortgage * (1 + rate/12) - (monthly_payment + extra_payment * extra_flag)
    total_paid = total_paid + (monthly_payment + extra_payment * extra_flag)
    print(months, round(total_paid), round(mortgage))

print("Total Paid", total_paid)
print("Months", months)
