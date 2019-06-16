from flaskblog import create_app  # import for init file of flaskblog package

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
