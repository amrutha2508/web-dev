# Flaskblog

### Register Page

<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/6b5a1a7c-b9b4-4f5a-b054-2db776a14f47" width="300"/>
  <img src="https://github.com/user-attachments/assets/683689d6-b8fa-4317-a764-3c8a1aa8b2d4" width="300"/>
</div>

### Login Page

<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/8fd0a799-a07e-4de8-b73f-d21021981dcc" width="300"/>
  <img src="https://github.com/user-attachments/assets/0dae322f-0405-438e-b558-9ea8c68489cc" width="300"/>
</div>

### Intial steps to work with the flask-blog
1.     source env/bin/activate # activate the virtual env
2.     export FLASK_APP=run.py # Add a FLASK_APP environment variable


### Accessing DB via Terminal 
When dealing with databases, if you want to access the db related to app i.e, "site.db" run the followng commands first on the terminal after activating the env
1.      export FLASK_APP=flaskblog.py # By using flask shell we can eliminate the need for app.app_context()
2.      flask shell # to open the flask shell, an empty instance folder will be created
3.      from flaskblog import User, Post, db
4.      db.create_all() # Now you can site.db in the instance folder
        >> user_1 = User(username="Corey", email="c@demo.com",password="password")
        >>> db.session.add(user_1)
        >>> user_2 = User(username="John Doe", email="jd@demo.com",password="password")
        >>> db.session.add(user_2)
        >>> db.session.commit()
        >>> User.query.all()
        [User('Corey','c@demo.com','default.jpeg'), User('John Doe','jd@demo.com','default.jpeg')]
        >>> User.query.first()
        User('Corey','c@demo.com','default.jpeg')
        >>> User.query.filter_by(username="Corey").all()
        [User('Corey','c@demo.com','default.jpeg')]
        >>> user = User.query.filter_by(username="Corey").first()
        >>> user.id
        1
        >>> user
        User('Corey','c@demo.com','default.jpeg')
    
  
        >>> post_1 = Post(title="block1",content="first post content", user_id = user.id)
        >>> post_2 = Post(title="block2",content="Second post content", user_id = user.id)
        >>> db.session.add(post_1)
        >>> db.session.add(post_2)
        >>> db.session.commit()
        >>> user.posts
        [Post('block1','2025-07-29 22:32:46.876946'), Post('block2','2025-07-29 22:32:46.877167')]
        >>> for post in user.posts:
        ...     print(post.title)
        ... 
        block1
        block2
        >>> post = Post.query.first()
        >>> post
        Post('block1','2025-07-29 22:32:46.876946')
        >>> post.user_id
        1
        >>> post.author
        User('Corey','c@demo.com','default.jpeg')

