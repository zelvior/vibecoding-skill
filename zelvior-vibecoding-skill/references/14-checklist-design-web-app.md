# Web App Checklists (checklist.design — Web App)

38 checklists. Source: https://www.checklist.design/web-app. Every item below is a required test for the screen it belongs to.

## 1. Home
The personalised starting point of the app — a dashboard that orients the user and surfaces the most relevant next actions.
- **Personalised greeting** — Using the user's name, orienting them on return. Recent context makes the greeting functional rather than decorative ("Welcome back, Sarah. You have 3 unread messages").
- **Key metrics or activity summary** — A headline view of the numbers that matter most. A fixed set of metrics becomes irrelevant as priorities vary — 3–5 with customisation covers the range without overwhelming.
- **Quick actions and shortcuts** — The 3–5 most commonly performed tasks, one click away. Usage data is the reliable guide, not guessed shortcuts.
- **Recent items or activity** — Most recently created or edited items so the user can jump straight back in. Last-accessed order serves returning users better than last-created.
- **Onboarding steps for new users** — A checklist or progress indicator guiding new users through valuable setup tasks. Retire the widget once complete; persistent onboarding checklists create noise.
- **Notification or alert surface** — A place for items requiring the user's attention. Treating "requires action" and "for your information" the same trains users to ignore everything.
- **Customisable layout** — The ability to rearrange, add, or remove widgets. Most users never customise — defaults are the experience for the majority.

## 2. Dashboard
The first screen after logging in: an at-a-glance overview of the most relevant data, actions, and recent activity.
- **Welcome state** — A brief summary of what has happened since the last visit, re-orienting returning users.
- **Key metrics** — The numbers most relevant to the user's goals, readable without leaving the home screen. Time period context (daily, weekly, monthly) gives numbers meaning at a glance.
- **Recent activity** — The most recently created or updated items, enabling users to resume work without hunting.
- **Needs attention** — Time-sensitive items requiring a decision, surfaced here instead of buried. Avoid alert fatigue: only critical, relevant items belong here.
- **Quick actions** — Shortcuts to the most common tasks without navigating away. The most frequent action after landing belongs here.
- **Empty state** — The state when there is nothing to show yet, with a clear first action. A blank dashboard is one of the most common reasons new users churn.
- **Layout control (if applicable)** — Controls to show, hide, or reorder widgets so the home screen matches how the user works.

## 3. Analytics
A live dashboard surfacing key metrics and trends, helping users understand what is happening right now.
- **Date range selector** — A date picker with shortcuts for today, last 7 days, last 30 days, this month, and custom range. Keyboard entry for custom ranges is valued.
- **Headline metrics** — The most important numbers as prominent headline figures ("snapshots" of performance).
- **Charts with labels and axes** — Visualisations with clearly labelled axes, a legend where needed, and readable tick marks.
- **Period comparison** — A percentage or absolute change indicator versus the prior period. Percentage suits larger values; absolute numbers suit lower values.
- **Segment breakdown** — The ability to slice a metric by channel, device, geography, or another attribute. Quick-select breakdowns based on popular selections are a thoughtful shortcut.
- **Last updated indicator** — A visible timestamp or refresh button showing when data was last updated (if not auto-refreshing).
- **Loading and empty states** — Skeleton loaders while fetching, and a contextual message when no data exists. "No data for this period" with a suggestion to adjust the range is more useful than a blank screen.

## 4. Reporting
Generated reports that can be exported, scheduled, and shared — structured summaries of data for stakeholders.
- **Report selection and parameters** — Choose the report type and configure inputs (date range, segments, filters). Saved presets remove significant recurring friction for weekly reports.
- **Scheduled or on-demand generation** — Run immediately or schedule automatic generation and delivery. Email delivery is the most common use case; format should be selectable per report.
- **Export options** — Download as PDF, CSV, or spreadsheet. When only one format is possible, CSV is more useful to more users.
- **Report title and generation date** — Clear labelling of what the report covers and when it was created. A report without its parameter context is hard to interpret when shared externally.
- **Summary or key findings section** — A brief narrative or highlights section at the top. An auto-generated summary adds value for recipients who will not read the full data.
- **Historical archive of past reports** — Previously generated reports downloadable or re-openable. Finding a quarterly report from six months ago should take one click.
- **Share or distribute options** — Sending the report to colleagues or external stakeholders. Shareable links with expiry work well for external recipients; requiring an account is a significant barrier.

