# import pandas
import pandas as pd

# read excel file, specifying sheet name, parse dates, column index
df = pd.read_excel('downloads/Employment and Unemployment Rates Feb 1971 to May 2023.xlsx',
                        sheet_name= 'data',
                        parse_dates=["Date"],
                        index_col="Date")

# import matplotlib
import matplotlib.pyplot as plt

# create a figure and set of subplots
fig, ax = plt.subplots()

# plot Employment as Blue
ax.plot(df.index, df["Employment %"],
        color='blue')

# set title, x and y labels
ax.set_title("UK Employment and Unemployment Rates Feb 1971 to May 2023")
ax.set_xlabel('Date')
ax.set_ylabel('Employment %', color='blue')

# set y label colour
ax.tick_params('y', colors='blue')

# create a twin axes sharing the x axis
ax2 = ax.twinx()

# plot Unemployment as Red
ax2.plot(df.index,
         df["Unemployment %"],
         color='red')

#set y label colour
ax2.set_ylabel('Unemployment %',
        color='red')

# set y label colour
ax2.tick_params('y', colors='red')

# show the graph
plt.show()
