
import numpy as np
import sys
import os
import json
from pathlib import Path

import sys
import subprocess
import traceback

# !pip install transformers
# !pip install sentencepiece
# !pip install nvidia-pyindex
# !pip install tritonclient[http]
# !pip install torch
# implement pip as a subprocess:

subprocess.check_call([sys.executable, '-m', 'pip', 'install','torch'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','boto3'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(f"TritonPythonModel:Bloom-176b:installed_packages={installed_packages}:")


import torch

import triton_python_backend_utils as pb_utils
import boto3
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

s3_client = boto3.client("s3")
print(f"TritonPythonModel:Bloom-176b:s3_client={s3_client}::")


class TritonPythonModel:
    # Every Python model must have "TritonPythonModel" as the class name!
    def initialize(self, args):
        print(f"TritonPythonModel:Bloom-176b:initialize():: called:args={args}", flush=True)
        self.output_dtype = pb_utils.triton_string_to_numpy(
            pb_utils.get_output_config_by_name(
                json.loads(args['model_config']), "OUTPUT__0" #"output"
            )['data_type']
        )
        print(f"TritonPythonModel:Bloom-176b:initialize()::output_type={self.output_dtype}", flush=True)
        
        #from transformers import T5ForConditionalGeneration, T5Tokenizer
        self.model = None #T5ForConditionalGeneration.from_pretrained("t5-small").cuda()
        
        try:
            from os import listdir
            from os.path import isfile, join
            onlyfiles = [f for f in listdir(".") if isfile(join('.', f))]
            print(f"TritonPythonModel:Bloom-176b:initialize()::current:working:dir={os.getcwd()}::", flush=True)
            print(f"TritonPythonModel:Bloom-176b:initialize()::onlyfiles::{onlyfiles}", flush=True)
            
            print(f"TritonPythonModel:Bloom-176b:initialize()::starting:download::", flush=True)
            self.start_download()
        except:
            print(f"TritonPythonModel:Bloom-176b:initialize():ERROR IN DOWNLOAD={traceback.format_exc()}::", flush=True)
            
        print(f"TritonPythonModel:Bloom-176b:initialize()::Completed::", flush=True)

    def download_files_executor(self, s3_files, model_dir='/tmp/model'):
        
        print(f"TritonPythonModel:Bloom-176b:download_files_executor():files={s3_files}::model_dir={model_dir}::Started::", flush=True)
        
        def _download_file(s3_1_file_path, model_dir):

            global s3_client

            local_file_path = os.path.join(model_dir, s3_1_file_path.split("/")[-1])

            bucket, *key = s3_1_file_path.split("/")
            key = "/".join(key)
            print(f"TritonPythonModel:Bloom-176b:download_files_executor():EXECUTOR::STARTED::local_file_path={local_file_path}::bucket={bucket}::key={key}::", flush=True)  
            try:
                s3_client.download_file(bucket, key, local_file_path)
                print(f"TritonPythonModel:Bloom-176b:download_files_executor():EXECUTOR::ENDED::local_file_path={local_file_path}::bucket={bucket}::key={key}::", flush=True)
            except:
                #time.sleep(0.5)
                print(f"TritonPythonModel:Bloom-176b:download_files_executor():EXECUTOR:ERROR IN DOWNLOAD={traceback.format_exc()}::bucket={bucket}:: key={key}::", flush=True)

            return local_file_path

        
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(_download_file, s3_file, model_dir) for s3_file in s3_files]
            for future in as_completed(futures):
                print (f"TritonPythonModel:Bloom-176b:download_files_executor()::downloaded: {future.result()}", flush=True)
                
        print(f"TritonPythonModel:Bloom-176b:download_files_executor():All:Executors:Started!!")

    def start_download(self):
        print(f"TritonPythonModel:Bloom-176b:start_download()::called::", flush=True) 
        s3_objects = s3_client.list_objects(Bucket='sagemaker-us-east-1-622343165275', Prefix='bloom/triton_models/bloom-176b/')["Contents"]
        s3_paths = [os.path.join('sagemaker-us-east-1-622343165275', obj["Key"]) for obj in s3_objects]
        print(f"TritonPythonModel:Bloom-176b::start_download()::downloading files::s3_paths:list::{s3_paths}::", flush=True)

        model_dir = "/tmp/model"
        os.makedirs(model_dir, exist_ok=True)
        print(f"TritonPythonModel:Bloom-176b::start_download()::temp:directory:created:::Now to start Executors", flush=True)
        
        self.download_files_executor(s3_paths, model_dir)               

                       
    def execute(self, requests):
        print(f"TritonPythonModel:Bloom-176b: execute() called:requests={requests}:", flush=True)
        
        responses = []
        try:
            for request in requests:
                print(f"TritonPythonModel:Bloom-176b: execute :EACH:Request:requests={request}:", flush=True)
                
                input_0 = pb_utils.get_input_tensor_by_name(request, "INPUT__0")
                print(f"TritonPythonModel:Bloom-176b: execute :EACH:Request:input_0={input_0}::", flush=True)
                try:
                    input_ids = input_0.as_numpy()
                    
                     # Convert to numpy array on cpu:
                    input_ids = torch.as_tensor(input_ids).long().cuda()
                    summary = self.model.generate(input_ids, num_beams=1)
                    np_summary = summary.cpu().int().detach().numpy()
                except:
                    pass
                
                summary = [1]*512  

               
                
                np_summary = np.array(summary)
                inference_response = pb_utils.InferenceResponse(
                    output_tensors=[
                        pb_utils.Tensor(
                            "OUTPUT__0",
                            np_summary.astype(self.output_dtype)
                        ),
                    ]
                )
                responses.append(inference_response)
                print(f"TritonPythonModel:Bloom-176b: execute():responses={responses}::{len(responses)}::", flush=True)
        except :
            print("TritonPythonModel:Bloom-176b: execute():Exception Thrown", flush=True)
            print (f"TritonPythonModel:Bloom-176b: execute(): traceback:eror:predict={traceback.format_exc()}", flush=True)
            
        return responses

    def finalize(self):
        print(f"TritonPythonModel:Bloom-176b: finalize()::TritonPythonModel finalized: called", flush=True)