## 5. Report View
A read-only view of generated business data containing charts, tables, and summaries designed for review and sharing.
- **Report metadata** — Title, author, date range, and generation time, providing context to make sense of the data outside the platform.
- **Summary or key findings section** — A brief narrative or highlights at the top, before the detailed data.
- **Data visualisations** — Charts, tables, and graphs that make the data easier to interpret. Line charts suit trends, bar charts comparisons.
- **Filter capabilities** — Clicking into a chart or row to explore the underlying data. Even read-only reports benefit from basic filtering, which saves regenerating the whole report.
- **Export to PDF, CSV, or spreadsheet** — Download options for sharing or further analysis. PDF suits presentations; CSV suits analysis.
- **Table of contents** — Sections and headings laid out for readers to navigate to specific areas.

## 6. Data Table
A structured grid for dense datasets with sorting, filtering, bulk operations, and column control.
- **Sortable columns** — Column headers that sort rows on click, toggling ascending and descending. A sort indicator keeps the current direction visible, since users lose track easily.
- **Column visibility and order** — Controls to show or hide individual columns and drag to reorder. Persist column preferences across sessions — resetting each visit is a consistent complaint.
- **Row selection and bulk actions** — Checkboxes on each row and a persistent action bar when rows are selected. Showing the count ("3 items selected") keeps the user oriented.
- **Row actions on hover** — Contextual actions (edit, delete, view) appearing on row hover. Two to three hover actions maximum; anything beyond belongs in an overflow menu.
- **Search and filter** — A search input for quick lookup alongside filters for narrowing. Active filters persisted visually as chips above the table.
- **Pagination** — Controls to navigate between pages, with a per-page row count option. Showing the total ("1–50 of 1,240") gives users a sense of scale and progress.
- **Frozen columns** — The first column pinned so it remains visible when scrolling horizontally. Essential for wide tables.
- **Export action** — Download the visible or selected rows as CSV, spreadsheet, or another format. Export must reflect the current filter and states.
- **Empty and loading states** — States when there are no rows or data is being fetched. Skeleton rows during loading prevent layout shift and set expectations.

## 7. List View
A simpler row or card layout for browsing collections where dense tabular structure is not needed.
- **Primary info hierarchy** — The primary identifier for each item prominent enough to scan without reading every detail. Typographic hierarchy is what makes lists scannable.
- **Secondary metadata without clutter** — Supporting details (date, category, owner) present but visually subordinate. More than 3–4 secondary fields makes rows dense; hide the least important until hover.
- **Item actions on hover** — Actions like edit, delete, or open appearing on hover. Right-aligned actions that fade in keep the list clean at rest.
- **Bulk selection mode** — Select multiple items and act on them together. A visible "X items selected" bar makes the mode clear — without it, selection state is easy to forget.
- **Sort and filter controls** — Ordering and narrowing controls. Active sort and filter state visible at all times; a filter applied and then navigated away from should persist on return.
- **Infinite scroll or load more** — A way to see additional items beyond the initial load. "Load more" is generally preferable to infinite scroll for content users need to reference.
- **Group or section headers** — Visual dividers and labels when items are organised into categories or time buckets. Sticky group headers keep the user oriented.
- **Empty and first-use states** — Helpful messages and actions when there are no items. A blank list is a top drop-off point for new users.

## 8. Feed
A stream of content, activity, or updates that users scroll through to stay informed.
- **Feed item preview** — A preview of each item (title, excerpt, or thumbnail) sufficient to judge whether it is worth opening. A consistent layout makes items easier to differentiate.
- **Author** — The name and avatar of the person who created or posted each item. Linking the author name to their profile is a natural interaction expectation.
- **Timestamps** — When each item was published or last updated. Relative time works for recent items; switch to the exact date and time eventually.
- **Engagement actions** — Ways to interact with feed items (like, comment, share, save, or react). Consider the prominence and frequency of each interaction.
- **New content indicator** — A banner or button appearing when new items have been posted since the feed loaded. Auto-injecting new posts while reading pushes content down and makes scrolling janky.
- **Filtering** — Controls for narrowing to a category, content type, or followed accounts. Always indicate when filters are active.
- **Pagination or infinite scroll** — A mechanism for loading more items at the bottom. Pagination suits work-related apps with extensive databases.
- **Empty state** — The state when there are no items, whether from no connections, no activity, or an empty filter result. A first-use empty state can point toward a specific action.

