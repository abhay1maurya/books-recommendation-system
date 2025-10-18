from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn import neighbors
from sklearn.preprocessing import MinMaxScaler

# Initialize the Flask app
app = Flask(__name__)

# Load and preprocess the data
df = pd.read_csv('books.csv', on_bad_lines='skip')
df2 = df.copy()

# Add rating categories
df2.loc[(df2['average_rating'] >= 0) & (df2['average_rating'] <= 1), 'rating_between'] = "between 0 and 1"
df2.loc[(df2['average_rating'] > 1) & (df2['average_rating'] <= 2), 'rating_between'] = "between 1 and 2"
df2.loc[(df2['average_rating'] > 2) & (df2['average_rating'] <= 3), 'rating_between'] = "between 2 and 3"
df2.loc[(df2['average_rating'] > 3) & (df2['average_rating'] <= 4), 'rating_between'] = "between 3 and 4"
df2.loc[(df2['average_rating'] > 4) & (df2['average_rating'] <= 5), 'rating_between'] = "between 4 and 5"

# One-hot encode categorical features
rating_df = pd.get_dummies(df2['rating_between'])
language_df = pd.get_dummies(df2['language_code'])

# Combine features
features = pd.concat([rating_df, language_df, df2['average_rating'], df2['ratings_count']], axis=1)

# Scale features
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

# Train the model
model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)

# Book recommender function
def BookRecommender(book_name):
    if book_name not in df2['title'].values:
        return ["Book not found in the database."]
    book_list_name = []
    book_id = df2[df2['title'] == book_name].index[0]
    for newid in idlist[book_id]:
        book_list_name.append(df2.loc[newid].title)
    return book_list_name

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form['book_name']
    recommendations = BookRecommender(book_name)
    return jsonify(recommendations)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
