# Electricity Rates Analysis

## Overview

This folder contains analyses of 2024-25 electricity usage and production for multiple addresses, comparing the consumption and production data with various tariffs to determine the optimal choice.

---

## Contents

### 1. [1MC Analysis](./energy_cost_comparison_2026_1mc.ipynb)
- This notebook analyzes electricity usage and production and gas usage for the address 1MC.
- It calculates totals for each rate stratification and compares them against several available tariffs to determine the best option.
- Takes into account standing charges, new customer bonuses and microgeneration returns.

### 2. [23OLR Analysis](./energy_cost_comparison_23olr.ipynb)
- This notebook analyzes electricity usage and production and gas usage for the address 23OLR.
- It calculates totals for each rate stratification and compares them against several available tariffs to determine the best option.
- Takes into account standing charges, new customer bonuses and microgeneration returns.

### 3. [Data](./data/)
- This folder contains the data used for the calculations.

### 4. [Output](./output/)
- This folder contains the outputs of the final calculations from the notebooks.
---

## How to Use

### Running in GitHub CodeSpaces:
1. Open the repository in [GitHub CodeSpaces](https://github.com/features/codespaces).
2. Navigate to the **electricity_rates** folder.
3. Open the desired notebook (e.g., `1mc.ipynb`) and execute it cell by cell.

### Running Locally:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CeamanCollins/my_work.git
   cd my_work/electricity_rates
   ```
2. Install the required dependencies:
   - **Using Pip**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Using Conda**:
     ```bash
     conda create --name <environment-name> --file requirements.txt
     ```
3. Open the notebooks using Jupyter or VSCode:
   ```bash
   jupyter notebook
   ```

---

## Technologies Used

- **Python**: The primary programming language for the analysis.
- **Jupyter Notebook**: Interactive environment for conducting and presenting the analysis.
- **Pandas**: For data manipulation and analysis.
- **GitHub CodeSpaces**: Cloud-based environment for running and testing the notebooks.

---

## Contact

If you have any questions or suggestions regarding this project, please contact **Céaman Collins** via [GitHub](https://github.com/CeamanCollins).
