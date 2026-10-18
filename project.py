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
        date = request.form.get("date")

        if date == special_date:
            return redirect(url_for("success"))
        else:
            return redirect(url_for("wrong"))
    return render_template("letter.html")

@app.route("/success")
def success():
    return render_template("sucess.html")


# Wrong date page
@app.route("/wrong")
def wrong():
    return render_template("wrong.html")


@app.route("/memories")
def memories():
    return render_template("memories.html")


@app.route("/surprise")
def surprise():
    return render_template("surprise.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)









