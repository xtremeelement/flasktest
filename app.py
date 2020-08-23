from flask import Flask, render_template

app = Flask(__name__)

myposts = [
    {
        'title': "post 1",
        'content': 'loremjlj  lksjdf lkj alsjdf',
        'author': 'testAuthor'
    },
    {
        'title': 'post 2',
        'content': 'lklka dkf as dflkaj sdf'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=myposts)

if __name__ == '__main__':
    app.run(debug=True)