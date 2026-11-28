# Design System Checklists (checklist.design — Design System)

32 checklists: 5 foundations + 27 components. Source: https://www.checklist.design/design-system. Every item is a required test for the layer or component.

## Foundations

### 1. Typography
The type layer defining a scale, hierarchy, and set of text styles that is consistent, accessible, and expressive across all product contexts.
- **Type scale** — A defined set of font sizes with a consistent ratio, covering captions to display headings. A modular scale (1.25, 1.333, 1.5) produces a more harmonious hierarchy than arbitrary sizes.
- **Semantic text styles** — Named styles describing role rather than size (display-large, body-default, label-small, caption). Style names chosen by size (24px, 18px, 14px) lead designers to select by measurement rather than role, making the system harder to evolve.
- **Typeface selection and loading** — The chosen typefaces detailing style and weight (e.g. Inclusive Sans Medium).
- **Line height per style** — Line height defined explicitly for every text style; tightly spaced headings and readable body require different values (e.g. 1.5 body, 1.2 heading, 1.1 display).
- **Letter spacing per style** — Letter spacing defined per style where needed, following a consistent pattern across style groups.
- **Responsive type behaviour** — How text styles respond to viewport size: fluid scaling, breakpoint overrides, or fixed sizes with responsive layout compensation.
- **Minimum readable size** — The smallest text size in use, and how readability at that size is validated in the actual rendering environment. Consider minimum size differently for desktop and mobile.
- **Accessibility responsiveness** — How text styles behave at 200% browser zoom, and whether any style communicates meaning through colour variation alone.

### 2. Accessibility
The accessibility foundation: standards, tooling, and shared conventions ensuring every component is built inclusively from the start.
- **Target conformance level** — The WCAG conformance target documented and referenced in contribution guidelines. WCAG AA is a typical baseline for most products, with AAA achievable for specific criteria such as text contrast.
- **Colour contrast standards** — Contrast ratios verified across all text and interactive element combinations: 4.5:1 for normal text, 3:1 for large text and UI components. Show these ratios in existing UI.
- **Focus indicator design** — A visible, high-contrast focus indicator designed for every interactive component. Show clear examples for common components like button and input field.
- **Keyboard navigation patterns** — Standard keyboard interaction patterns documented and applied consistently (arrow keys for menus and listboxes, Enter and Space for activation, Escape for dismissal).
- **ARIA pattern library** — Attributes making web content accessible to assistive technology, with roles, states, and properties defined for every interactive component pattern.
- **Screen reader testing** — Components tested with at least VoiceOver on Safari and NVDA on Chrome before shipping.
- **Accessibility annotations in design** — A shared annotation kit used in design files to specify ARIA labels, roles, reading order, and focus behaviour.
- **Accessibility in contribution guidelines** — Accessibility requirements part of the component contribution checklist.

### 3. Spacing / Grid
The spatial layer: a consistent scale for spacing, a grid for layout, and rules making both feel deliberate and coherent.
- **Spacing scale** — A defined set of spacing values (typically base-4 or base-8, covering 4, 8, 12, 16, 24, 32, 48, 64, 96) used for all margin, padding, and gap decisions. Base-8 is most commonly adopted because it divides evenly across common device pixel ratios.
- **Semantic spacing tokens** — Named tokens describing purpose (space-component-padding-sm, space-layout-section-gap). Raw spacing values hardcoded in components make global spacing changes much harder.
- **Column grid** — A defined column grid for each major breakpoint (typically 4 columns mobile, 8 tablet, 12 desktop) with gutter and margin values specified.
- **Breakpoints** — A named set of breakpoints (sm, md, lg, xl) shared between design and code. Breakpoint names tied to device types age poorly; content-based naming (narrow, mid, wide) describes viewport behaviour rather than hardware.
- **Component vs layout spacing** — A clear distinction between spacing inside components and spacing used to compose layouts, since different scales apply to each.
- **Density variants** — Where applicable, defined compact and comfortable density modes, common in data-heavy products where users choose between information density and breathing room.
- **Baseline grid alignment** — Text baselines and component heights designed to align to the base unit, so stacking elements produces predictable, harmonious vertical rhythm.

