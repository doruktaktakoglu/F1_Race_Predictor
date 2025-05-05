F1 Race Predictor 🏎️💨 | Powered by FastF1 and Machine Learning
Welcome to my F1 Race Predictor project! As a huge Formula 1 fan (and a massive Max Verstappen supporter!), I’ve created this project to predict race outcomes based on qualifying times, driver performances, and the quality of their cars (teams). The goal is to use data-driven insights to simulate and predict race results using FastF1 and machine learning techniques.

🚗 What is this project about?
Formula 1 is all about precision, strategy, and performance, and this project aims to bring that into the world of data science. By leveraging data from past races, team performances (Constructors' Championship), and the magic of machine learning, I’ve built a model to predict race outcomes. This can give us insights into potential race winners and help us understand how qualifying performances and car quality impact race results.

This repo includes:

FastF1 Integration: Extracts real-time data from the F1 website (FastF1 library) for current and past races, including lap times and qualifying results.

Machine Learning Model: A Gradient Boosting Regressor model is used to predict race times based on qualifying data and the quality of the cars (as represented by the Constructors' Championship standings).

Data Preprocessing: The data is cleaned, merged, and features like driver performance and constructor rank are added to improve the predictions.

I built this to simulate how Max Verstappen might perform (no surprise, he’s always at the top!), but the model can be extended to predict outcomes for any driver and team!

🏁 Key Features
Real-Time Data Fetching: Pulls live data for race sessions and qualifying from the 2024 and 2025 F1 seasons.

Car Quality Feature: Incorporates the Constructors' Championship ranking as an additional feature to assess car quality in predictions.

Driver Mapping: Maps each driver to their respective teams, considering their historical performance to make more accurate predictions.

Race Outcome Predictions: Provides predicted race times for drivers based on qualifying performance and car quality.

🧑‍💻 Technologies Used
FastF1: For extracting official F1 data (lap times, qualifying results, etc.).

Pandas & NumPy: For data manipulation and analysis.

Scikit-learn: For building and training the machine learning model.

Gradient Boosting Regressor: Used to predict lap times based on features like qualifying performance and constructor rankings.

🏆 Supported Drivers and Teams
While I’m personally rooting for Max Verstappen (Red Bull Racing) and his incredible streak, the model can support any driver and team combination. The project currently supports a range of 2025 drivers such as Lando Norris, Charles Leclerc, Lewis Hamilton, and others.

🚀 How to Use
To run the F1 Race Predictor on your local machine:

Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/f1-race-predictor.git
cd f1-race-predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the script to start predicting race outcomes for the 2025 season:

bash
Copy
Edit
python predict_race.py
🏎️ Why Max Verstappen?
As a huge Max Verstappen fan, I’ve built this project with the hope of showcasing his incredible talent and dominance on the track. Whether it's his strategic racecraft, his unmatched consistency, or his ability to perform under pressure, Max is a driver who always delivers. My predictions? Well, Max will probably take the top spot, as usual! 😉

🧑‍🔬 Contributing
If you’re a fellow F1 fan, feel free to contribute to this repo! Whether it’s adding new features, improving the model, or integrating more data sources — the more, the merrier! Feel free to fork the repo and submit pull requests.

👑 About Me
I’m an F1 enthusiast, passionate about data science, and of course, supporting Max Verstappen and Red Bull Racing. My dream is to bring the excitement of Formula 1 into the world of machine learning, combining my two loves: speed and data!

