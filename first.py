import torch

if torch.cuda.is_available():
    print("CUDA is available.")
    # Optional: Print additional information about the CUDA device
    print(f"CUDA Device Name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Device Count: {torch.cuda.device_count()}")
else:
    print("CUDA is not available.")