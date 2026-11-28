# Mobile App Checklists (checklist.design — Mobile)

28 checklists. Source: https://www.checklist.design/mobile. Every item is a required test for the mobile screen or pattern.

## 1. Push Notif. Opt-in
The custom screen shown before the system notification prompt to persuade a user to accept push notifications.
- **Value proposition** — A specific explanation of what the notifications will contain and why they are worth receiving.
- **Notification preview** — A realistic visual mock of what a notification looks like (title, body, app icon). A genuine-looking sample rather than a generic illustration significantly helps.
- **Opt-in timing** — The point in the flow at which the opt-in is presented, after the user has experienced enough value to understand what they are opting into. Presenting a push opt-in before any meaningful action is the fastest way to get a denial.
- **Decline path** — A clear dismiss option that does not penalise the user or block progress.
- **Re-engagement path** — For users who decline, a way to revisit the opt-in later (typically surfaced in settings).
- **One screen, one ask** — A single, focused screen making one case for one permission.

## 2. Gesture navigation
The touch-based interaction patterns that let users navigate and act without tapping buttons.
- **Swipe to go back** — The standard action to go back without tapping a button. This can be disabled on screens where a horizontal swipe exists, to avoid a conflict.
- **List item swipe actions** — Revealing quick actions such as delete, archive, mark as read on an item without opening it. Suitable only if there are 2–3 actions available; any more may be too significant a space loss.
- **Pull to refresh** — For scrollable content lists, with a visible indicator and haptic confirmation when triggered.
- **Long press menus** — Triggered by long pressing, revealing actions relevant to that specific element. These are for quick actions, and the action should exist elsewhere in a more accessible way in the app.
- **Pinch to zoom** — Image and map content supporting standard pinch-to-zoom, with the zoom level reset logically on navigation away.
- **Drag to reorder** — Lists or cards that can be reordered supporting long-press-to-lift and drag, with clear visual feedback during the drag state.
- **Gesture hints** — A subtle animation or tooltip on first encounter with a key gesture, hinting at its existence. If the gesture is significant, the hint could persist until the user tries the action.
- **Haptic feedback** — Beneficial for key gesture moments where the finger may cover the screen and it is unclear whether the gesture was engaged (pull-to-refresh, long press, drag).

## 3. Splash Screen
The first screen a user sees when launching the app, before it initialises and transitions to the home screen.
- **Logo or wordmark** — The app brand mark centred on a clean background.
- **Brand background** — A solid or subtly branded background making the transition from the mobile home screen clear.
- **Launch duration** — The splash visible only for as long as the app genuinely needs to initialise (not used as decorative padding).
- **Transition to first screen** — A smooth, intentional animation into the first real screen, ideally not a hard cut or jarring flash.
- **No interactive elements** — The splash screen contains no buttons, inputs, or tappable areas; it is purely for transition.
- **Loading indicator** — For any initialisation taking more than a second, so the user knows something is happening. This could be the logo, wordmark, or illustration used as the key visual in a looping animation.

## 4. Checkout
The payment flow on mobile optimised for native payment methods and small-screen constraints.
- **Native payment methods** — Apple Pay and Google Pay as primary checkout options, completing the purchase with a single biometric tap. Still offer manual card entry if users will be concerned about third-party tool usage.
- **Persistent order summary** — The item list, quantities, and total available throughout the flow — persistently visible or accessible with a single tap.
- **Minimal form fields** — Only the fields genuinely required to complete the purchase (card details, delivery address).
- **Autofill capabilities** — Shipping address fields supporting iOS and Android autofill, removing the need to type a full address manually.
- **Keyboard types per field** — Appropriate keyboard types throughout (numeric for card numbers and CVV, date or numeric pad for expiry).
- **Checkout progress** — A clear step indicator for a multi-step experience, e.g. separate Details, Payment, and Checkout pages.
- **Error recovery** — The experience after a payment failure, returning to the payment step with all previously entered data intact and a clear explanation of the reason.
- **Order/payment confirmation** — A clear confirmation screen with summary, payment method, and amount, plus other relevant information such as expected arrival date for physical delivery. It is common to email an invoice; remind the user of that so they know they do not have to keep the page open.

