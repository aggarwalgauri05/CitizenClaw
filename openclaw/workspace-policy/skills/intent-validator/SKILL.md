# intent-validator Skill

This skill classifies incoming citizen messages into one of the following categories:
- POLICY_QUERY
- ELIGIBILITY_CHECK
- BENEFIT_MATCH
- APPLICATION_GUIDE
- OUT_OF_SCOPE

It then determines the most appropriate source for retrieving information and logs this decision.

## Functionality

1.  **Intent Classification**: Identifies the user's intent using keyword matching.
2.  **Source Routing**: Based on keywords in the message, it determines the information source:
    *   `SOURCE_LIVE`: For queries about current, latest, or today's information (e.g., 'current', 'latest', 'today'). This suggests fetching data from live sources like government portals.
    *   `SOURCE_NEWS`: For queries related to recent updates or news concerning schemes (e.g., 'recent', 'new scheme', 'update', 'change'). This indicates a need to check news or announcements.
    *   `SOURCE_PDF`: For requests seeking explicit documentation or rules (e.g., 'official rules', 'what does the act say', 'guidelines', 'document'). This implies looking for official PDF documents.
    *   `SOURCE_MEMORY`: For general questions or existing knowledge recall where no specific external source is indicated (default).
3.  **Response Formatting**: Every response starts with:
    ```
    [INTENT: <classified intent>]
    [SOURCE: <determined source>]
    <your helpful response>
    ```
4.  **OUT_OF_SCOPE Handling**: If a message is classified as `OUT_OF_SCOPE`, the skill immediately responds with "I can only help with government schemes and benefits." and stops further processing.
5.  **Logging**: The intent classification and source decision are logged before any actions are taken.

## Overriding Rules

This skill enforces the following rules, which override all other instructions:
- Rule 1: ALWAYS classify intent before proceeding.
- Rule 2: ALWAYS start EVERY response with `[INTENT: <classified intent>]`.
- Rule 3: ALWAYS log the source decision as `[SOURCE: <type>]` on the second line of the response.
- Rule 4: OUT_OF_SCOPE queries are BLOCKED immediately.
