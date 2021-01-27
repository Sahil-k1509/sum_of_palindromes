from flask import Flask, render_template, request, url_for
from algorithms.three_palindrome import find_palindromes
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == "POST":
        try:
            number = request.form.to_dict()['number']
            # print(number)
            p1, p2, p3, timetaken = find_palindromes(int(number), g=10, print_pal=False)
            # print(p1, p2, p3, timetaken)

            return {
                    "number1": p1,
                    "number2": p2,
                    "number3": p3
                };
        except Exception as e:
            print(e)
            return str(e), 400
            # return str(e), 400    
          
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(debug=True)