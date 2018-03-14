import csv
import statistics

Date = []
Revenue = []

with open('budget_data2.csv', newline="") as csvfile:
    ignore = csvfile.readline()
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(row[1])


Total_Months = len(Date)
     
New_Revenue = [int(x) for x in Revenue]
Total_Revenue = sum(New_Revenue)
Total_Revenue_Dollar = '${:,.2f}'.format(Total_Revenue)

Monthly_Change = [y-x for x, y in zip(New_Revenue, New_Revenue[1:])]

Average_Monthly_Change = statistics.mean(Monthly_Change)
Avg_Monthly_Change_Dollar = '${:,.2f}'.format(Average_Monthly_Change)

Max_Monthly_Change = (max(Monthly_Change))
Max_Monthly_Change_Dollar = '${:,.2f}'.format(Max_Monthly_Change)


x = Max_Monthly_Change
Index_of_Monthly_Change_Max = (Monthly_Change.index(x))

Min_Monthly_Change = (min(Monthly_Change))
Min_Monthly_Change_Dollar = '${:,.2f}'.format(Min_Monthly_Change)


print("Total Months:", Total_Months)

print("Total Revenue:",Total_Revenue_Dollar)

print("Average Revenue Change: ", Avg_Monthly_Change_Dollar)

print("Highest Increase in Revenue:", Max_Monthly_Change_Dollar)

print("Lowest Increase in Revenue:", Min_Monthly_Change_Dollar)





