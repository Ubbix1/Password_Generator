from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    password_length = int(request.form['password_length'])
    password = generate_password(password_length)
    user_ip = request.remote_addr

    # Store password and user IP in a text file
    with open('passwords.txt', 'a') as file:
        file.write(f'Password: {password}\tIP Address: {user_ip}\n')

    return render_template('index.html', password=password)


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == '__main__':
    app.run(debug=True)
