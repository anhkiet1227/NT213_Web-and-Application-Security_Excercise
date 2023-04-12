import pandas as pd
import socket

# Load CSV file
input_file = 'cau1.csv'  # Replace with your CSV file name
output_file = 'domains_with_ip.csv'  # Replace with desired output file name

# Read CSV file into a DataFrame
df = pd.read_csv(input_file)

# Add IP Address column to DataFrame
df['IP Address'] = ''

# Resolve IP addresses for domains
for index, row in df.iterrows():
    try:
        # Get domain name from row
        domain = row['Domain']

        # Resolve IP address
        ip = socket.gethostbyname(domain)
        df.at[index, 'IP Address'] = ip

    except socket.error:
        # Error occurred while resolving IP address
        df.at[index, 'IP Address'] = 'N/A'

# Write DataFrame to CSV output file
df.to_csv(output_file, index=False)

print("IP addresses for domains have been written to", output_file)