### 4. Color System
The color layer: a palette that is purposeful, accessible, themeable, and expressed as tokens rather than raw values.
- **Primitive palette** — A base set of named color ramps (blue-100 through blue-900, neutral-0 through neutral-1000) serving as raw material for all semantic decisions. Systems where components reference primitive values directly are significantly harder to theme.
- **Semantic color tokens** — Named tokens describing purpose rather than appearance, so the system can be reskinned without touching components (color-background-primary, color-text-danger, color-border-interactive).
- **Interactive state colors** — Defined values for default, hover, pressed, focused, disabled, and selected states applied consistently across all interactive elements.
- **Feedback colors** — A consistent set for success, warning, error, and informational states, used across alerts, form validation, badges, and status indicators. Feedback colors that pass contrast in light mode frequently fail in dark mode — test each token pair against every surface in both themes.
- **Contrast ratios (accessibility)** — A breakdown of text and interactive element combinations verified to meet WCAG AA minimums: 4.5:1 for normal text, 3:1 for large text and UI components. Not all colors pair together nicely, so define this for all usage.
- **Dark and light mode definition** — A complete parallel set of semantic token values for the opposite mode. This is not as simple as inverting one mode; the two require their own system (still using the same primitive colors).
- **Brand color integration** — Brand colors mapped into the semantic system maintaining accessibility. Where brand values fall below contrast thresholds, restrict them to decorative contexts, with accessible token values carrying text and interactive roles.
- **Color blindness considerations** — The palette tested against common color vision deficiencies for when color conveys state. Consider relative items to the color, so an icon or text helps convey state if the color is not successfully visible.

### 5. Tokens
The layer where defined variables are outlined across the platform to enable consistency, theming, and alignment with code.
- **Three-tier token architecture** — Tokens organised into primitive, semantic, and component tiers: primitives store raw values, semantic tokens describe purpose, component tokens scope decisions to a specific element. It is okay to start with just primitives and component tokens, and only utilise semantic for theming.
- **Naming convention** — A consistent, predictable naming pattern so any token name communicates its purpose without documentation. `blue-500` tells you the value; `color-interactive-primary-default` tells you when and where to use it.
- **Token documentation** — Each semantic token documented with its intended use, example contexts, and what it can and cannot be used for.
- **Token governance** — A clear rule for what constitutes a token versus a hardcoded value, and a process for reviewing and approving new tokens before they join the system. New tokens should be suggested with clear reasoning of purpose and scalable use.
- **Design tool sync** — Tokens maintained in the design tool as variables. Aim to connect tokens to code; naming convention 1:1 is ideal for ongoing maintenance.
- **Versioning and changelog** — Token changes versioned and communicated so consuming teams know when values change and the impact on their surfaces.

## Components

### 6. Button
An interactive element that triggers an action when clicked or tapped, communicating clickability and feedback.
- **Base style** — The default style: fill, outline, or underline.
- **Shape** — Visual properties: padding, border, border radius, shadow.
- **Variants** — Each visual type representing button structure, e.g. primary and secondary buttons.
- **Copy** — Instructional text detailing what will happen when clicked. Users should understand what will happen before clicking. Generic copy like "Okay" or "Cancel" is acceptable only with context around the action.
- **States** — How the button changes based on interaction: hover, focused, disabled.

### 7. Icon
A small, symbolic visual element representing an action, feature, or concept.
- **Responsiveness** — Flexibility in icon detail at varying sizes. Ensure the icon is recognisable at all sizes it is displayed at, and whether detail needs simplifying at smaller sizes.
- **Visual style consistency** — All icons share the same stroke weight, corner radius, and optical sizing approach.
- **Color** — Black and white, flat colors, or gradients. Incorporate branding colours into the style.
- **Naming** — Name an icon by what it literally is so it can be used flexibly. Do not name it by an action, e.g. a pencil icon should not be named "edit", as it could be used for another purpose elsewhere.

### 8. Badge
A small visual indicator displaying short, dynamic information like counts or status, often as a colored circle or pill overlaid on other elements.
- **Detail** — A badge can have a numeric value or a basic shape. A basic shape is effective for conveying one update; a numeric value represents the amount of updates.
- **Color** — Badges can represent standard states — error, success, warning. Be consistent in the details: outlines, shadows, perspective, corners, and colours.
- **Offset position** — A badge should sit outside its relevant element to gain attention more easily.

