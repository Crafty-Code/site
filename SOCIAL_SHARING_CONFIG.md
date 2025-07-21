# Social Sharing Configuration

The CraftyTheme now includes a comprehensive social sharing system that allows users to easily share content on various platforms. This system is fully configurable and can be customized per content type.

## Features

- **Multiple Platforms**: Support for Twitter, LinkedIn, Facebook, Reddit, Pinterest, WhatsApp, Telegram, Email, and copy-to-clipboard
- **Content Type Specific**: Different sharing configurations for blog posts, book reviews, and pages
- **Proper URL Encoding**: All URLs and text are properly encoded for external platforms
- **Customizable Messages**: Configure custom prefixes for different platforms
- **Responsive Design**: Mobile-friendly sharing buttons with consistent theming
- **Accessibility**: Proper ARIA labels and keyboard navigation support

## Configuration

### Basic Setup

Add the following configuration to your `config/_default/params.toml`:

```toml
# Social Sharing Configuration
[sharing]
  # Enable sharing for different content types
  enable_blog_sharing = true
  enable_book_sharing = true
  enable_page_sharing = false  # For other page types
  
  # Available sharing platforms
  [sharing.platforms]
    twitter = true
    linkedin = true
    facebook = true
    reddit = true
    pinterest = false
    whatsapp = false
    telegram = false
    email = true
    copy_link = true
    
  # Custom sharing messages
  [sharing.messages]
    twitter_prefix = "Check out this article:"  # Text added before the title on Twitter
    email_subject_prefix = "Interesting read:"  # Email subject prefix
    
  # Sharing section customization
  [sharing.display]
    show_section_title = true
    blog_section_title = "Share this article"
    book_section_title = "Share this book review"
    page_section_title = "Share this page"
```

### Platform-Specific Features

#### Twitter
- Includes custom prefix text before the title
- Properly encodes URLs and text
- Opens in a new window with proper targeting

#### LinkedIn
- Uses LinkedIn's official sharing API
- Automatically includes the page URL

#### Facebook
- Uses Facebook's Sharer API
- Includes the page URL for proper preview generation

#### Reddit
- Includes both URL and title
- Opens Reddit's submit page

#### Pinterest
- Automatically includes the page's featured image if available
- Includes description text for better context

#### WhatsApp & Telegram
- Combines title and URL in the message
- Mobile-optimized sharing

#### Email
- Includes subject line with custom prefix
- Body includes title, description, and URL
- Uses proper email encoding

#### Copy Link
- Modern clipboard API with fallback for older browsers
- Visual feedback when copying is successful
- Works in both secure (HTTPS) and non-secure contexts

## Usage

### In Templates

The sharing partial is automatically included in blog and book single page templates. To add it to other templates:

```hugo
{{ partial "social-sharing.html" (dict "context" . "type" "page") }}
```

### Parameters

- `context`: The page context (always use `.`)
- `type`: Content type for customization (`blog`, `book`, or `page`)

### Customization

#### Disable Sharing for Specific Pages

Add to your page's front matter:

```yaml
---
disable_sharing: true
---
```

Then modify your template to check this parameter:

```hugo
{{ if not .Params.disable_sharing }}
  {{ partial "social-sharing.html" (dict "context" . "type" "blog") }}
{{ end }}
```

#### Custom Sharing Messages

You can customize the sharing messages per content type by modifying the `[sharing.messages]` section in your params.

#### Platform Selection

Enable or disable specific platforms by setting their values to `true` or `false` in the `[sharing.platforms]` section.

## Styling

The sharing buttons use the theme's color system and are fully responsive. They automatically adapt to light and dark modes.

### Button Colors

- **Twitter**: Blue (`bg-blue-500`)
- **LinkedIn**: Dark Blue (`bg-blue-700`)
- **Facebook**: Blue (`bg-blue-600`)
- **Reddit**: Orange (`bg-orange-600`)
- **Pinterest**: Red (`bg-red-600`)
- **WhatsApp**: Green (`bg-green-600`)
- **Telegram**: Blue (`bg-blue-500`)
- **Email/Copy**: Gray (`bg-gray-600`)

### Responsive Behavior

- Buttons stack vertically on mobile devices
- Flex layout with proper spacing
- Touch-friendly button sizes

## SEO Benefits

The sharing system includes several SEO-friendly features:

1. **Proper URL Structure**: All shared URLs are absolute and properly formatted
2. **Meta Description**: Uses the page's description or summary for better social previews
3. **Image Sharing**: Pinterest automatically includes featured images
4. **Structured Sharing**: Each platform receives optimized content for their specific format

## Accessibility

- All sharing links include proper `title` attributes
- Keyboard navigation is fully supported
- Screen reader friendly with semantic HTML
- Color contrast meets WCAG guidelines

## Browser Compatibility

- **Modern Browsers**: Full clipboard API support
- **Older Browsers**: Fallback clipboard functionality
- **Mobile**: Optimized for touch interfaces
- **JavaScript Disabled**: Links still work for external platforms

## Performance

- Minimal JavaScript footprint
- CSS uses existing theme classes
- No external dependencies
- Lazy-loaded functionality

## Future Enhancements

The analytics system is already implemented! Here's what you get:

1. **Analytics Integration**: ✅ **COMPLETED** - Track sharing events across multiple platforms
2. **Share Performance Metrics**: ✅ **COMPLETED** - Monitor which platforms and content perform best
3. **Custom Platform Support**: Add more niche platforms
4. **Share Count Display**: Show share counts when available  
5. **Inline Sharing**: Add floating share buttons
6. **Advanced Customization**: Per-page platform selection

## Analytics Features

The sharing system now includes comprehensive analytics tracking:

### Supported Platforms
- **Google Analytics 4**: Custom events with detailed parameters
- **Google Tag Manager**: Data layer events for flexible tracking (advanced option)

### What Gets Tracked
- **Platform Used**: Which sharing button was clicked
- **Content Type**: Whether it's a blog post, book review, or page
- **Content Details**: Title and URL of shared content
- **Timing**: When shares happen for pattern analysis

### Quick Setup
Enable Google Analytics tracking in your `params.toml`:

```toml
[sharing.analytics]
  enable_tracking = true
  track_google_analytics = true
  track_gtm = false                 # Set to true if using Google Tag Manager
```

For complete analytics setup instructions, see `SOCIAL_SHARING_ANALYTICS.md`.
