import matplotlib.pyplot as plt
import numpy as np
print("How many times have you had caffeine today?")
n_times = input()
amount_remaining = 0
y = 0
for i in range(int(n_times)):
    print("---------------------------------")
    print("Enter the mg of caffeine consumed at event number " + str(i+1))
    print("---------------------------------")
    print("Espresso Shot: 70mg ")
    print("Cup of Coffee: 100mg ")
    print("Starbucks coffee: 200-400mg ")
    amount_consumed = float(input())
    print("---------------------------------")
    print("How many hours ago was this consumed? You may use decimals if you like. ")
    time_consumed = float(input())-0.5 ##subtract 30min absorption time
    amount_remaining += amount_consumed*(np.exp(-time_consumed/10)) #calculate remaining mg using exponential decay and 5h half-life
    #Plot caffeine graph below but don't show yet
    x = np.linspace(0, 12, 12)
    y += amount_consumed*(np.exp((-time_consumed-x)/10))    
    fig, ax = plt.subplots()
    plt.grid(axis='y', color='0.95')
    ax.plot(x, y, linewidth=2.0)
print("---------------------------------")
print("There is " + str(int(amount_remaining)) + "mg of caffeine left in your system. Press enter to plot your projected future caffeine concentration.")
user_yes_plot = input()
print("---------------------------------")
plt.xlabel("Hours since now")
plt.ylabel("mg of caffeine remaining")
plt.show()
