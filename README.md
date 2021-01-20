# Disaster Response Pipeline Project

### Motivation

The purpose of project is to build a model which can classify the messages and requets put in by people stuck in disaster. This application provides a webapp which would recieve the messages from people at disaster location and correctly clasiffy what kind of support they need. This would help to expedite the help/support provided by disaster response team as this application would automatically classify high volume of message to right response team/groups.

### Install
This project requires Python 3.x and the following Python libraries to be installed:

NumPy,
Pandas,
Matplotlib,
Json,
Plotly,
Nltk,
Flask,
Sklearn,
Sqlalchemy,
Pickle

### files
process_data.py: This code process csvfile ( messages.csv and categories.csv  ) and uploades data into a SQLite database containing a merged and cleased version of this data.

train_classifier.py: This file takes the processed data in SQLite as input and then fits data into classifier. This code predicts the classes for test data and then provides a classification report. This code deumps the model weights into a classifier.pkl file.

run.py: This file contains codes for running Flask application and to build graphs (visualization) on web. This file also has code which recieves the user input and converts that into tokens to be provided to trained model and get the predicted classes as output and shown on webapp.

ETL Pipeline Preparation.ipynb: This file was used for the initia analysis of input data files and then building the skeleton for ETL pipeline.

ML Pipeline Preparation.ipynb: This file was used for building skeletn of classifier pipeline. 



### Running Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
