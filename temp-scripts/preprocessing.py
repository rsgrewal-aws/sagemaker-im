# Cell 06
import argparse
import pathlib
import boto3
import os
import pandas as pd
import logging
from sklearn.model_selection import train_test_split

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--validation-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    args, _ = parser.parse_known_args()
    logger.info("Received arguments {}".format(args))
    
    # Set local path prefix in the processing container
    local_dir = "/opt/ml/processing"    
    
    input_data_path_claims = os.path.join("/opt/ml/processing/claims", "claims.csv")
    input_data_path_customers = os.path.join("/opt/ml/processing/customers", "customers.csv")
    
    logger.info("Reading claims data from {}".format(input_data_path_claims))
    df_claims = pd.read_csv(input_data_path_claims)
    
    logger.info("Reading customers data from {}".format(input_data_path_customers))
    df_customers = pd.read_csv(input_data_path_customers)
    
    logger.debug("Formatting column names.")
    # Format column names
    df_claims = df_claims.rename({c : c.lower().strip().replace(' ', '_') for c in df_claims.columns}, axis = 1)
    df_customers = df_customers.rename({c : c.lower().strip().replace(' ', '_') for c in df_customers.columns}, axis = 1)
    
    logger.debug("Joining datasets.")
    # Join datasets
    df_data = df_claims.merge(df_customers, on = 'policy_id', how = 'left')

    # Drop selected columns not required for model building
    df_data = df_data.drop(['customer_zip'], axis = 1)
    
    # Select Ordinal columns
    ordinal_cols = ["police_report_available", "policy_liability", "customer_education"]

    # Select categorical columns and filling with na
    cat_cols_all = list(df_data.select_dtypes('object').columns)
    cat_cols = [c for c in cat_cols_all if c not in ordinal_cols]
    df_data[cat_cols] = df_data[cat_cols].fillna('na')
    
    logger.debug("One-hot encoding categorical columns.")
    # One-hot encoding categorical columns
    df_data = pd.get_dummies(df_data, columns = cat_cols)
    
    logger.debug("Encoding ordinal columns.")
    # Ordinal encoding
    mapping = {
               "Yes": "1",
               "No": "0" 
              }
    df_data['police_report_available'] = df_data['police_report_available'].map(mapping)
    df_data['police_report_available'] = df_data['police_report_available'].astype(float)

    mapping = {
               "15/30": "0",
               "25/50": "1", 
               "30/60": "2",
               "100/200": "3"
              }
    
    df_data['policy_liability'] = df_data['policy_liability'].map(mapping)
    df_data['policy_liability'] = df_data['policy_liability'].astype(float)

    mapping = {
               "Below High School": "0",
               "High School": "1", 
               "Associate": "2",
               "Bachelor": "3",
               "Advanced Degree": "4"
              }
    
    df_data['customer_education'] = df_data['customer_education'].map(mapping)
    df_data['customer_education'] = df_data['customer_education'].astype(float)
    
    df_processed = df_data.copy()
    df_processed.columns = [c.lower() for c in df_data.columns]
    df_processed = df_processed.drop(["policy_id", "customer_gender_unkown"], axis=1)
    
    # Split into train, validation, and test sets
    train_ratio = args.train_ratio
    val_ratio = args.validation_ratio
    test_ratio = args.test_ratio
    
    logger.debug("Splitting data into train, validation, and test sets")
    
    y = df_processed['fraud']
    X = df_processed.drop(['fraud'], axis = 1)
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=val_ratio, random_state=42)

    train_df = pd.concat([y_train, X_train], axis = 1)
    val_df = pd.concat([y_val, X_val], axis = 1)
    test_df = pd.concat([y_test, X_test], axis = 1)
    dataset_df = pd.concat([y, X], axis = 1)
    
    logger.info("Train data shape after preprocessing: {}".format(train_df.shape))
    logger.info("Validation data shape after preprocessing: {}".format(val_df.shape))
    logger.info("Test data shape after preprocessing: {}".format(test_df.shape))
    
    # Save processed datasets to the local paths in the processing container.
    # SageMaker will upload the contents of these paths to S3 bucket
    logger.debug("Writing processed datasets to container local path.")
    train_output_path = os.path.join(f"{local_dir}/train", "train.csv")
    validation_output_path = os.path.join(f"{local_dir}/val", "validation.csv")
    test_output_path = os.path.join(f"{local_dir}/test", "test.csv")
    full_processed_output_path = os.path.join(f"{local_dir}/full", "dataset.csv")

    logger.info("Saving train data to {}".format(train_output_path))
    train_df.to_csv(train_output_path, index=False)
    
    logger.info("Saving validation data to {}".format(validation_output_path))
    val_df.to_csv(validation_output_path, index=False)

    logger.info("Saving test data to {}".format(test_output_path))
    test_df.to_csv(test_output_path, index=False)
    
    logger.info("Saving full processed data to {}".format(full_processed_output_path))
    dataset_df.to_csv(full_processed_output_path, index=False)
