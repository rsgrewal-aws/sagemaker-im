"""
ModelHandler defines an example model handler for load and inference requests for MXNet CPU models
"""
import glob
import json
import logging
import os
import re
from collections import namedtuple

import mxnet as mx
import numpy as np
import traceback
import json
import uuid

class ModelHandler(object):
    """
    A sample Model handler implementation.
    """

    def __init__(self):
        self.initialized = False
        self.mx_model = None
        self.shapes = None
        print(f"Modelhandler::__init__:called")

    def get_model_files_prefix(self, model_dir):
        """
        Get the model prefix name for the model artifacts (symbol and parameter file).
        This assume model artifact directory contains a symbol file, parameter file,
        model shapes file and a synset file defining the labels
        :param model_dir: Path to the directory with model artifacts
        :return: prefix string for model artifact files
        """
        sym_file_suffix = "-symbol.json"
        checkpoint_prefix_regex = "{}/*{}".format(
            model_dir, sym_file_suffix
        )  # Ex output: /opt/ml/models/resnet-18/model/*-symbol.json
        checkpoint_prefix_filename = glob.glob(checkpoint_prefix_regex)[
            0
        ]  # Ex output: /opt/ml/models/resnet-18/model/resnet18-symbol.json
        checkpoint_prefix = os.path.basename(checkpoint_prefix_filename).split(sym_file_suffix)[
            0
        ]  # Ex output: resnet18
        print(f"Modelhandler::Prefix for the model artifacts: {checkpoint_prefix}")
        
        return checkpoint_prefix

    def get_input_data_shapes(self, model_dir, checkpoint_prefix):
        """
        Get the model input data shapes and return the list
        :param model_dir: Path to the directory with model artifacts
        :param checkpoint_prefix: Model files prefix name
        :return: prefix string for model artifact files
        """
        shapes_file_path = os.path.join(model_dir, "{}-{}".format(checkpoint_prefix, "shapes.json"))
        if not os.path.isfile(shapes_file_path):
            raise RuntimeError("Missing {} file.".format(shapes_file_path))

        with open(shapes_file_path) as f:
            self.shapes = json.load(f)

        data_shapes = []

        for input_data in self.shapes:
            data_name = input_data["name"]
            data_shape = input_data["shape"]
            data_shapes.append((data_name, tuple(data_shape)))

        return data_shapes

    def initialize(self, context):
        """
        Initialize model. This will be called during model loading time
        :param context: Initial context contains model server system properties.
        :return:
        """
        self.initialized = True
        properties = context.system_properties
        # Contains the url parameter passed to the load request
        model_dir = properties.get("model_dir")
        gpu_id = properties.get("gpu_id")
        print(f"Modelhandler::initialize::model_dir::{model_dir}::")
        
        checkpoint_prefix = self.get_model_files_prefix(model_dir)

        # Read the model input data shapes
        data_shapes = self.get_input_data_shapes(model_dir, checkpoint_prefix)
        print(f"Modelhandler::initialize::data_shaped={data_shapes}::")
        
        # Load MXNet model
        try:
            ctx = mx.cpu()  # Set the context on CPU
            sym, arg_params, aux_params = mx.model.load_checkpoint(
                checkpoint_prefix, 0
            )  # epoch set to 0
            self.mx_model = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
            self.mx_model.bind(
                for_training=False,
                data_shapes=data_shapes,
                label_shapes=self.mx_model._label_shapes,
            )
            self.mx_model.set_params(arg_params, aux_params, allow_missing=True)
            
            
            self.labels = [f"label::{l}" for l in range(1111)]
            print(f"GPU:Modelhandler::initialize::Labels created::labels:{len(self.labels)}:")
            
            self.redis_client = None
            self.init_redis()
                  
        except (mx.base.MXNetError, RuntimeError) as memerr:
            if re.search("GPU:Failed to allocate (.*) Memory", str(memerr), re.IGNORECASE):
                print(f"GPU:Modelhandler::initialize::Memory allocation exception: {memerr}")
                raise MemoryError
            raise

    def init_redis(self):
        try:
            
            print(f"GPU:Trying redis::{self.redis_client}::")
            if not self.redis_client:
                from redis import Redis
                self.redis_client = Redis(
                    # - vpce-0ee05c94e950bcd3c-hafv9vy6.elasticache.us-east-1.vpce.amazonaws.com
                    # - elasticache.us-east-1.amazonaws.com
                    # - 'testredis.m7ovi1.ng.0001.use1.cache.amazonaws.com'
                    host='testredis.m7ovi1.ng.0001.use1.cache.amazonaws.com', 
                    port=6379, #decode_responses=True, ssl=True, 
                    username='default', #'testredisuser', 'default'
                    #password='testRedisUserPassword'
                )
                # redis_client = Redis(
                #     host='testredis.m7ovi1.ng.0001.use1.cache.amazonaws.com',
                #     username='testredisuser',
                #     password='testRedisUserPassword', ssl_cert_reqs=None,  decode_responses=True)

                print("GPU:Redis client starting to connect ")
                if self.redis_client.ping():
                    print("GPU:Connected to Redis")
            
            #self.get(redis_client,custom_attrs)
            print("GPU:Finished redis call")
            
        except:
            print(f"GPU:error:connecting:to REDIS:{traceback.format_exc()}:")
        
        
    def preprocess(self, request):
        """
        Transform raw input into model input data.
        :param request: list of raw requests
        :return: list of preprocessed model input data
        """
        # Take the input data and pre-process it make it inference ready
        
        # extract from the request image id 

        img_list = []
        for img_arr in self.get_img(self.redis_client):
            # Input image is in bytearray, convert it to MXNet NDArray
            img = mx.img.imdecode(img_arr)
            if img is None:
                return None

            # convert into format (batch, RGB, width, height)
            img = mx.image.imresize(img, 224, 224)  # resize
            img = img.transpose((2, 0, 1))  # Channel first
            img = img.expand_dims(axis=0)  # batchify
            img_list.append(img)

        print(f"GPU:Modelhandler::preprocess::FROM:REDIS:img_list::size={len(img_list)}")
        
        return img_list

    def inference(self, model_input):
        """
        Internal inference methods
        :param model_input: transformed model input data list
        :return: list of inference output in NDArray
        """
        # Do some inference call to engine here and return output
        Batch = namedtuple("Batch", ["data"])
        self.mx_model.forward(Batch(model_input))
        prob = self.mx_model.get_outputs()[0].asnumpy()
        return prob

    def postprocess(self, inference_output, custom_attrs):
        """
        Return predict result in as list.
        :param inference_output: list of inference output
        :return: list of predict results
        """
        # Take output from network and post-process to desired format
        prob = np.squeeze(inference_output)
        print(f"GPU:Modelhandler::postprocess::probability:{len(prob)}::{len(self.labels)}::custom_attrs={custom_attrs}::")
        a = np.argsort(prob)[::-1]
        
        print(f"GPU:Modelhandler::postprocess::probability={a[0:5]}::")
        
        return [["probability=%f, class=%s" % (prob[i], self.labels[i]) for i in a[0:5]]]


    def get(self, redis_client,custom_attrs):
        print(f"GPU:Modelhandler::REDIS:CACHE:Starting::custom_attrs={custom_attrs}::")
        key_mask = "customer:*"
        customers = []
        for key in redis_client.scan_iter(key_mask):
            customer_id = key #key.split(':')[1]
            customer = redis_client.hgetall(key)
            customer['id'] = customer_id
            customers.append(customer)
            print(f"GPU:Modelhandler::REDIS:CACHE::{customer}")
        return customers

    def post(self, redis_client, json_struct):
        print(json_struct)
        json_str = json.dumps(json_struct)

        customer_id = json_struct['customer_id'] #str(uuid.uuid4())
        key = "customer:" + customer_id
        write_redis = redis_client.hset(key, mapping=json_struct)
        #customer = json_str
        #customer['id'] = customer_id
        return write_redis, 201

    def get_img(self,redis_client):
        key_mask = "raw_image:*"
        image_list = []
        for key in redis_client.scan_iter(key_mask):
            image_id = key 
            image = redis_client.get(key)
            image_list.append(image)
            #print(image)
        return image_list

    def post_img(self,redis_client, img_id, raw_image_bytes):

        key = "raw_image:" + img_id
        print(f"key={key}")
        write_redis = redis_client.set(key, raw_image_bytes)
        return write_redis, 201    

    def handle(self, data, context):
        """
        Call preprocess, inference and post-process functions
        :param data: input data
        :param context: mms context
        """

        print("GPU:model_handler:handle")
        print(f"GPU:model_handler:context={context}:")
        custom_attrs = None
        try:
            print(f"GPU:model_handler:context={dir(context)}:")
            print(f"GPU:model_handler:context={context.request_ids}") #get_all_request_header()}")
            print(f"GPU:loaded CUSTOM ATTR: {custom_attrs}")
        except:
            print(f"GPU:context:error:{traceback.format_exc()}:")
        
        model_input = self.preprocess(data)
        model_out = self.inference(model_input)
        return self.postprocess(model_out, custom_attrs)


_service = ModelHandler()


def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    return _service.handle(data, context)