## 5. Tab Bar Navigation
The persistent bottom navigation bar giving access to the top-level sections of the app.
- **Tab count** — Limited to the most important destinations — 3 to 5 items is the typical range. More than 5 dilutes each option and may not fit.
- **Icon and label** — Each tab paired with both an icon and a text label. Labels may not be necessary only if the icons are explicitly clear about what lies within that section.
- **Active and default states** — The active tab should be visually distinct, whether by colour, border, or icon weight.
- **Badge counts** — Useful for tabs with unread counts like messages and notifications, updating in real time. Instead of a number, a dot is suitable if numbers feel less relevant.
- **Fixed presence** — For the sections the tab bar applies to, it should remain visible, and can be hidden on any page a level deeper.
- **Tap target size** — Each tab at least 44×44pt to be reliably tappable with a thumb in any grip position.
- **Haptic feedback** — A subtle tap haptic on tab selection confirming the action.

## 6. In-App Notifications
The in-app feed of alerts, updates, and messages received — distinct from system push notifications.
- **Reverse chronological order** — Newest notifications at the top so users do not have to scroll for the latest.
- **Unread indicators** — Unread notifications visually distinct from read ones, e.g. a dot, bolder text, or background colour difference.
- **Mark all as read** — A single action to clear all unread indicators at once. Essential for apps with many notifications or where the user is likely to be away for a long time.
- **Notification grouping** — Related notifications grouped together, e.g. multiple comments on the same post shown as a single expandable item rather than separate rows. Best applied to high-activity content.
- **Swipe to dismiss action** — Individual notifications dismissible by swiping left, revealing a delete action.
- **Deep link on tap** — Tapping a notification navigating directly to the relevant content.
- **Empty state** — For when there are no notifications, to indicate they have not received any… yet.
- **Settings shortcut** — A direct link from the notifications screen to notification preferences.
- **Notification content** — Information relevant to triggering the notification, e.g. the change, author, and time it occurred.

## 7. Action Sheet
The sheet that slides up from the bottom of the screen to present options or confirmations — the mobile equivalent of a dropdown menu or modal dialog.
- **Heading and actions** — As with modals, there must be a clear heading outlining the purpose of the action sheet, along with relevant actions the user can select.
- **Swipe or backdrop dismiss** — The sheet dismissible by dragging it down or tapping the dimmed area behind it, along with the expected close button.
- **Destructive action styling** — Any destructive option (delete, remove, block) styled in red and positioned last, separated from safe actions. Users scan top-to-bottom and tap quickly; a destructive action buried at the bottom prevents accidental taps.
- **Cancel action** — A clearly labelled cancel/close option that dismisses the sheet without taking any action. Typically the secondary action, similar to a desktop modal.
- **Snap points (if expandable)** — Defining where the action sheet expands or compresses on resize, instead of being free-form. A drag handle at the top indicates the sheet can be expanded (or dismissed).
- **Content scrollability** — Consider what sticks as you scroll so the sheet remains contextual and stays fixed in position. Similar to modals, avoid scrollability here unless unavoidable.
- **Keyboard relation** — Consider the action sheet size and responsiveness if the keyboard needs to be triggered while it is active.
- **Backdrop dimming** — The screen behind darkened to draw focus to the action sheet.

## 8. Billing
Payment history, receipts, and everything related to how the user is charged.
- **Manage via App Store** — A link or prompt directing users to the App Store or Play Store to manage their subscription. Apple and Google require subscription management through their platform; a buried path there is a consistent source of support contacts and poor reviews.
- **Next billing date and amount** — The next scheduled payment date and amount visible without digging into billing history. Surfacing this proactively reduces cancellations driven by surprise charges.
- **Billing history and receipts** — A list of past charges with amounts and dates, with individual receipts accessible. Particularly important for users paying with a work card, who often need receipts for expense reporting.
- **Restore purchases** — A button to restore previously purchased subscriptions or in-app purchases after reinstalling or signing in on a new device. Required by Apple for apps with in-app purchases.
- **Refund help link** — Guidance on how to request a refund, typically via the platform's own process. Refunds are handled by Apple or Google, not the app directly; making this clear reduces confusion and support volume.
- **Tax display** — Tax or VAT amounts displayed separately from the base price where legally required.

