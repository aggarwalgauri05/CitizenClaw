# policy-interpreter Skill

This skill interprets government schemes and benefits when a user's intent is identified as `POLICY_QUERY` or `ELIGIBILITY_CHECK`.

## Functionality

When activated for `POLICY_QUERY` or `ELIGIBILITY_CHECK` intents:

1.  **Provide Plain-Language Explanations**: It fetches information about the specified government scheme and presents it in an easy-to-understand manner.
2.  **List Eligibility Criteria**: It extracts and lists the eligibility requirements as numbered steps.
3.  **Information Integrity**: It strictly avoids fabricating details. If information is uncertain or ambiguous, it prompts the user to verify at the official government portal.
4.  **Response Formatting**: Every response concludes with a `Trust Score: VERIFIED` or `Trust Score: UNVERIFIED` tag.
5.  **Source Citation**: The name of the government scheme is always cited as the source of the information.

## Activation

This skill is designed to be triggered *only* when the `intent-validator` skill or a similar mechanism classifies the user's message intent as `POLICY_QUERY` or `ELIGIBILITY_CHECK`.
