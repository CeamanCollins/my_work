# Electricity Rates Analysis

## Overview

This folder contains analyses of 2024 electricity usage for multiple addresses, comparing the consumption data with various tariffs to determine the optimal choice. The analysis includes visualizations of electricity consumption and generated electricity fed back into the grid.

---

## Contents

### 1. [1MC Analysis](./1mc.ipynb)
- This notebook analyzes electricity usage for the address 1MC.
- It calculates totals for each rate stratification and compares them against several available tariffs to determine the best option.

### 2. [23OLR Analysis](./23olr.ipynb)
- This notebook analyzes electricity usage for the address 23OLR.
- It calculates totals for each rate stratification and compares them against several available tariffs to determine the best option.

### 3. [Ardamine Analysis](./ardamine.ipynb)
- This notebook analyzes electricity usage for the address Ardamine.
- It calculates totals for each rate stratification and compares them against several available tariffs to determine the best option.

### 4. [Weekly Electricity Visualization](./electricity_plots.ipynb)
- This notebook visualizes electricity usage and electricity fed back into the network at three addresses:
  - 1MC
  - 23OLR
  - Ardamine

### 5. [Feed-in Tariff Analysis](./feed_in.ipynb)
- This notebook calculates the financial benefit earned through feeding excess electricity back into the network.

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
- **Matplotlib**: For creating visualizations like graphs and charts.
- **NumPy**: For numerical computations.
- **GitHub CodeSpaces**: Cloud-based environment for running and testing the notebooks.

---

## Contact

If you have any questions or suggestions regarding this project, please contact **Céaman Collins** via [GitHub](https://github.com/CeamanCollins).
