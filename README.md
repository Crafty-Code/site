# CraftyCode Website

This repository contains the website for CraftyCode, built with Hugo and styled with Tailwind CSS. The site is available at [https://craftycode.org/](https://craftycode.org/).

## 🚀 Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.140.0 or higher)
- [Git](https://git-scm.com/downloads)
- [Node.js](https://nodejs.org/) (optional, for advanced features)

### Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/craftycode-site.git
   cd craftycode-site
   ```

2. **Start development server:**

   ```bash
   make dev
   ```

   This starts both Tailwind CSS watching and Hugo server with live reload.

3. **Alternative development commands:**

   ```bash
   # Using Make
   make css-watch  # Watch for CSS changes
   make server     # Start Hugo server only
   
   # Using npm (if you have Node.js)
   npm run dev     # Start development mode
   npm run start   # Start Hugo server only
   ```

4. **Open your browser:** <http://localhost:1313>

### Building for Production

```bash
# Build everything for production
make build

# Or step by step
make css-build  # Build Tailwind CSS
hugo --gc --minify  # Build Hugo site
```

## 🎨 Styling with Tailwind CSS

This site uses Tailwind CSS v4 for styling. The build process is fully automated:

### During Development

- Tailwind CSS automatically rebuilds when you modify templates
- Changes are reflected instantly with Hugo's live reload

### During Deployment

- GitHub Actions automatically builds Tailwind CSS
- CSS is minified for production

### Manual CSS Building

```bash
# Build CSS once
make css-build

# Watch for changes
make css-watch

# Using the standalone CLI directly
./tailwindcss-linux-x64 -i ./themes/craftytheme/assets/css/main.css -o ./themes/craftytheme/static/css/main.css --minify
```

## 📁 Project Structure

```text
├── archetypes/          # Content templates
├── assets/              # Raw assets (images, css source)
├── config/              # Hugo configuration
├── content/             # Markdown content files
├── layouts/             # Hugo layout templates
├── static/              # Static files
├── themes/craftytheme/  # Custom Hugo theme
│   ├── assets/css/      # Tailwind CSS source
│   ├── layouts/         # Theme templates
│   └── static/css/      # Generated CSS output
├── .github/workflows/   # GitHub Actions
├── tailwindcss-linux-x64 # Tailwind CSS CLI binary
├── tailwind.config.js   # Tailwind configuration
├── Makefile            # Build commands
└── package.json        # npm scripts
```

## � Content Creation

### Content Types

This site supports multiple content types with specific layouts and features:

#### Blog Posts (`type: "blog"`)

Blog posts are ideal for tutorials, articles, and technical content. They support rich metadata and interactive features.

**Required Parameters:**

```toml
+++
title = "Your Blog Post Title"
description = "Brief description for SEO and social media"
date = 2024-01-15T10:00:00Z
author = "Author Name"
type = "blog"
+++
```

**Optional Parameters:**

```toml
# Content Organization
category = "Programming"           # Main category
tags = ["javascript", "tutorial"] # Array of tags
keywords = ["keyword1", "keyword2"] # SEO keywords

# Content Metadata  
difficulty = "beginner"            # beginner, intermediate, advanced
reading_time = 8                   # Override calculated reading time (minutes)
toc = true                        # Enable table of contents
draft = false                     # Set to true for drafts

# SEO & Social Media
image = "/images/blog/post-image.jpg"  # Featured image
summary = "Custom excerpt text"        # Override auto-generated summary

# Interactive Features
comments = true                    # Enable comments (if supported)
share = true                      # Enable social sharing buttons

# Technical Content
code_lang = "javascript"          # Default code block language
github_repo = "username/repo"     # Related GitHub repository
demo_url = "https://demo.com"     # Live demo URL

# Author Override (if different from site author)
author_bio = "Custom author bio"
author_image = "/images/authors/author.jpg"
author_social = { twitter = "handle", github = "username" }
```

**Example Blog Post Front Matter:**

```toml
+++
title = "Building Modern Web Apps with React and TypeScript"
description = "Learn how to create scalable web applications using React with TypeScript, including best practices and real-world examples."
date = 2024-07-15T09:00:00Z
author = "Jeff"
category = "Web Development"
tags = ["react", "typescript", "javascript", "frontend"]
keywords = ["React TypeScript", "web development", "frontend framework"]
difficulty = "intermediate"
toc = true
image = "/images/blog/react-typescript.jpg"
github_repo = "craftycoder/react-typescript-example"
demo_url = "https://react-ts-demo.netlify.app"
type = "blog"
draft = false
+++
```

#### Book Reviews (`type: "books"`)

Book reviews showcase detailed analysis of technical and business books with rich metadata and purchase integration.

**Required Parameters:**

```toml
+++
title = "Book Title: Subtitle"
author = "Reviewer Name"          # Your name as reviewer
book_author = "Original Author"   # Book's actual author
date = 2024-01-15T10:00:00Z
type = "books"
rating = 5                        # 1-5 star rating
+++
```

**Optional Parameters:**

```toml
# Book Metadata
description = "Comprehensive review description for SEO"
pages = 464                       # Number of pages
publisher = "Publisher Name"      # Publishing house
isbn = "978-0132350884"          # ISBN number
price = "$29.99"                 # Current price

# Content Organization
tags = ["programming", "clean-code"] # Topical tags
keywords = ["keyword1", "keyword2"]  # SEO keywords

# Visual & Purchase
image = "/images/books/book-cover.jpg"     # Book cover image
affiliate_link = "https://amazon.com/dp/123" # Purchase link
purchase_links = [                         # Multiple purchase options
  { name = "Amazon", url = "https://amazon.com/..." },
  { name = "Barnes & Noble", url = "https://bn.com/..." }
]

# Review Metadata
review_date = 2024-01-15T10:00:00Z  # When you read it (vs publish date)
difficulty_level = "intermediate"    # Book's difficulty level
target_audience = "developers"       # Who should read this
reading_time_book = "8 hours"       # Estimated time to read book

# Additional Context
series = "Clean Code Series"         # If part of a series
edition = "2nd Edition"             # Book edition
language = "English"                # Book language
subjects = ["Software Engineering", "Best Practices"] # Academic subjects

# Personal Notes
personal_rating = 4.5               # Different from public rating
would_recommend = true              # Boolean recommendation
read_count = 2                      # How many times you've read it
```

**Example Book Review Front Matter:**

```toml
+++
title = "Clean Code: A Handbook of Agile Software Craftsmanship"
author = "CraftyCode Team"
book_author = "Robert C. Martin"
date = 2024-01-15T10:00:00Z
description = "A comprehensive review of Robert Martin's influential book on writing clean, maintainable code that every developer should read"
rating = 5
pages = 464
publisher = "Prentice Hall"
isbn = "978-0132350884"
price = "$29.99"
tags = ["programming", "clean-code", "software-development"]
keywords = ["clean code", "software craftsmanship", "programming best practices"]
image = "/images/books/clean-code-cover.jpg"
affiliate_link = "https://amazon.com/dp/0132350884"
difficulty_level = "intermediate"
target_audience = "developers"
type = "books"
+++
```

### Content Creation Tips

1. **Use descriptive titles**: Make them SEO-friendly and compelling
2. **Write good descriptions**: These appear in search results and social media
3. **Tag appropriately**: Use 3-5 relevant tags for discoverability  
4. **Include images**: Featured images improve social media sharing
5. **Set difficulty levels**: Help readers choose appropriate content
6. **Enable TOC for long posts**: Improves navigation and user experience

### Content File Organization

```text
content/
├── en/
│   ├── blog/
│   │   ├── post-title.md
│   │   └── category/
│   │       └── specialized-post.md
│   └── books/
│       ├── book-review-title.md
│       └── categories/
│           └── programming/
│               └── specific-book.md
├── es/
│   ├── blog/
│   └── books/
└── [other-languages]/
```

## �🛠️ Available Commands

Run `make help` to see all available commands:

```bash
make help          # Show help
make dev           # Start development mode
make build         # Build for production
make css-build     # Build Tailwind CSS
make css-watch     # Watch CSS changes
make server        # Start Hugo server
make clean         # Clean build artifacts
make install-deps  # Install Tailwind CSS CLI
```

## 🤖 Content Automation Tools

## 🤖 Content Automation Tools

### SEO Generator

The SEO Generator automatically generates SEO metadata for markdown blog posts using OpenAI's GPT-4.

#### Setup Requirements

- Python 3.8 or higher
- OpenAI API key and Assistant ID
- Required packages:

  ```bash
  pip install openai python-dotenv tomli tomli_w
  ```

#### Configuration

Create a `.env` file in `site/.local/workflows` directory:

```env
OPENAI_API_KEY=your_openai_api_key
SEO_ASSISTANT_ID=your_assistant_id
TRANSLATOR_ASSISTANT_ID=your_translator_id
```

#### Using the SEO Generator

```bash
python .local/workflows/SeoGenerator.py content/en/blog/your-post.md
```

**What it does:**

- Generates SEO-optimized titles and descriptions
- Adds Open Graph metadata for social media
- Includes Twitter card metadata
- Preserves existing TOML front matter

### Content Translator

Automatically translates markdown content to multiple languages while preserving formatting.

#### Using the Translator

```bash
python .local/workflows/Translator.py content/en/blog/your-post.md
```

**Supported Languages:**

Spanish, French, German, Italian, Irish, Portuguese, Dutch, Swedish, Danish, Norwegian, Finnish

**Translation Features:**

- Parallel translation to all supported languages
- Maintains markdown formatting and code blocks
- Preserves technical terms
- Creates language-specific directories automatically
- Adds translation metadata

#### Automation Notes

- Both tools require active OpenAI API keys
- Scripts use TOML format for front matter
- Run after creating new content for SEO and translation
- Files are created in appropriate language directories
