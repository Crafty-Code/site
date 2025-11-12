# Images Directory

This directory contains images used throughout the CraftyCode site.

## Structure

- `books/` - Book cover images for book reviews
- `blog/` - Featured images for blog posts
- `logo.png` - Site logo
- `title.png` - Site title image

## Adding Images

### Book Covers

Place book cover images in `books/` directory. Reference them in your book review front matter:

```toml
image = "/images/books/your-book-cover.jpg"
```

### Blog Post Images

Place featured images in `blog/` directory. Reference them in your blog post front matter:

```toml
image = "/images/blog/your-featured-image.jpg"
```

## Image Guidelines

- **Format**: Use JPG for photos, PNG for graphics with transparency, WebP for modern browsers
- **Size**: Optimize images before uploading (recommended max width: 1200px)
- **Naming**: Use descriptive, lowercase names with hyphens (e.g., `clean-code-cover.jpg`)
- **Alt text**: Always provide meaningful alt text in your content

## Missing Images

If images are missing:

1. Check the file path matches the front matter reference
2. Ensure images are in the correct subdirectory
3. Verify file extensions match (case-sensitive on some systems)
4. Clear Hugo cache and rebuild: `hugo --gc`
