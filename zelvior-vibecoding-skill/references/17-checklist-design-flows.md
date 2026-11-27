# Flows Checklists (checklist.design — Flows)

13 checklists. Source: https://www.checklist.design/flows. Each is a step-sequence test for a user flow: every step below must exist, and the reasoning notes are the acceptance criteria.

## 1. Adding to cart
Shopping online means users need to easily add products to their cart; this fundamental action can make or break a sale.
1. **Outline variant selection for product** — Make clear what details must be picked to add an item to the cart (size, colour, amount, or something else).
2. **Primary action on product page is add to cart** — One of the most prominent buttons on the page, drawing the user's attention. This may change if you want an "add to cart" button on a grid view of multiple products.
3. **Feedback once added** — Immediate confirmation the item has been added. This can be done several ways depending on the amount of intrusion desired (two options are shown).
4. **Link to cart view** — Typically in a primary navigation, so that if the user continues shopping but is then ready to checkout, the cart is easily accessible. Show the number of products to catch attention that items were added but not purchased; a total price can also be considered.

## 2. Uploading media
1. **Empty state** — A clear visual placeholder with an upload icon and simple text indicating a file can be dropped into the area to upload. Also suitable to offer a click-to-upload route in case a user prefers that option.
2. **Drag and drop interaction** — When a file is across the interaction canvas, a clear visual state change indicating it has detected a file attempting to be dropped, so the user knows it is safe to release the file.
3. **Progress indicator** — Display progress that updates in real-time so users know the upload is working. If a percentage is not possible, a loading indicator can at least show something is happening. Include file names and show overall progress when uploading multiple files.
4. **File restrictions & constraints** — Clearly state limits on what files can be uploaded, commonly file size and format, shown in the upload area before users attempt to upload. If a file outside the constraints is attempted, an error message should explain that it does not follow the constraints.
5. **Outcome status** — Visual indicators like green checkmarks for successful uploads and red warning icons for failures. For failures, include an error message explaining what went wrong and what users can do to fix it.
6. **Upload actions** — Ways to interact with an upload. Choose which actions to show by default vs. on hover based on available space, aiming to avoid overwhelming users with too many visible options. Common actions: retry failed uploads, cancel upload in progress, delete files, rename files.
7. **Showing multiple uploaded files** — Display files in a clean list or grid with thumbnails when possible, and ensure the layout is scalable. What information is shown depends on context — a file name or size may be relevant in one case, while seeing the uploaded images in another.

## 3. Verifying account
Verification promises security early in onboarding, so it must be a smooth experience that feels like help rather than a burden.
1. **Establish a trigger point** — Clearly indicate when verification is required, with context as to why. It is common to verify the email or phone number used for account creation, since this ensures the person with access to those details is the one creating the account.
2. **Method selection (optional)** — Depending on the level of sophistication, offer multiple verification methods (email, SMS, authenticator). The common default is what the user signed up with — e.g. if signing up with email, send the code to email.
3. **Confirm delivery and contact information used** — Display the email address or phone number where verification will be sent, so the user can see it is the correct destination. If no code arrives and the contact information was incorrect, they can see this, go back, and enter the correct value.
4. **Ability to input verification code** — The input field can be intuitive with a field per digit, but the default input field is perfectly accessible.
5. **Incorrect value (and resend option)** — Provide specific error messages for different failure scenarios and clear next steps: expired code — offer a link to send a new code; incorrect code — ask to check email/SMS again or offer a link to send a new code; too many incorrect attempts — contact the support team or wait for a defined period before trying again.
6. **Verification success state** — Display clear confirmation when verification succeeds and continue to the next step of the interface.

## 4. Canceling subscription
A user can decide to end their experience and stop paying. Just because they are leaving does not mean a graceful exit is impossible — make cancellation obvious to find and easy to travel through.
1. **Show a link in account details** — This does not have to be the first or most prominent link, but it should be clearly visible. If unsure about the account page, it is suitable to place on the billing settings.
2. **Confirm intent to cancel** — Sometimes a user misclicks, so it is okay to ask if they are sure rather than automatically cancelling. While the user is there, you can make a last-ditch effort to reel them back — but it cannot be pressuring or manipulative. If the product can only be accessed with a subscription, remind them of the product's value; if a free version exists, remind them of that specific subscription's value.
3. **Request a reason for canceling (optional)** — Helpful for receiving feedback on why a user is cancelling: too expensive, competitor preferred, no longer needed. An easy way to start identifying key factors affecting churn.
4. **Confirm subscription has been canceled** — Now that it is canceled, make sure the user is told when their subscription is active until.

