from huggingface_hub import InferenceClient

client=InferenceClient(token="hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

MODEL="stabilityai/stable-diffusion-xl-base-1.0"

prompt=input()