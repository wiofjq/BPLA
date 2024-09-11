from flask import Flask
import pages, posts, errors


def create_app():
    app = Flask(__name__)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)
    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=8000, debug=True)










