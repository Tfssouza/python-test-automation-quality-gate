import json
from pathlib import Path


def load_posts_test_data():
    path = Path("data/posts.json")
    return json.loads(path.read_text(encoding="utf-8"))