## 9. Notifications
An area surfacing alerts, updates, and activity relevant to the user.
- **Notification list** — A chronological feed of alerts, messages, and activity updates. Date grouping (today, yesterday, this week) makes the list more scannable.
- **Read and unread states** — A clear visual distinction between seen and unseen notifications. An unread count can appear on the icon or button that opens notifications.
- **Notification type** — A visual or label indicating the type (mention, system alert, billing event).
- **Timestamp** — Relative time for recent items, a complete date and time for older ones.
- **Actions (if applicable)** — An action related to the notification event, e.g. a "reply" button on a direct message notification.
- **Mark all as read** — A single action to clear all unread indicators at once.
- **Empty state** — A clear message when there are no notifications.

## 10. Notification Settings
Where users configure exactly which notifications they receive, through which channels, and how frequently.
- **Categories** — Notification types organised into logical groups (product activity, mentions, billing, security, marketing).
- **Channel selection** — Controls for which channel each notification type arrives through (in-app, email, push, SMS). Not all channels suit all notification types — a billing alert via push is rarely necessary.
- **Frequency controls** — Controls for how often notifications arrive (immediately, daily digest, weekly summary).
- **Global mute** — A way to temporarily silence all notifications without turning each one off individually.
- **Save confirmation** — A clear indication that preference changes have been saved. Auto-save works well; the key is ensuring the user knows the changes are enabled.

## 11. Feedback
In-app prompts collecting user opinion — NPS surveys, CSAT ratings, and open text — surfaced at the right moment and frequency.
- **Prompt timing** — The moment the request appears, based on demonstrated engagement rather than a fixed page count or time-on-site. Highest-signal feedback comes from users who just completed a meaningful task.
- **Contextual trigger** — The specific page or action that initiates the request, relevant to the question. "How easy was it to export this report?" after an export beats "How are you finding the product?" on the dashboard.
- **Single-question entry** — Starting with one question rather than a multi-step form. Drop-off between questions is steep.
- **Rating scale** — A numeric scale (0–10 for NPS, 1–5 for CSAT) as the primary signal. Segment the follow-up question by score band.
- **Open text follow-up** — An optional field for elaboration. Label it explicitly as optional; "Tell us more (optional)" outperforms an unlabelled field.
- **Dismissal option** — A clearly visible way to close the prompt without responding. Make dismissal low-friction and label it neutrally — "Not now" rather than "Skip" or "No thanks".
- **Frequency cap** — A limit on how often the same user sees a prompt. A user who has dismissed twice is signalling disinterest.
- **Exit-intent prompt** — A request triggered when the user shows signs of leaving. Exit-intent is more reliable on web; limit it to one question.
- **Submission confirmation** — A brief acknowledgement received, shown before returning the user to context. "Thanks, we've got your feedback" is better than a promotional template line.

## 12. Comments
- **Anchor to context** — Comments attached to a specific piece of content (a paragraph, image, task, or row), not floating in a general thread.
- **Reply threading** — Replies nested under the comment they respond to, keeping discussion together without flattening into a chronological list.
- **Resolve and archive (if applicable)** — A way to mark a thread as resolved, removing it from the active view while keeping it accessible in history.
- **Reactions** — Emoji reactions on individual comments as a lightweight acknowledgement without a reply.
- **@mention element** — Mentioning a user by name, notifying them directly. Visually distinguish mentions from plain text.
- **Edit action** — The ability to edit a comment after posting, with a visible edited marker for transparency.
- **Delete action** — Ability to delete a comment after posting, with a confirmation modal beforehand.
- **Comment count indicator** — A visible count or badge on the item being discussed, so collaborators can see where active threads exist.

## 13. Chat
A screen for real-time or asynchronous messaging between users, one-on-one or in a group.
- **Message thread** — Chronological display, most recent at the bottom. Auto-scroll to the latest on load is expected, but scrolling up to read history must never be interrupted by new messages.
- **Message input** — A text field for composing and sending, supporting multi-line input (Shift + Enter for a new line, Enter to send).
- **Sender identification** — The sender's name and avatar alongside each message. Consecutive messages from the same sender do not need repeated name and avatar.
- **Timestamps** — When each message was sent; relative time for recent, full timestamp for older.
- **Read receipts** — An indicator of whether the other participant has seen the message. Not all users want this visibility; worth making optional.
- **File and media sharing** — The ability to attach images, files, or links, and show those attachments in the conversation.
- **Reactions** — Emoji reactions on individual messages as a lightweight response.