## 9. Search
The search experience on mobile, where keyboard handling and filtering results are unique to web.
- **Sticky search bar** — The search input fixed at the top of the screen as results scroll beneath it. A search bar that scrolls away forces users to scroll back up to refine the query.
- **Keyboard auto-focus** — The keyboard opens immediately when the user navigates to the search screen — no extra tap required to start typing.
- **Live results** — Results updating as the user types rather than requiring a submit tap.
- **Recent searches** — Previously searched terms shown before the user starts typing, for convenience in revisiting results.
- **Filter bottom sheet** — Filtering accessed via a bottom sheet rather than a separate screen, keeping search context visible while adjusting. A full-screen filter page can be better if filtering is extensive, e.g. a retail store or booking system.
- **Skeleton loading** — Skeleton cards in the expected result shape shown while results load as the user types.
- **No results state** — A helpful empty state with suggestions, e.g. checking spelling, removing filters, or trying related terms.
- **Clear query button** — An action inside or near the search field to clear the current query with one tap.

## 10. Camera
Capturing photos, video, or documents, and reviewing and customising the capture experience.
- **Permission request** — Camera permission requested at the moment capture is triggered, not on app launch or during onboarding. Asking earlier without context of camera usage does not feel trustworthy.
- **Viewfinder and capture button** — A full-screen viewfinder with a clearly positioned, large capture button. The button should be reachable by thumb at the bottom of the screen.
- **Flash controls** — Flash toggle accessible without leaving the capture screen, with auto, on, and off states clearly indicated.
- **Camera flip** — A clear camera flip button accessible during capture, positioned so it is not accidentally triggered during shooting.
- **Post-capture preview** — A preview shown after capturing, giving the user the chance to retake or confirm before the media is used.
- **Gallery picker of captures** — The option to open a photo library containing only photos captured within that series until exiting the camera.

## 11. Map View
The native map screen showing location-based content, user position, and contextual overlays.
- **Pin and marker designs** — Custom markers clearly distinguishable from each other and from the base map, sized for reliable tap accuracy. Ensure the marker design for the current location is the most prominent, as all map view interactions are centred around it.
- **Marker clustering (if applicable)** — How markers are shown when a group is so close together they cannot be shown individually and must be grouped.
- **Native map components** — Leverage MapKit for iOS or Google Maps for Android to utilise existing foundations and layout that is time-consuming to create from scratch.
- **Location permission** — The point in the flow at which location permission is requested, with context explaining the level of access needed and why. Consider the UI if permissions are denied, providing instructions on changing the permission in settings.
- **Current location re-centre** — A clearly visible button to re-centre the map to the user's current position without zooming or scrolling to it.
- **Selected item bottom sheet** — Tapping a marker expanding a bottom sheet with details about that location, not a full-screen navigation away from the map.
- **Search or filter actions** — Search or filter controls accessible as a persistent overlay on the map or as a separate screen. When filters are on the map, the applied filters should be visible for context.
- **Offline handling** — When offline, cached map tiles displayed where available, with a clear indicator that the map may not be current.

## 12. Onboarding Checklist
The in-app progress checklist guiding a new user through key setup steps by completing actions.
- **Card or sheet presentation** — The checklist presented as a dismissible bottom sheet or a persistent card on the home screen, not a full-screen overlay.
- **Task count and progress** — A visible count of completed versus total tasks and a progress bar or ring that updates as steps are completed.
- **Tap to start each task** — Each checklist item tappable, navigating directly to the relevant screen or feature, not just informational.
- **Completion celebration** — When all tasks are complete, show a brief celebratory moment before the checklist disappears (animation, confetti, congratulatory message).
- **Dismissible action** — The checklist is dismissible for users who do not want it, not a forced guided path.
- **Persistent but unobtrusive** — The checklist is accessible from a consistent location (dashboard, profile, home).
- **Personalised to user type (if applicable)** — If there are different user types or ways to use the app, include onboarding questions that direct to tailored steps so the checklist feels personal.

## 13. Paywall
A hard gate that blocks access to locked content and offers a path to subscribe.
- **Locked feature context and breakdown** — A clear statement or short list of which specific feature(s) the user is being blocked from accessing.
- **Upgrade CTA** — The primary action to start a subscription or free trial, positioned prominently. Be specific about what is unlocked, e.g. "Unlock unlimited projects" or "Access full library".
- **Free trial offer** — A clear statement of any trial period available before subscription billing begins. "Try free for 7 days" framed as low-commitment is consistently one of the highest-converting messages on a paywall.
- **Dismiss action** — A clear, neutral way to close the paywall and return to the free experience. This should be obvious and accessible.
- **Restore purchases** — A way for existing subscribers to recover access after reinstalling or signing in on a new device.
- **No guilt language** — Dismiss and decline actions written in neutral language, without shaming or pressuring users into subscribing. "No thanks, I don't want to save money" is manipulative and unnecessary.

