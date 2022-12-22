import subprocess
import sys


subprocess.check_call([sys.executable, "-m", "pip", "install", "torchvision" ,"tqdm"])
import json
import numpy
import torch
import os
import torchvision
import triton_python_backend_utils as pb_utils
import torchvision.transforms as T
from tqdm import tqdm

class logosDS(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data.as_numpy()
        print(len(self.data))

    def __getitem__(self, idx):
        input0 = self.data[idx]
        image_transform = T.Compose([
            T.ToTensor(),
        ])

        img = image_transform(input0)

        return {
            'index': idx,
            'image': img
        }

    def __len__(self):
        return len(self.data)




class TritonPythonModel:
    """Your Python model must use the same class name. Every Python model
    that is created must have "TritonPythonModel" as the class name.
    """

    def initialize(self, args):
        """`initialize` is called only once when the model is being loaded.
        Implementing `initialize` function is optional. This function allows
        the model to intialize any state associated with this model.

        Parameters
        ----------
        args : dict
          Both keys and values are strings. The dictionary keys and values are:
          * model_config: A JSON string containing the model configuration
          * model_instance_kind: A string containing model instance kind
          * model_instance_device_id: A string containing model instance device ID
          * model_repository: Model repository path
          * model_version: Model version
          * model_name: Model name
        """

        # You must parse model_config. JSON string is not parsed here
        print(args)
        self.model_config = model_config = json.loads(args['model_config'])
        self.model_repository = args['model_repository']
        print(self.model_config)
        print(self.model_repository)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=False,
                                                                    progress=True,
                                                                    pretrained_backbone=True)
        repo_dir = os.path.join(args['model_repository'], args['model_version'])
        print(repo_dir)
        print(os.listdir(repo_dir))
        model = torch.load(os.path.join(repo_dir, "model.pth"), map_location=self.device)
        print("model loaded")
        model.to(self.device)
        print(self.device)
        model.eval()
        print("model evaled")
  

        # Instantiate the PyTorch model
        self.model = model

    def execute(self, requests):
        """`execute` must be implemented in every Python model. `execute`
        function receives a list of pb_utils.InferenceRequest as the only
        argument. This function is called when an inference is requested
        for this model. Depending on the batching configuration (e.g. Dynamic
        Batching) used, `requests` may contain multiple requests. Every
        Python model, must create one pb_utils.InferenceResponse for every
        pb_utils.InferenceRequest in `requests`. If there is an error, you can
        set the error argument when creating a pb_utils.InferenceResponse.

        Parameters
        ----------
        requests : list
          A list of pb_utils.InferenceRequest

        Returns
        -------
        list
          A list of pb_utils.InferenceResponse. The length of this list must
          be the same as `requests`
        """

        responses = []
        print(type(requests))
        # Every Python backend must iterate over everyone of the requests
        # and create a pb_utils.InferenceResponse for each of them.
        for request in requests:

            in_0 = pb_utils.get_input_tensor_by_name(request, "INPUT__0")

            ds = logosDS(in_0)
            print("len ds",len(ds))
            num_workers=1
            print("num_workers",num_workers)
            data_loader = torch.utils.data.DataLoader(
                ds,
                batch_size=1,
                num_workers=num_workers,
                shuffle=False
            )
            with torch.no_grad():
                bboxes = []
                labels = []
                scores = []
                tk0 = tqdm(data_loader, desc="Iteration")
                for step, batch in enumerate(tk0):
                    inputs = batch["image"]
                    image_ids = batch["index"]
                    preds = self.model(inputs.to(self.device))
                    for im_name, pred in zip(image_ids, preds):
                        bbox = pred["boxes"].cpu().numpy()
                        label = pred["labels"].cpu().numpy()
                        score = pred["scores"].cpu().numpy()
                        bboxes.append(bbox.tobytes())
                        labels.append(label.tobytes())
                        scores.append(score.tobytes())

            output_tensors = [pb_utils.Tensor("BBOX", numpy.array(bboxes, dtype=object)),
                              pb_utils.Tensor("LABELS", numpy.array(labels, dtype=object)),
                              pb_utils.Tensor("SCORES", numpy.array(scores, dtype=object))]
            inference_response = pb_utils.InferenceResponse(output_tensors=output_tensors)
            responses.append(inference_response)

        # You should return a list of pb_utils.InferenceResponse. Length
        # of this list must match the length of `requests` list.
        return responses

    def finalize(self):
        """`finalize` is called only once when the model is being unloaded.
        Implementing `finalize` function is optional. This function allows
        the model to perform any necessary clean ups before exit.
        """
        print('Cleaning up...')