## 5. Filtering items
Filtering helps users find what they need in large collections by specifying values of properties the items contain.
1. **Show action near item collection** — Place above or beside the collection it affects, using recognisable icons and/or labels.
2. **Show available filter options** — When the action is triggered, options can be shown on the same page for immediate feedback, or on another page. This depends on the amount of filtering possible and whether the user is likelier to tweak filters ongoing or apply several then view results. Consider a filtering priority order, with the most common options at the front.
3. **Consider different filter types** — The standard filter is a multi-select option picker, but certain properties benefit from a different management approach. Sliders, checkboxes, dropdowns, and others are worth considering; for each property ask what feels like the easiest way to change that value.
4. **Show active filters clearly when applied** — On the item collection page, display which filters are currently applied. You can also apply a high-level active state to the filter action to imply use, if showing all applied filters is too cluttered.
5. **Provide easy filter removal** — Let users clear individual filters or all filters at once for easier refining of results.
6. **Show result count** — Not a must-have, but handy where it is meaningful for users to see what the total results value has reduced to. It helps users feel whether their result is too narrow or broad, directing them to add or remove filters.
7. **Empty state** — A combination of filters can produce no results. Explain this clearly and suggest adjusting or clearing filters to see results.

## 6. Saving changes
Users constantly update their details — an email address, a typo in their name, payment details. Confirm that a change has been saved in the clearest way.
1. **Show action that enables change** — There should be an action to enable information to be updated. It may be automatically editable, but that can be riskier for some software. If read-only by default, a button can trigger the editable version to then update and save.
2. **Disable save action until changes are made** — An action should be visible as the source of confirming changes to be saved, usually a button. Initially it can be disabled, indicating no changes have been made and there is nothing to save. A common location is in the navigation above the fold, so it is always visible over the content; another option is after all the editable content.
3. **State changes to active once a change is made** — When a change is waiting to be saved, changing the button state to active brings the user's attention to the action.
4. **Action changes to loading state when pressed** — Now that changes are being saved, show that the action is in progress, e.g. a loading spinner in the action, since the user's view will be on that element.
5. **Notify changes have been saved** — The page will reload or update, and this is the critical part. The user should be informed that their changes have been saved, so they can safely leave the page knowing the details are locked in until they choose to change them again.

## 7. Entering promo code
A reward for a user to earn a discount on their purchase; a pre-requisite in any e-commerce website. Avoid a confused customer by making clear what is happening with their code — whether it works, expired, or is not applicable.
1. **Show promo code input field** — The cart or checkout are pages expected to have a promo code field. It should be in a place that can be seen when scanning towards the button to continue.
2. **Promo code applied successfully** — The change can be reflected using success state colours (likely green). There are two different options, divided by how much information you want to show; for both, hiding the input field altogether makes it clear only one code can be entered.
3. **Reflect promo code impact** — Shown with the promo code entry as a total amount, or represented on an item-to-item basis. It is important to also show or at least repeat the discount near the total at checkout.
4. **Promo code error** — The code may not be applicable, or entered incorrectly.
5. **Remove promo code** — A user might not like the discount offered and prefer the original sale price, or they found a better promo code to use.

## 8. Showing input error
Users mistype all the time — a finger slipping or rushing through letters. For an everyday occurrence, solving an error should be obvious and seamless. The key parts are strong visuals, clear communication, and state changes.
1. **Keep the input in default state** — The text field should be checked for errors only after the information has been entered.
2. **Allow user to enter information** — Let the user type without interruptions and submit the information; do not assess as changes are made.
3. **Signal error after loss of focus** — After the input has lost focus (the user clicked another element), the field should be assessed. Explain why the error happened and what is required to resolve it. For accessibility, combine the text with a visual icon indicating an error was found.
4. **Return to default state upon reattempt** — Once the user focuses on the field again, the error message should disappear. If there is an error again, the process simply repeats until they are able to continue.

## 9. Resetting password
Sometimes a user cannot remember their password to log back in. The process should feel straightforward so the user gets back into their account as smoothly as possible.
1. **Place reset link close to password field** — Style it as a link to show it is clickable.
2. **Ask for account details to verify** — Usually the email address is requested, because it can recognise the account and be the channel the link is securely sent to. If the user already entered their email on the previous login page, prefill this field to speed up the flow.
3. **Show information has been sent** — Based on the account information provided, explain how they can continue. If an email was provided, send an email for the next step; if a mobile number was provided, send a code or link to open.
4. **The message sent explains next steps** — This could be a link to a page allowing the user to reset their password, or a code for the user to provide on a page to verify their account before resetting.
5. **Reset the password!** — Whether it is a verification code or a link behind an email address, the next page should be a clear text field to enter a new password. Provide guidelines if there are requirements for the password to pass a strength threshold.
6. **Password successfully reset** — After the reset, indicate success and push their momentum to their initial intent: logging in.

