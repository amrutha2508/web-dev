from flaskblog import create_app # going to import from the __init__.py file within flaskblog package

app = create_app()
if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


