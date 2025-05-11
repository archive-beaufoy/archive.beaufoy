import torch
import torch.nn as nn
import torch.nn.functional as F
import time

# Set device: 'cpu' or 'mps' if available
device_cpu = torch.device("cpu")
device_mps = torch.device("mps") if torch.backends.mps.is_available() else None

# Define Mish activation
class Mish(nn.Module):
    def forward(self, x):
        return x * torch.tanh(F.softplus(x))

# Define the model as described
class SimpleConvModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.initial_conv = nn.Conv2d(3, 48, kernel_size=3, padding=1)
        self.block = nn.Sequential(*[
            nn.Sequential(nn.Conv2d(48, 48, kernel_size=3, padding=1), Mish())
            for _ in range(8)
        ])
        self.final_conv = nn.Conv2d(48, 3, kernel_size=3, padding=1)

    def forward(self, x):
        x = self.initial_conv(x)
        x = F.interpolate(x, size=(1024, 1024), mode='bicubic', align_corners=True, antialias=True)
        x = self.block(x)
        x = F.interpolate(x, size=(2048, 2048), mode='bicubic', align_corners=True, antialias=True)
        x = self.final_conv(x)
        return x

# Function to benchmark
def benchmark(device):
    model = SimpleConvModel().to(device)
    input_tensor = torch.randn(1, 3, 2048, 2048, device=device)

    # Warmup
    for _ in range(3):
        _ = model(input_tensor)

    torch.cuda.empty_cache() if device.type == 'cuda' else None
    torch.mps.empty_cache() if device.type == 'mps' else None

    torch.manual_seed(0)
    start = time.time()
    with torch.no_grad():
        for _ in range(5):
            _ = model(input_tensor)
    end = time.time()
    print(f"Device: {device} | Time per forward pass: {(end - start)/5:.4f} seconds")

# Run benchmarks
benchmark(device_cpu)
if device_mps:
    benchmark(device_mps)
else:
    print("MPS not available on this machine.")
