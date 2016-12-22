from gaesessions import SessionMiddleware

def webapp_add_wsgi_middleware(app):
	app = SessionMiddleware(app, cookie_key="Wrong_input_key_qwertyqwertyqwertyqwerty")
	return app