## 14. Onboarding
The first-run experience that orients a new user, collects necessary setup information, and delivers an early sense of the app's value.
- **Steps** — The number of steps, limited to what is genuinely required before the app can be used. Steps that can be deferred without preventing day-one use belong later, not in onboarding.
- **Progress indicator** — A clear indication of how many steps remain and where the user currently is. Users who can see the end of onboarding are significantly less likely to abandon it.
- **Step navigation** — A clear mechanism for advancing, e.g. a "next" button or a horizontal swipe gesture.
- **Contextual permissions** — Permissions surfaced at their contextually relevant moment within onboarding, rather than grouped at the start. Grouping all permission requests at the beginning can lead to denials given the lack of context.
- **Skip option** — A visible way to exit early and explore the app, with setup available to complete later. Users who skip and explore freely often complete setup voluntarily once they understand the value.
- **Personalisation step** — One or two choices that make the app feel tailored from the start, e.g. name, interests, or a key piece of information applying to the product.
- **Keyboard handling** — Views that adjust correctly when the keyboard appears, appropriate keyboard types per field, and Next advancing to the following input.

## 15. Dashboard
A glanceable summary of what matters most in an app experience, typically with leads to other specific areas.
- **Thumb-zone layout** — Primary actions and key content placed in the lower two-thirds of the screen where thumbs naturally reach. The top quarter of a phone is largely unreachable for one-handed use, so interactive elements placed there are routinely missed.
- **Widget-based structure** — Content organised into discrete, scannable cards or widgets rather than long scrolling sections. A dashboard answering ten questions at once answers none well; each card works best focused on a single thing.
- **Pull to refresh** — Dragging down refreshes the dashboard data, with a visible indicator and haptic on trigger.
- **Glanceable metrics** — The most important numbers or status indicators visible without any interaction.
- **Quick actions** — The most common tasks accessible directly from the dashboard without navigating to another screen. The action users take most frequently after opening the app is what the quick actions should surface — rarely the action the team assumed.
- **Personalised content** — Where applicable, content and order reflecting the user's history, preferences, or role.
- **Per-widget states** — Each widget handling its own loading skeleton and empty state; the dashboard never partially loads in a confusing way.
- **Notification surface** — Time-sensitive alerts or action items surfaced on the dashboard so users do not hunt for what requires attention.

## 16. Profile
The public-facing identity of a user that others see when they look them up — not the account.
- **Profile photo** — An option to set an avatar image, either from the camera roll or by taking a new photo. Offering both options and including a crop step covers the common case where camera photos are not framed for a circular avatar.
- **Display name and/or username** — The name shown publicly and the handle used to identify the account in @mentions or search. If both are editable, make clear which is visible to others and which is used as an identifier.
- **Bio** — A short text field where users describe themselves or their work. Show a character limit counter as the user approaches it, preventing a hard cutoff from feeling unexpected.
- **Public fields only** — The screen contains only information visible to other users; private account settings live on a separate screen.
- **Profile preview** — A read-only view of how the profile will appear to other users, available before saving.
- **External links (if relevant)** — Optional fields for linking to a website, portfolio, or other social accounts.

## 17. Chat
The one-to-one or group messaging screen, handling keyboard behaviour, message input, media sharing, and real-time updates on a mobile screen.
- **Keyboard push-up** — The message input bar rising with the keyboard when it opens, so conversation history is not obscured. The behaviour differs between iOS and Android, so explicit handling on both platforms prevents the common bug of the keyboard obscuring the input bar.
- **Input bar** — A persistent input bar at the bottom containing a text field, send button, and media attachment option, thumb-reachable in all grip positions.
- **Message bubbles** — Sent messages on the right, received on the left, consistent with messaging conventions. Breaking the sent-right received-left convention for a design reason is rarely worth the disorientation.
- **Swipe to reply** — Swiping a message right revealing a reply-to action, threading the response to the specific message.
- **Long press message actions** — Long pressing a message opening a reaction picker and action menu, e.g. react, reply, copy, delete.
- **Read receipts** — Sent message status shown as subtle indicators below or within the bubble (sent, delivered, read).
- **Media and file sharing** — Images, videos, and files shareable directly from the input bar, with inline previews in the conversation thread.
- **Typing indicator** — An animated indicator when the other party is composing.
- **Scroll to latest** — When new messages arrive while the user is scrolled up, a button to jump to the latest message.

