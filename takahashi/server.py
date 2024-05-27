from flask_blog import app

if __name__=='__main__':
    app.run()

# error about '実行したまま終了せずに新しいファイルを実行させようとしたとき'
#      * Serving Flask app "flask_blog" (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
# Traceback (most recent call last):
#   File "/home/matcha-23training/projects/Flask-_awesome/takahashi/server.py", line 4, in <module>
#     app.run()
#   File "/home/matcha-23training/.pyenv/versions/3.10.8/lib/python3.10/site-packages/flask/app.py", line 990, in run
#     run_simple(host, port, self, **options)
#   File "/home/matcha-23training/.pyenv/versions/3.10.8/lib/python3.10/site-packages/werkzeug/serving.py", line 991, in run_simple
#     s.bind(server_address)
# OSError: [Errno 98] Address already in use