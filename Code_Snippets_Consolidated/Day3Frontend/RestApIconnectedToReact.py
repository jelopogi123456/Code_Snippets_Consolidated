from flask import Flask, jsonify,request
import pandas as pd
import json
import re
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def clean_text(text):
    # Replace all non-alphanumeric characters with spaces
    cleaned_text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    return cleaned_text

# Load the summarized articles from the JSON file
df = pd.read_json('C:\\Users\\MARK3\\Downloads\\summarized_article_intern.json', orient='records')

@app.route('/api/v1/summarized_articles', methods=['GET'])
def get_summarized_article():
    filters = request.args.to_dict()
    filtered_df = df.copy()
    for key, value in filters.items():
        filtered_df = filtered_df[filtered_df[key].astype(str).str.contains(value, case=False)]
    articles = filtered_df.to_dict('records')
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
