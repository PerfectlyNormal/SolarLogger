
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Plotter:
    def __init__(self, timezone, city, installed_max):
        self._timezone = timezone
        self._city = city
        self._installed_max = installed_max

    def generate_image(self, today, kWh, x, y, png_file):
        # Start the graph
        fig, ax = plt.subplots(figsize=(16,9))

        #   Colour Masks
        min = 500
        step = 500
        i = 0

        colors = ["#F0FF00", "#F1ED00", "#F2DB00", "#F2D300", "#F3C100", "#F4B800", "#F5A700", "#F59E00", "#F69500", "#F68C00", "#F78300", "#F77B00", "#F87200", "#F86900", "#F96000", "#F95700", "#FA4F00", "#FA4600", "#FB3D00", "#FB3400", "#FC2B00", "#FC2300", "#FD1A00", "#FD1100", "#FE0800", "#FF0000"]

        for color in colors:
            mask = y < min if i == 0 else y >= i
            plt.bar(x[mask], y[mask], width=.002, color=color)
            i += step

        #   X Axis
        hours = mdates.HourLocator(tz=self._timezone)
        hoursFmt = mdates.DateFormatter('%H:%M', tz=self._timezone)
        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(hoursFmt)

        day = x[0]
        x_start = day.replace(hour=5,  minute=0, second=0) # 0500
        x_end   = day.replace(hour=22, minute=0, second=0) # 2200

        ax.set_xlim(x_start, x_end)

        #   Y Axis
        ax.set_ylim(50, self._installed_max)

        #   Axis properties
        ax.grid(axis="y", color='#FFFFFF', linestyle='-', linewidth=0.5)

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate()

        #   Background Colour
        ax.set_facecolor("#1f77b4")

        #   Set the labels
        plt.xlabel(today)
        plt.ylabel('Generated Electricity (Watts)')
        plt.title('Solar Panels (' + self._city + ')\nGenerated ' + str(kWh) + 'kWh')

        #   Save the Image
        plt.savefig(png_file, bbox_inches='tight')
