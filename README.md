  ![Heart Attack Prediction Model](src/HeartAttackPredictionModelGif.gif)

## Project Introduction

This project aims to build a heart attack risk prediction model that utilizes accessible and feasible features (physical condition, lifestyle, medical history, etc).

## Table of Contents

- [References to Analysis](#references-to-analysis)
- [Project Overview](#project-overview)
- [Data Science Solutions](#data-science-solutions)
- [Dataset Description](#dataset-description)
- [Data Dictionary](#data-dictionary)


## References to Analysis
For those who wish to deepen their understanding of the processes and findings in Exploratory Data Analysis, Modeling, and Evaluation, please refer to the links below for direct access to Jupyter Notebooks
1. [Data Import Preliminary Preprocessing Preliminary EDA]()

## Project Overview
- **Motivation:**<br>
 My interest in this project is deeply personal; having lost my uncle to cardiac arrest and witnessing family members affected by cardiac disease, I often feel anxious about my own risk of having a heart attack, especially during times of high stress, lack of sleep, or insufficient exercise. This personal experience drives my eagerness to build a model that can assess the risk of heart attacks and 

- **Problem Description:** <br>
Heart attacks are a leading cause of death worldwide, incurring long-term health issues and substantial financial costs. Current risk assessment tools are limited by their reliance on blood test results and restrictions such as user's age. This project aims to create a more user-friendly, accessible heart attack prediction model using readily available features.

- **Affected Groups:** <br>
According to the CDC, approximately 805,000 people in the U.S. experience a heart attack each year, translating to someone suffering a heart attack every 40 seconds. This number underscores a staggering reality: many more people could be suffering from heart attacks when considering global population and undiagnosed cases. Common signs include chest discomfort, shortness of breath, upper body discomfort, and light-headedness. Symptoms can be subtle, particularly in women, who may experience non-painful signs such as fatigue or nausea, which can lead to delays in seeking emergency care. Therefore, it is crucial for individuals to be aware of their heart attack risk and stay vigilant for any relevant symptoms.


## Data Science Solution

- **Solution Overview:**<br>
The project aims to develop a classification model that predicts whether a user is at risk of having a heart attack. The model will utilize accessible features, including basic physical conditions, lifestyle and habits, medical history, and vaccination history.
- **Existing Solutions Drawbacks:**<br>
Multiple approaches have been developed to assist healthcare providers in assessing the risk of cardiovascular disease. Atherosclerotic Cardiovascular Disease [(ASCVD) Risk Calculator](https://tools.acc.org/ascvd-risk-estimator-plus/#!/calculate/estimate/) assesses the chances of a person aged 40 to 79 developing heart disease over the next 10 years. Similarly, [The American Heart Association Prevent Online Calculator](https://professional.heart.org/en/guidelines-and-statements/prevent-calculator) assesses the risk of heart failure for users aged 30 to 79.<br>
However, these models impose age restrictions, preventing users under 30 or over 80 from accessing them, and they require specific information such as HDL cholesterol levels, which can only be obtained through blood tests. An interesting finding during the exploratory data analysis (EDA) process is that age is positively correlated with the risk of heart attack; in fact, individuals aged 80 and above have the highest likelihood of experiencing a heart attack among all age groups. 

- **Expected Outcomes and Impact:** <br>
The model is designed to be accessible anytime, anywhere, allowing users to promptly identify their risk of heart attacks. This increased awareness of heart attack symptoms could lead to quicker responses during emergencies, ultimately saving lives. Even a modest reduction in heart attack incidents, such as 1%, could help approximately 8,050 individuals avoid experiencing a heart attack. With the average healthcare costs associated with heart attacks estimated at over $20,000,this could result in annual savings of approximately $161 million.


## Dataset Description

- **Data Source Update:** <br>
The previous data source was a Kaggle dataset where the owner transformed and generalized SAS data from the 2022 CDC BRFSS Survey. Upon detailed inspection, I discovered that the Kaggle dataset misrepresented several survey categories by categorizing 'Unknown' responses as missing values. This led to many entries being incorrectly labeled as missing when they actually contained valid information. Consequently, I decided to switch to the original 2022 BRFSS Survey Data to ensure accurate representation. Additionally, I expanded the dataset by combining it with the 2023 BRFSS Survey Data, effectively doubling its size.
- **Source of the Dataset:** <br>
The dataset for this project is sourced from the Centers for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System (BRFSS). This program conducts over 400,000 adult interviews each year through telephone surveys to gather comprehensive data on the health status and risk behaviors of U.S. residents.<br>
For this project, we utilize two specific datasets:<br>
1. [2022 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2022.html): This dataset includes information from the 2022 survey, detailing various health-related behaviors, conditions, and demographic factors.
2. [2023 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2023.html): This dataset features the latest survey data from 2023, further enriching our analysis with updated health information.


- **Overview of Dataset:** <br>
The 2022 BFRSS Survey dataset includes 445,132 observations and the 2023 BFRSS Survey dataset includes 433,323 observations.<br>
Both datasets contain various features structured as follows:
  - **Target Variable**: `had_heart_attack` (categorical, binary)
  - **Features**: 31 categorical variables, and 6 numerical variables

## Data Dictionary
The values within each variable reflect the respondents' answers to the corresponding questions.

### Field of Interest
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `had_heart_attack`           | (Ever told) you had a heart attack? | Categorical   |

#### Interviewee's Basic Information
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `year`    | Year which observation was recorded                             | Numeric   |
| `sex`                        | Sex of respondent                                   | Categorical   |
| `race_ethnicity_category`    | Race/ethnicity category                             | Categorical   |
| `age_category`               | Age category                                       | Categorical   |
| `state`                      | States in U.S. where respondent resides            | Categorical   |
| `height`          | Reported height in meters                           | Numeric       |
| `weight`       | Reported weight in kilograms                        | Numeric       |
| `bmi`                        | Body Mass Index                                     | Numeric       |

#### Health and Lifestyle Information
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `alcohol_drinkers`          | Adults who reported at least one drink in 30 days | Categorical   |
| `general_health`            | Respondent's general health condition                | Categorical   |
| `smoker_status`             | Respondent's smoking status                         | Categorical   |
| `e_cigarette_usage`         | Respondent's e-cigarette usage status              | Categorical   |
| `physical_activities`       | Participation in physical activities in the past month              | Categorical   |
| `physical_health_days`      | Poor physical health days in past 30 days         | Categorical   |
| `mental_health_days`        | Poor mental health days in past 30 days           | Categorical   |
| `stress_levels`        | How often does respondents feel stress in past 30 days         | Categorical   |

#### Medical History:<br>
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `had_angina`                | (Ever told) had angina or coronary heart disease?  | Categorical   |
| `had_stroke`                | (Ever told) had a stroke                           | Categorical   |
| `had_asthma`                | (Ever told) had asthma                             | Categorical   |
| `had_skin_cancer`           | (Ever told) had non-melanoma skin cancer          | Categorical   |
| `had_copd`                  | (Ever told) had COPD or related diseases           | Categorical   |
| `had_diabetes`              | (Ever told) had diabetes                           | Categorical   |
| `had_kidney_disease`        | (Ever told) had kidney disease (not stones)       | Categorical   |
| `had_depressive_disorder`    | (Ever told) had a depressive disorder              | Categorical   |
| `had_arthritis`              | (Ever told) had some form of arthritis             | Categorical   |
| `deaf_or_hard_of_hearing`   | Deaf or serious difficulty hearing                  | Categorical   |
| `blind_or_vision_difficulty` | Blind or serious difficulty seeing                  | Categorical   |
| `difficulty_walking`        | Serious difficulty walking or climbing stairs       | Categorical   |
| `difficulty_concentrating`   | Difficulty concentrating due to physical or mental conditions | Categorical   |
| `difficulty_dressing_bathing`| Difficulty dressing or bathing                      | Categorical   |
| `difficulty_errands`        | Difficulty doing errands due to physical or mental conditions | Categorical   |

#### Health Assessment Information
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `last_checkup_time`         | Time since last routine checkup                    | Categorical   |
| `chest_scan`                | Have you ever had a CT or CAT scan of your chest? | Categorical   |

#### Vaccination and Drug Use
| Variable                     | Description                                         | Data Type     |
|:----------------------------|:---------------------------------------------------|:-------------|
| `flu_vax`           | Received flu vaccine in the past 12 months         | Categorical   |
| `tetanus_vax`      | Received a tetanus shot in the past 10 years       | Categorical   |
| `pneumo_vax`           | Ever had a pneumonia shot                           | Categorical   |








