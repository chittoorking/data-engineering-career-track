When loading a flat file, pandas infers the best data type for each column. Sometimes its guesses are off, particularly for numbers that represent groups or qualities instead of quantities.

Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. Let's specify the correct data types with the dtype argument.

pandas has been imported for you as pd.

Instructions 
Load vt_tax_data_2016.csv with no arguments and view the dataframe's dtypes attribute. Note the data types of zipcode and agi_stub.

Create a dictionary, data_types, specifying that agi_stub is "category" data and zipcode is string data.
Reload the CSV with the dtype argument and the dictionary to set the correct column data types.
View the dataframe's dtypes attribute.




# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub":"category",
			  "zipcode":str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())
