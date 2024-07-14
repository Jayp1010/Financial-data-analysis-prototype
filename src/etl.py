import pandas as pd
from sqlalchemy import create_engine
from validation import validate_data
from encryption import encrypt_data, generate_key

def extract_data(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].astype(float)
    return df

def load_data(df, table_name, db_engine):
    df.to_sql(table_name, db_engine, if_exists='replace', index=False)

def run_etl(file_path, table_name, db_url):
    df = extract_data(file_path)
    df = transform_data(df)
    validate_data(df)
    key = generate_key()
    encrypted_df = encrypt_data(df, key)
    engine = create_engine(db_url)
    load_data(encrypted_df, table_name, engine)

if __name__ == '__main__':
    file_path = 'data/sample_financial_data.csv'
    table_name = 'financial_data'
    db_url = 'postgresql://username:password@localhost:5432/financial_db'
    
    run_etl(file_path, table_name, db_url)
