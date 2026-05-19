import argparse
import torch

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='resnet18')
args = parser.parse_args()

print(f'Training model: {args.model}')

# Add training pipeline here
# Dataset loading
# Model initialization
# Optimization
# Checkpoint saving
