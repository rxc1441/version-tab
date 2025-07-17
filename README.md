# version-tab
[![Dependabot Updates](https://github.com/rcghpge/version-tab/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/rcghpge/version-tab/actions/workflows/dependabot/dependabot-updates)
[![CodeQL Advanced](https://github.com/rcghpge/version-tab/actions/workflows/codeql.yml/badge.svg)](https://github.com/rcghpge/version-tab/actions/workflows/codeql.yml)
[![Bandit](https://github.com/rcghpge/version-tab/actions/workflows/bandit.yml/badge.svg)](https://github.com/rcghpge/version-tab/actions/workflows/bandit.yml)
[![pages-build-deployment](https://github.com/rcghpge/version-tab/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/rcghpge/version-tab/actions/workflows/pages/pages-build-deployment)

A research-driven deep learning repository focused on mathematical problem solving, symbolic reasoning, math-based vectorization, and large language model (LLM) development.

Based on the original work of Saxton et al., 2019, this project explores ESA/SA vectorizers, T5-based inference, end-to-end analysis, and advanced deep learning research. It is an extension of `version-sdk`, a custom software development kit for data science workflows and other domains.

**Research Paper:** [Analysing Mathematical Reasoning Abilities of Neural Models](https://openreview.net/pdf?id=H1gR5iR5FX)

**Mathematics Datasets:**
- [Google DeepMind](https://github.com/google-deepmind/mathematics_dataset)
- [Hugging Face](https://huggingface.co/datasets/deepmind/math_dataset)

Initial benchmarks were considered but not implemented due to time constrained research and builds. They are provided under `data/` and `docs/`

---

## 📁 Project Structure

```
version-tab/
├── CITATION.cff
├── LICENSE
├── README.md
├── .github
├── .gitattributes
├── .gitignore
├── data
├── docs
├── models
├── notebooks
├── predictions
├── pixi.toml
└── pixi.lock
```

---

## ⚡ Setup

This project is built with [Pixi](https://pixi.sh/latest/) to manage environments and dependencies.

```bash
# Install Pixi if not already installed
curl -sSf https://pixi.sh/install.sh | bash

# Initialize Pixi (creates pixi.toml and pixi.lock)
pixi init

# Install dependencies from pixi.toml
pixi install

# Enter the Pixi environment
pixi shell
```

---

## 🚀 Quick Start

### Option 1: Using `pixi shell`

```bash
python models/basemodel.py
jupyter lab
```

### Option 2: Without entering the shell

```bash
pixi run python models/basemodel.py
pixi run jupyter lab
```

---

## 📊 Running & Viewing Results

1️⃣ Add your data in `math/` subdirectories.

2️⃣ Run:

```bash
python builds/basemodel.py or other models
```

- Generates predictions
- Outputs metrics (accuracy, F1 score, symbolic equivalence)
- Saves CSV results to `predictions/`

3️⃣ Check the model summary in `models/basemodel_summary.txt`.

---

## 🧪 Notebooks

Start Jupyter Lab:

```bash
jupyter lab
```

Open `basemodel.ipynb` or `prototype.ipynb` inside the `notebooks/` folder for exploratory workflows.

---

## 🔗 Links

- [Google DeepMind Math Dataset](https://github.com/google-deepmind/mathematics_dataset)
- [Hugging Face Math Dataset](https://huggingface.co/datasets/deepmind/math_dataset)

---

## Citations & Acknowledgements

If you found this repository helpful, please also consider citing the following works:

- Saxton et al., *Analysing Mathematical Reasoning Abilities of Neural Models*, arXiv:1904.01557.  
  https://arxiv.org/abs/1904.01557

- Gervais et al., *MathWriting: A Dataset for Handwritten Mathematical Expression Recognition*, arXiv:2404.10690.  
  https://arxiv.org/abs/2404.10690

- OpenAI, *Improving Mathematical Reasoning with Process Supervision*, 2022.  
  https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/

- Hendrycks et al., *Measuring Mathematical Problem Solving With the MATH Dataset*, arXiv:2103.03874.  
  https://arxiv.org/abs/2103.03874

For additional resources and implementation details, please see the [`docs`](https://github.com/rcghpge/version-tab/tree/main/docs) directory.

Data sources, licensing information, and data usage guidelines can be found in the [`data`](https://github.com/rcghpge/version-tab/tree/main/data) directory.

---

## 🛡️ Security Note
This repository is intended for research and open source collaborations and is not intended for production-grade use.

Security and reproducibility improvements are important and welcome via PR's 

---

