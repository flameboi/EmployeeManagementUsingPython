#!/usr/bin/env python
# coding: utf-8

# # SUBJECT:  2CS404 PSC LEARNING ASSIGNMENT
# ROLL NO:  19BCE517,
# Semester: 4th,
# Name:     Nimbark Param,
# Division: C

# Note: When you evaluate my code, make sure you have put both csv files in same folder which I have attached in zip file : "Employee.csv" and "Employee2.csv"

# # QUESTION 1:
# Create Employee.CSV file which contain following
# details of employee.
# Employee: Name, City, Company name, Basic
# Salary
# Take input from the user and store 10 records in file [10 Marks]:

# In[1]:


#imoporting packages
import matplotlib.pyplot                                  
import pandas as pd
import numpy as np


#creating a fuction that creates dataframe containing fields : Name, City, CompanyName, BasicSalary


def values_insert():                                                 #creating function : values_insert
    print("Enter Name, City, Company name Basic Salary:")   
    
    df = pd.DataFrame(
        
                     {
                       "Name":input("Enter name:"),                  #takes "name" from user and stores in dataframe df
                       "City":input("Enter city:"),                  #takes "city" name from user and stores in dataframe df
                       "CompanyName":input("Enter Company name:"),   #takes "Companyname" from user and stores in dataframe df
                       "BasicSalary":input("Enter Salary:")          #takes "salary" from user and stores in dataframe df
                      }
                        for i in range(10))                           #for loop to iterate loop 10 times which will take values 10 times from user 
    
    
    print(df)                                                        #printing dataframe values
    
    
    #Converting DataFrame to CSV 
    
    
    df.to_csv('Employee.csv')                                        #df DataFrame will be converted to "Employee.csv" file                                      
    

#Calling a function that we just created:    
    
values_insert()                                                      #Function call


# # Explaination:
# 
# Here, I have created a function named "vales_insert" in which I have created a DataFrame named "df", using pandas               which is taking These vallues: Name, City, Company name, Basic Salary.
#              
# At the end of the dataframe df, I have used for loop with range = 10 which will iterate the process of taking                   input from user 10 times and store values in dataframe df.
#               
# After that we have used "to_csv()" function to convert our data frame into csv file.
#               
# And at last, we have called our function "values_insert" which will seek processes to continue                              

# # Question 2:
# Update Employee.CSV file as follow:
# Add column Gross salary (GS)
# GS = Basic + DA( 12% of Basic) + HRA(5% of Basic)                                              [10 Marks] :

# In[18]:


#importing packages
import pandas as pd

df = pd.read_csv (r'Employee.csv')                                 #reading data from "Employee.csv" file


BasicSalary = df['BasicSalary']                                    #Assigning values of BasicSalary from dataframe to variable


#GS = Basic + DA( 12% of Basic) + HRA(5% of Basic)

DA = (BasicSalary * 12) / 100                                      #12% of DA
HRA = (BasicSalary * 5) / 100                                      #5% of HRA
GSS = BasicSalary + DA + HRA                                       #GSS = Variable that holds calculated Gross Salary
print("Gross Salary is:")
print(GSS)                                                         #printing Gross Salary of all users

GS = pd.DataFrame(GSS)                                             #creating DataFrame of Gross Salary

dff=pd.DataFrame(df)                                               #copying df DataFrame to dff object
dff['Gross Salary']=GS                                             #ADDING GROSS SALARY DATAFRAME TO dff DATAFRAME
                                                             

dff.to_csv('Employee2.csv')                                        #Making another csv having updated column "Gross Salary"

dff                                                                #Printing dff DataFrame Including Gross Salary Column


# # Explaination:
# Here, I have first opened and read values of Employee.csv file that we created in question 1.
# 
# Then, I assigned  values of BasicSalary from dataframe to variable called BAsicSalary
# 
# After that I created GSS variable and assigned values to calculate Gross Salary :
# DA = (BasicSalary * 12) / 100                                     
# HRA = (BasicSalary * 5) / 100                                      
# GSS = BasicSalary + DA + HRA
# 
# Then i created dataframe of Gross Salary And added Column "GrossSalary" in our DataFrame df.
# 
# After that, I converted dff to 2nd csv file named "Employee2.csv" using : dff.to_csv('Employee2').
# 

