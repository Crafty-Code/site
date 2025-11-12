# CraftyCode Theme Configuration Guide

This file contains all available theme configuration options for the CraftyCode Hugo theme. 
Copy the sections you want to customize to your `config/_default/params.toml` file.

## Complete Theme Configuration Example

```toml
# Basic site settings
date_format = "2 January 2006"
show_reading_time = true
showLanguageSwitcher = true

# Theme Configuration
[theme]
  # Dark mode settings
  enable_dark_mode = true
  default_mode = "auto"  # Options: "auto", "light", "dark"
  
  # Color scheme configuration
  [theme.colors]
    # Primary brand colors - affects gradients, buttons, and accents
    primary = "blue"      # Options: blue, green, purple, red, yellow, indigo, pink, teal, gray
    accent = "blue"       # Secondary color for highlights and CTAs
    
    # Header colors
    [theme.colors.header]
      light_bg = "gray-800"          # Header background in light mode
      dark_bg = "gray-900"           # Header background in dark mode
      light_text = "white"           # Main header text in light mode
      dark_text = "gray-100"         # Main header text in dark mode
      light_nav_text = "gray-200"    # Navigation text in light mode
      dark_nav_text = "gray-100"     # Navigation text in dark mode
      light_nav_hover = "blue-400"   # Navigation hover color in light mode
      dark_nav_hover = "blue-400"    # Navigation hover color in dark mode
      light_border = "gray-600"      # Header border in light mode
      dark_border = "gray-600"       # Header border in dark mode
    
    # Footer colors
    [theme.colors.footer]
      light_bg = "gray-800"              # Footer background in light mode
      dark_bg = "gray-900"               # Footer background in dark mode
      light_text = "gray-300"            # Footer text in light mode
      dark_text = "gray-300"             # Footer text in dark mode
      light_heading = "white"            # Footer headings in light mode
      dark_heading = "gray-100"          # Footer headings in dark mode
      light_border = "gray-600"          # Footer border in light mode
      dark_border = "gray-700"           # Footer border in dark mode
      light_link_hover = "blue-400"      # Footer link hover in light mode
      dark_link_hover = "blue-400"       # Footer link hover in dark mode
    
    # Content area colors
    [theme.colors.content]
      light_bg = "white"             # Main content background in light mode
      dark_bg = "gray-800"           # Main content background in dark mode
      light_text = "gray-900"        # Body text in light mode
      dark_text = "gray-100"         # Body text in dark mode
      light_heading = "gray-900"     # Headings in light mode
      dark_heading = "white"         # Headings in dark mode
      light_muted = "gray-600"       # Muted text in light mode
      dark_muted = "gray-400"        # Muted text in dark mode
    
    # Card and component colors
    [theme.colors.card]
      light_bg = "white"             # Card background in light mode
      dark_bg = "gray-900"           # Card background in dark mode
      light_border = "gray-200"      # Card borders in light mode
      dark_border = "gray-700"       # Card borders in dark mode
      light_shadow = "gray-100"      # Card shadows in light mode
      dark_shadow = "gray-900"       # Card shadows in dark mode
    
    # Button colors
    [theme.colors.button]
      primary_light_bg = "blue-600"      # Primary button background (light)
      primary_dark_bg = "blue-700"       # Primary button background (dark)
      primary_light_text = "white"       # Primary button text (light)
      primary_dark_text = "white"        # Primary button text (dark)
      primary_light_hover = "blue-700"   # Primary button hover (light)
      primary_dark_hover = "blue-600"    # Primary button hover (dark)
      
      secondary_light_bg = "gray-200"    # Secondary button background (light)
      secondary_dark_bg = "gray-700"     # Secondary button background (dark)
      secondary_light_text = "gray-900"  # Secondary button text (light)
      secondary_dark_text = "gray-100"   # Secondary button text (dark)
      secondary_light_hover = "gray-300" # Secondary button hover (light)
      secondary_dark_hover = "gray-600"  # Secondary button hover (dark)
    
    # Form colors
    [theme.colors.form]
      light_input_bg = "white"           # Input background in light mode
      dark_input_bg = "gray-800"         # Input background in dark mode
      light_input_border = "gray-300"    # Input border in light mode
      dark_input_border = "gray-600"     # Input border in dark mode
      light_input_focus = "blue-500"     # Input focus color in light mode
      dark_input_focus = "blue-400"      # Input focus color in dark mode
      light_input_text = "gray-900"      # Input text in light mode
      dark_input_text = "gray-100"       # Input text in dark mode
    
    # Syntax highlighting colors (for code blocks)
    [theme.colors.syntax]
      light_bg = "gray-50"               # Code block background in light mode
      dark_bg = "gray-900"               # Code block background in dark mode
      light_border = "gray-200"          # Code block border in light mode
      dark_border = "gray-700"           # Code block border in dark mode
```