## 10. Deleting account
Sometimes it is just not meant to be, and that is okay. Users come and go, so recognise your solution is only for some and not all. For those who want to leave, make it as simple as possible. You can try to understand why they are leaving, but do not get too in the way — there is no need to be passive aggressive or guilt tripping. They will remember it, and likely share the experience with others who will reconsider your product.
1. **Show a link to delete account** — Do not make this difficult. The link should be visible in the profile or settings of a product, and also available in the support area.
2. **Politely ask for feedback** — It helps to know why somebody is choosing to leave. But it should not be pressured or forcefully asked. Convey the request as feedback to improve other people's experience and to also consider their personal reasons.
3. **Explain what it means to delete the account before confirming** — Be clear about what happens to the account and the information in it if a user closes. Is all the data permanently deleted? Can they come back and restore their account? Is the deletion immediate, or can they use their account until a certain date?
4. **Confirm account has been deleted** — Now that their account is deleted and it is finally complete, embrace that. Be comfortable acknowledging they have left, and show no passive aggressiveness.

## 11. Contacting support
If there is ever a problem, a user should know how to get help. Then when they try, they should know exactly what kind of communication they are receiving. Making support not only available but suited to how users tackle a problem matters. If you are explaining to a user in text where the interface elements are, when a screenshot would tell a clearer story, that is the first problem to solve before even getting to theirs.
1. **Show a link to contact support** — This can be placed in a number of areas: the footer of a website, settings in a mobile app, or a page experiencing an error. Use clear copy and easy-to-recognise visuals to highlight the link.
2. **Show methods of contact** — If there is one option, showcase it. If there are multiple options (chat, call, FAQ), list them and represent each of their benefits. Chat is great for a specific, complicated issue needing an instant response; FAQ is great for standard questions that are easy to explain. Consider the order — FAQ first lets a user find their own answer without waiting on a response, but a direct chat can be seen as more convenient since it is less direct troubleshooting.
3. **Outline how to communicate and what is expected** — Once a method is chosen, make it clear how the method will work. Illustrate the response time and what the user will need to provide to receive support.

## 12. Making a card payment
When paying for something online, two thoughts come to mind: is this safe, and is this clear? A well-designed payment experience covers these by communicating what is happening with the user's money and that it is all happening securely.
1. **Offer payment methods** — Other methods can be shown, but this flow focuses on the user selecting "credit or debit card", since it has the most internal effort to design and build compared with other services which are often third-party integrations.
2. **Request card details** — Show all relevant text fields to complete. Consider the size of these fields relative to the details entered. In a product where the user revisits and saved payment methods are available, consider a flow allowing the user to add/remove payment methods.
3. **Submit payment with card details entered** — Consider validation before a user submits their details. Numbers can be mistyped and the card may have expired, so address these numerous error states.
4. **Show payment processing** — A payment may not trigger instantly, taking a few seconds or minutes. A loading page is crucial to calm the user's nerves about what is happening to their money.
5. **Confirmation payment processed successfully** — Clearly indicate to the user that their payment was processed and the funds were received.
6. **Outline next steps** — What now? Does the payment trigger something? If so, let the user know. Example 1: a physical product was purchased — once processed, tell the user the order is in motion. Example 2: a user signed up for a subscription — offer a link to continue to the product to start using it.

## 13. Submitting a form
A form helps a user achieve anything from creating an account to subscribing to a newsletter. They are often the last step of a user's journey, so should be quick and easy to complete.
1. **Show button to submit** — Below the form fields, a button to submit the information needs to be present. The copy can be changed to fit the form, e.g. "Subscribe" if someone is providing their email address to receive emails.
2. **Show loading state after submission** — The user must see the form is in the process of being submitted. Also make sure the hover state is considered before they press the button.
3. **Show success message when it submits** — The form was submitted; communicate that back to the user with a clear success message.
4. **If it doesn't, show an error message** — Sometimes things do not work out. If the form cannot submit because of invalid information or another error, that also needs to be shown.
5. **An error may occur because of the wrong information** — If the criteria for a text field are not met, the form can fail to submit due to that error, and it must be detailed.
