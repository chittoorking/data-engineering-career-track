# atasets may have columns that are most accurately modeled as Boolean values. However, pandas usually loads these as floats by default, 
# since defaulting to Booleans may have undesired effects like turning NA values into Trues.

# fcc_survey_subset.xlsx contains a string ID column and several True/False columns indicating financial stressors.
# You'll evaluate which non-ID columns have no NA values and therefore can be set as Boolean, then tell read_excel() to load them as such with the dtype argument.

# pandas is loaded as pd.

# Instructions 1
# Count NA values in each column of survey_data with isna() and sum(). Note which columns besides ID.x, if any, have zero NAs.


# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

# output:
#   ID.x                        0
# HasDebt                     0
# HasFinancialDependents      7
# HasHomeMortgage           499
# HasStudentDebt            502
# dtype: int64

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={"HasDebt":bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

# HasFinancialDependents  HasHomeMortgage  HasStudentDebt
# HasDebt                                                         
# False                     112.0              0.0             0.0
# True                      205.0            151.0           281.0
