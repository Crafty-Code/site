# Social Sharing Analytics Guide

The CraftyTheme social sharing system now includes comprehensive analytics tracking to help you understand how your content is being shared and which platforms perform best.

## Primary Analytics Platform

### Google Analytics 4 (GA4) - Recommended
Google Analytics 4 is the primary analytics platform supported by this theme, providing comprehensive social sharing insights:

- **Event Name**: `share` (configurable)
- **Event Category**: `Social Sharing`
- **Event Label**: Platform name (linkedin, reddit, whatsapp, etc.)
- **Custom Parameters**: content_type, content_title, content_url, platform
- **Built-in Reports**: Comprehensive event reporting and custom dimensions
- **Real-time Data**: See shares as they happen
- **Audience Insights**: Understand who shares your content
- **Goal Tracking**: Set up conversion goals based on sharing behavior

### Google Tag Manager (GTM) - Advanced Option
For advanced users who want more control over tracking:

- **Event Name**: `social_share` (configurable)
- **Data Layer Variables**: social_platform, content_type, content_title, content_url, share_value
- **Custom Triggers**: Set up complex tracking scenarios
- **Multiple Platforms**: Forward data to multiple analytics services
- **A/B Testing**: Easy integration with testing platforms

## Alternative Analytics Platforms

*For advanced users who want additional tracking capabilities:*

### Google Tag Manager (GTM) - Advanced Option
For advanced users who want more control over tracking:

- **Event Name**: `social_share` (configurable)
- **Data Layer Variables**: social_platform, content_type, content_title, content_url, share_value
- **Custom Triggers**: Set up complex tracking scenarios
- **Multiple Platforms**: Forward data to multiple analytics services
- **A/B Testing**: Easy integration with testing platforms

*Note: Other privacy-focused analytics platforms like Plausible and Fathom can be added through custom implementation if needed.*

## Quick Setup (Google Analytics Only)

For most users, you only need Google Analytics tracking. Add this to your `config/_default/params.toml`:

```toml
[sharing.analytics]
  enable_tracking = true
  track_google_analytics = true     # Track share events in Google Analytics
  track_gtm = false                 # Set to true if you use Google Tag Manager
  track_plausible = false           # Set to true if you use Plausible
  track_fathom = false              # Set to true if you use Fathom
  
  # Event configuration (defaults work for most cases)
  [sharing.analytics.event_names]
    google_analytics = "share"      # GA4 event name
    
  # Data to include in tracking (all recommended)
  [sharing.analytics.properties]
    include_content_type = true     # Include blog/book/page in tracking
    include_content_title = true    # Include page title in tracking
    include_content_url = true      # Include page URL in tracking
    include_platform = true         # Include sharing platform in tracking
```

## Full Configuration (All Platforms)

*Only needed if you want to use multiple analytics platforms:*

```toml
[sharing.analytics]
  enable_tracking = true
  track_google_analytics = true     # Track share events in Google Analytics
  track_gtm = true                 # Track share events in Google Tag Manager
  track_plausible = true           # Track share events in Plausible Analytics
  track_fathom = true              # Track share events in Fathom Analytics
  
  # Custom event names for different analytics platforms
  [sharing.analytics.event_names]
    google_analytics = "share"      # GA4 event name
    gtm = "social_share"           # GTM event name
    plausible = "Share"            # Plausible event name
    fathom = "social-share"        # Fathom goal ID prefix
    
  # Additional tracking data
  [sharing.analytics.properties]
    include_content_type = true     # Include blog/book/page in tracking
    include_content_title = true    # Include page title in tracking
    include_content_url = true      # Include page URL in tracking
    include_platform = true         # Include sharing platform in tracking
```

## Analytics Data Structure

### Google Analytics 4 Events
```javascript
gtag('event', 'share', {
  'event_category': 'Social Sharing',
  'event_label': 'twitter',
  'content_type': 'blog',
  'content_title': 'How to Build Amazing Web Apps',
  'content_url': 'https://yoursite.com/blog/amazing-web-apps',
  'platform': 'twitter',
  'value': 1
});
```

### Google Tag Manager Data Layer
```javascript
dataLayer.push({
  'event': 'social_share',
  'social_platform': 'twitter',
  'content_type': 'blog',
  'content_title': 'How to Build Amazing Web Apps',
  'content_url': 'https://yoursite.com/blog/amazing-web-apps',
  'share_value': 1
});
```

## Setting Up Analytics Dashboards

### Google Analytics 4 Dashboard

1. **Navigate to Reports > Engagement > Events**
2. **Look for the "share" event**
3. **Create custom reports with dimensions:**
   - Event label (platform)
   - Custom parameter: content_type
   - Custom parameter: platform

