from flask import *
import smtplib
import requests

# my_email = "greensolomon59@gmail.com"
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(my_email, password="ckag bmmb fhww dkwa")
# connection.sendmail(from_addr=my_email, to_addrs="bluebids86@gmail.com")


my_email = "greensolomon59@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(my_email, password="ckag bmmb fhww dkwa")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        message = data["message"]
        connection.sendmail(from_addr=my_email, to_addrs="bluebids86@gmail.com", msg=f"{message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/sent")
def send_email():
    return "<h1> Email sent successfully! </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
