from flask import Flask, render_template, request
from contact_models import Contact
from google.cloud import ndb

app = Flask(__name__, template_folder='template')
client = ndb.Client()
@app.route(r'/', methods=["GET"])
def contact_book():
    query = Contact.query()
    names = [c.name for c in query]
    return render_template("contact_book.html",name=names[0])

@app.route(r"/add", methods=["GET","POST"])
def add_contact():
    if request.form:
        with client.context():
            contact = Contact(name = request.form.get("name"),
                          phone = request.form.get("phone"),
                          email = request.form.get("email")) 
            contact.put()   
    return render_template("add_contact.html")

if __name__ == '__main__':
    app.run()
