# version-tab

A research-driven deep learning repository focused on mathematical problem solving, symbolic reasoning, math-based vectorization, and large language model (LLM) development.

Based on the original work of Saxton et al., 2019, this project explores ESA/SA vectorizers, T5-based inference, end-to-end analysis, and advanced deep learning research. It is an extension of `version-sdk`, a custom software development kit for data science workflows and other domains.

**Research Paper:** [Analysing Mathematical Reasoning Abilities of Neural Models](https://openreview.net/pdf?id=H1gR5iR5FX)

**Mathematics Datasets:**
- [Google DeepMind](https://github.com/google-deepmind/mathematics_dataset)
- [Hugging Face](https://huggingface.co/datasets/deepmind/math_dataset)

---

## 📁 Project Structure

```
version-tab/
├── docs/        
├── models/         
├── notebooks/      
├── predictions/    
├── requirements.txt
├── pixi.toml
├── pixi.lock
└── README.md
```

---

## ⚡ Setup

```bash
# Install Pixi if not already installed
curl -sSf https://pixi.sh/install.sh | bash

# Initialize Pixi (creates pixi.toml and pixi.lock)
pixi init

# Install dependencies from requirements.txt
pixi add --pip -r requirements.txt

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