# # QUESTION 3:
# Plot graph Employee Vs salary [10 Marks]

# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

hr = pd.read_csv('Employee2.csv')                            #Reeading data from Employee2.csv and storing it into hr object                         
col_names = hr.columns.tolist()                              #Converting DataFrames to list
print("Column names:")
print(col_names)                                             #printing column names
print("\n")
print("\nEmployee VS Salary:")
hr.head()                                                   #printing Head part of the dataframe                               


# In[20]:


hr=hr.rename(columns = {'BasicSalary':'gss'})              #Changing name of BasicSalary To gss for easy use


# In[21]:


hr.dtypes                                                  #Displaying datatypes of our List items


# In[22]:


hr.isnull().any()                       #Checking if there is any null values in any record (Important to avoid conflicts)


# In[23]:


hr.shape                                   #Shaping of all values


# In[24]:


hr['gss'].unique()                         #Using of unique constaraint for Basic Salary


# In[25]:


hr['gss']=np.where(hr['gss'] =='Name', 'EVS', hr['gss'])                #Combining Name and Basic Salary 
hr['gss']=np.where(hr['gss'] =='BasicSalary', 'EVS', hr['gss'])         #Combining Name and Basic Salary


# In[26]:


hr.groupby('gss').mean()                                                #Grouping of "Salary" and finding mean


# In[27]:


hr.groupby('Name').mean()                                               #Grouping of "Name" and finding mean


# In[30]:


import matplotlib.pyplot as plt
import pandas as pd

# a simple line plot

dff.plot(kind='bar',x='Name',y='BasicSalary', color='purple')                       #plotting graph 
plt.title('Employee VS Basic Salary:')
plt.savefig('EmployeeVsSalary.png')                                                 #To save PNG file of this graph


# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
ax = plt.gca()                                                                    #gca() to take multiple axes
dff.plot(kind='line',x='Name',y='BasicSalary', color='red', ax=ax)                #Taking multiple Axis
dff.plot(kind='line',x='Name',y='Gross Salary', color='green', ax=ax)
plt.title('Employee VS Basic Salary & Gross Salary:')
plt.show()
plt.savefig('EmployeeVsgss.png')                                                  #To save png file of this graph


# # Explaination:
# In this, I have first taken employee2.csv file as an input and read its contents
# Then I have converted its columns into list
# After that I have Grouped all column values and shaped them
# Then I checked for NULL values
# In next step, I used mean() to find mean of Salary and Name columns to plot values
# After that I plotted Employee VS Salary Graph using matplotlib.pyplot.
# 

# Explaination:

# # Question 4:
# Search record from file:
# 
# 1. User enter the name of city and display the
# information of all the employee belongs to that
# city. [5 Marks]
# 2. Display the list of employee company wise [5 Marks]

# In[78]:


import pandas as pd

#1st PART:

a = []                                                     #creating a string a to store city that user enters                    
a = input("\nenter city:")                                 #Taking city as an input from user
print ("\nyour city is:"  +a)                
print("\n")

a = a.split()                                               #converting string to list

dff=pd.DataFrame(df)                                        #Assigning df dataframe to dff

print("Displaying all information of Employee that belongs to " +a[0])                 
print("\n")

print(dff.loc[dff['City'].isin(a)])                       #using isin() to filter and display only cities which match with city entered by user


# # Explaination:
# Here, I have first created a string a[], then I have taken Input string from user (city)
# After that I converted string to list using split()
# Then Passed dataframe objest df object to dff
# And after, used isin() to filter and display all corresponding details only for columns where cities entered by user matches.
# 

# In[122]:


#2nd PART:

print("\n")

print("Displaying list of employees company wise:")
print("\n")
dff.sort_values(by='CompanyName', ascending=True)          #Here, I have used sort_values function to sort values by company name


# # Explaination: 
# In this I have used dff DataFrame in which sort_values() is used, which is sorting all details of employee by Company Name.

# # END OF THE ASSIGNMNET
# Thank You.
