from flask import Flask, render_template, request
import re

app = Flask(__name__)

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
                error = "Invalid YouTube URL. Please enter a valid YouTube video URL."
            else:
                # Ghi chú: Không thể kiểm tra khả năng nhúng mà không dùng API.
                # Nếu nhúng thất bại (do cấm nhúng), iframe sẽ hiển thị lỗi tự động.
                # Chúng ta vẫn cung cấp liên kết YouTube như phương án dự phòng.
                pass
    
    return render_template('index.html', embed_url=embed_url, youtube_url=youtube_url, error=error)

if __name__ == '__main__':
    #app.run(debug=True, host='localhost', port=5000)
    app.run(debug=True, host='0.0.0.0', port=3000) # dòng này để phù hợp trên replit


