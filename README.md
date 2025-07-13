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

## 🛠️ Available Commands

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
