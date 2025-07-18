from flask import Flask, render_template, request, jsonify
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def get_youtube_embed_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    )
    match = re.match(youtube_regex, url)
    return f"https://www.youtube.com/embed/{match.group(4)}" if match else None

@app.route('/', methods=['GET', 'POST'])
def index():
    embed_url = None
    youtube_url = None
    error = None
    
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        if youtube_url:
            embed_url = get_youtube_embed_url(youtube_url)
            if not embed_url:
                return jsonify({'error': 'Invalid YouTube URL. Please enter a valid YouTube video URL.'}), 400
            return jsonify({'embed_url': embed_url})
    
    return render_template('index.html', embed_url=embed_url, youtube_url=youtube_url, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
