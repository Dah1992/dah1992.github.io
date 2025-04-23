import os, json
from datetime import datetime

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '')

with open('_data/products.json') as f:
    products = json.load(f)

os.makedirs('_review_pool', exist_ok=True)

for prod in products:
    slug = slugify(prod['name'])
    fname = f"{slug}.md"
    date = datetime.now().strftime('%Y-%m-%d')
    content = f"""---
layout: post
title: "{prod['name']} Review"
date: {date}
categories: {prod['category']}
image: {prod['image']}
description: Auto-generated review of {prod['name']}.
---

![{prod['name']}]({prod['image']})

The **{prod['name']}** is a top smart home device.

### Buy Now
[Check Price](/go/{slug})
"""
    with open(os.path.join('_review_pool', fname), 'w') as f:
        f.write(content)
    print(f"Generated: {fname}")