## Pre-configured Color Schemes

### Blue Theme (Default)
```toml
[theme.colors]
  primary = "blue"
  accent = "blue"
```

### Green Theme
```toml
[theme.colors]
  primary = "green"
  accent = "emerald"
```

### Purple Theme
```toml
[theme.colors]
  primary = "purple"
  accent = "violet"
```

### Red Theme
```toml
[theme.colors]
  primary = "red"
  accent = "rose"
```

### Minimal Dark Theme
```toml
[theme]
  default_mode = "dark"
  
  [theme.colors]
    primary = "gray"
    accent = "blue"
    
    [theme.colors.header]
      light_bg = "black"
      dark_bg = "black"
    
    [theme.colors.footer]
      light_bg = "black"
      dark_bg = "black"
```

## Available Tailwind Colors

The theme supports all standard Tailwind CSS colors:
- `blue`, `indigo`, `purple`, `pink`
- `red`, `orange`, `yellow`, `green`
- `teal`, `cyan`, `sky`, `emerald`
- `lime`, `violet`, `fuchsia`, `rose`
- `gray`, `slate`, `zinc`, `neutral`, `stone`

## Usage Examples

### Using Theme Classes in Templates

```html
<!-- Header with theme colors -->
<header class="{{ partial "theme-classes.html" (dict "context" . "type" "header" "variant" "bg") }}">
  <h1 class="{{ partial "theme-classes.html" (dict "context" . "type" "header" "variant" "text") }}">
    {{ .Site.Title }}
  </h1>
</header>

<!-- Primary button -->
<button class="{{ partial "theme-classes.html" (dict "context" . "type" "button" "element" "primary") }}">
  Click me
</button>

<!-- Card with theme colors -->
<div class="{{ partial "theme-classes.html" (dict "context" . "type" "card" "variant" "bg") }} {{ partial "theme-classes.html" (dict "context" . "type" "card" "variant" "border") }} border rounded-lg p-4">
  <p class="{{ partial "theme-classes.html" (dict "context" . "type" "content" "variant" "text") }}">
    Card content
  </p>
</div>
```

## Migration from Hardcoded Colors

If you have custom templates with hardcoded colors, replace them as follows:

### Before (hardcoded):
```html
<div class="bg-gray-800 dark:bg-gray-900 text-white dark:text-gray-100">
```

### After (configurable):
```html
<div class="{{ partial "theme-classes.html" (dict "context" . "type" "header" "variant" "bg") }} {{ partial "theme-classes.html" (dict "context" . "type" "header" "variant" "text") }}">
```

## Best Practices

1. **Keep it consistent**: Use the same color family for related elements
2. **Test both modes**: Always verify your colors work in both light and dark mode
3. **Consider accessibility**: Ensure sufficient contrast between text and background colors
4. **Use semantic names**: The theme classes are named by purpose (header, content, etc.) rather than specific colors
5. **Gradual migration**: You can adopt the theme system gradually, template by template

## Custom CSS Integration

If you need custom CSS that respects the theme configuration, you can use the theme variables:

```css
.my-custom-element {
  background: var(--header-bg-light);
  color: var(--header-text-light);
}

.dark .my-custom-element {
  background: var(--header-bg-dark);
  color: var(--header-text-dark);
}
```

The theme variables are automatically generated from your configuration and available in CSS.
