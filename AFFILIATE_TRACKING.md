# Affiliate Click Tracking

To track clicks via Google Analytics, add this snippet to each redirect page (before the refresh meta):

```html
<script>
  gtag('event', 'click', {
    'event_category': 'affiliate',
    'event_label': '{{ page.url }}'
  });
</script>
<meta http-equiv="refresh" content="0; url=https://www.amazon.com/dp/ASIN?tag=youraffiliatetag">
```