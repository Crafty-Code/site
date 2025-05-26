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
  pip install openai python-dotenv tomli tomli_w
  ```

### Configuration

1. Create a `.env` file in the `site/.local/workflows` directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SEO_ASSISTANT_ID=your_assistant_id
   TRANSLATOR_ASSISTANT_ID=your_translator_id
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
- Preserves existing TOML front matter while adding SEO data
- Supports all markdown files in the content directory

### Notes

- The script requires an active OpenAI API key
- The script uses TOML format for front matter
- The script will preserve any existing front matter while adding SEO metadata
- Run the script after creating new blog posts to ensure proper SEO optimization

## Content Translator

The Content Translator is a Python script that automatically translates markdown content to different languages using an existing OpenAI agent. It maintains the original formatting and structure while providing accurate translations.

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- OpenAI Assistant ID for translation
- Required Python packages:
  ```bash
  pip install openai python-dotenv tomli tomli_w
  ```

### Configuration

1. Update your `.env` file in the `site/.local/workflows` directory to include:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SEO_ASSISTANT_ID=your_seo_assistant_id
   TRANSLATOR_ASSISTANT_ID=your_translator_assistant_id
   ```

### Usage

The script is located at `site/.local/workflows/Translator.py`. To use it:

```bash
python Translator.py path/to/your/markdown/file.md
```

The script will automatically translate the content to all supported languages in parallel.

### Supported Languages

- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Irish (ie)
- Portuguese (pt)
- Dutch (nl)
- Swedish (sv)
- Danish (da)
- Norwegian (no)
- Finnish (fi)

### Features

- Parallel translation to all supported languages
- Maintains source file structure across translations
- Preserves markdown formatting and code blocks
- Uses TOML for front matter
- Translates front matter fields including title, description, keywords, etc.
- Adds translation metadata to each file
- Creates language-specific directories automatically

### Notes

- Files must be in a content/{lang}/ directory structure
- Maximum of 6 parallel translations at once
- Technical terms and code blocks are preserved in their original form
- Translation metadata is added to track the source language and translation status

### Features

- Translates content while preserving markdown formatting
- Maintains the original structure of the document
- Adds translation metadata to the front matter
- Creates translated files in the appropriate language directory
- Preserves technical terms that shouldn't be translated

### Notes

- The script requires an active OpenAI API key and a configured translator assistant
- Translations are generated using your custom OpenAI assistant
- The script will create the necessary language directories if they don't exist
- Run the script after creating new content to ensure proper translation
