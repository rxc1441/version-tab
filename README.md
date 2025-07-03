# version-tab

A research and novel deep learning repository focused on mathematical problem-h I'll solving, symbolic reasonying, math-based vectorization, and large language model (LLM) development.

Based on the original work of Saxton et. al, 2019. This project explores ESA/SA vectorizers, T5-based generation, and end-to-end model analysis, prototyping, and novel builds. Links to resources will be listed below.

Research Paper:[Analysing Mathematical Reasoning Abilities of Neural Models](https://openreview.net/pdf?id=H1gR5iR5FX)

Mathematics Dataset: 
- [Google DeepMind](https://github.com/google-deepmind/mathematics_dataset)
- [Hugging Face](https://huggingface.co/datasets/deepmind/math_dataset)




mmm

---

## 📁 **Project Structure**

```
version-tab/
├── docs/           # Static HTML reports, and plots
├── models/         # basemodel and test run on larger models.
├── notebooks/      # Jupyter notebooks for exploratory workflows
├── predictions/    # Saved prediction outputs
├── requirements.txt
├── __init__.py
└── README.md
```

The `math/` dataset and `keras-hub/` modules are not included in the repository. You will need to download or prepare these directories locally.

---

## ⚡ **Setup**

> 💡 Only `requirements.txt` is pushed to remote. You are not pushing `pixi.toml` or `pixi.lock`.

```bash
# Install Pixi if not already installed
curl -sSf https://pixi.sh/install.sh | bash

# Initialize Pixi project (creates pixi.toml)
pixi init

# Install dependencies from requirements.txt
pixi add --pip -r requirements.txt

# Enter the Pixi environment shell
pixi shell
```

---

## 🚀 **Quick Start**

### ✅ Option 1: Using `pixi shell`

Once inside the shell, you can run commands as usual:

```bash
python builds/model.py
jupyter lab
```

### ✅ Option 2: Without using `pixi shell`

If you prefer not to enter the shell, prefix each command:

```bash
pixi run python builds/model.py
pixi run jupyter lab
```

---

## 📥 **Prepare data and modules**

- Download or create the `math/` dataset locally (e.g., `train-medium/`, `interpolate/`, `extrapolate/`, etc.).
- Download or copy any necessary custom modules (such as `keras-hub/`).

---

## 📊 **Running and Viewing Results**

1️⃣ **Add your data**  
Place `.txt` math problem files into your local `math/` subdirectories.

2️⃣ **Run the prototype or models**

```bash
python builds/model.py
```

- Generates predictions
- Outputs metrics (accuracy, F1, symbolic equivalence)
- Saves CSV results to `predictions/`


4️⃣ **Check model summary**

See `models/model_summary.txt` of the basemodel.

---

## 🧪 **Notebooks**

Launch notebooks for exploratory workflows:

```bash
jupyter lab
```

Then open `model.ipynb` or `prototype.ipynb` inside the `notebooks/` folder.

