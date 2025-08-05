# version-tab

* **One Sentence Summary**

  A comparative deep learning and classical ML repository for modeling symbolic math reasoning, housing market trends, and housing price prediction using real-world and synthetic datasets.

---

## Overview

* **Definition of Tasks / Challenge**

  This project tackles three supervised learning tasks:

  1. Multiclass classification of symbolic math problems from the Google DeepMind MATH dataset.
  2. Semantic classification of real estate markets (hot, cold, stable) using Texas A\&M housing activity data.
  3. Regression modeling of median home values using the California housing dataset from Scikit-learn.

* **Approach**

  Vectorization (TF-IDF, ESA/SA), feature engineering (labels), and neural networks to handle classification tasks. For regression, the implementation is a standard linear regression model. Evaluation included accuracy, F1-score, and R^2 metrics.

* **Performance Summary**

  - MATH multiclass classification: \~61% interpolate accuracy, ~73% extrapolate accuracy
  - Texas housing market trend classification: \~86% accuracy
  - California median housing pices regression: R^2 \~0.78

---

## Summary of Workdone

### Data

* **Type:**

  * MATH: symbolic text inputs (.txt), output: math concept labels
  * Texas Housing Data: tabular CSV, input features: inventory + sales %, output: semantic label
  * California Housing Data: numeric tabular, input features (8), output: continuous price

* **Size:**

  * MATH: \~1,000+ samples per concept type
  * Texas Housing Data: \~35 samples
  * California Housing Data: \~21,000 samples

* **Splits:**

  * MATH: train/interpolate/extrapolate
  * Texas Housing Data: 85/15 train/test 
  * California Housing Data: 90/10 train/test

  For all datasets considered for this project please see `data/` directory for more information
  
#### Preprocessing / Cleanup

* Applied TF-IDF, ESA/SA vectorizers (MATH)
* Encoded labels via `LabelEncoder`
* Normalized numeric inputs via `StandardScaler`

#### Data Visualization

* Confusion matrices for classification results
* PCA plots mapping SA/ESA embeddings
* Scree plots and biplots for top concept features
* Training curves accuracy vs val accuracy, training loss vs val loss
* Actual vs. predicted scatter plots (regression)

### Problem Formulation

* **Input / Output:**

  * MATH: symbolic math text → concept label
  * Texas Housing Data: sales/inventory data → semantic class
  * California Housing Data: 8 census features → median house value

* **Models:**

  * Base Model with MATH: Keras multiclass classifier (Dense+Dropout)
  * Classification model with Texas Housing Data: Keras 3-class classifier (hot, cold, stable)
  * Regression model with California Housing Data: Linear Regression (Median house values)

* **Loss / Optimizer / Hyperparameters:**

  * Classification: `sparse_categorical_crossentropy`, Adam, Dropout (0.2-0.3)
  * Regression: closed-form least squares (MSE/R^2)

---

### Training

* **How Models Were Trained:**

  * Keras models run on CPU (10–20 epochs)
  * Regression trained instantly via Scikit-learn

* **Duration:**
  
  * Base Model took a bit because of vectorizing the data
  * Classification: \~30s
  * Regression: \~1s

* **Training Curves:**

  * Loss vs. accuracy plotted
  * Monitored interpolation and extrapolation accuracy for MATH

* **Challenges:**

  * ESA/SA vectorizer preprocessing
  * No set standards in these spaces
  * Label mismatch handling for unseen extrapolation classes
  * Explainable AI - XAI


### Performance Comparison

| Task                 | Model            | Dataset     | Metric   | Score  |
| -------------------- | ---------------- | ----------- | -------- | ------ |
| Model inference for math  | Keras (TF-IDF)   | Interpolate | Accuracy | \~61%  |
|                      |                  | Extrapolate | Accuracy | \~73%  |
| Texas Housing Market Trends | Keras            | Test        | Accuracy | \~86%  |
| California Median Housing Prices   | LinearRegression | Test        | R^2      | \~0.78 (78%) |

---

## 📊 Visual Overview

Click images to enlarge

---

### MATH Model Results
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/basemodelmathdata.png" alt="MATH Input" width="400" height="300"/></td>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/basemodelsaesaplot.png" alt="ESA/SA Plot" width="400"/></td>
  </tr>
