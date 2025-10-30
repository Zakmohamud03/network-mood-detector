import os
import time
import matplotlib.pyplot as plt

# List of hosts to ping (you can update this list)
hosts = ['192.168.1.1', '192.168.1.2', 'google.com']

# Variables to track online/offline counts
online_count = 0
offline_count = 0

# Open the results file to write the ping status
with open("mood_results.txt", "w") as result_file:
    result_file.write("Network Mood Detector Results\n")
    result_file.write("============================\n")
    
    # Loop through the hosts and ping each
    for host in hosts:
        print(f"Pinging {host}...")
        response = os.system(f"ping -n 1 {host}")
        
        if response == 0:
            result = f"{host} is online"
            online_count += 1  # Increment online counter
        else:
            result = f"{host} is offline"
            offline_count += 1  # Increment offline counter
        
        # Write the result to the text file
        result_file.write(result + '\n')

        # Print the result to the terminal
        print(result)
        
        # Optional: Add a little delay to avoid overloading the system
        time.sleep(1)

# Inform the user that the script has finished running
print("Network Mood Detector completed. Check mood_results.txt for results.")

# Now, let's create a simple bar chart visualisation

# Labels for the bar chart
labels = ['Online', 'Offline']
# Data to plot (online and offline counts)
counts = [online_count, offline_count]

# Plotting the bar chart
plt.bar(labels, counts, color=['green', 'red'])

# Adding a title and label to the chart
plt.title('Network Mood Detection')
plt.ylabel('Count')

# Display the chart
plt.show()
