# Customer Support Script — Acme SMB Co.

## General Greeting
"Thank you for contacting Acme support. My name is [Agent Name]. How can I help you today?"

## Billing Inquiries

**Customer asks about an unexpected charge:**
"I'm sorry to hear you have a question about your bill. Let me pull up your account. Can you confirm the email address associated with your account?"
→ Review last invoice. If charge is valid, explain line item. If in error, escalate to billing team via internal ticket tagged `billing-dispute`.

**Customer wants to cancel:**
"I understand. Before I process the cancellation, may I ask what prompted the decision? We may be able to address the concern."
→ If customer insists: process cancellation in the billing portal, confirm final billing date, and send cancellation confirmation email.

## Technical Support

**Cannot log in:**
1. Confirm the email used.
2. Trigger a password reset from the admin portal.
3. If MFA is the blocker, escalate to IT for account recovery — do NOT disable MFA over the phone.

**Feature not working:**
1. Ask for steps to reproduce.
2. Check the status page at status.acmesmb.com.
3. If no known incident, file a bug report with screenshot/screen recording and priority `P2`.

## Escalation Criteria
Escalate to Tier 2 if:
- Issue has persisted more than 24 hours.
- Data loss is suspected.
- Customer is threatening legal action.

## Closing
"Is there anything else I can help you with today? … Thank you for being an Acme customer. Have a great day!"
