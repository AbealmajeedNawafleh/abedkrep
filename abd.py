# DataPrebKit
# Abedalmajeed Nawafleh


from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues
# show the data with NAN values
DataWithNullValues.isna()
# here I show the numbers of the NAN values at all columns
DataWithNullValues.isna().sum()
# here i will show the sum of all null values in data fram
DataWithNullValues.isna().sum().sum()


# **********************************************************************************************************************************


# Filling Null Values Using fillna()
DataWithNullValues
# if we want filling null values only in any one colunm we will do :

DataWithNullValues['society'] = DataWithNullValues['society'].fillna(0)
# note that null values replaced with zero
DataWithNullValues
# now i will replace all null values with zero
DataWithNullValues = DataWithNullValues.fillna(0)
DataWithNullValues
# note that all null values convert to zero
DataWithNullValues.isnull().sum()
DataWithNullValues.isnull().sum().sum()
# now we want to do this process easier using functions :


def ProcessNullValues(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.fillna(0)
    else:
        print('There are not Null Values')
    return nameOfFile


# here we will save the new processed data in new name.
ProcessDataWithNullValues = ProcessNullValues(DataWithNullValues)
# show the process data
ProcessDataWithNullValues
ProcessDataWithNullValues.isnull().sum().sum()


# *********************************************************************************************************************************


# Filling Null Values with a previous value
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues
# using the same function with some edit


def ProcessNullValuesWithePreviousValue(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.fillna(method='pad')
    else:
        print('There are not Null Values')
    return nameOfFile


# here we will save the new processed data in new name.
ProcessDataWithNullValues = ProcessNullValuesWithePreviousValue(
    DataWithNullValues)
# show the process data
# note that all null values replaced by the previous value
ProcessDataWithNullValues
ProcessDataWithNullValues.isnull().sum().sum()


# **********************************************************************************************************************************************


# Filling Null Values with a next value
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')

DataWithNullValues
# using the same function with some editing


def ProcessNullValuesWitheNextValue(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.fillna(method='bfill')
    else:
        print('There are not Null Values')
    return nameOfFile


# here we will save hte new processed data in new name to save it.
ProcessDataWithNullValues = ProcessNullValuesWitheNextValue(DataWithNullValues)
# show the process data
# note that all null values replaced by the next value
# note that the last value is equal zero but there isn't next value to replace NAN with it ,so we will fill it by zero:
ProcessDataWithNullValues
ProcessDataWithNullValues.isna().sum().sum()
ProcessDataWithNullValues = ProcessDataWithNullValues.fillna(0)
ProcessDataWithNullValues


# ***********************************************************************************************************************************


# Filling Null Values with adjacent value
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues
# using the same function with some editing


def ProcessNullValuesWitheAdjacentValue(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.fillna(method='pad', axis=1)
    else:
        print('There are not Null Values')
    return nameOfFile


# here we will save hte new process data in new name to save it.
ProcessDataWithNullValues = ProcessNullValuesWitheAdjacentValue(
    DataWithNullValues)
# show the process data
ProcessDataWithNullValues
# note that all null values replaced by the adjacent value
ProcessDataWithNullValues.isnull().sum().sum()

# way 2
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues

# using the same function with some editing


def ProcessNullValuesWitheAdjacentValue2(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.fillna(method='bfill', axis=1)
    else:
        print('There are not Null Values')
    return nameOfFile


# here we will save hte new process data in new name to save it.
ProcessDataWithNullValues = ProcessNullValuesWitheAdjacentValue2(
    DataWithNullValues)
# show the process data
ProcessDataWithNullValues
# note that all null values replaced by the adjacent value
ProcessDataWithNullValues.isnull().sum().sum()

# **********************************************************************************************************************************
# Replace () function
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues
# this fuction replace NAN data with any data you select it .
DataWithNullValuesReplace = DataWithNullValues.replace(
    to_replace=np.nan, value=9999)
DataWithNullValuesReplace
# using the same function with some editing


def DataWithNullValuesReplace(nameOfFile):
    if nameOfFile.isnull().sum().sum() > (0):
        nameOfFile = nameOfFile.replace(to_replace=np.nan, value=9999)
    else:
        print('There are not Null Values')
    return nameOfFile


DataWithNullValuesReplace(DataWithNullValues)
# using this func we can replace any value ever it not missing value , for example:
replacedData = DataWithNullValues.replace(to_replace=1, value=3333)
replacedData

# ***********************************************************************************************************************************
# using interpolation
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
DataWithNullValues
# note that in row number 13316 there is NAN number in balcony colunm
DataWithNullValues['balcony'] = DataWithNullValues['balcony'].interpolate(
    method='linear')
# note that in row number 13315 the value interplated to 0.5 in balcony column becouse it between [0 and 1]
DataWithNullValues


# ******************************************************************************************************************************************


# Categorical Data Encoding:
# dumies
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')
catf = ['area_type', 'availability', 'location', 'size', 'society']
x = pd.get_dummies(DataWithNullValues.loc[0:10, :], columns=catf)
x


# way2
# read the csv file that has the null values to procces it.
DataWithNullValues = pd.read_csv(
    'C:\\Users\\96277\\Desktop\\Dataset\\Data with Null Values\\Bengaluru_House_Data.csv')

lbl = LabelEncoder()
DataWithNullValues.area_type = lbl.fit_transform(DataWithNullValues.area_type)
