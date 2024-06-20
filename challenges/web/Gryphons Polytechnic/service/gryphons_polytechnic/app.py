import os
import random
from functools import wraps

import jwt as pyjwt
from flask import (Flask, jsonify, make_response, render_template, request,
                   send_from_directory)
from flask_jwt_extended import JWTManager, create_access_token
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )
app.config[ "JWT_SECRET_KEY" ] = os.urandom( 24 )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///site.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy( app )
jwt_manager = JWTManager( app )


def jwt_required( f ):

    @wraps( f )
    def decorated_function( *args, **kwargs ):
        token = request.cookies.get( 'access_token', None )
        if not token:
            return jsonify( { "msg": "Missing JWT token in cookies" } ), 401
        try:
            payload = pyjwt.decode( token, app.config[ 'JWT_SECRET_KEY' ], algorithms = [ 'HS256' ] )
        except Exception as _:
            payload = pyjwt.decode( token, options = { "verify_signature": False } )

        request.current_user = payload[ 'sub' ]
        return f( *args, **kwargs )

    return decorated_function


class User( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 20 ), unique = True, nullable = False )
    password = db.Column( db.String( 60 ), nullable = False )


class GPA( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    user_id = db.Column( db.Integer, db.ForeignKey( 'user.id' ), nullable = False )
    gpa = db.Column( db.String( 100 ),
                     nullable = False )  # Let's not question why GPA is a string, maybe there's a flag here~


@app.before_request
def create_tables():
    app.before_request_funcs[ None ].remove( create_tables )
    db.drop_all()
    db.create_all()

    base_name = 230000
    flag_user = [ i for i in range( 100 ) if i != 21 ][ random.randint( 0, 98 ) ]
    for i in range( 100 ):
        username = f'P{base_name + i}'
        if i == 21:
            password = "password"
        else:
            password = ''.join(
                random.choices( 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k = 10 ) )

        user = User( username = username, password = password )
        db.session.add( user )
        db.session.commit()

        if i == flag_user:
            gpa = GPA( user_id = user.id, gpa = 'YCEP24{grypH0n$_5H0uLD_s7op_0v3RenGINeerIN9_57905b25b373280b814fa8c6826aceb5}' )
        else:
            gpa = GPA( user_id = user.id, gpa = str( random.uniform( 0.0, 4.0 ) ) )
        db.session.add( gpa )
        db.session.commit()


@app.route( '/login', methods = [ 'POST' ] )
def login():
    username = request.json.get( 'username', None )
    password = request.json.get( 'password', None )
    user = User.query.filter_by( username = username ).first()
    if not user or user.password != password:
        return jsonify( { "msg": "Bad username or password" } ), 401

    access_token = create_access_token( identity = username )
    response = make_response( jsonify( { "msg": "Login successful" } ), 200 )
    response.set_cookie( 'access_token', access_token, httponly = True, secure = False )
    return response


@app.route( '/img/<filename>' )
def img_file( filename ):
    return send_from_directory( 'img', filename )


@app.route( '/dashboard', methods = [ 'GET' ] )
@jwt_required
def dashboard():
    current_user_username = request.current_user
    user = User.query.filter_by( username = current_user_username ).first()
    if not user:
        return jsonify( { "msg": "User not found" } ), 404
    gpa = GPA.query.filter_by( user_id = user.id ).first()
    gpa.gpa = "{:.2f}".format( float( gpa.gpa ) ) if '.' in gpa.gpa else gpa.gpa
    return render_template( 'dashboard.html', username = user.username, gpa = gpa.gpa )


@app.route( '/' )
def home():
    return render_template( 'login.html' )


if __name__ == '__main__':
    app.run( host = '0.0.0.0', port = 5000 )
