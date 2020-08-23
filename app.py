from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import dbtest
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/postdb'

db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False,default='N/A')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'Blog post ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        # new_post = BlogPost(title=post_title, content=post_content)
        # db.session.add(new_post)
        # db.session.commit()
        dbtest.create(post_title, post_content, "john")
        return redirect('/posts')
    else:
        # myposts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
        myposts = dbtest.getAll()
        return render_template('posts.html', posts=myposts)
        
if __name__ == '__main__':
    app.run(debug=True)