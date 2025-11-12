/**
 * Social Sharing Analytics Module
 * Handles tracking of social sharing events across multiple analytics platforms
 */

(function() {
  'use strict';

  // Configuration (populated by Hugo template)
  const config = window.socialSharingConfig || {};
  
  /**
   * Track a social sharing event across all enabled analytics platforms
   * @param {string} platform - The sharing platform (e.g., 'twitter', 'linkedin')
   * @param {string} contentType - The content type (e.g., 'blog', 'book', 'page')
   * @param {string} contentTitle - The title of the shared content
   * @param {string} contentUrl - The URL of the shared content
   */
  function trackSocialShare(platform, contentType, contentTitle, contentUrl) {
    const eventData = {
      platform,
      contentType,
      contentTitle,
      contentUrl,
      timestamp: new Date().toISOString()
    };

    // Google Analytics 4
    if (config.trackGA4 && typeof gtag !== 'undefined') {
      const gaEventData = {
        event_category: 'Social Sharing',
        event_label: platform,
        value: 1
      };
      
      if (config.includeContentType) gaEventData.content_type = contentType;
      if (config.includeContentTitle) gaEventData.content_title = contentTitle;
      if (config.includeContentUrl) gaEventData.content_url = contentUrl;
      if (config.includePlatform) gaEventData.platform = platform;
      
      gtag('event', config.eventNames.googleAnalytics, gaEventData);
    }

    // Google Tag Manager
    if (config.trackGTM && typeof dataLayer !== 'undefined') {
      const gtmData = {
        event: config.eventNames.gtm,
        social_platform: platform,
        share_value: 1
      };
      
      if (config.includeContentType) gtmData.content_type = contentType;
      if (config.includeContentTitle) gtmData.content_title = contentTitle;
      if (config.includeContentUrl) gtmData.content_url = contentUrl;
      
      dataLayer.push(gtmData);
    }

    // Custom analytics hook
    if (typeof window.customShareTracking === 'function') {
      window.customShareTracking(platform, contentType, contentTitle, contentUrl);
    }

    // Debug logging (only if debug mode is enabled)
    if (config.debug || localStorage.getItem('sharing_debug') === 'true') {
      console.log('Share event tracked:', eventData);
    }
  }

  /**
   * Enhanced copy to clipboard with analytics tracking
   */
  function copyToClipboardWithTracking(text, button, platform, contentType, contentTitle, contentUrl) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text)
        .then(() => {
          showCopySuccess(button);
          trackSocialShare(platform, contentType, contentTitle, contentUrl);
        })
        .catch(() => {
          fallbackCopyToClipboard(text, button, platform, contentType, contentTitle, contentUrl);
        });
    } else {
      fallbackCopyToClipboard(text, button, platform, contentType, contentTitle, contentUrl);
    }
  }

  /**
   * Fallback clipboard method for older browsers
   */
  function fallbackCopyToClipboard(text, button, platform, contentType, contentTitle, contentUrl) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
      document.execCommand('copy');
      showCopySuccess(button);
      trackSocialShare(platform, contentType, contentTitle, contentUrl);
    } catch (err) {
      console.error('Failed to copy text:', err);
    }
    
    document.body.removeChild(textArea);
  }

  /**
   * Show visual feedback for successful copy operation
   */
  function showCopySuccess(button) {
    const originalHTML = button.innerHTML;
    button.innerHTML = '<i class="fas fa-check"></i> Copied!';
    button.classList.add('bg-green-600');
    button.classList.remove('bg-gray-600', 'hover:bg-gray-700');
    
    setTimeout(() => {
      button.innerHTML = originalHTML;
      button.classList.remove('bg-green-600');
      button.classList.add('bg-gray-600', 'hover:bg-gray-700');
    }, 2000);
  }

  /**
   * Track external link shares with small delay to ensure tracking fires
   */
  function trackExternalShare(platform, contentType, contentTitle, contentUrl) {
    trackSocialShare(platform, contentType, contentTitle, contentUrl);
    
    // Small delay to ensure tracking fires before navigation
    setTimeout(() => {
      if (config.debug) {
        console.log('External share tracking completed for:', platform);
      }
    }, 100);
  }

  // Expose functions globally
  window.trackSocialShare = trackSocialShare;
  window.copyToClipboardWithTracking = copyToClipboardWithTracking;
  window.trackExternalShare = trackExternalShare;

})();
