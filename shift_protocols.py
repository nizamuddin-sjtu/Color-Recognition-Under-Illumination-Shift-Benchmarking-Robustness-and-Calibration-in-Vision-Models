import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--protocol', type=str, default='shift_a')
parser.add_argument('--model', type=str, default='resnet18')
args = parser.parse_args()

print(f'Running {args.protocol} using {args.model}')

# Shift-A protocol
# Shift-B protocol
# Cross-illumination evaluation
