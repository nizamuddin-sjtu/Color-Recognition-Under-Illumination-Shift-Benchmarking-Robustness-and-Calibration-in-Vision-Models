import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='resnet18')
args = parser.parse_args()

print(f'Running calibration for: {args.model}')

# Temperature scaling
# Expected Calibration Error computation
# Reliability analysis
