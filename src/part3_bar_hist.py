'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta(pred_universe):
    '''
    Using the pre_universe data frame, create a bar plot for the fta column.
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file
    '''
    sns.barplot(data=pred_universe, x='fta', y ='prediction_felony')
    plt.savefig('./data/part3_plots/fta_barplot.png')
    plt.clf()

# 2. Hue the previous barplot by sex
def barplot_fta_sex(pred_universe):
    '''
    Hue the previous barplot by sex
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file
    '''
    sns.barplot(data=pred_universe, x='fta', y='prediction_felony', hue='sex')

    plt.savefig('./data/part3_plots/fta_barplot_sex.png')
    plt.clf()

# 3. Plot a histogram of age_at_arrest
def histogram_age(pred_universe):
    '''
    Plot a histogram of age_at_arrest
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file   

    '''
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histogram.png')
    plt.clf()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_bins(pred_universe):
    '''
    Plot histogram with custom age bins
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file

    '''
    bins = [18,21,30,40, 100]

    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.savefig('./data/part3_plots/age_histogram_bins.png')
    plt.clf()