## 14. Empty State
The state of a screen or component when there is no data to display — a new user, cleared content, or a search with no results.
- **Illustration or icon** — A visual that signals the empty state and gives the screen personality rather than feeling broken. The visual should be contextual (an empty inbox and a deleted account should not look the same).
- **Clear heading** — A short, plain-language title naming what is missing. "No projects yet" is clear; "It's empty" is not.
- **Supporting description** — A brief explanation of what belongs in this space, most useful for first-time users.
- **Primary action** — A CTA pointing toward the next step: creating, importing, connecting. It should create the first item, not just link somewhere generic.
- **Zero state vs. no-results state** — A distinction between empty because nothing was created versus no search or filter results. A no-results state without a reset or broader search is a dead end.
- **Error state variant** — A separate variant for when content failed to load, as opposed to genuinely being empty. Showing an empty state when the real issue is a loading error makes users assume they lost their data.

## 15. Onboarding
A guided experience introducing new users to the product and getting them to their first moment of value quickly.
- **Progress indicator** — An indication of how many steps are involved and where the user currently is. 3 to 5 is the reliable range; every step beyond five is another opportunity to lose the user.
- **Welcome message** — A brief message acknowledging this is a new experience and orienting the user toward what the product does.
- **Account setup** — The minimum information needed to personalise the experience, gathered at the start. Delay fields not genuinely needed to start using the product.
- **Product highlights** — Key features introduced through short contextual tips or a visual walkthrough. Offer a skip route for users who have seen the content or prefer learning by doing.
- **First action prompt** — A clear prompt directing the user to an action or feature. This should be the quickest step toward understanding the product's value.
- **Completion confirmation** — A clear acknowledgement that setup is complete, transitioning the user into the main product.

## 16. Multi-step form
A form split across multiple steps or screens to reduce cognitive load when collecting a large amount of information.
- **Progress indicator** — A clear visual showing how many steps exist and which one the user is on. Labels for each step give context on upcoming steps.
- **Step heading and context** — A clear title and brief context for each step, so users know what they are being asked to provide.
- **Field grouping** — Each step containing only fields that belong together logically (e.g. phone and email for contact details).
- **Step-level validation** — Validation at each step before proceeding, not surfaced all at once at the end.
- **Back navigation** — The ability to return to a previous step to review or change answers without losing subsequent progress.
- **Save and resume** — The ability to save progress and return to the form later, particularly for forms requiring information that cannot be instantly provided.
- **Final review step** — A summary of all entered information before final submission, giving the user a chance to review and edit. Offer a link to each section at this step.

## 17. Search Results
Displaying and navigating results matching a user's query from within the product.
- **Search input** — A search field at the top of the results, pre-filled with the current query so it can be refined without starting over.
- **Result count** — How many results were found. Show it even at zero, since it tells the user the search ran rather than something broke.
- **Result items** — Each result with enough to identify it — title, type, image, and a snippet of the matching content. Highlighting the matched term confirms the match.
- **Result type indicators** — A label or icon marking what kind of item each result is (document, person, project, message).
- **Filters** — The ability to narrow results by category, date, status, or other relevant values.
- **No results state** — The state when a query returns no matches, ideally with suggestions for what to try instead. Offer alternatives rather than a blank space.
- **Recent searches** — A list of previous queries, shown when the search field is focused but empty.

## 18. Single Item Detail
A screen displaying the full details of a single record — a user, order, document, or any other entity — after selecting it from a list.
- **Clear title or identifier** — The name, ID, or primary label of the item, shown prominently at the top.
- **Status indicator (if applicable)** — A clear signal of the item's current state (active, pending, completed, archived). Colour-blind users cannot distinguish status by colour alone, so include a text label.
- **Key details section** — The most important attributes surfaced prominently, with secondary details below or in a sidebar. Hierarchy here is critical.
- **Edit action** — A clear way to modify the item's details, either inline or via an edit mode.
- **Related items or activity** — Associated records, linked content, or a change history. An activity log of who did what and when is highly valued in collaborative products.
- **Breadcrumb or back navigation** — A way to return to the list or parent context.
- **Destructive actions** — Delete or archive options available on the detail screen but kept visually separate from primary actions.

