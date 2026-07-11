Task 1: Accessibility Audit & Semantic Fixes

Initial Lighthouse Accessibility Score: 94

Issues Identified:
1. Insufficient color contrast
2. Heading hierarchy not sequential

Accessibility Improvements Applied:
• Added labels for form inputs
• Added descriptive alt text for images
• Verified semantic HTML structure
• Reviewed heading hierarchy

Final Lighthouse Accessibility Score: 95

Result:
Accessibility score improved from 94 to 95 after implementing semantic accessibility fixes.

Task 2: ARIA & Keyboard Navigation

Implemented:
• aria-label for navigation
• aria-current for active page
• tabindex for course cards
• Enter key support for keyboard users
• aria-live region for dynamic updates
• aria-expanded toggle for menu button
• Visible keyboard focus styling

Result:
All interactive elements are accessible through keyboard navigation and include appropriate ARIA attributes.

Task 3: Colour Contrast & Cross-Browser Testing

Implemented:
• Checked and improved colour contrast ratios
• Updated button and text colours to meet WCAG AA
• Tested layout in Chrome, Firefox and Edge
• Documented CSS Grid browser support using CanIUse
• Added CSS Variables Ponyfill for compatibility
• Added feature detection using @supports

Result:
The Student Portal satisfies accessibility contrast requirements and renders consistently across modern browsers.