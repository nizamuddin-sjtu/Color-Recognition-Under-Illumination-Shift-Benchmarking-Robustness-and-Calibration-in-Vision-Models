# Color-Recognition-Under-Illumination-Shift-Benchmarking-Robustness-and-Calibration-in-Vision-Models

## Overview

This repository accompanies the manuscript:

> Submitted to *The Visual Computer* (Springer).

This work introduces a controlled benchmark for studying illumination robustness and probabilistic calibration in color recognition systems. The benchmark isolates illumination as an independent visual factor and evaluates how modern vision models behave under changing lighting conditions while semantic color labels remain fixed.

The repository includes:

- Deep learning training and evaluation pipelines
- Cross-illumination robustness protocols
- Calibration analysis using Expected Calibration Error (ECE)
- Classical machine learning baselines
- Dataset manifest generation
- Reproducibility instructions

---

# Motivation

Reliable color interpretation is essential for many visual computing systems, including:

- Extended Reality (XR)
- Augmented and Virtual Reality (AR/VR)
- Human–Robot Interaction (HRI)
- Robotic perception
- Autonomous systems
- Scene understanding
- Interactive visual interfaces

Although modern vision models often achieve near-perfect in-distribution accuracy, their predictions may become unreliable under illumination shift. This repository provides a compact benchmark for evaluating such failures under controlled lighting variations.

---

# Dataset

## Dataset Name

**Different Colors in Challenging Lightening v2**

## Dataset Link

Kaggle Dataset:

https://www.kaggle.com/datasets/nizamuddinmaitlo/different-colors-in-challenging-lightening-v2

---

# Dataset Structure

The dataset is organized as:

```text
<Color>/<Illumination>/<image>
```

Example:

```text
Blue/indoor/img001.jpg
Yellow/sunLight/img102.jpg
Pink/fluorescentLight/img210.jpg
```

---

# Color Classes

- Black
- Blue
- Gray
- Orange
- Pink
- Purple
- Skyblue
- White
- Yellow

---

# Illumination Conditions

- fluorescentLight
- indoor
- indoorNight
- sunLight

---

# Benchmark Protocols

## 1. In-Distribution Evaluation

Standard stratified train/validation/test evaluation.

Split ratio:

- 70% Training
- 15% Validation
- 15% Testing

Stratification is performed over the joint:

```text
Color × Illumination
```

---

## 2. Cross-Illumination Shift A

### Train

- indoor
- fluorescentLight

### Test

- sunLight
- indoorNight

This protocol evaluates generalization under unseen lighting conditions.

---

## 3. Cross-Illumination Shift B

### Train

- sunLight
- indoorNight

### Test

- indoor
- fluorescentLight

---

# Implemented Models

## Deep Learning Models

- ResNet-18
- MobileNetV3-Large
- ViT-Tiny

All deep models are initialized using ImageNet pretrained weights.

---

## Classical Baselines

- SVM-RBF
- Random Forest

Classical models use:

- Lab color histogram features
- PCA dimensionality reduction

---

# Calibration Evaluation

This repository evaluates both:

- Recognition accuracy
- Probabilistic calibration

Metrics include:

- Macro-F1
- Macro Accuracy
- Expected Calibration Error (ECE)

Temperature scaling is applied for post-hoc calibration.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/illumination-robust-color-recognition.git

cd illumination-robust-color-recognition
```

---

# Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Main dependencies:

- torch
- torchvision
- timm
- scikit-image
- scikit-learn
- pandas
- matplotlib
- Pillow

---

# Running the Benchmark

## Kaggle Version

The notebook automatically detects the dataset under:

```text
/kaggle/input
```

Attach the dataset using the Kaggle "Add data" option.

Run:

```bash
python benchmark.py
```

or execute the notebook directly in Kaggle.

---

# Generated Artifacts

The benchmark produces:

- manifest.csv
- train.csv
- val.csv
- test.csv
- results_in_distribution.csv
- results_shift_ab.csv
- results_classical.csv

---

# Example Results

| Model | Macro-F1 | Calibration |
|---|---|---|
| ResNet18 | Strong | Stable |
| MobileNetV3 | Strong | Moderate |
| ViT-Tiny | Competitive | Sensitive to illumination shift |

Cross-illumination experiments show that performance drops significantly under unseen lighting conditions despite strong in-distribution accuracy.

---

# Research Contributions

This benchmark contributes:

1. Controlled illumination robustness evaluation
2. Joint analysis of accuracy and calibration
3. Cross-illumination generalization protocols
4. Lightweight visual computing benchmark
5. Reproducible evaluation pipeline

---

# Citation

If you use this repository, please cite:

```bibtex
@article{maitlo2026illumination,
  title={Color Recognition under Illumination Shift for Visual Computing Systems: A Robustness and Calibration Benchmark},
  author={Maitlo, Nizamuddin and Shaikh, Riaz Ahmed and Arshid, Kaleem and Noonari, Nooruddin and Hussain, Afifa},
  journal={The Visual Computer},
  year={2026}
}
```

---

# License

This repository is released for academic and research purposes.

---

# Contact

## Corresponding Author

Nizamuddin Maitlo

Email:
contentwriter.nizam@gmail.com

Kaggle:
https://www.kaggle.com/nizamuddinmaitlo

---

# Acknowledgement

This repository was developed to support transparent and reproducible research on illumination-robust color perception for visual computing systems.
