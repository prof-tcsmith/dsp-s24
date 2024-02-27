# Assignment WE05 Decision Trees

## Instructions

1. Find a dataset for either regression or classification. The dataset should be large enough to train a model and test it. The dataset should be in a format that can be read by Python. The dataset should be from a reliable source. The dataset should be interesting to you - be as original as possible (don't just copy what a friend did)

2. Drop any variables that are not relevant to your analysis. For example, if you have an ID column.

3. Create a 70/30 test/training split

4. Check for missing values and handle appropriately
   1. Drop any rows or columns with too many missing values
   2. Impute missing values (mean or median for continuous, mode for categorical)

5. Feature engineer a new column. Can you think of a new column that would be a calculation of other columns? For instance, if you have a dataset of people's weights and heights, can you create a new column for BMI? Can you create a categorical column based on continuous data - for instance, small/medium/large?

6. Identify numeric, binary, and categorical columns (multi-class).

7. Create transformer pipelines for each type of column. For numeric, impute any missing values, and then scale the data using the StandardScaller. For binary data, impute missing values using a constant with the majority of the values found in the variable (more 1's or more 0's?). For categorical variables impute with a constant (call it 'unknown') and then encode using OneHotEncoding. 

8. Combine all of the transformer pipelines into a single pipeline using the ColumnTransformer.

9. Fit and transform the training data using the combined pipeline.

10. Fit the test data using the combined pipeline.

11. Create a baseline using a dummy classifier or dummy regressor (depending on your dataset).

12. Use GridSearchCV to test a number of parameter combinations for your model. You are fitting either a DecisionTreeRegressor or a DecisionTreeClassifier (depending on your dataset).

13. Select the best model based on the GridSearchCV results, and evaluate the models performance by comparing the baseline to the best model. (For classification, use accuracy, precision, recall, and F1 score. For regression, use RMSE).
    
14. Submit your notebook and any other files to the assignment link.


