import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    plt.plot(years, [slope * year + intercept for year in years], label='First line of best fit')
    
    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    slope, intercept, r, p, se = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years_2 = range(2000, 2051)
    plt.plot(years_2, [slope * year + intercept for year in years_2], label='Second line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()