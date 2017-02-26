from application import create_app,db
app = create_app()
app.debug = True
app.run(host='0.0.0.0', port=5000)