### 9. Card
A contained, modular component grouping related information and actions within a distinct container.
- **Style** — Consider default background, border, shadow.
- **Consistency** — Ensure one base style for all cards.
- **Spacing** — A framework to sort padding levels by. Choose an easily divisible number as the padding difference, like divided by 4 or 5.
- **Responsiveness** — Consider the structure of the content at all screen sizes. Adopt a top-down approach on mobile to avoid overfilling rows.
- **Content hierarchy** — The primary action(s) you want users to perform. Display links at the end of the card so the user is informed by the content before making a decision.

### 10. Avatar
A visual representation of a user, identifying individuals across a digital interface.
- **Visualiser** — Show what the avatar looks like before posting or updating.
- **Link to upload or select avatar** — An accessible link for the user to select. If the avatar itself should be clickable to change, add an indicator on it (e.g. a pencil icon).
- **Placeholder image** — If a user has not uploaded an avatar, there should be a placeholder (a default icon or the user's initials).
- **Acceptable file types** — Tell the user what file types are allowed (JPEG, PNG, SVG).
- **Status change updating avatar** — Feedback that the avatar changed (a banner or toast, for example), though it does not have to be part of the avatar component.
- **Alternatives** — If a user does not want to upload an image, offer an illustrative alternative — better than nothing and it can still convey personality.
- **Editing uploaded avatar** — Allow the user to crop and resize their avatar before saving.

### 11. Input Field
An interactive area where users enter and edit text or data, with labels and validation feedback.
- **Input field** — Interactive text field for user data. Ensure text size is readable on all devices.
- **Label** — Stating what information the user is meant to provide. Avoid all caps for text labels to improve readability.
- **Placeholder text** — Text inside the field acting as an example of what to enter. Placeholder text colour must be notably lighter than default text so users do not assume the field is filled.
- **Data format** — Set fields to allow relevant text values, e.g. numeric only for a phone number. Hint at the preferred format with placeholder text or a hint.
- **Illustration or icon** — A visual cue helps break up a long list of text fields.
- **Hint** — Elaborate on the title of the field in case a user struggles to know what to enter.

### 12. Searchbar
An interactive input field for finding content by entering keywords or phrases, often with autocomplete.
- **Input field** — A clear container for the user to start typing in.
- **Label or placeholder text** — Identify that the field is for searching. Use placeholder text to suggest examples of what to search for.
- **Quick links, autocomplete and suggestions** — As the user types, offer available links and phrases based on what has been entered. With enough usage data, base suggestions on previous searches.
- **Submit search button** — A visible link to submit the search and view results. Include a loading icon or feature once search has been submitted in case of a connection issue.
- **Previous searches** — Showing what a user has searched before speeds up the experience if they frequently search the same queries.
- **Appropriate visibility** — Search should be directly linked to what is being looked for, whether across the entire platform or a specific area.

### 13. Checkbox
An interactive control allowing users to select or unselect items — a single item triggering logic, or a list to select amongst.
- **Label** — Text paired with the checkbox indicating what is enabled if selected.
- **Default selection** — Whether the checkbox is selected by default. An active checkbox by default depends on its purpose — how much this conveniences the user.
- **Style** — Ensure the checkbox is unique and stands out from other input options, considering whether it is in a container, how it is grouped, and what colour it uses.
- **States** — Default, hover, focused, active, and disabled.

### 14. Radio
An interactive control to select exactly one option from a predefined set of mutually exclusive choices.
- **Label** — Text associated with the radio input.
- **Grouping** — There must be more than one radio option for the experience to work. Use radio to surface all input options when only one can be selected. Radios with short labels can be aligned horizontally, but should usually be vertical.
- **Default selection** — Start with a radio option selected. This need not be the first option; it can be the more likely option based on research.
- **Style** — Ensure the radio is unique and stands out from other input options.
- **Clickability** — Consider what is clickable to make the radio option active (text label, container).
- **States** — Default, active, and disabled.

### 15. Toggle
A switch-like control for quickly alternating between two opposing states with a single click or tap.
- **Context** — Explaining what the toggle will do. A toggle should always be turning a function on or off, not between two opposing versions of a function. Use toggles for straightforward decisions with low-risk implications.
- **Transition** — A clear visual change as the toggle switches between states.
- **State** — How the button changes based on interaction. Contrast active and inactive with brand colour for active and keeping the inactive muted.

### 16. Tabs
Navigation elements that organize and separate content into different sections within the same view.
- **Labels** — Name of each tab. The label should be logical enough for the user to predict what is in the tab. Keep it concise, ideally 1 word.
- **Content area** — Where the content for the active tab is displayed: typically underneath a horizontal tab, or to the right of a vertical tab.
- **Style** — How the active and inactive tabs differentiate visually, as well as the tab container overall.
- **Item order** — Arrange tabs ordered by popularity or familiarity.
- **States** — Default, active, hover are the key states.

### 17. Table
A grid component for dense data.
- **Table header** — The value of each column providing structure for the row content. Fix the header on scroll to continue giving context.
- **Row style** — Borders and contrasting background colours to differentiate rows.
- **Spacing** — Define the consistent padding of each row and the header.
- **Search** — The ability to find a specific keyword or row. Ensure all possible data points can be searched and defined by text input.
- **Actions** — Performing a task based on the row and information seen, e.g. view, edit, delete.
- **Filter and sort** — Allow users to customise what they want to see and in which order.
- **Responsiveness** — Determine the structure on significantly smaller devices — whether information collapses into an accordion, for example. Horizontal scrolling is an alternative to rethinking a new layout.
- **Pagination** — Breakpoints in the table for digesting information in parts.

### 18. Tooltip
A small informational popup appearing on hover or focus, providing additional context or explanations.
- **Information** — Keep content clear and concise. Information should be entirely relevant to what the tooltip is for and elaborate on what is already visible.
- **Contrast** — The background should be different from the underlying content. An inverse colour works best — if what is behind is dominantly light, make the tooltip dark with light text.
- **Visibility** — How a tooltip looks and shows. It should activate on hover or focus of the relevant icon or text. Only one tooltip should be visible at a time, and it should not cover the content it relates to.
- **Dismiss action** — Depending on how intrusive or extensive the tooltip is, a dismiss lets the user feel more in control and makes the tooltip feel more flexible and non-compulsory.

### 19. Dropdown Menu
A dropdown triggered from a button or right-click target to reveal a menu of actions.
- **Trigger affordance** — The element that opens the menu: an overflow icon, chevron button, or right-click target.
- **Menu item anatomy** — The structure of each action: label, optional leading icon, optional trailing shortcut, optional destructive styling. Mixing icon and non-icon items in the same list throws off the scan.
- **Section dividers and groups** — Dividers and/or labels breaking related actions into sections once the menu gets large.
- **Destructive item styling** — Visual differentiation (typically the danger colour) for actions that cannot be undone. Always place destructive actions at the end of the menu, after a divider, to reduce misclicks.
- **Nested submenu** — A secondary menu triggered by a parent item, used for grouping related but distinct actions. Limit nesting to one level to avoid being too layered and confusing.
- **Disabled items** — Menu items visible but not triggerable. A tooltip revealing the reason it is disabled is handy.
- **Positioning and overflow** — The menu's placement relative to its trigger, repositioning automatically to stay within the viewport.
- **Keyboard shortcut display** — Shortcut hints aligned to the trailing edge of the item label.

### 20. Loading
A loading indicator communicating that content or an action is being processed, through animations like spinning wheels, progress bars, or skeleton screens.
- **Visual indicator** — A clear representation that content is loading or in progress of change.
- **Text** — Explaining the loading state. Let the standard "loading" text be a fallback, and try to be more specific, e.g. "adding your contacts, syncing your emails".
- **Time** — Determine how long the gap between two actions must be to require a loading component. Do not interrupt two actions that instantly transition; if there is a known 5-second period, the component is appropriate.
- **Accessibility** — Ensure the loading state can be clearly seen. Place the indicator in a container regardless of background; if it stands alone, create a version appropriate for light/dark backgrounds.
- **Visuals** — Entertain the user with an illustration during the loading state.

### 21. Skeleton
A placeholder mimicking the structure of content while it loads, providing visual feedback and reducing perceived wait time.
- **Match content structure** — Skeletons should mirror the size and layout of the content that will replace them, to reduce jumpiness on load.
- **Animation** — Subtle motion to indicate loading without being too distracting: shimmer, pulse, or wave motion.
- **Style** — Flat shapes with no depth, rounded or sharp.
- **Color scheme** — Typically a neutral gray or very soft colour that does not call attention and contrasts just enough with its background.
- **Transition to real content** — A smooth, subtle movement like a fade out before the content loads.

### 22. Alert
- **Descriptive message** — Alert copy that explains what happened and what the user needs to do, rather than generic labels like "Error" or "Success".
- **Placement and stacking** — Where alerts appear in the layout (inline near relevant content, at the top of a form, or in a fixed notification area), and how multiple simultaneous alerts are ordered.
- **Dismissible option** — A close button on informational alerts that do not require action, letting the user clear them when done.
- **Icon reinforcement** — An icon alongside the message reinforcing the alert type — not as a substitute for colour but as a signal for colour-blind users.
- **Semantic variants** — Distinct visual treatments for informational, success, warning, and error states, using colour, iconography, or both.
- **Inline action (if applicable)** — An optional link or button inside the alert for the most relevant next action, avoiding navigation elsewhere to resolve it.

### 23. Banner
A prominent notification item displaying important messages using distinct colors and placement to stand out from regular page content.
- **Style** — How the banner types look (fill, text colour, border radius, etc.). Ensure the banner stands out enough on your default UI, as its usage means it should not be missed.
- **Content** — A title is a must; a description can be considered if a title does not convey enough information.
- **Types** — Banners typically appear as 5 options: information, success, warning, error, neutral. This helps visually establish context and level of importance.
- **Call to action button** — A banner may call for the user to do something, like fix the error it is calling out. Only have a button if it feels needed; banners typically work best to inform.
- **Placement** — Where the banner sits on the page, dependent on context and importance. Consider the impact on the experience: information affecting the entire application should be a banner at the top on every page; information affecting a small feature may sit within that section.
- **Dismissable** — Whether the banner can be dismissed. Positive/neutral banners (info and success) suit this, but not warning/error banners as they are too critical.

### 24. Toast
A brief, non-disruptive message appearing temporarily at the edge of the screen to provide feedback about an action or system status.
- **Copy** — The text in the toast. Copy should be clear and concise, focusing on a status or action.
- **Placement** — The toast should appear on the corners of the viewport, not as the focus.
- **Usage** — Toasts are triggered to appear after an action or event.
- **Variants** — Dictated by colour usually, affecting the emotion of a message. If informing a status, do not rely on just color — leverage icons or the copy.
- **Length of appearance** — Visible long enough to read but short enough not to obstruct other information for too long. Read the text out loud slowly to gauge how much time is needed.
- **Dismissable** — Depending on the amount of content, a toast can be closed by the user; it should fade away shortly after appearing if it cannot be manually dismissed.

### 25. Accordion
A vertically stacked list of items that reveal or hide associated content sections when clicked, organizing information hierarchically and saving screen space.
- **Header** — The clickable area that triggers expanding and collapsing and has a title. The header text should clearly convey the content inside.
- **Expand/collapse icon** — A visual indicator of the current state — typically a plus/minus, or a caret/chevron that rotates between states.
- **Content area** — The content that shows or hides when toggled, containing detailed information associated with the header. Headers should be text only; content can be anything suited to help answer or elaborate on the header (text, image, video, etc).
- **States** — Default (collapsed), expanded, hover, focused, and disabled.
- **Expanding logic** — Decide whether users can open multiple sections at once or one at a time. This can be determined by whether information from other items is related and should be seen together.

### 26. Carousel
A slideshow component displaying content one slide at a time, alternated through manual navigation or automatic transition.
- **Ways of interaction** — Defining whether transitions are auto-play, navigated by controls, or both.
- **Visual progress indicator** — Show dots, numbers, or a progress bar so users know how many slides there are and which one is currently being viewed. Make the current slide's indicator noticeably different so position can be tracked at a glance.
- **Dimensions and alignment** — The size of the items and their responsiveness across devices. Decide how content sits inside the item container so it fills the required space without being stretched or non-uniform.
- **Animation behaviour** — The direction, speed, and feeling of how items transition between each other.
- **Focused item state** — If the carousel shows one item at a time, the focused one should appear different from items entering and exiting. Size, transparency, and colour are typical properties to change on non-focused items.

### 27. Slider
An interactive control allowing users to select a value from a continuous range by dragging a handle along a track.
- **Style** — How the range and the handles look visually.
- **Intervals** — Whether the slider intervals are continuous (any value between 0–10000) or stepped (fixed values like a 0–5 rating).
- **Handles** — The elements users select to drag and change the value. Handles should clearly "break" out from the slider container to be easily identified.
- **Labelling** — Text conveying the spectrum of the slider, or the intervals between those ends.
- **Interaction states** — What the handles and slider look like when the user is changing the value.

### 28. Date Picker
- **Calendar grid** — A month view with days arranged in a weekly grid, navigable forward and backward by month, as the primary date selection surface.
- **Text input alongside** — A free-text date field paired with the calendar, so users who know the date can type it rather than relying on clicking only. Suitable when selected dates may be months or years away, e.g. date of birth.
- **Date range selection (if applicable)** — The ability to select a start and end date, with the range highlighted across the grid and both values independently editable.
- **Disabled dates** — Past dates, unavailable dates, or out-of-range dates visually distinct from selectable ones.
- **Today shortcut** — A clearly labelled button or link to jump to today's date.
- **Locale and format** — The calendar respecting regional conventions (week starting Monday or Sunday; date format in the text input matching the user's locale, DD/MM or MM/DD).
- **Time selection (if applicable)** — When a time is also required, a time picker integrated with or accessible directly from the date picker, not a separate disconnected control.

### 29. Breadcrumb
A secondary navigation element showing the user their current location within a hierarchy.
- **Current location** — The current page shown as the final item in the trail, visually distinct from preceding levels, typically not a link.
- **Level links** — All preceding levels rendered as active links, each navigating directly to that level rather than requiring back-button presses.
- **Separator character** — A consistent visual separator between levels (a slash, chevron, or arrow) distinguishing hierarchy from a list of links.
- **Truncation for long paths** — Deep hierarchies collapsed with an ellipsis, preserving root and current page while hiding intermediate levels behind a toggle. Breadcrumbs that wrap onto multiple lines disrupt layouts more than a collapsible ellipsis. Truncation at three to four visible levels is a consistent balance.

### 30. Modal
A dialog box or popup appearing on top of main content, requiring attention or interaction before returning to the main interface.
- **Title** — Clear, simple text explaining the action of the modal.
- **Actionable item** — A button or link to continue or close. Users should always know where they are going or what event will happen before clicking a button. If the button has generic copy like "Okay" or "Cancel", include a label above it describing the event or purpose.
- **Close action** — A way to exit the modal.
- **Responsiveness** — Consider the modal size on different devices, and whether a modal is suitable on all. On mobile, adapt the modal to full screen to gain more space.
- **Background change behind modal** — Darken, blur, or lighten the background to bring focus to the modal.
- **Description** — In case more information is required to understand how to make their decision.

### 31. Drawer
A panel that slides in from the edge, overlaying content, providing access to detailed information without completely navigating away from the current page.
- **Placement** — Which edge the drawer slides from — most commonly from left (navigation) or right (details/settings).
- **Dimensions** — Typically full height, but width can vary. It should be wide enough for complex content without taking over the entire page.
- **Overlay** — A semi-transparent background for the remaining screen area to bring focus to the drawer.
- **Header** — Top section with a title describing contents or purpose, along with a close action (optional). A description of contents can be included if the header is too simple.
- **Content area** — The main section, which should be scrollable if content exceeds window height.
- **Open and close trigger** — How the user activates the drawer. Typically a button to open, while closing can have multiple ways: clicking the overlay, a close button, or pressing Esc should all be active options.
- **Footer** — A fixed area at the bottom for actions, usually a primary and secondary, e.g. Save & Cancel.

### 32. Stepper
A numeric input control with increment and decrement buttons for adjusting a value by discrete steps, such as quantity, duration, or count.
- **Increment and decrement controls** — Buttons on either side of the numeric display for adjusting the value up or down by a fixed step.
- **Direct text entry** — The ability to type a value directly into the display field, in addition to using the buttons. Suitable where value changes could have large jumps, e.g. more than 10.
- **Min and max bounds** — Defined minimum and maximum values the stepper will not exceed, with the relevant button visually disabled when a boundary is reached. Disable the stepper at the minimum/maximum rather than hiding the controls.
- **Step size** — The amount by which the value changes per button press — typically 1, but configurable for units like 5, 10, or 0.5.
- **Input validation** — Handling of values entered directly that fall outside the min/max range or contain non-numeric characters.
- **Size variants (if needed)** — Small, medium, and large sizes for different contexts — a compact quantity selector in a product card vs. a settings input.
- **Keyboard support** — Arrow keys incrementing and decrementing the value when the input is focused.
