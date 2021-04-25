from flask import Flask, render_template, redirect, url_for, flash, abort, request, send_from_directory
import os
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = "3*##$!d2dsfhx_sdadas55:da/f&&1;;'&"



@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/rreth-nesh')
def about():
    return render_template("about.html")

@app.route('/sherbimet-tona')
def sherbime():
    return render_template("sherbime.html")

@app.route("/contact", methods=['POST','GET'])
def kontakt():
    if request.method=='POST':
        data=request.form
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login("glenlohja1@yahoo.com", "lozybvymlfezdgce")
            connection.sendmail(
                from_addr="glenlohja1@yahoo.com",
                to_addrs="info@upt-support.com",
                msg=f"Subject:Message from {data['subject'].title()}\n\nName: {data['name']}\nEmail: {data['email']}"
                f"\nMessage: {data['message']}"
            )
        return render_template("contact.html", message='yes')    
    return render_template("contact.html",message='no')



# @app.route('/detyra-kursi/<lenda>')
# def detyra(lenda):
#     return render_template("detyrakursi.html",lenda=lenda)


# @app.route('/sitemap.xml')
# def static_from_root():
#     return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run(debug=True)