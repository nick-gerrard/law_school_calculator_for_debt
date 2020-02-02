#!/Users/nickgerrard/opt/anaconda3/bin/python

#List of original variables. Eventually, this will turn into imports of .txt or .csv files.

fin_aid = 20000
tuition = 64548
cost_of_living = 30000

#Loans are calculated by: Tuition + CoL - Financial_Aid
#Make sure to add the compound interest formulat for loans, including debt payment.
loans = (tuition + cost_of_living - fin_aid)

#Salary Section
#All lists go 75th percentile, 50th percentile, 25th percentile
est_salary = [0,180000,0]

est_bonus = [0,7000,0]

cost_of_living_post_ls = 85000

#functions to estimate net worth

def net_worth_after_1():
  total_positive = est_salary[1] + est_bonus[1]
  total_negative = ((fin_aid * -3) + (tuition * 3) + (cost_of_living * 3) + 
  cost_of_living_post_ls)
  net_worth = total_positive - total_negative
  print("Your net worth after 1 year post law school is {0}. Great Job!".format(net_worth))
  
def net_worth_after_5():
  total_positive = (est_salary[1] + est_bonus[1]) * 5
  total_negative = ((fin_aid * 3) + (tuition * 3) + (cost_of_living * 3) + 
  (cost_of_living_post_ls * 5))
   



net_worth_after_1()