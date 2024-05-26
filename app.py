from flask import Flask, render_template_string, request, redirect, url_for
import random

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_lists = int(request.form.get('num_lists', 3))
        return redirect(url_for('lists', num_lists=num_lists))
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Number of Lists</title>
            <style>
              body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                background-color: #f0f0f0;
              }
              .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 400px;
                width: 100%;
                text-align: center;
                margin-top: 40px;
              }
              h1 {
                margin-bottom: 20px;
              }
              button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
              }
              button:hover {
                background-color: #0056b3;
              }
              input[type="number"] {
                width: 60px;
                padding: 5px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                text-align: center;
              }
            </style>
          </head>
          <body>
            <div class="container">
              <h1>Select Number of Lists</h1>
              <form method="post">
                <label for="num_lists">Number of Lists:</label>
                <input type="number" id="num_lists" name="num_lists" value="3" min="1" required><br><br>
                <button type="submit">Next</button>
              </form>
            </div>
          </body>
        </html>
    ''')

@app.route('/lists/<int:num_lists>', methods=['GET', 'POST'])
def lists(num_lists):
    lists = [[] for _ in range(num_lists)]
    shuffled_lists = [[] for _ in range(num_lists)]
    total_words = 0
    
    if request.method == 'POST':
        for i in range(num_lists):
            words = request.form.get(f'words{i}', '')
            words_list = words.split('\n')
            words_list = [word.strip() for word in words_list if word.strip()]
            total_words += len(words_list)
            lists[i] = words_list
            shuffled_lists[i] = random.sample(words_list, len(words_list))
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Randomize Words</title>
            <style>
              body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                background-color: #f0f0f0;
              }
              .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 1200px;
                width: 100%;
                margin-top: 40px;
              }
              h1 {
                margin-bottom: 20px;
                text-align: center;
              }
              h2 {
                margin-bottom: 20px;
                text-align: center;
              }
              .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
              }
              textarea {
                width: 100%;
                box-sizing: border-box;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                resize: none;
              }
              button {
                display: block;
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                margin: 20px auto;
              }
              button:hover {
                background-color: #0056b3;
              }
              ul {
                list-style-type: none;
                padding: 0;
              }
              li {
                background: #f9f9f9;
                margin: 5px 0;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
              }
            </style>
          </head>
          <body>
            <div class="container">
              <h1>漢字リストのランダム化</h1>
              <h2>Kanji List Randomizer</h2>
              <form method="post">
                <div class="grid">
                  {% for i in range(num_lists) %}
                    <div>
                      <h3>List {{ i + 1 }}</h3>
                      <textarea name="words{{ i }}" rows="5" placeholder="Enter words, each on a new line"></textarea>
                    </div>
                  {% endfor %}
                </div>
                <button type="submit">Randomize</button>
              </form>
              <div class="grid">
                {% for i in range(num_lists) %}
                  {% if shuffled_lists[i] %}
                    <div>
                      <h3>Shuffled Words for List {{ i + 1 }}:</h3>
                      <ul>
                      {% for word in shuffled_lists[i] %}
                        <li>{{ word }}</li>
                      {% endfor %}
                      </ul>
                      <p class="word-count">Word Count: {{ shuffled_lists[i] | length }}</p>
                    </div>
                  {% endif %}
                {% endfor %}
              </div>
                <div class="total-words" style="font-weight: bold;" >Total Words: {{ total_words }}</div>
            </div>
          </body>
        </html>
    ''', num_lists=num_lists, shuffled_lists=shuffled_lists, total_words=total_words)

if __name__ == '__main__':
    app.run(debug=True)


