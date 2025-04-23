import os
from datetime import datetime

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '')

def generate_review(name, asin, image_url, category, tag='youraffiliatetag'):
    slug = slugify(name)
    fname = f"{slug}.md"
    date = datetime.now().strftime('%Y-%m-%d')
    content = f"""---
layout: post
title: "{name} Review"
date: {date}
categories: {category}
image: {image_url}
description: Auto-generated review of {name}.
---

![{name}]({image_url})

The **{name}** offers...
### Buy Now
[Check Price](/go/{slug})

"""
    os.makedirs('_review_pool', exist_ok=True)
    with open(os.path.join('_review_pool', fname), 'w') as f:
        f.write(content)
    print(f"Generated: {fname}")