from flask import Flask, request, redirect, render_template_string, abort
import string
import random

app = Flask(__name__)

# In-memory storage for URL mappings
url_store = {}

# HTML template for the main page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
</head>
<body>
    <h1>URL Shortener</h1>
    <form method="POST" action="/shorten">
        <label for="url">Enter URL to shorten:</label><br>
        <input type="url" id="url" name="url" required style="width: 300px;"><br><br>
        <input type="submit" value="Shorten">
    </form>
    {% if short_url %}
    <p>Your shortened URL: <a href="{{ short_url }}" target="_blank">{{ short_url }}</a></p>
    {% endif %}
</body>
</html>
"""

def generate_short_code(length=6):
    """Generate a random short code."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            # Generate unique short code
            short_code = generate_short_code()
            while short_code in url_store:
                short_code = generate_short_code()
            url_store[short_code] = original_url
            short_url = f"http://localhost:4567/{short_code}"
    return render_template_string(HTML_TEMPLATE, short_url=short_url)

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    if not original_url:
        return redirect('/')
    # Generate unique short code
    short_code = generate_short_code()
    while short_code in url_store:
        short_code = generate_short_code()
    url_store[short_code] = original_url
    short_url = f"http://localhost:4567/{short_code}"
    return render_template_string(HTML_TEMPLATE, short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in url_store:
        return redirect(url_store[short_code])
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='localhost', port=4567, debug=True)