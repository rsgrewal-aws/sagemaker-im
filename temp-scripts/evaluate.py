
# Cell 12

import json
import logging
import pathlib
import pickle
import tarfile

import numpy as np
import pandas as pd
import xgboost as xgb

from sklearn.metrics import roc_auc_score

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    model_path = "/opt/ml/processing/model/model.tar.gz"
    with tarfile.open(model_path) as tar:
        tar.extractall(path=".")

    logger.debug("Loading xgboost model.")
    # The name of the file should match how the model was saved in the training script
    model = pickle.load(open("xgboost-model", "rb"))

    logger.debug("Reading test data.")
    test_local_path = "/opt/ml/processing/test/test.csv"
    df_test = pd.read_csv(test_local_path)
    
    # Extract test set target column
    y_test = df_test.iloc[:, 0].values
   
    cols_when_train = model.feature_names
    # Extract test set feature columns
    X = df_test[cols_when_train].copy()
    X_test = xgb.DMatrix(X)

    logger.info("Generating predictions for test data.")
    pred = model.predict(X_test)
    
    # Calculate model evaluation score
    logger.debug("Calculating ROC-AUC score.")
    auc = roc_auc_score(y_test, pred)
    metric_dict = {
        "classification_metrics": {"roc_auc": {"value": auc}}
    }
    
    # Save model evaluation metrics
    output_dir = "/opt/ml/processing/evaluation"
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

    logger.info("Writing evaluation report with ROC-AUC: %f", auc)
    evaluation_path = f"{output_dir}/evaluation.json"
    with open(evaluation_path, "w") as f:
        f.write(json.dumps(metric_dict))