## 18. Settings
The screen where users manage their account, preferences, notifications, and app behaviour.
- **Grouped table layout** — Settings organised into clearly labelled sections (Account, Notifications, Privacy, Support) using the native grouped list pattern. Grouped settings are a platform convention users have deeply internalised; deviating forces users to relearn navigation they already know.
- **Native toggle controls** — Binary settings presented with the platform-native toggle switch (UISwitch on iOS, Material Switch on Android). Custom toggles that look slightly off create subtle distrust, since the difference is small but users notice it.
- **Destructive actions grouped** — Log out, delete account, and other irreversible actions in their own section at the bottom, visually distinguished in red.
- **Account details at top** — The user's avatar, name, and email shown prominently at the top, a clear anchor for whose account is being managed.
- **Deep link to specific settings** — A direct link from relevant in-app prompts to the specific settings screen they reference. Telling users where to find a setting is far less effective than linking them there directly.
- **Support and feedback access** — A clear path to contact support, submit feedback, or access help documentation, accessible from within settings.
- **App version** — The current app version shown at the bottom — essential for support conversations and identifying build-specific issues.
- **Legal links** — Links to the Privacy Policy and Terms of Service accessible within settings, as required by app stores.

## 19. In-App Browser
A browser experience inside a mobile app, handy for opening web links or accessing web data via API.
- **URL bar visibility** — The URL of the current page visible to the user, confirming the domain before they interact with any forms or enter credentials. Users who cannot see the URL cannot verify they are on a legitimate domain — URL visibility is a security baseline.
- **Close action** — A clear, persistent button for closing the browser and returning to the app (typically in a fixed toolbar rather than hidden behind a gesture).
- **Open in external default browser action** — An option to open the URL in the user's default browser, while preserving the in-app browser experience still.
- **Share action** — Allowing the URL to be shared without opening the default browser.
- **Loading feedback** — A progress indicator while the page loads (a top progress bar or an activity indicator) so the user knows the browser is working.

## 20. Cart
- **Item list** — Each item shown with its image, name, selected variants, and quantity.
- **Quantity stepper** — Plus and minus controls for adjusting quantity inline, large enough to tap accurately without zooming.
- **Swipe to remove** — A swipe-left gesture on a cart item revealing a remove action.
- **Price breakdown** — Subtotal, applied discounts, estimated tax, and total shown before the checkout action. If prices will change after the cart, e.g. a delivery fee, specify that it will be shown later.
- **Empty cart state** — The state shown when no items are in the cart, with a clear prompt to continue browsing.
- **Promo code field** — The ability to enter the code and see the discount across items and the total. Can also be visible at checkout, but users may want to see the discounts here first.

## 21. Login
Everything a returning user needs to authenticate quickly and securely.
- **Social sign-in** — Sign-in options connecting to an existing Apple or Google account, bypassing manual credential entry. On iOS, Apple Sign In is required by App Store guidelines if any other social provider is offered.
- **Email field** — The input where users enter the email address associated with their account.
- **Password field** — A masked text input for the account password, with the option to reveal what has been typed.
- **Biometric authentication** — Face ID or fingerprint sign-in for returning users who have already authenticated once with a password. Encouraged to suggest after initial login so it is faster in the future.
- **Credential autofill** — System-level support for pre-filling saved email and password from the user's password manager. `textContentType` on iOS and `autoComplete` on Android are the attributes that trigger native autofill.
- **Forgot password link** — The link users reach for when they can't recall their password, leading into the reset flow.
- **Error states** — Feedback shown when authentication fails, distinguishing between an unrecognised email address and an incorrect password. Generic "incorrect credentials" gives no useful signal; knowing which is wrong helps users recover without guessing.
- **Passwordless sign-in (magic link)** — An alternative sending a one-time link to the user's email, requiring no password. Useful for infrequent-use apps where remembering a password between sessions is difficult.

