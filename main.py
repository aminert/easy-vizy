from flask import Flask, request, render_template, jsonify


app = Flask(__name__)


def get_image_urls(ids):
    """function to map ids to image URLS"""
    return [f"http://127.0.0.1:8000/{id}" for id in ids]


@app.route('/', methods=['GET'])
def app_main():
    ids = request.args.get('asset_ids').split(',')
    image_urls = get_image_urls(ids)
    return render_template("index.html", image_urls=image_urls, info=ids)


@app.errorhandler(500)
def error_500(e):
    response = {"error": "internal server error"}
    return jsonify(response), 500


@app.errorhandler(404)
def error_404(e):
    response = {"error": "404 not found"}
    return jsonify(response), 404