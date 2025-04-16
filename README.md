# CraftyCode Website

This repository contains the website for CraftyCode, built with Hugo. The site is available at [https://craftycode.org/](https://craftycode.org/).

## SEO Generator

The SEO Generator is a Python script that automatically generates SEO metadata for markdown blog posts using OpenAI's GPT-4. It analyzes your content and adds optimized metadata including titles, descriptions, and social media cards.

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- OpenAI Assistant ID for SEO generation
- Required Python packages:
  ```bash
  pip install openai python-dotenv pyyaml
  ```

### Configuration

1. Create a `.env` file in the `site/.local/workflows` directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SEO_ASSISTANT_ID=your_assistant_id
   ```

### Usage

The script is located at `site/.local/workflows/SeoGenerator.py`. To use it:

```bash
python SeoGenerator.py path/to/your/markdown/file.md
```

For example, to generate SEO metadata for the time management blog post:

```bash
python SeoGenerator.py content/en/blog/time_management.md
```

### Features

- Automatically generates SEO-optimized titles and descriptions
- Adds Open Graph metadata for better social media sharing
- Includes Twitter card metadata
- Preserves existing front matter while adding SEO data
- Supports all markdown files in the content directory

### Notes

- The script requires an active OpenAI API key
- Make sure your OpenAI Assistant is configured to return YAML-compatible JSON
- The script will preserve any existing front matter while adding SEO metadata
- Run the script after creating new blog posts to ensure proper SEO optimization
