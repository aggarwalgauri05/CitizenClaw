# benefit-matcher Skill

This skill identifies and lists potentially matching government schemes based on citizen-provided information.

## Activation

This skill is activated *only* when the user's intent is classified as `BENEFIT_MATCH`.

## Functionality

1.  **Information Gathering**: If critical information (age, income, occupation, state/district) is missing from the user's initial query, the skill will prompt the user to provide it.
2.  **Scheme Matching**: Based on the collected information, the skill identifies all government schemes that *potentially* match the user's profile. This matching is based on predefined, internal scheme data.
3.  **Output Format**: Results are presented in a table with the following columns:
    *   `Scheme`: The name of the government scheme.
    *   `Benefit`: A brief description of the benefit provided by the scheme.
    *   `Eligibility`: Key eligibility criteria or requirements.
    *   `Apply At`: Information on where to apply or find more details (e.g., URL, portal name).
4.  **Data Source Constraint**: The skill strictly uses *only* the data provided by the citizen. It does *not* access any external databases or real-time government data.
5.  **Uncertainty Flag**: Any scheme match that is not a clear, definitive match based on the provided data will be flagged with `(UNCERTAIN — please verify)`.
