# Regular ML/DL Models (Notebooks)

This repository contains five machine learning and deep learning notebooks that demonstrate classification across **tabular**, **image**, **audio**, and **text** data.  
Each notebook is self-contained and includes preprocessing, model training, evaluation, and (where relevant) interactive inference.

> **Datasets:** All datasets used were downloaded from Kaggle. They are **not included** in this repository. Please set dataset paths in the notebooks to run them locally.

---

## Contents

- **`f.ipynb`** — Tabular data classification (fully connected neural network)
- **`vid.ipynb`** — Image classification with interactive image upload for inference
- **`transform.ipynb`** — Transfer learning on images using pretrained backbones
- **`audio.ipynb`** — Audio classification (mel-spectrogram + CNN)
- **`text.ipynb`** — Sarcasm detection using Transformers (BERT/DistilBERT)

---

## Environment Setup

```bash
# Create virtual environment
python -m venv venv
# Activate
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers
pip install librosa
pip install scikit-learn
pip install pandas numpy matplotlib tqdm
pip install ipywidgets