4. **Key Metrics to Track:**
   - Total share events
   - Shares by platform
   - Shares by content type
   - Most shared content
   - Share conversion rate

### Google Tag Manager Setup

1. **Create Variables:**
   ```
   - Variable Name: Social Platform
   - Variable Type: Data Layer Variable
   - Data Layer Variable Name: social_platform
   ```

2. **Create Triggers:**
   ```
   - Trigger Name: Social Share
   - Trigger Type: Custom Event
   - Event Name: social_share
   ```

3. **Create Tags:**
   - Forward to GA4
   - Send to other analytics platforms
   - Custom tracking implementations

## Custom Analytics Integration

### Adding Your Own Analytics Platform

Add a custom tracking function:

```javascript
// Add this to your site's custom JavaScript
window.customShareTracking = function(platform, contentType, contentTitle, contentUrl) {
  // Your custom analytics code here
  console.log('Custom tracking:', {
    platform: platform,
    contentType: contentType,
    contentTitle: contentTitle,
    contentUrl: contentUrl
  });
  
  // Example: Send to your custom analytics service
  fetch('/api/track-share', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      event: 'social_share',
      platform: platform,
      content_type: contentType,
      content_title: contentTitle,
      content_url: contentUrl,
      timestamp: new Date().toISOString()
    })
  });
};
```

## Key Performance Indicators (KPIs)

### Share Volume Metrics
- **Total Shares**: Overall sharing activity
- **Shares per Post**: Average sharing rate
- **Platform Performance**: Which platforms drive most shares
- **Content Type Performance**: Blog vs. Book vs. Page sharing rates

### Engagement Metrics
- **Share-to-View Ratio**: Percentage of visitors who share
- **Platform Preference**: Most popular sharing platforms
- **Content Performance**: Which content gets shared most
- **Time-based Patterns**: When content gets shared most

### Business Impact Metrics
- **Share-driven Traffic**: Visitors who came from shared links
- **Share-driven Conversions**: Conversions attributed to shares
- **Viral Coefficient**: How many additional visitors each share brings
- **Share Quality**: Engagement of shared traffic vs. other sources

## Advanced Analytics Features

### Cohort Analysis
Track sharing behavior over time:
- First-time vs. repeat sharers
- Sharing patterns by user segments
- Content lifecycle sharing patterns

### Attribution Modeling
Understand the sharing journey:
- Which content leads to newsletter signups
- Share influence on purchase decisions
- Multi-touch sharing attribution

### A/B Testing Integration
Test sharing optimization:
- Different sharing button designs
- Platform selection variations
- Sharing message optimization

## Privacy and Compliance

### GDPR Compliance
- Analytics tracking respects `do-not-track` headers
- Cookie consent integration available
- Data anonymization features

### Data Retention
- Configure retention periods per platform
- Regular data cleanup procedures
- User data deletion capabilities

## Troubleshooting

### Common Issues

1. **Analytics Not Firing**
   - Check browser console for errors
   - Verify analytics scripts are loaded
   - Confirm configuration is correct

2. **Missing Data**
   - Check analytics platform filters
   - Verify event names match configuration
   - Review custom dimensions setup

3. **Duplicate Events**
   - Check for multiple analytics scripts
   - Review custom tracking implementation
   - Verify trigger configurations

### Debug Mode

Enable debug logging by adding to your browser console:
```javascript
localStorage.setItem('sharing_debug', 'true');
```

This will show detailed console logs for all sharing events.

## Migration Guide

### From Basic Sharing
If you're upgrading from basic sharing without analytics:

1. **Add analytics configuration** to `params.toml`
2. **Update social sharing partial** (automatic with theme update)
3. **Configure analytics platforms** in their respective dashboards
4. **Set up custom reports** and dashboards
5. **Test tracking** with browser dev tools

### Best Practices

1. **Start Simple**: Begin with one analytics platform
2. **Test Thoroughly**: Verify tracking in development
3. **Regular Review**: Check analytics data weekly
4. **Iterate**: Optimize based on performance data
5. **Privacy First**: Respect user privacy preferences

## Support and Resources

- **Google Analytics 4**: [GA4 Events Documentation](https://developers.google.com/analytics/devguides/collection/ga4/events)
- **Google Tag Manager**: [GTM Custom Events Guide](https://developers.google.com/tag-manager/devguide)
- **Plausible Analytics**: [Plausible Events API](https://plausible.io/docs/custom-event-goals)
- **Fathom Analytics**: [Fathom Goals Documentation](https://usefathom.com/docs/features/goals)
