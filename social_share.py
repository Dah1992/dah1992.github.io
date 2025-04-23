import os
import sys
from urllib.parse import urljoin
import requests

def get_post_url(filename):
    slug = filename.split('-', 1)[-1].replace('.md', '')
    return urljoin(os.getenv('SITE_URL', 'https://dah1992.github.io'), slug + '/')

def post_twitter(filename, token):
    url = get_post_url(filename)
    text = f"New review live: {url} #SmartHome"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"text": text}
    r = requests.post("https://api.twitter.com/2/tweets", json=payload, headers=headers)
    print("Twitter response:", r.status_code, r.text)

def post_linkedin(filename, token):
    url = get_post_url(filename)
    text = f"Check out our latest smart home review: {url}"
    headers = {"Authorization": f"Bearer {token}", "X-Restli-Protocol-Version": "2.0.0", "Content-Type": "application/json"}
    payload = {
        "author": "urn:li:person:YOUR_PERSON_URN",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    r = requests.post("https://api.linkedin.com/v2/ugcPosts", json=payload, headers=headers)
    print("LinkedIn response:", r.status_code, r.text)

if __name__ == "__main__":
    platform = sys.argv[1]
    filename = sys.argv[2]
    token = sys.argv[3]
    if platform == "twitter":
        post_twitter(filename, token)
    elif platform == "linkedin":
        post_linkedin(filename, token)
    else:
        print("Unsupported platform")