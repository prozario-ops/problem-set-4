'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?

import seaborn as sns
import matplotlib.pyplot as plt
import os


def catplot_felony(pred_universe):
    """
    Plot prediction for felony rearrest by charge type.
    """
    sns.catplot(
        data = pred_universe,
        x='has_felony_charge' ,
        y='prediction_felony',
        kind='bar'
    )
    plt.savefig('./data/part4_plots/catplot_felony.png')
    plt.close()


def catplot_nonfelony(pred_universe):
    """
    Plot prediction for nonfelony rearrest by charge type.
    """

    sns.catplot(
        data= pred_universe,
        x ='has_felony_charge',
        y='prediction_nonfelony',

        kind='bar'
    )
    plt.savefig('./data/part4_plots/catplot_nonfelony.png')
    plt.close()

    print(
        "#2 The difference between the plots may be explained by the fact that "
        "the model may be better at predicting felony rearrest than nonfelony rearrest, "
        "or that felony charge history is more strongly associated with felony rearrest "
        "than it is with nonfelony rearrest."
    )


def catplot_felony_hue(pred_universe):
    """
    Plot felony rearrest by charge type with actual felony rearrest as hue.
    """

    sns.catplot(
        data=pred_universe,
        x ='has_felony_charge',
        y=  'prediction_felony',
        hue= 'y_felony',
        kind='bar'
    )

    plt.savefig('./data/part4_plots/catplot_felony_hue.png' )
    plt.close()

    print(
        "#3 Answer: This suggests the model heavily relies on current felony charge status. "
        "Individuals with current felony charges may receive higher predicted risk scores "
        "even when they are not actually rearrested for a felony later on."
    )