## 19. Admin Panel
Where administrators manage users, configure the product, and oversee activity across the organisation.
- **Role-based access** — The admin panel visible and accessible only to users with the appropriate permissions.
- **User management** — A view of all users with the ability to invite, edit roles, and remove members.
- **Organisation settings** — Controls for configuring the product at an account level — name, logo, SSO, domains.
- **Usage overview** — High-level metrics on how the product is being used, with the ability to export for reporting.
- **Billing and plan management** — Access to subscription details, seat counts, and invoices at the account level.
- **Audit log** — A record of account-related actions taken by users (logins, permission changes, deletions).
- **Danger zone** — Destructive account-level actions (deleting the workspace, transferring ownership). Establish friction with visual separation and typed confirmation for irreversible actions.

## 20. User Management
A screen allowing admins to view, invite, and manage the users with access to a product or workspace.
- **User list** — A table of all users showing name, email, role, and account status. Activity information helps spotlight inactive users.
- **Invite user action** — A clear way to add members by email, with an option to set their role before sending. A bulk invite action is valuable and a common way to transfer a company user base.
- **Roles and permissions** — The ability to assign and change what each user can see and do. Use universal terms (admin, member, viewer) rather than custom titles.
- **Pending invitation status** — A view of invitations sent but not yet accepted, with the option to resend or revoke.
- **Search and filter** — The ability to find users quickly by name, email, role, or other applicable information.
- **Remove or deactivate user** — A clear way to revoke access, with a distinction between temporary deactivation and permanent removal.

## 21. Account
Where users view and manage their personal information, preferences, and account-level details.
- **Profile photo** — A way to upload or change the profile image. Consider a sensible fallback like initials or a placeholder icon for users who have not uploaded one.
- **Display name** — The name shown to other users or across the product interface (username, email, first and last name). Clarify whether this is a public-facing name or an internal account label.
- **Account details** — Fields for email, phone, job title, or other identifying information. If extensive, group them (contact information, job history).
- **Linked accounts (if applicable)** — A view of which third-party accounts are connected for sign-in or data access, with the ability to disconnect.
- **Save confirmation** — Clear feedback that changes have been saved, inline or as a toast. Auto-save with subtle confirmation is more pleasant; an explicit save button should remain disabled until there are changes.
- **Delete or deactivate account** — Options to deactivate or permanently delete, clearly separated from other settings.

## 22. Public Profile
The view of a user that other people in the product see, distinct from the private, editable account settings profile.
- **Avatar and display name** — The user's photo and name shown prominently as the primary identifier. A fallback avatar using initials is better than a blank space.
- **Role or title** — The user's job title, team, or role within the product context, where relevant.
- **Bio or description** — A short free-text description the user wrote about themselves.
- **Activity or contributions** — A summary of what the user has done in the product (posts, projects, comments, or other public actions). Surfacing activity the user has not opted in to show is a privacy violation.
- **Contact or follow action** — A way to initiate contact, follow, or connect, depending on what the product supports.
- **Joined date (optional)** — When the user joined the product.
- **Profile visibility controls** — Which profile fields are visible according to the user's own privacy preferences.

## 23. Settings
A screen giving users control over their account, preferences, and application behaviour.
- **Structure** — Organising controls into logical categories (account, notifications, security, billing). Consider elevating the most commonly changed settings rather than the most important.
- **Account details** — Fields where users update their name, email address, and profile photo.
- **Security details** — The ability to change the password, two-factor authentication, and other security information. These fields should require re-authentication to save changes.
- **Notification preferences** — Controls for which notifications the user receives and through which channel, grouped by type. Grouping reduces the chance of a user disabling all notifications rather than some.
- **Billing** — Managing payment method, upgrading, or cancelling. This can be a preview with a link directly to the billing page if separate.
- **Additional preferences (if applicable)** — Language, timezone, date format, and appearance settings like dark mode.
- **Danger zone** — Destructive actions like account deletion, clearly separated. Include a confirmation step with details on what will be lost.

## 24. API Keys
A screen where users generate and manage API keys and other developer-facing credentials.
- **Key list** — A table of all existing keys showing name, creation date, last used date, and permissions. Only show the last few characters after creation for identification without revealing the entire key.
- **Generate key** — A clear way to create a new key, with the option to name it and set scope or permissions. Requiring a name before generation is useful, as unnamed keys become impossible to manage.
- **Copy key on creation** — The full key revealed exactly once immediately after creation, with a prominent copy button. Users must be explicitly told this is the only time the key will be shown in full.
- **Key permissions or scopes** — The ability to limit what each key can access (read-only, specific resources, full access). Least-privilege is a security best practice; when fine-grained scopes are easier to set, more users choose them.
- **Revoke key** — A clear way to immediately invalidate a key, with a confirmation step. Revocation is instant and irreversible, so the confirmation must communicate this clearly.
- **Documentation link** — A direct link to API documentation so developers can start without searching for it.

