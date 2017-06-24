# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:41:34 2017

@author: Tanichka
"""

def count_m(first_sum, monthly_salary_save,r):
    sumsum = 0
    count_month = 0
    while sumsum < first_sum:
        i=0
        while i < 6:
            sumsum=(sumsum *r) / 12 + sumsum + monthly_salary_save 
            count_month += 1
            i += 1
            if sumsum < first_sum:
                break
        monthly_salary_save=monthly_salary_save*float(semi_annual_rise) + monthly_salary_save    
    return count_month

portion_down_payment=0.25
current_savings=0
annual_salary=input("annual_salary-годовая ЗП - ")
portion_saved=input("portion_saved-часть секономленого - ")
total_cost=input("total_cost-общая стоимость - ")
semi_annual_rise=input("semi_annual_rise - рост ЗП - ")
r = 0.0033

first_sum=(int(total_cost))*(float(portion_down_payment))
monthly_salary=int(annual_salary)/12
monthly_salary_save=monthly_salary*float(portion_saved)

mounth=count_m(first_sum, monthly_salary_save,r)
result = str(mounth)
print("Количество месяцев - " + result)

#sumsum=(sumsum *r) + sumsum + monthly_salary_save