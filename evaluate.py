import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='resnet18')
args = parser.parse_args()

print(f'Evaluating model: {args.model}')

# Load trained model
# Compute Macro-F1
# Compute Accuracy
# Save predictions