## 25. Integrations
A screen showing the third-party tools and services a product can connect with, allowing users to link existing workflows.
- **Catalogue** — A browsable list or grid of all available integrations with logos, names, and a brief description. Group into installed and not installed after the first successful connection.
- **Categories or filtering** — Browse integrations by category to narrow a large catalogue (productivity, communication, analytics, CRM).
- **Search** — A search field to find a specific integration by name without scrolling the full list.
- **Connection status** — A clear indicator on each integration showing connected, disconnected, or connected with an issue. Pair a dot with a label if you want to be explicit.
- **Connect and disconnect actions** — A clear way to initiate or remove a connection, with a confirmation step before disconnecting. Include what will stop working in the confirmation.
- **Integration detail** — A dedicated view showing what data it accesses, configuration options, and a sync or activity log.
- **Request an integration** — A way for users to suggest tools they would like supported. This doubles as a lightweight research tool for where to invest next.

## 26. Version History
A screen outlining different versions of an item or experience that can be navigated between.
- **Version timeline** — A list of saved versions in reverse chronological order, each labelled with a timestamp and the user who saved it.
- **Named versions** — The ability to give a version a name (milestone, submission date, phase label) so it is findable without scrolling timestamps. Named versions are what users navigate by; autosave versions are for recovery.
- **Version preview** — A read-only preview of any past version, visible without committing to a restore.
- **Diff or change summary** — A visual indication of what changed between two versions (added, removed, modified). A diff view reduces the time to evaluate which version to restore.
- **Restore action** — A clear way to make a past version current, with a confirmation step setting expectations about the current content.
- **Autosave indicator** — A persistent, subtle indicator of when the document was last saved automatically, visible without being disruptive.

## 27. Audit Log
A screen providing a chronological record of significant actions taken within a product: who did what, and when.
- **Event list** — A table of logged events showing the action performed, the user who performed it, and a timestamp. Recent-first is the natural default for admins investigating.
- **Actor identification** — The name and identifier of the user who triggered each event, including system-generated actions. Log the user ID alongside the name, since display names change.
- **Event type** — A categorised label for what kind of action was taken (login, permission change, deletion, export).
- **Affected resource** — The specific record, file, or setting changed, and what was changed. Linking to the affected resource lets admins investigate in context.
- **Date range filter** — The ability to narrow the log to a specific time period.
- **Search and filter** — Filter by user, event type, or affected resource.
- **Export** — The ability to download the audit log as CSV for compliance reporting or external review.

## 28. Document View
A rich content view for reading, editing, and collaborating on structured documents.
- **Document title and metadata** — Name, owner, and last-modified details at the top. An editable inline title is the expected pattern; requiring a separate settings screen to rename is a common frustration.
- **Table of contents** — A navigable outline from the document's headings. A TOC that requires scrolling back to the top defeats its purpose — sticky or floating placement is what makes it useful.
- **Rich text with inline media** — Formatted text, images, embeds, and other content types within the body. How gracefully paste handles Word or Google Docs imports determines the cleanup work users face.
- **View and edit mode distinction** — A clear difference between reading and editing. Accidental edits are a major frustration; a clear mode switch prevents unintentional content changes.
- **Version history or change tracking** — A log of previous versions with restore or compare. Even basic "last 10 versions" history is enormously valuable for user trust.
- **Auto-save and last-saved indicator** — Changes saved automatically with a visible timestamp. "Saving... → Saved 3 seconds ago" is the gold standard.
- **Inline comments or annotations** — Comments on specific sections or text selections. Threading keeps conversations self-contained and the document readable.
- **Share and permission controls** — Share the document and control view or edit access. A document shared with the whole organisation looks identical to a private one without a persistent sharing state indicator — that ambiguity causes accidental data exposure.

## 29. Billing
Payment methods, invoices, and everything related to the financial side of the account.
- **Payment method on file** — The current card or payment method linked to the account, shown with masked details. The last 4 digits are enough to identify the card without exposing sensitive information.
- **Add or update payment method action** — A way to enter a new card or change the current one.
- **Next billing date and amount** — When the next payment will be taken and for how much, including the plan name alongside the amount.
- **Invoices and receipts** — A list of past charges with the ability to download a PDF invoice for each. Invoices must include company name, address, and VAT number — legally required in many countries.
- **Tax and VAT (if applicable)** — Applicable tax or VAT shown on invoices and billing history.
- **Failed payment recovery** — Clear messaging and recovery instructions when a payment attempt fails. Surface this prominently, as it can eventually restrict access if unresolved.
- **Billing contact email** — The email address where invoices and billing notifications are sent. For larger teams this is often different from the account owner's email.

