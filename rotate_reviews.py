import os, shutil
from datetime import datetime

POOL = "_review_pool"
POSTS = "_posts"
os.makedirs(POOL, exist_ok=True)
os.makedirs(POSTS, exist_ok=True)

files = sorted([f for f in os.listdir(POOL) if f.endswith(".md")])
if not files:
    print("No reviews to post.")
    exit()
filename = files[0]
today = datetime.now().strftime("%Y-%m-%d")
newname = f"{today}-{filename}"
shutil.move(os.path.join(POOL, filename), os.path.join(POSTS, newname))
print(f"Posted review: {newname}")