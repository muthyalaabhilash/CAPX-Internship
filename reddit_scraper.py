import praw
import pandas as pd
import re
from datetime import datetime

# Set up Reddit authentication
reddit = praw.Reddit(
    client_id='LHhkdd-Js1WB1oZvUZGRnA',  # Replace with your actual client_id
    client_secret='cRNKh0qJUdvrcZ8Frj5rhq-55tze2g',  # Replace with your actual client_secret
    user_agent='my_reddit_scraper by /u/Mean-Ad-8092'  # e.g., 'stock_scraper by /u/your_username'
)

# Access the desired subreddit
subreddit = reddit.subreddit('stocks')  # You can change 'stocks' to 'investing' or any other subreddit

# Function to extract stock tickers using regex
def extract_tickers(text):
    # Matches dollar sign followed by 1-5 uppercase letters (e.g., $TSLA, $AAPL)
    return re.findall(r'\$\b[A-Z]{1,5}\b', text)

# Scrape top posts and their comments
posts_data = []
for post in subreddit.hot(limit=50):  # Adjust the limit as needed
    post_content = post.selftext
    tickers = extract_tickers(post.title + " " + post_content)  # Extract tickers from title and body

    # Fetch comments
    post.comments.replace_more(limit=0)  # Replace "more comments" with actual comments
    comments = [comment.body for comment in post.comments.list()]  # Fetch all comments as a list

    posts_data.append({
        'Post Title': post.title,
        'Post Content': post_content,
        'Author/Source': post.author.name if post.author else 'Deleted',
        'Timestamp': datetime.fromtimestamp(post.created).strftime('%Y-%m-%d %H:%M:%S'),
        'Engagement Metrics (Upvotes)': post.score,
        'Engagement Metrics (Comments)': post.num_comments,
        'URL': post.url,
        'Stock Mentions': ', '.join(tickers) if tickers else 'None',
        'Comments': ' || '.join(comments) if comments else 'No comments'  # Combine comments into a single string
    })

# Save the data into a CSV file
df = pd.DataFrame(posts_data)
df.to_csv('reddit_stocks_posts_with_comments.csv', index=False)

print("Data has been saved to reddit_stocks_posts_with_comments.csv")