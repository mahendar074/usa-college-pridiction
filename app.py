from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import random
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

data = pd.read_csv("Admission_Predict_Ver1.1.csv")

x = data[['CGPA', 'GRE Score', 'TOEFL Score']]
y = data[['Chance of Admit']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.20)
linreg = LinearRegression()
linreg.fit(x_train, y_train)



email_sender='YOUR MAIL @gmail.com'
email_password='# Replace with your actual app password'






def send_email(receiver_email, name, chance_of_admit, top_colleges):
    body = "Top 5 Colleges:\n"
    for index, college in top_colleges.iterrows():
        body += f"{college['University']} - {college['Location']}\n"
    email_rev = receiver_email

    sub = f"Hey {name}, You have a predicted chance of admission of {chance_of_admit:.2f}%."

    sub = sub.replace('\n', '')

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_rev
    em['Subject'] = sub
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_rev, em.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


    



@app.route('/')
def index():
    return render_template('form.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        name = request.form['name']
        gre_score = int(request.form['gre_score'])
        toefl_score = int(request.form['toefl_score'])
        user_data = [[random.uniform(6, 10), gre_score, toefl_score]]
        chance_of_admit = linreg.predict(user_data)[0]

        scaled_chance_of_admit = (((gre_score / 340) * 100) + ((toefl_score / 120) * 100)) / 2

        colleges = data.sample(5)[['University', 'Location']]

        # Send email to user
        send_email(request.form['email'], name, scaled_chance_of_admit, colleges)

        return render_template('result.html', name=name, chance_of_admit=scaled_chance_of_admit, top_colleges=colleges)
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
