from flask import Flask, render_template, request, redirect, url_for
import random

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            num_lists = int(request.form.get('num_lists', 3))
            return redirect(url_for('lists', num_lists=num_lists))
        return render_template('index.html')

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

        return render_template('lists.html', num_lists=num_lists, shuffled_lists=shuffled_lists, total_words=total_words)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
