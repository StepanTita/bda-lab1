# Classifying last name and country of origin

This is a small notebook that tries to compare various approaches toward the classification of highly unbalanced data. 
Results:
- We utilize RNN and CNN here for classifying the last names' countries of origin and retrieve the top 3 results.
- Usually, the correct answer is between the top 3. Rarely it is not in the list. 
- Even when the last name cannot be uniquely identified, e.g., Russian and Ukrainian, the models usually do well
by having both languages in the top 3. This means the extracted patterns are descriptive and extrapolated
