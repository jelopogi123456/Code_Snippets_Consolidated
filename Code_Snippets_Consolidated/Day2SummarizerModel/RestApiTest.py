from flask import Flask, jsonify
import pandas as pd
import json
import re
app = Flask(__name__)

def clean_text(text):
    # Replace all non-alphanumeric characters with spaces
    cleaned_text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    return cleaned_text


# Load the summarized articles from the JSON file
df = pd.read_json('C:\\Users\\MARK3\\Downloads\\summarized_article_intern.json', orient='records')

# Define the route to get all summarized articles
@app.route('/api/v1/summarized_articles', methods=['GET'])
def get_summarized_articles():
    # Convert DataFrame to a list of dictionaries
    articles = df[['summarized_articles']].to_dict(orient='records')
    for article in articles:
        for k, v in article.items():
            article[k] = clean_text(str(v)).strip()
    return json.dumps(articles)

@app.route('/api/v1/summarized_articles/<int:index>', methods=['GET'])
def get_summarized_article(index):
    try:
        # Retrieve the article from the DataFrame by index
        article = df.loc[index, ['summarized_articles']].to_dict()
        for k, v in article.items():
            article[k] = clean_text(str(v)).strip()
        return json.dumps(article)
    except KeyError:
        return jsonify({'error': 'Article not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
