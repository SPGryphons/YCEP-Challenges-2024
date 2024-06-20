from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
  admin_cookie = request.cookies.get('admin')
  if admin_cookie == 'true':
    return 'YCEP24{v3Ry_EZ_C0oK1e_MAn1pU1@t!0N}'
  elif admin_cookie is None:
    resp = make_response("Sorry, only users with admin cookie can access this page.")
    resp.set_cookie('admin', 'false')
    return resp
  else:
    return 'Sorry, only users with admin cookie can access this page.'

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=1337)