## 22. Sign up
A low-friction registration flow collecting only what is needed and setting a positive first impression.
- **Third party sign-up** — Account creation through an existing Apple, Google, or social media account, removing the need to set a password.
- **Required fields** — The minimum information needed to create an account (typically email and password, if not social auth). Every additional field reduces completion rate.
- **Password strength** — Visual feedback showing how secure the chosen password is as the user types. Showing requirements inline (not only on a submission error) lets users meet them before submitting.
- **Terms and privacy** — The acknowledgement that the user accepts the terms of service and privacy policy before creating an account.
- **Email verification** — The step asking users to confirm their email address after the account has been created. It is common to allow access to the product before confirming, so users are not blocked and drop off.
- **Welcome state** — The screen shown immediately after account creation, confirming success and pointing toward the first action.
- **Already have an account** — A link for returning users who arrived at the sign-up screen instead of login.
- **Marketing opt-in (if applicable)** — A separate, explicit consent field for users willing to receive marketing emails.

## 23. Account
Private account settings: credentials, linked accounts, notifications, and destructive actions.
- **Email** — The current email address displayed with an option to update it. Verifying the new address before completing the change is standard practice; notifying the old address too adds a useful security signal.
- **Password change** — A way for users to update their account password. Requiring the current password before accepting a new one prevents unauthorised changes on an unlocked device.
- **Linked accounts** — A view of which third-party accounts are connected for sign-in or data access, with the ability to disconnect.
- **Save confirmation** — Clear feedback that changes have been saved, inline or as a toast. Auto-save with subtle confirmation is more pleasant; an explicit save button should remain disabled until there are changes.
- **Delete or deactivate account** — Options to deactivate or permanently delete the account, clearly separated from other settings.

## 24. Upgrade
A soft upsell screen presenting the value of upgrading to users who are open to it.
- **Value proposition** — The headline reason to upgrade, presented before scrolling, focused on outcome rather than a feature list. "Design faster" is more compelling than "Access 200+ templates", since outcomes convert better than feature counts.
- **Features unlocked** — A concise list of what becomes available with the paid tier, prioritised by relevance to the user's current context.
- **In-app purchase options** — Subscription tiers presented using the platform's native purchase sheet where possible. StoreKit on iOS and Google Play Billing on Android provide the familiar payment UI users already trust.
- **Annual plan savings** — Monthly and annual pricing shown together, with the saving on the annual plan made prominent. Showing the monthly equivalent alongside a "Save 40%" callout converts better than displaying the annual total alone.
- **Social proof** — Ratings, review counts, or short testimonials that validate the purchase decision.
- **Free trial call-out** — A clear indication that a trial period is available, with no commitment required to start. Making the trial the primary CTA reduces friction; trial-to-paid conversion is typically high.
- **Transparent pricing** — The full price and billing cadence shown before the payment sheet, matching what was displayed earlier in the flow. Users who encounter a higher price at checkout feel deceived — a leading cause of refund requests.

## 25. Activity Feed
A chronological stream of actions taken by users and the system — a browsable record of what has happened, distinct from notifications that demand attention.
- **Feed item anatomy** — The consistent structure of each entry: who did what, to which object, and when. When actor, action, and object occupy the same position across item types, users can scan without reading every word.
- **Relative timestamps** — Times in human-readable relative format ("just now", "2 minutes ago", "yesterday") for recent activity. Switch to absolute dates for items older than 7 days; "3 weeks ago" stops being useful when a user needs to pinpoint when something happened.
- **Avatar and attribution** — A visual identifier (avatar or icon) for the person or system responsible for each item. System-generated events need distinct visual treatment so users can tell human activity from automated actions without reading the description.
- **Object link** — Each feed item linking directly to the resource it describes. The feed is most useful when it doubles as a navigation shortcut; tapping an item should arrive at exactly the thing that changed, not a category view.
- **Activity grouping** — Related actions from the same actor or on the same object consolidated into a single item. "Sarah edited 6 items" is far less noisy than six separate edit events — group aggressively.
- **Filter controls** — A way to narrow the feed by actor, action type, or time period. When the feed spans a large team or long period, filtering is the difference between a useful audit trail and a wall of noise.
- **Empty state** — Helpful content when the feed has no items, for new users who have not generated activity and for filtered views returning nothing. A new user's empty feed is a prompt, not a gap — use it to suggest the first action that will generate activity.
- **Load more** — A mechanism for viewing older activity beyond the initial page load. Infinite scroll works against users who treat the feed as a reference; a "Load more" button preserves scroll position.

