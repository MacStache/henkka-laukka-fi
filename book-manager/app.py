from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BOOKS_JSON_PATH = os.path.join(BASE_DIR, "data", "books.json")
BOOK_IMAGES_DIR = os.path.join(BASE_DIR, "static", "books")
REVIEWS_DIR = os.path.join(BASE_DIR, "content", "lyhkarit")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg")
BOOK_FIELDS = [
    "title",
    "firstName",
    "lastName",
    "image",
    "status",
    "startDate",
    "finishDate",
    "reviewUrl",
]


def _normalize_books(books):
    normalized = []
    for item in books:
        normalized.append({field: item.get(field) for field in BOOK_FIELDS})
    return normalized

@app.route('/')
def index():
    with open(BOOKS_JSON_PATH, 'r', encoding='utf-8') as f:
        books = json.load(f)
    return render_template('index.html', books=books)

@app.route('/api/books', methods=['GET'])
def get_books():
    with open(BOOKS_JSON_PATH, 'r', encoding='utf-8') as f:
        books = json.load(f)
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def save_books():
    incoming = request.json or []

    with open(BOOKS_JSON_PATH, 'r', encoding='utf-8') as f:
        current = json.load(f)

    if isinstance(incoming, list):
        if len(incoming) > len(current):
            new_count = len(incoming) - len(current)
            new_items = incoming[-new_count:]
            merged = new_items + incoming[:-new_count]
        else:
            merged = incoming
    else:
        merged = [incoming] + current

    merged = _normalize_books(merged)

    with open(BOOKS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    return jsonify({"success": True})

@app.route('/api/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    with open(BOOKS_JSON_PATH, 'r', encoding='utf-8') as f:
        books = json.load(f)
    books.pop(index)
    books = _normalize_books(books)
    with open(BOOKS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
    return jsonify({"success": True})


@app.route('/api/image-folders', methods=['GET'])
def list_image_folders():
    folders = []
    if os.path.isdir(BOOK_IMAGES_DIR):
        for name in sorted(os.listdir(BOOK_IMAGES_DIR)):
            path = os.path.join(BOOK_IMAGES_DIR, name)
            if os.path.isdir(path):
                folders.append(name)
    return jsonify(folders)


@app.route('/api/images', methods=['GET'])
def list_images():
    folder = (request.args.get('folder') or '').strip().strip('/')
    base_dir = BOOK_IMAGES_DIR
    base_url = "/books"

    if folder:
        candidate = os.path.abspath(os.path.join(BOOK_IMAGES_DIR, folder))
        root = os.path.abspath(BOOK_IMAGES_DIR)
        if os.path.commonpath([candidate, root]) != root:
            return jsonify([])
        base_dir = candidate
        base_url = f"/books/{folder}"

    images = []
    if os.path.isdir(base_dir):
        for name in sorted(os.listdir(base_dir)):
            path = os.path.join(base_dir, name)
            if os.path.isfile(path) and name.lower().endswith(IMAGE_EXTENSIONS):
                images.append(f"{base_url}/{name}")
    return jsonify(images)


@app.route('/api/reviews', methods=['GET'])
def list_reviews():
    reviews = []
    if os.path.isdir(REVIEWS_DIR):
        for name in sorted(os.listdir(REVIEWS_DIR)):
            path = os.path.join(REVIEWS_DIR, name)
            if os.path.isfile(path) and name.lower().endswith(".md"):
                slug = os.path.splitext(name)[0]
                reviews.append(f"/lyhkarit/{slug}/")
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
