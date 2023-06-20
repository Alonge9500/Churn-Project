# Customer Churn Analysis and Deployment

By *Alonge Daniel*, a Data Scientist passionate about data and technology.

- GitHub: [Alonge 9500](https://github.com/Alonge9500)
- LinkedIn: [Alonge Daniel](https://www.linkedin.com/in/alonge-daniel-27b4b4139/)
- Email: [Alonge Daniel](mailto:alongedaniel19@gmail.com)

I' will appreciate any comment and correction on this work 

This repository contains code for analyzing customer churn dataset, performing preprocessing tasks, and deploying a Flask web application for churn prediction. The project aims to predict customer churn, i.e., identify customers who are likely to stop using a product or service, using machine learning techniques.

## Problem Statement

Customer churn is a critical challenge for businesses. Identifying customers at risk of churning can help businesses take proactive measures to retain them. The goal of this project is to build a churn prediction model using a customer dataset and deploy it as a web application. By predicting churn, businesses can take targeted actions to retain customers and improve customer satisfaction.

## Dataset

The project uses a customer churn dataset that includes various features related to customer behavior, demographics, and usage patterns. The dataset contains the following columns:

- customer_id: Unique identifier for each customer
- gender: Customer's gender (male/female)
- age: Customer's age
- tenure: Number of months the customer has been with the company
- usage: Usage pattern of the customer
- churn: Binary flag indicating whether the customer churned (1) or not (0)

## Getting Started

To run the code and deploy the application, follow these steps:

1. Clone the repository: `git clone <https://github.com/Alonge9500/Churn-Project>`
2. Install the required libraries: `pip install -r requirements.txt`
3. Download the dataset file (customer_churn.csv) and place it in the project directory.
4. Run the Jupyter notebook: `jupyter notebook`
5. Open the notebook `churn_analysis.ipynb` and execute the code cells sequentially for data analysis, preprocessing, and model training.
6. Run the Flask application: `python app.py`
7. Access the application in your browser at `http://localhost:5000`.

## Data Analysis

The notebook includes exploratory data analysis (EDA) of the customer churn dataset. It examines the distribution of features, performs visualizations, and identifies any correlations between variables. This helps gain insights into the data and understand the factors influencing customer churn.

## Data Preprocessing

Data preprocessing is an essential step to prepare the dataset for model training. The notebook covers various preprocessing tasks, such as handling missing values, encoding categorical variables, scaling numerical features, and splitting the data into training and testing sets.

## Model Training and Evaluation

The notebook trains a machine learning model on the preprocessed data to predict customer churn. It utilizes popular algorithms such as logistic regression, random forest, or gradient boosting. The model is evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.

## Deployment with Flask

The repository includes a Flask web application for deploying the trained churn prediction model. The application provides a user interface where users can input customer information and receive a churn prediction. The model is loaded and used to make real-time predictions.

## Deployment on AWS EC2

The project also demonstrates how to deploy the Flask application on AWS EC2 for public access. Detailed instructions are provided in the `aws_deployment.md` file, which covers setting up an EC2 instance, installing dependencies, and running the application on the EC2 instance.

## Conclusion

The customer churn analysis and deployment project showcases the prediction of customer churn using machine learning and deployment with Flask. By performing data analysis, preprocessing, and training a model, it offers insights into customer behavior and churn factors. The deployment on AWS EC2 allows the application to be accessed publicly, enabling businesses to leverage the churn prediction model.

## License

This project is licensed under the [MIT License](LICENSE