## 26. Feedback
In-app prompts asking users for their opinion — NPS surveys, rating scales, and open text — at the right moment and frequency.
- **Prompt timing** — The moment the request appears, chosen to follow a point of completed value rather than a fixed session count. Highest-quality feedback comes from users who have just done something successfully. Asking after a failure, or on launch, produces noise.
- **Contextual trigger** — The specific in-app event or screen that initiates the request, relevant to the question. "How easy was it to complete that payment?" immediately after checkout produces better signal than "How do you feel about the app?" on the home screen.
- **Single-question entry** — Starting with one question rather than a form, to lower the barrier to responding. NPS surveys convert because they start with one question; drop-off at step one is the most significant.
- **Rating scale** — A numeric scale (0–10 NPS or 1–5 CSAT) as the primary signal. Segment the follow-up question by score range; a single follow-up for all three produces averaged, less useful responses.
- **Open text follow-up** — An optional text field shown after the rating. Mark it explicitly as optional and say so. "Tell us more (optional)" outperforms an unlabelled empty field.
- **Dismissal option** — A clear way to close the prompt without responding. Label the dismiss action neutrally — "Not now" rather than "No thanks". The user who dismisses today is still worth asking again in three months.
- **Frequency cap** — A limit on how often the same user sees a request, regardless of how many trigger conditions are met. Once per session is a reasonable maximum; once per month a reasonable minimum interval.
- **Submission confirmation** — A brief acknowledgement that feedback was received before returning the user to their previous context. A one-line thank you that disappears after two seconds is enough; without confirmation, some users submit again assuming the first attempt failed.

## 27. Referral
The flow through which users earn rewards for introducing new members to the app.
- **Unique referral link or code** — A personalised URL or code that tracks sign-ups back to the referring user, copyable in one tap.
- **Reward explanation** — A clear statement of what the referring user earns and what the new user receives, shown before deciding whether to share. Showing both sides ("Give a friend one month free, get one month free yourself") is useful.
- **Share sheet integration** — A button that opens the native share sheet pre-loaded with the referral link and a suggested message. Pre-fill the message with something that helps the narrative rather than just a standalone link.
- **Channel shortcuts** — Direct share paths for high-performing channels (messaging, email) alongside the generic share sheet.
- **Referral status list** — A view showing who the user has referred, whether each person signed up, and whether the reward condition has been met.
- **Reward progress** — A clear display of pending and confirmed rewards, and for tiered programmes, progress toward the next milestone.
- **Terms and eligibility** — A concise summary of the conditions under which a referral counts and a reward is earned. Surface key conditions inline, e.g. who qualifies, any limit on total rewards.
- **Empty state** — The state of the referral screen before any referrals, with a clear prompt to begin sharing.

## 28. Invite
The flow for adding collaborators or members to a shared space, with role assignment and pending invite management.
- **Email invite** — The primary method of inviting someone by entering their email address directly.
- **Role or permission selection** — A control for setting what the invited person can see and do once they accept. Show what each role can and cannot do before sending, since this prevents over-permissioning and the back-and-forth of revoking access later. Keep roles to three or fewer where possible.
- **Contact picker** — Access to the device's contacts list for finding people without typing a full address. On iOS this requires explicit permission; prime the user with a custom screen before the system prompt, since "Find people you already know" performs better than asking cold.
- **Bulk invite** — A way to add multiple people at once, by entering several addresses or pasting a list. Support comma-separated and line-break-separated input, since users are likely to paste from spreadsheets or threads.
- **Pending invites + actions** — A list of sent invitations not yet accepted, with the option to resend or revoke each. Show when each invite was sent and when it expires.
- **Shareable invite link** — A link granting access to anyone who opens it, with a configurable permission level. Include an expiry option and a usage limit on the link for security.
- **Seat or member limit** — A visible count of remaining available seats, surfaced before the user reaches the plan's member cap.
- **Access scope summary** — A clear statement of what the invited person will be able to see and do, shown to the sender before confirming.
