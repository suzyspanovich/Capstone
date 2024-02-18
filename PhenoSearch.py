#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

#Function to generate random positive or negative for a letter based on given probabilities
def generate_pos_neg(prob_pos):
    return np.random.choice(['Positive', 'Negative'], p=[prob_pos, 1-prob_pos])

#Setting the statistics for each letter
letter_statistics = {
    'V': 0.95,  # Probability of being positive for letter V
    'W': 0.25,  # Probability of being positive for letter W
    'X': 0.72,  # Probability of being positive for letter X
    'Y': 0.50,  # Probability of being positive for letter Y
    'Z': 0.13   # Probability of being positive for letter Z
}

#Generating donors
num_donors = 1000
donors_data = {'Donor_ID': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

for i in range(num_donors):
    donors_data['Donor_ID'].append(i+1)
    for letter, prob_pos in letter_statistics.items():
        donors_data[letter].append(generate_pos_neg(prob_pos))

#Creating DataFrame
donors_df = pd.DataFrame(donors_data)

#Option to Save DataFrame to CSV
donors_df.to_csv('donors_database.csv', index=False)

#Printing the first five donors in table form
print("\nFirst five donors:")
print(donors_df.head())


# In[4]:


#Searching for donors with a combination of negative letters
def search_donors(combination):
    filtered_donors = donors_df.copy()
    for letter in combination:
        filtered_donors = filtered_donors[filtered_donors[letter] == 'Negative']
    return filtered_donors

#Example: Searching for donors with negative letters 'V', 'W', 'X', and 'Y'
negative_combination = ['V', 'W', 'X']
filtered_donors = search_donors(negative_combination)

# Displaying the filtered donors
print("\nDonors with negative letters", negative_combination)
if not filtered_donors.empty:
    print(filtered_donors)
else:
    print("No donors found with negative letters", negative_combination)


# In[ ]:




