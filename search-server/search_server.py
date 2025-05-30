from flask import Flask, jsonify, request, send_from_directory
import os
import glob

# ✅ HTML 파일이 저장된 기본 폴더 경로
HTML_FOLDER = os.path.abspath(os.environ.get('HTML_FOLDER', 'html'))

# ✅ Flask 앱 정의
app = Flask(__name__, static_folder=HTML_FOLDER, static_url_path='')

@app.route('/')
def home():
    return send_from_directory(HTML_FOLDER, 'index.html')

# ✅ 검색 기능 (검색어가 포함된 HTML 파일 반환)
@app.route('/search', methods=['GET'])
def search_html_files():
    search_term = request.args.get('query', '')
    if not search_term:
        return jsonify({"error": "검색어를 입력하세요."}), 400

    html_files = glob.glob(os.path.join(HTML_FOLDER, '**', '*.html'), recursive=True)
    results = []

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_term in content:
                relative_path = os.path.relpath(file, HTML_FOLDER).replace("\\", "/")
                results.append({
                    "filename": os.path.basename(file),
                    "filepath": f"/{relative_path}"
                })

    return jsonify({"results": results})

# ✅ HTML 정적 파일 제공
@app.route('/<path:filename>')
def serve_html(filename):
    return send_from_directory(HTML_FOLDER, filename)

# ✅ 앱 실행 (PORT 환경변수 우선, 없으면 5000번 포트 사용)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