## 30. Checkout
The screen where users review their order and complete a purchase — one of the highest-stakes screens in any transactional product.
- **Order summary** — A clear breakdown of what is being purchased (item names, quantities, prices). Visible throughout checkout, since users should not have to navigate back to check what they are buying.
- **Total cost** — The final amount, including taxes, fees, or discounts. Unexpected costs revealed at the last step are the leading cause of cart abandonment.
- **Payment method** — Fields or options for payment details (card, PayPal, Apple Pay, others). Express checkout options like Apple Pay and Google Pay offered prominently significantly increase conversion.
- **Billing and shipping address** — Fields to enter or confirm both addresses. Billing defaulting to match shipping, with an option to uncheck if different, saves unnecessary typing.
- **Promo code** — A field to apply a discount code, positioned visibly within the order summary.
- **Security indicators** — Visual signals that the transaction is secure (lock icons, SSL badges, recognised payment logos), suited to sit near the payment fields.
- **Confirmation step** — A final review before the payment is submitted, giving users a chance to check before committing.

## 31. Pricing
A pricing page breaking down costs, features, and options for paying to access the product.
- **Plan names, prices and frequency** — The name and cost of each plan, with billing frequency clearly stated.
- **Billing period toggle** — A switch between monthly and annual billing, with the annual discount shown if applicable.
- **Feature comparison (if price options)** — A side-by-side breakdown of what each plan includes and excludes.
- **Call to action** — A button on each plan to start a trial, subscribe, or contact sales.
- **Free tier or trial details** — What is included, how long it lasts, and what happens when it ends. State clearly whether the account downgrades or charges automatically once the trial ends.
- **FAQ section** — Answers to the most common questions about billing, plan limits, cancellation, and payment.
- **Enterprise option** — A prompt for organisations needing a custom arrangement beyond the standard plans.

## 32. Upgrade
The dedicated page a user lands on when they have decided to subscribe or move to a higher plan.
- **Current vs. target plan** — A comparison of the user's current plan and the target tier, making the difference in value explicit. Side-by-side is more effective than listing only the new plan.
- **Feature highlights** — The three to five most compelling features that come with the upgraded plan. Features most relevant to the user's existing usage convert better than a generic list.
- **Billing period toggle** — A toggle between monthly and annual billing, with the price updating accordingly. Defaulting to the annual price sets a lower monthly anchor.
- **Trust signals** — Reassurances like "cancel anytime", SSL badges, and accepted payment logos. "Cancel anytime" belongs near the primary CTA, not the footer, since it addresses the most common objection at the moment of decision.
- **Primary CTA** — The main action ("Upgrade now" or "Start free trial") visible without scrolling. If a trial is available, it should be the primary CTA — lower commitment converts better. One CTA is better than two.
- **Objection handling** — Answers to the most common questions or hesitations. At minimum: what happens at the end of a trial, whether it auto-renews, and how to cancel.
- **Transparent pricing** — The price shown matching exactly what appears at checkout. Any surprise at the payment step causes significant abandonment.

## 33. Maintenance
A screen shown when the application is temporarily unavailable due to scheduled maintenance or an unexpected outage.
- **Clear status message** — A plain-language explanation that the product is unavailable and why. Scheduled maintenance and unexpected outages need different messaging; conflating them feels evasive.
- **Estimated return time** — When the product is expected back, as specifically as possible. Vague messages like "back soon" frustrate users; even "within 2 hours" is more reassuring.
- **Status page link** — A link to a live status page where users can monitor progress and see real-time updates. A status page on a separate domain remains accessible when the main infrastructure is down.
- **Contact or support link** — A way to reach support for urgent issues that cannot wait for the window to end.
- **Brand consistency** — A maintenance page styled consistently with the product, even if content is minimal. A well-designed maintenance page reduces user anxiety.

