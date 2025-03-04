This repository contains the code and data for Assignment 1 of PDS course. This assignment focuses on creating a reproducible workflow for data processing and visualization on two datasets.

Folder Structure:

Assignment_1/
│
├── Q1_Frailty_Dataset/                # Frailty Dataset Analysis
│   ├── raw_data/                      # Raw dataset
│   │   └── frailty_data.csv           
│   ├── results/                       # Processed data and summary results
│   │   ├── cleaned_frailty_data.csv   # Cleaned dataset
│   │   └── summary_statistics.csv     # Summary statistics file
│   └── scripts/                       # Data processing scripts
│       └── data_processing.py        # Script to clean and process the frailty dataset
│
├── Q2_Student_Performance/           # Student Performance Dataset Analysis
│   ├── raw_data/                     # Raw dataset
│   │   └── StudentsPerformance.csv
│   ├── results/                      # Visualization results
│   │   ├── correlation_heatmap.png   
│   │   ├── math_score_distribution.png
│   │   ├── math_scores_gender.png
│   │   ├── reading_vs_writing.png
│   │   └── test_prep_math.png
│   └── scripts/                      # Data visualization scripts
│       └── data_visualization.py
│
└── README.md                         # Project description

Task Description

Task 1: Frailty Dataset Processing
        Cleaned data
        Calculated summary statistics
        Exported the cleaned dataset and summary to CSV files

Task 2: Student Performance Dataset Visualization
        Performed exploratory data analysis
        Generated visualizations for correlations, gender-based performance, and test preparation effects
