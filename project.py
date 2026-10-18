from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

# Unga special date-ai inga change pannikko
special_date = "14-06-2022"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/letter", methods=["GET", "POST"])
def letter():

    if request.method == "POST":

        date = request.form["date"]

        if date == special_date:
            return redirect(url_for("memories"))

        else:
            return render_template(
                "letter.html",
                message="Wrong date! Try again, my love ❤️"
            )

    return render_template("letter.html", message="")


@app.route("/memories")
def memories():
    return render_template("memories.html")


@app.route("/surprise")
def surprise():
    return render_template("surprise.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)









