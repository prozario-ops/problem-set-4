'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

import seaborn as sns
import matplotlib.pyplot as plt


def scatter_charge_type(pred_universe):
    """
    Scatterplot with felony and nonfelony predictions.
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file
    """
    sns.lmplot(
        data= pred_universe,
        x ='prediction_felony',
        y='prediction_nonfelony',
        hue ='has_felony_charge' ,
        fit_reg=False
    )

    plt.savefig('./data/part5_plots/scatter_charge_type.png')
    plt.close()
    print("#1 The group of dots on the right side has higher predicted felony risk and is mostly made up of people with a current felony charge.")



def scatter_calibration(pred_universe):
    """
    Scatterplot prediction felony vs actual felony rearrest.
    args:        pred_universe: dataframe with prediction universe data
    returns:     None, saves plot as PNG file
    """
    sns.lmplot(
        data=pred_universe,
        x='prediction_felony' ,
        y='y_felony',
        fit_reg=False
    )

    plt.savefig('./data/part5_plots/scatter_calibration.png')
    plt.close()

    print("#2 The model appears somewhat calibrated because higher predicted probabilities include more actual rearrests, but the separation is not perfect.")

