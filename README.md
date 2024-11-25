Stock Movement Prediction using Reddit Data


This project uses data scraped from Reddit's stocks subreddit to predict stock movements based on sentiment and engagement metrics.

Features
Scraping Reddit posts and comments using the PRAW library.
Sentiment analysis with VADER to extract polarity scores.
Machine learning model (Random Forest) for prediction.
Metrics for model evaluation (accuracy, precision, recall, F1-score).

Setup Instructions

1. Clone the Repository
bash
Copy code
git clone <repository_url>
cd <repository_name>


2. Set Up Python Environment
Ensure Python 3.7 or later is installed. Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies
Install all required libraries using the provided requirements.txt:
bash
Copy code
pip install -r requirements.txt


4. Configure Reddit API Credentials
Set up a .env file to store Reddit API credentials:
plaintext
Copy code
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USER_AGENT=your_user_agent
Replace the placeholders with your Reddit API credentials.



Running the Project
1. Scrape Reddit Data
Run the scraper script to collect data from the stocks subreddit:
Copy code
python reddit_scraper.py
Output: reddit_stocks_posts_with_comments.csv (contains posts, comments, and engagement metrics).


2. Preprocess Data
Preprocess the scraped data for machine learning:
Copy code
Ml NLP Algo.ipynd

3. Train the Model
Train the Random Forest model using the preprocessed data

4. Evaluate the Model
Evaluate the model on the test dataset


Steps 2 ,3, 4, done in one file: Ml NLP Algo.ipynd


