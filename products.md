---
layout: page
title: All Products
permalink: /products/
---

# Our Smart Home Picks

<ul class="product-grid">
  {% for p in site.data.products %}
    <li>
      <img src="{{ p.image }}" alt="{{ p.name }}" />
      <h2>{{ p.name }}</h2>
      <a class="btn" href="https://www.amazon.com/dp/{{ p.asin }}?tag=youraffiliatetag" target="_blank">
        Buy on Amazon
      </a>
    </li>
  {% endfor %}
</ul>