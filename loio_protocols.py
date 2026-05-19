import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--leave_out', type=str, default='sunLight')
parser.add_argument('--model', type=str, default='resnet18')
args = parser.parse_args()

print(f'LOIO evaluation excluding: {args.leave_out}')

# Leave-One-Illumination-Out protocol
# Train on remaining illumination conditions
# Evaluate on unseen illumination
