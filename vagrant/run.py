from application import create_app
app = create_app()
app.debug = True
app.run(host='0.0.0.0', port=5000)
