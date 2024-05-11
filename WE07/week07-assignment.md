# Title: Text Classification Challenge

## Introduction:

Text classification is pivotal in deriving insights from unstructured textual data in business analytics and information systems. This assignment is designed to offer hands-on experience in developing a predictive model using various machine-learning techniques for text classification. You will work in your assigned teams to identify a unique dataset suitable for a text classification problem, preprocess the data, implement several machine learning models, and critically analyze the results.

## Objective:

Your task is to develop a predictive model that accurately classifies text data. You will go through the complete model development process, including data acquisition, preprocessing, model training, and evaluation. This assignment will help you enhance your understanding of natural language processing (NLP) and text analysis techniques and provide practical experience in applying various machine learning algorithms.

## Assignment Tasks:

Dataset Identification: Identify a unique dataset for a text classification problem. The dataset should be approved by the instructor to ensure its suitability and uniqueness. Identify this data ASAP to ensure you can claim the dataset you would like to work with before someone else does. 

## Data Preprocessing:

Perform text lemmatization to reduce words to their base or root form.
Remove stop words that do not contribute to the predictive model.
Apply Singular Value Decomposition (SVD) for dimensionality reduction to improve model performance.
Apply any other data prep techniques that you feel are necessary
Feature Engineering: Encode the text data using sklearn's TfidfVectorizer to convert text data into a matrix of TF-IDF features.

## Model Development and Testing: Implement and test the following seven models:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- AdaBoost
- XGBoost

# Hyperparameter Tuning: Use hyperparameter tuning to find the optimal settings for each model to ensure the best possible performance.

# Documentation: Submit your work in a Jupyter notebook, ensuring a balance between text explanation and code. The notebook should include:

* An introduction that outlines the problem statement, dataset, and objective of the analysis.
* A detailed description of the data preprocessing steps and rationale behind chosen methods.
* A review and discussion of the model development process, including challenges faced, model comparison, and final model selection.
* A critical analysis of the results, including insights gained and potential applications of your model.

## Submission Requirements:

A single Jupyter notebook per team, submitted via the designated platform before the deadline.
The notebook should be well-organized, professionally formatted, and include both code and comprehensive text explanations.


## Rubric

| Criteria                                  | Excellent (90-100%)                                         | Good (80-89%)                                                   | Satisfactory (70-79%)                                       | Needs Improvement (<70%)                                          |
|-------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------|
| **Code Quality**                          | Code is well-organized, efficient, and follows best practices. | Code is organized and functional with minor inefficiencies.    | Code is functional but lacks organization or efficiency.    | Code is disorganized, inefficient, or contains significant errors. |
| **Data Preprocessing**                    | Demonstrates thorough understanding and application of preprocessing techniques. | Adequate preprocessing with minor oversights.                   | Preprocessing steps are applied but lack depth or rationale. | Inadequate preprocessing, significantly affecting model performance. |
| **Model Implementation and Tuning**       | Models are correctly implemented and optimally tuned. Demonstrates deep understanding. | Models are correctly implemented with effective tuning.         | Models are implemented with basic tuning.                    | Models are incorrectly implemented or poorly tuned.                |
| **Analysis and Interpretation**           | Provides insightful analysis, with a comprehensive review and discussion of results. | Provides a clear analysis with a coherent discussion.           | Analysis and discussion are present but lack depth.          | Analysis and discussion are superficial or missing.               |
| **Presentation and Organization**         | Notebook is exceptionally organized, with a professional appearance and seamless integration of text and code. | Notebook is well-organized with clear sections and good integration of text and code. | Notebook is organized but could be improved in presentation. | Notebook is poorly organized and difficult to follow.             |
| **Innovation and Creativity**             | Demonstrates exceptional creativity in approach, analysis, and problem-solving. | Shows good creativity and a solid approach to problem-solving. | Some evidence of creativity, but mostly follows standard approaches. | Lacks creativity, with heavy reliance on standard approaches.       |

**Note**: Teamwork and collaboration will also be considered in the evaluation process, with peer feedback contributing to individual scores within each team.

Please ensure that your submission adheres to all the requirements specified in the assignment description. Late submissions will incur a penalty, and