# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:25:06 2017

@author: Tanichka
"""
def count_m(first_sum, monthly_salary_save,r):
    sumsum = 0
    count_month = 0
    while sumsum < first_sum:
        sumsum=(sumsum *r) + sumsum + monthly_salary_save
        count_month+=1
    return count_month

portion_down_payment=0.25
current_savings=0
annual_salary=input("annual_salary-годовая ЗП - ")
portion_saved=input("portion_saved-часть секономленого - ")
total_cost=input("total_cost-общая стоимость - ")
r = 0.0033

first_sum=(int(total_cost))*(float(portion_down_payment))
monthly_salary=int(annual_salary)/12
monthly_salary_save=monthly_salary*float(portion_saved)

mounth=count_m(first_sum, monthly_salary_save,r)
print("Количество месяцев - " + mounth)