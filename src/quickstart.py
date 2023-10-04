
#an instance of the Flask class will be the WSGI app
from flask import Flask, abort
from markupsafe import escape

#flask needs to know where to look for resources (like templates and static files)
#they are often saved in the application's module or package
app = Flask(__name__)

#the route decorator tells flask the url that should trigger the function.
#this is a variable section! with the variable <name>
@app.route("/name/<name>")
def hello_world(name):
 return f"Hello, {escape(name)}!"

@app.route("/coffee")
def coffee():
 abort(418)

#glossary
#wsgi: web server gateway interface, a simple calling convention for web servers to forward requests to web applications or frameworks written in python.
#web servers need to interact with the application. They do this with their own api.
#web applications written in python would use different api's to communicate with the web server. This WSGI is a common standard for all python applications
#there are 3 levels to WSGI: the web server (like apache or ngind), the WSGI middle ware which implements the api for both, and the python application which is just a python callable.
#the io module: interface to stream handling.
#io.BytesIO: a simple stream of in-memory bytes
#functions are triggered by following an url.
#flask comes with a development server to test things out. But when you go serious, use a real server like nginx or apache.
#request.method : the request method of the request
#request.form : form data, data transmitted in POST or PUT request
#request.args.get('key', '') : access a parameter submitted in the url

#observations
#you can separate the response by the method used to access the url. This separation can be done in the methods argument to the app.route function, or by separating the functions by methods and decorating them with app.get and app.post and all the other methods.
#by default, a route only answers to GET requests
#you can have static files accessible to your application. Store them in a directory beside the app named static. You can generate the route with url_for('static', 'colors.css')
#flask will look for templates in the templates folder. besides the module of your app, or within the package of the app.
#to use the render_template() function, just return its result. Remember that flask just display the return of the functin associated with their url.
#there are proxy objects. Objects that point to a unique object bound to each working thread. They can't fake their type, so they will not be identified as the proxied object. If you want to make a instance check, you need the proxied object. To send a signal or pass data to a background thread you need the proxied object.
#sessions make it possible to remember information from one request to another. Flask does this with a signed cookie. the current session is saved in an object.
#sharing data between requests in a multithreaded environment
"""
Context locals
some global objects are not the actual objects.
They are proxies to
 an object that is
 local to
 a specific context.
a context is like a thread. And when flask handles a request,
it binds the current application and the WSGI environment to the correct context.

That is how flask has global variables work nicely with concurrency.
"""

#file upload:
#set enctype="multipart/form-data" attribute in your html form,
# or your browser will not transmit your files
#every uploaded file is stored in the files attribute on the request object.
#every uploaded file is stored in that dictionary.
#they have a special method called .save(), that stores the file on the file system of the server.
#if you want to see the name of the file in the client's system,
#use the filename attribute.
#But don't use that as the name to save it in your server, because it can be forged.
#At least, pass it through werkzeug.utils.secure_filename(request.files['filename'])

#cookies
#request.cookies.get('cookiename')
#return flask.make_response(render_template(...)).set_cookie('username', 'theusername')

#redirect
#return flask.redirect(url_for('login'))
#abort(401)

#customize error page
#from flask import render_template
#@app.errorhandler(418)
#def im_a_teapot(error):
# return render_template('im_a_teapot'), 418

#questions
#what is the configuration dictionary?
#what is a response object? Why are cookies set on it and not the default response?
# they seem to be returned by functions, the way strings are.
