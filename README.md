# Outlier detection - CSIC 2010 Dataset Analysis and Classification

This repository contains solutions for an interview assignment to parse, analyze, and classify HTTP requests using the CSIC 2010 dataset. The goal is to train a classifier to distinguish between normal (legitimate) and malicious (anomalous) HTTP requests.

## About the Dataset

The CSIC 2010 HTTP dataset is a well-known dataset used for anomaly detection and web attack detection in cybersecurity research. It was created by the CSIC (Spanish Research National Council) and contains thousands of normal and malicious HTTP requests to test intrusion detection systems (IDS) and web application firewalls (WAF).

Key Features of the CSIC 2010 Dataset:
* Contains 36,000+ HTTP requests (both normal and anomalous).

* Includes various types of web attacks, such as:

   * SQL Injection (SQLi)

   * Cross-Site Scripting (XSS)

   * Buffer Overflow

   * Path Traversal

   * Parameter Tampering

* Used for machine learning-based intrusion detection research.

* Requests are labeled as normal or attack.

## Repository Structure

- **/dataset**: Contains the CSIC 2010 dataset in a zip file format.
- **/initial-solution**: First attempt at solving the assignment, including initial exploration and model prototyping.
- **/LLMs-solutions**: Solutions generated using large language models like ChatGPT and Gemini.
- **/final-solution**: Final refined solution for the assignment with improved performance and analysis.

## Assignment Overview

### Goal

The primary objective is to develop a classifier capable of identifying malicious HTTP requests by training on normal traffic data and evaluating both normal and anomalous test data. The dataset is structured as follows:

- **Normal Traffic (Train)**
- **Normal Traffic (Test)**
- **Anomalous Traffic (Test)**

Although the dataset is designed for unsupervised learning, supervised learning techniques can be applied by combining normal and anomalous data into a labeled dataset. This allows for direct classification using any preferred machine learning model.

### Approach

1. **Data Parsing and Exploration**:
   - Load and inspect the dataset to understand its structure and content.
   - Perform data preprocessing and feature engineering to prepare for model training.

2. **Model Training and Evaluation**:
   - Train a supervised classifier on the labeled dataset.
   - Evaluate the model's performance using appropriate metrics (e.g., accuracy, precision, recall, F1-score).
   - Iterate on model improvement based on initial results.

3. **Analysis and Conclusion**:
   - Analyze the classifier's performance and draw conclusions on its effectiveness.
   - Discuss the potential for using the classifier in a production environment.

## Getting Started

### Prerequisites

Ensure you have Python and Jupyter Notebook installed on your system. You will also need to install the required libraries listed in the `requirements.txt` file.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/realivanivani/net-traffic-classifier.git
   cd net-traffic-classifier
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

- **Run Jupyter Notebook**:
  ```bash
  jupyter notebook
  ```

- Open and execute the notebooks in each solution folder to see the development process and final results.

## Conclusion

In the final solution notebook, we provide a detailed discussion on the model's performance and the feasibility of deploying such a classifier in a production environment. We also highlight any challenges faced and insights gained throughout the process.

## References

Include any academic papers, online resources, or documentation that were helpful during the assignment.

## License

This project is licensed under the CSIC License - see their page [LICENSE]([LICENSE](http://www.isi.csic.es/dataset/)) for details.

## Contact

For any questions or feedback, please contact [Ivan Ivani] at [jasamivanivani@gmail.com].