## 34. 2FA
A screen that guides users through setting up or completing two-factor authentication to add a second layer of security.
- **Method selection** — Authenticator app, SMS, or email code. Offer at least 2 methods, since some users do not have access to one or the other.
- **Setup instructions** — Clear step-by-step guidance, particularly for authenticator flows requiring a QR code scan.
- **QR code or setup key** — A scannable QR code or copyable key for linking an authenticator app. Ensure the QR code size is large enough to be easy to scan.
- **Verification step** — A code entry step confirming the setup was successful before 2FA is enabled. Enabling without this risks a silent setup failure that locks the user out.
- **Recovery codes** — A set of one-time backup codes for use if the user loses access to their 2FA method. Make download or copying a required step before completing setup.
- **Setup confirmation** — A clear success state confirming 2FA is now active on the account.
- **Disable or reset option** — A way to turn off or reconfigure 2FA from account security settings. Re-authentication should be required before disabling.

## 35. Login
A login page — the gateway for users to access personalised features, secure content, and their own data.
- **Email and password fields** — The two standard authentication inputs. Pre-filling the email after a failed login so the user only re-enters the password reduces friction.
- **Show/hide password toggle** — A button alongside the password field that reveals or conceals what has been typed.
- **Forgot password** — A link that begins the password reset flow for users who cannot remember their credentials.
- **Remember me** — A checkbox that persists the user's session across browser closures.
- **SSO or social login** — Alternative authentication via a third-party identity provider (Google, Microsoft, GitHub) that bypasses the email/password form.
- **Sign up link** — A link to account creation for users who do not yet have an account.
- **Error messages** — Feedback shown when authentication fails, indicating what the user should try next.

## 36. Help Center
A self-serve documentation hub where users find answers without contacting support.
- **Search with suggestions** — A prominent search input returning relevant articles as the user types. Autocomplete increases the chance of finding an answer quicker.
- **Content categories** — A hierarchy of topics for browsing when users are unsure what to search. Categories should reflect how users think about the product, not internal team structure.
- **Featured and popular content** — The most-viewed or most-useful articles surfaced on the homepage. Ensure featured content does not stay stale as features change.
- **Article formatting** — Proper heading hierarchy, screenshots, and formatted code blocks where relevant. Screenshots become outdated after redesigns, so a regular review process is critical.
- **Last updated date** — The date each article was last reviewed or edited, shown at the top. A recent date reassures the user the content is current and valid to follow.
- **Helpfulness feedback** — A simple thumbs up/down or yes/no at the end of each article to identify content that needs reconsidering.
- **Related articles** — Links to similar or adjacent articles that might answer follow-up questions.

## 37. Kanban board
A visual board organising items into columns representing stages or statuses, tracking work through a workflow.
- **Columns** — Distinct vertical lanes for each workflow stage (To Do, In Progress, Done, or custom). Adding, renaming, and reordering columns must be available, since every team structures its workflow differently.
- **Cards** — Individual items showing title and key metadata. Title, assignee, and due date on the card face covers most use cases without cluttering.
- **Drag and drop** — Moving cards between columns and reordering within a column. A visual drop target is required; without it, users are never sure where the card will land.
- **Quick add card** — A fast way to create a new card directly within a column without opening a full form.
- **Card detail on click** — Clicking a card opens full detail (description, comments, attachments, history) without leaving the board. Use a side panel or modal rather than navigating away — losing board context frustrates users.
- **Column item count** — A count of cards in each column, visible in the column header. Useful for conversations and tracking without counting individually.
- **Filtering, sorting and grouping** — Re-organising cards by assignee, label, priority, or due date to focus on a subset of work.

## 38. Timeline / Gantt View
A screen displaying tasks, milestones, or events along a horizontal time axis, used in project management to show schedules and dependencies.
- **Time axis** — A horizontal axis representing time, with clear date markers (days, weeks, or months by zoom level). A single timescale rarely fits all project sizes; zoom controls let users shift between day, week, and month views.
- **Task bars** — Horizontal bars for each task or milestone positioned by start and end dates. Colouring bars by status, assignee, or category makes patterns visible at a glance.
- **Dependencies** — Visual connectors between tasks that must complete in sequence, showing which items are blocked. Dependency lines can overwhelm a busy timeline, so show them on hover or when a task is selected.
- **Today indicator** — A vertical line marking the current date so users immediately see what is on track and what is overdue.
- **Milestones** — Distinct markers for key dates or deliverables that are not duration-based tasks.
- **Drag to reschedule** — Moving or resizing task bars by dragging to update dates directly on the timeline. A date tooltip while dragging gives precise feedback on new start and end dates.
- **Row grouping** — The ability to organise tasks by assignee, team, project phase, or another dimension.
