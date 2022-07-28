
# Cell 15
"""
Lambda function creates an endpoint configuration and deploys a model to real-time endpoint. 
Required parameters for deployment are retrieved from the event object
"""

import json
import boto3


def lambda_handler(event, context):
    sm_client = boto3.client("sagemaker")

    # Details of the model created in the Pipeline CreateModelStep
    model_name = event["model_name"]
    model_package_arn = event["model_package_arn"]
    endpoint_config_name = event["endpoint_config_name"]
    endpoint_name = event["endpoint_name"]
    role = event["role"]
    instance_type = event["instance_type"]
    instance_count = event["instance_count"]
    primary_container = {"ModelPackageName": model_package_arn}

    # Create model
    model = sm_client.create_model(
        ModelName=model_name,
        PrimaryContainer=primary_container,
        ExecutionRoleArn=role
    )

    # Create endpoint configuration
    create_endpoint_config_response = sm_client.create_endpoint_config(
        EndpointConfigName=endpoint_config_name,
        ProductionVariants=[
        {
            "VariantName": "Alltraffic",
            "ModelName": model_name,
            "InitialInstanceCount": instance_count,
            "InstanceType": instance_type,
            "InitialVariantWeight": 1
        }
        ]
    )

    # Create endpoint
    create_endpoint_response = sm_client.create_endpoint(
        EndpointName=endpoint_name, 
        EndpointConfigName=endpoint_config_name
    )
