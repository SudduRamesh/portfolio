from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
import smtplib
from email.message import EmailMessage


@app.route("/")

@app.route("/welcome")
def welcome():
  return render_template('welcome.html',title='Welcome to my Portfolio')

@app.route("/home")
def home():

  return render_template('home.html',  title='About Me')

@app.route("/contact",methods=['GET','POST'])
def contact():
      
    
  if request.method == 'POST':
     
        
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

  

    #  gmail credentials of owner of the website
    your_email = "sudduramesh371@gmail.com"
    your_password = "tnzg jypw kgiy aexq"
    # connecting to the SMPT server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(your_email, your_password)
    sender_email ="sudduramesh371@gmail.com"
    receiver_email = "sudduramesh371@gmail.com"
    # emailing the content of the contact form to the owner.
    msg = EmailMessage()
    msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nMessage : "+str(message))
    msg['Subject'] = 'Some one visited your portfolio, and want to contact you'
    msg['From'] = sender_email
    msg['To'] = receiver_email
  
    try:
      server.send_message(msg)
    except:
      pass
    flash('Message sent successfully!')
    return render_template('contacted.html',title='Register')
  return render_template('contact.html',title='Register')




if __name__ == '__main__':
    app.run(debug=True)
