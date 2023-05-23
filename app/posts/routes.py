from flask import render_template

from app.posts import posts 

from app.extensions import db
from app.models.post import Post

@posts.route('/posts', methods=['GET' , 'POST'])
def index():
    posts = Post.query.all()
    return render_template ('posts/index.html', posts=posts)

@posts.route('/categories')
def categories():
    return render_template('posts/categories.html')