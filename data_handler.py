from datetime import datetime
from dateutil import parser
import csv
import numpy as np
import pytz

from inverter import get_runtime_ppv

async def collect(ip_address, csv_file):
    # Get the Watt value from the Inverter
    watts = await get_runtime_ppv(ip_address)
    zone = pytz.timezone('UTC')
    time = datetime.now(zone).isoformat()

    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer = writer.writerow([time,watts])

def summarize(csv_file, zone):
    data = np.genfromtxt(csv_file,
                unpack=True,
                names=['timestamp','watts'],
                dtype=None,
                delimiter=',',
                converters={0: lambda x: parser.parse(x).astimezone(zone)})

    x = data[0]
    y = data[1]

    # Calculate the total kWh generated.
    # Sum the readings and divide by 60. (Because we read every minute & there are 60 minutes in an hour).
    # Divide by 1,000 to get kWh
    # Only need 2 decimal places of precision

    kWh = round( (sum(y) / 60 / 1000), 2)
    return kWh, x, y
