This project is a machine learning-based Resume Analyzer that evaluates a resume against a selected job role and provides structured, actionable feedback.

## Overview

The application extracts skills from resume text and compares them with the required skills for a selected role. It calculates a match score and highlights both matched and missing skills, along with suggestions for improvement.

## Features

- Role-based resume analysis  
- Skill extraction from text  
- Match score with visual progress indicator  
- Identification of matched and missing skills  
- Targeted suggestions for improvement  

## Tech Stack

- Python  
- Scikit-learn  
- Streamlit  

## Dataset

The resume dataset used in this project is sourced from Kaggle.  
It contains real-world resumes categorized into different job roles and was used to understand resume structure and terminology.

## How It Works

1. The user pastes their resume into the application  
2. Selects a target job role  
3. The system extracts relevant skills from the resume  
4. It compares them with predefined role requirements  
5. Displays:
   - Match score  
   - Matched skills  
   - Missing skills  
   - Suggestions for improvement  

## How to Run

1. Install dependencies:
   pip install pandas scikit-learn streamlit  

2. Run the application:
   streamlit run app.py  

## Future Improvements

- Support for PDF and DOCX resume uploads with automatic text extraction  
- Use of advanced NLP models (such as transformer-based models) for better semantic understanding  
- Improved skill extraction using named entity recognition (NER)  
- Personalized recommendations based on industry trends and job descriptions  
- Integration with live job portals to match resumes with real job listings  
- Visualization enhancements such as charts for skill coverage and match distribution  
- User authentication and profile saving for repeated analysis  
- Deployment as a full web application with backend services  

## Author

Developed as a Machine Learning project for academic purposes.
