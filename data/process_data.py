import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """ This function loads the data from 2 CSV sheets and process them to
    load into a dataframe . This function also does basic processing of data like getting column names, updating 0,1 against 
    each category"""
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    # merge datasets
    df = messages.merge(categories,on='id')
    # create a dataframe of the 36 individual category columns
    categories = categories['categories'].str.split(';', expand=True)
    # select the first row of the categories dataframe
    row = categories[:1].values.tolist()[0]
    #extract a list of new column names for categories.
    category_colnames = [ str(w)[:-2] for w in row ]
    # rename the columns of `categories`
    categories.columns = category_colnames
    #Convert category values to just numbers 0 or 1.
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = [val[-1] for val in categories[column] ]
    
        # convert column from string to binary
        categories[column] = categories[column].apply(lambda x: 1 if int(x)>0 else 0)
    # drop the original categories column from `df`
    df.drop('categories',axis=1,inplace=True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories], axis=1)
    return df

def clean_data(df):
    """ This function cleans data . It removes duplicates and remove null values"""
    
    # deleting data with null values in messages types
    df.dropna(subset=['related','request'],inplace=True)
    #drop duplicates
    df=df.drop_duplicates()
    
    return df

def save_data(df, database_filename):
    
    """ This function """
    engine = create_engine('sqlite:///'+database_filename)
    connection = engine.raw_connection()
    cursor = connection.cursor()
    command = "DROP TABLE IF EXISTS {};".format('disastermessages')
    cursor.execute(command)
    connection.commit()
    cursor.close()
    df.to_sql('disastermessages', engine, index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()