from website import create_app

app = create_app()

# This makes a running web server
if __name__ == '__main__':
    # This runs the web app server- turn this off when in production
    app.run(debug=True)
