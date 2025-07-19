# Crafty Theme Color Configuration Guide

This guide explains how to customize the colors in the Crafty Theme through the Hugo configuration files.

## Configuration Location

All theme colors are configured in `/config/_default/params.toml` under the `[theme.colors]` section.

## Available Color Options

### Primary Colors

```toml
[theme.colors]
primary = "blue"    # Primary brand color
accent = "blue"     # Accent color for highlights
```

**Available colors:** `blue`, `green`, `purple`, `red`, `yellow`, `indigo`, `pink`, `teal`

### Component-Specific Colors

Each component has separate light and dark mode configurations:

#### Header Colors
```toml
[theme.colors.header]
light_bg = "gray-800"           # Header background in light mode
dark_bg = "gray-900"            # Header background in dark mode
light_text = "white"            # Header text in light mode
dark_text = "gray-100"          # Header text in dark mode
light_nav_text = "gray-200"     # Navigation text in light mode
dark_nav_text = "gray-100"      # Navigation text in dark mode
light_nav_hover = "blue-400"    # Navigation hover color in light mode
dark_nav_hover = "blue-400"     # Navigation hover color in dark mode
light_border = "gray-600"       # Header border in light mode
dark_border = "gray-600"        # Header border in dark mode
```

#### Footer Colors
```toml
[theme.colors.footer]
light_bg = "gray-800"           # Footer background in light mode
dark_bg = "gray-900"            # Footer background in dark mode
light_text = "gray-300"         # Footer text in light mode
dark_text = "gray-300"          # Footer text in dark mode
light_heading = "white"         # Footer headings in light mode
dark_heading = "gray-100"       # Footer headings in dark mode
light_border = "gray-600"       # Footer border in light mode
dark_border = "gray-700"        # Footer border in dark mode
light_link_hover = "blue-400"   # Footer link hover in light mode
dark_link_hover = "blue-400"    # Footer link hover in dark mode
```

#### Content Area Colors
```toml
[theme.colors.content]
light_bg = "white"              # Main content background in light mode
dark_bg = "gray-800"            # Main content background in dark mode
light_text = "gray-900"         # Body text in light mode
dark_text = "gray-100"          # Body text in dark mode
light_heading = "gray-900"      # Heading text in light mode
dark_heading = "white"          # Heading text in dark mode
light_muted = "gray-600"        # Muted/secondary text in light mode
dark_muted = "gray-400"         # Muted/secondary text in dark mode
```

#### Card and Component Colors
```toml
[theme.colors.card]
light_bg = "white"              # Card background in light mode
dark_bg = "gray-900"            # Card background in dark mode
light_border = "gray-200"       # Card border in light mode
dark_border = "gray-700"        # Card border in dark mode
light_shadow = "gray-100"       # Card shadow in light mode
dark_shadow = "gray-900"        # Card shadow in dark mode
```

#### Button Colors
```toml
[theme.colors.button]
# Primary buttons
primary_light_bg = "blue-600"      # Primary button background in light mode
primary_dark_bg = "blue-700"       # Primary button background in dark mode
primary_light_text = "white"       # Primary button text in light mode
primary_dark_text = "white"        # Primary button text in dark mode
primary_light_hover = "blue-700"   # Primary button hover in light mode
primary_dark_hover = "blue-600"    # Primary button hover in dark mode

# Secondary buttons
secondary_light_bg = "gray-200"     # Secondary button background in light mode
secondary_dark_bg = "gray-700"      # Secondary button background in dark mode
secondary_light_text = "gray-900"   # Secondary button text in light mode
secondary_dark_text = "gray-100"    # Secondary button text in dark mode
secondary_light_hover = "gray-300"  # Secondary button hover in light mode
secondary_dark_hover = "gray-600"   # Secondary button hover in dark mode
```

#### Form Colors
```toml
[theme.colors.form]
light_input_bg = "white"           # Form input background in light mode
dark_input_bg = "gray-800"         # Form input background in dark mode
light_input_border = "gray-300"    # Form input border in light mode
dark_input_border = "gray-600"     # Form input border in dark mode
light_input_focus = "blue-500"     # Form input focus color in light mode
dark_input_focus = "blue-400"      # Form input focus color in dark mode
light_input_text = "gray-900"      # Form input text in light mode
dark_input_text = "gray-100"       # Form input text in dark mode
```

#### Syntax Highlighting Colors
```toml
[theme.colors.syntax]
light_bg = "gray-50"               # Code block background in light mode
dark_bg = "gray-900"               # Code block background in dark mode
light_border = "gray-200"          # Code block border in light mode
dark_border = "gray-700"           # Code block border in dark mode
```

## Color Values

All color values should use Tailwind CSS color names with numeric suffixes:

- **Gray scale:** `gray-50`, `gray-100`, `gray-200`, `gray-300`, `gray-400`, `gray-500`, `gray-600`, `gray-700`, `gray-800`, `gray-900`
- **Brand colors:** `blue-100`, `blue-200`, etc. up to `blue-900`
- **Other colors:** `green-xxx`, `purple-xxx`, `red-xxx`, `yellow-xxx`, `indigo-xxx`, `pink-xxx`, `teal-xxx`
- **Special values:** `white`, `black`

## How to Apply Changes

1. Edit `/config/_default/params.toml`
2. Modify the desired color values under `[theme.colors]`
3. Rebuild your site with `hugo server` or `hugo build`
4. The changes will be applied automatically through the theme's CSS custom properties system

## Example Custom Configuration

Here's an example of how to create a green-themed site:

```toml
[theme.colors]
primary = "green"
accent = "teal"

[theme.colors.header]
light_nav_hover = "green-400"
dark_nav_hover = "green-400"

[theme.colors.footer]
light_link_hover = "green-400"
dark_link_hover = "green-400"

[theme.colors.button]
primary_light_bg = "green-600"
primary_dark_bg = "green-700"
primary_light_hover = "green-700"
primary_dark_hover = "green-600"

[theme.colors.form]
light_input_focus = "green-500"
dark_input_focus = "green-400"
```

## Theme System Architecture

The theme uses a three-tier system:

1. **Configuration** (`params.toml`) - Define color values
2. **CSS Variables** (`theme-variables.html`) - Convert to CSS custom properties
3. **Theme Classes** (`theme-classes.html`) - Apply colors to components

This ensures consistent color usage across all components and easy customization through configuration files.
