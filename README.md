# F1 Race Predictor

Welcome to my F1 Race Predictor project! 🚗💨

As a huge **Formula 1** fan and a dedicated supporter of **Max Verstappen**, this project was born from my passion for the sport and the desire to make predictions on F1 race outcomes using historical data and machine learning models. The goal is to create a model that can predict the performance of drivers based on their qualifying times, race times, and additional car-related features, such as the car's constructor quality.

## Features

- **Race & Qualifying Data**: Retrieves and processes F1 race data from both 2024 and 2025 sessions.
- **Machine Learning**: Implements machine learning models (currently Gradient Boosting Regressor) to predict race times.
- **Constructor's Championship Data**: Adds car performance data from the Constructor's Championship to enhance predictions.

## How It Works

This project uses the **FastF1** library to fetch real-time and historical Formula 1 data. We use this data to train a machine learning model that predicts the race times of drivers based on their qualifying performance. The model is further enhanced with information about car constructors' performance.

## Dependencies

- **FastF1**: A Python library for fetching F1 data.
- **pandas**: For data manipulation.
- **sklearn**: For implementing machine learning algorithms.
- **numpy**: For numerical operations.

## Getting Started

To get started, clone this repository and install the necessary dependencies.

```bash
git clone https://github.com/yourusername/f1-race-predictor.git
cd f1-race-predictor
pip install -r requirements.txt
