import os
import csv
import statistics

Date = []
Revenue = []

with open('budget_data_1.csv', newline="") as csvfile:
    ignore = csvfile.readline()
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(row[1])


Total_Months = len(Date)
     
New_Revenue = [int(x) for x in Revenue]
Total_Revenue = sum(New_Revenue)

Monthly_Change = [y-x for x, y in zip(New_Revenue, New_Revenue[1:])]


Average_Monthly_Change = statistics.mean(Monthly_Change)


Max_Monthly_Change = (max(Monthly_Change))


x = Max_Monthly_Change
Index_of_Monthly_Change_Max = (Monthly_Change.index(x))

Min_Monthly_Change = (min(Monthly_Change))


print("Total Months:", Total_Months)

print("Total Revenue: $",Total_Revenue)

print("Average Revenue Change: $", Average_Monthly_Change)

print("Highest Increase in Revenue: $", Max_Monthly_Change)

print("Lowest Increase in Revenue: $", Min_Monthly_Change)






    








        





        







    










