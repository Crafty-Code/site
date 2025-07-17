# Analytics Configuration Guide

The CraftyCode theme supports multiple analytics services with built-in privacy features. It's compatible with Hugo's native Google Analytics configuration and provides additional privacy controls.

## Google Analytics 4 (GA4)

### Option 1: Hugo's Native Configuration (Recommended)

Hugo has built-in Google Analytics support. This is the simplest method:

**In `config/production/hugo.toml`:**
```toml
[services]
  [services.googleAnalytics]
    id = 'G-XXXXXXXXXX'  # Replace with your actual GA4 ID
```

### Option 2: Theme Configuration (With Privacy Controls)

For additional privacy features, use the theme's analytics configuration:

**In `config/_default/params.toml`:**
```toml
[analytics]
  google_analytics_id = "G-XXXXXXXXXX"  # Replace with your actual ID
  respect_do_not_track = true
  anonymize_ip = true
```

### Automatic Detection

The theme automatically detects and uses:
1. Hugo's native GA configuration first
2. Falls back to theme configuration if needed
3. Applies privacy controls when using theme configuration

### Privacy Features (Theme Configuration Only)
- Automatic IP anonymization
- Do Not Track header respect
- GDPR-compliant consent handling
- Deferred loading for better performance

## Google Tag Manager (GTM)

### Setup
1. Create a GTM container at [Google Tag Manager](https://tagmanager.google.com)
2. Get your Container ID (format: `GTM-XXXXXXX`)
3. Add it to your configuration:

```toml
[analytics]
  google_tag_manager_id = "GTM-XXXXXXX"  # Replace with your actual ID
```

### Benefits
- Manage multiple tracking codes from one place
- Advanced event tracking
- A/B testing integration
- E-commerce tracking

## Plausible Analytics

### Setup
1. Sign up at [Plausible](https://plausible.io)
2. Add your domain
3. Configure in params.toml:

```toml
[analytics]
  plausible_domain = "yourdomain.com"
```

### Features
- Privacy-focused (no cookies)
- GDPR compliant by default
- Lightweight script
- No personal data collection

## Fathom Analytics

### Setup
1. Sign up at [Fathom Analytics](https://usefathom.com)
2. Get your Site ID
3. Add to configuration:

```toml
[analytics]
  fathom_site_id = "ABCDEFGH"  # Replace with your Site ID
```

### Features
- Cookie-free tracking
- GDPR compliant
- Real-time analytics
- Fast loading

## Privacy Settings

### Complete Privacy Configuration
```toml
[analytics]
  # Your analytics service IDs
  google_analytics_id = "G-XXXXXXXXXX"
  
  # Privacy settings
  respect_do_not_track = true     # Respect DNT header
  anonymize_ip = true             # Anonymize visitor IPs
  cookie_consent = true           # Show cookie consent banner
```

### Privacy Features
- **Do Not Track**: Respects browser DNT headers
- **IP Anonymization**: Anonymizes visitor IP addresses
- **Cookie Consent**: Optional consent banner
- **Deferred Loading**: Analytics load only after user interaction

## Cookie Consent Banner

Enable the built-in cookie consent banner:

```toml
[analytics]
  cookie_consent = true
```

### Features
- Theme-aware styling
- Persistent user choice
- Accept/Decline options
- Analytics control integration

## Multiple Analytics Services

You can use multiple services simultaneously:

```toml
[analytics]
  google_analytics_id = "G-XXXXXXXXXX"
  plausible_domain = "yourdomain.com"
  fathom_site_id = "ABCDEFGH"
  
  respect_do_not_track = true
  anonymize_ip = true
  cookie_consent = true
```

## Development vs Production

### Development Setup
```toml
# In config/_default/params.toml
[analytics]
  # Leave empty for development
  google_analytics_id = ""
```

### Production Setup
```toml
# In config/production/params.toml
[analytics]
  google_analytics_id = "G-XXXXXXXXXX"
  respect_do_not_track = true
  anonymize_ip = true
```

## Testing Analytics

### Verify Google Analytics
1. Install the [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) extension
2. Open your site with the extension enabled
3. Check the console for tracking events

### Verify Plausible
1. Visit your Plausible dashboard
2. Check real-time visitor count
3. Verify events are being tracked

### Verify Fathom
1. Open your Fathom dashboard
2. Check current visitors
3. Verify page views are being recorded

## GDPR Compliance

### Built-in GDPR Features
- IP anonymization
- Do Not Track respect
- Cookie consent management
- No personal data collection (with privacy-focused services)

### Legal Compliance
- Update your privacy policy
- Mention analytics usage
- Provide opt-out instructions
- Include cookie information

## Performance Optimization

### Features
- Deferred script loading
- Conditional loading based on DNT
- Minimal script size
- CDN-served scripts

### Best Practices
- Use only necessary analytics services
- Enable IP anonymization
- Respect user privacy preferences
- Regular privacy policy updates

## Troubleshooting

### Common Issues
1. **Analytics not working**: Check measurement ID format
2. **Console errors**: Verify script URLs and IDs
3. **No data**: Check site domain configuration
4. **DNT not respected**: Ensure `respect_do_not_track = true`

### Debug Mode
Enable debug mode for Google Analytics:
```toml
[analytics]
  google_analytics_id = "G-XXXXXXXXXX"
  debug_mode = true  # Add this for debugging
```

This comprehensive analytics system provides flexibility while maintaining user privacy and compliance with modern privacy regulations.