</table>

### Texas Housing Classification Results
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/classificationmodel.png" alt="Classification Model" width="400"/></td>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/classificationtraining.png" alt="Training Curve" width="400"/></td>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/classificationtrainingaccuracy.png" alt="Accuracy Curve" width="400"/></td>
  </tr>
</table>

### California Housing Regression Results
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/regressionmodel.png" alt="Regression Model" width="400"/></td>
    <td><img src="https://raw.githubusercontent.com/rcghpge/version-tab/main/assets/regressionmodelr2.png" alt="R2 Score" width="400"/></td>
  </tr>
</table>

---

### Conclusions

* Keras is a challenge for symbolic reasoning in ML/DL - It is barely understood today.
* Keras performs well on tabular multiclass problems.
* Feature engineering was key in Texas real estate market trend prediction.
* Even simple linear regression achieved strong results on housing price prediction.

---

### Future Work

* Add GPT/T5 reasoning layer to MATH classification
* Integrate multi-modal housing datasets (e.g., geospatial)
* Apply SHAP/XAI to interpret classification boundaries
* XAI - Explainable AI
* Secure ML/DL systems

---

## How to Reproduce Results

### Requirements

```bash
curl -sSf https://pixi.sh/install.sh | bash
pixi init
pixi install
pixi shell
```

### Run Models

```bash
# Real Estate Market Classifier
python models/classificationmodel.py

# Median Housing Price Regression Model
python models/regressionmodel.py

# MATH Classifier
python models/basemodel.py
```

### Jupyter

```bash
jupyter lab
# Open any of:
# notebooks/classificationmodel.ipynb
# notebooks/regressionmodel.ipynb
# notebooks/basemodel.ipynb
```

---

### Overview of Files in Repository

```bash
verion-tab/
├── .github/workflows/           # CI/CD workflows (e.g., CodeQL)
├── assets/                      # GUI rendering images
├── data/                        # Tabular and symbolic datasets (incl. MATH)
├── docs/                        # HTML documentation and dataset explorer
├── models/
│   ├── basemodel.py             # MATH classification model
│   ├── classificationmodel.py  # Texas Housing semantic market classifier
│   ├── regressionmodel.py      # California housing price regression model
├── notebooks/                  # Jupyter notebooks for each modeling task
├── predictions/                # Final output submissions and test predictions
├── .gitattributes              # Git settings for text encoding / line endings
├── .gitignore                  # Ignored files for Git tracking
├── CITATION.cff               # Citation metadata for academic referencing
├── LICENSE                     # Open source license (MIT)
├── README.md                   # Project overview and documentation (this file)
├── pixi.lock                   # Lockfile for Pixi environment reproducibility
├── pixi.toml                   # Pixi environment specification
```

---

### Software Setup

* Python >= 3.12.11
* TensorFlow, Scikit-learn, Seaborn, Pandas, NumPy
* Pixi or Conda environment preferred

---

### Data

* MATH Dataset: Google DeepMind (text)
* A\&M Dataset: housing-activity.csv 
* Housing Dataset: auto-loaded via `fetch_california_housing()`

#### Preprocessing Steps

* TF-IDF vectorization, ESA joblib loading
* Standard scaling and label encoding via sklearn

---

### Training

* Run each `models/*.py` script or corresponding notebook
* You will need to build the vectorizers
* Models log metrics and save output summaries to `.txt`
* Run Jupyter notebooks for EDA, or building your own models

#### Performance Evaluation

* View `classification_report` output in terminal
* Visualize via Seaborn/Matplotlib plots in notebooks
* Confusion matrix and residual histograms included

---

## Citations

Further citation of works cited are referenced at `data/` and `docs/`

* Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... & Liu, P. J. (2020). [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683). *Journal of Machine Learning Research, 21(140), 1–67*.
* Saxton et al., "Mathematical Reasoning Tasks", DeepMind (2019)
* Hendrycks et al., "MATH: Measuring Mathematical Problem Solving", arXiv:2103.03874
* Scikit-learn California Housing Dataset
* Texas A\&M, Texas Real Estate Research Center 
* TensorFlow, Scikit-learn documentation

---

