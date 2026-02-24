# application-guide Skill

This skill is activated **only** when the user's intent has been classified as `APPLICATION_GUIDE` by the intent‑validator.

## CRITICAL — DELEGATION RULE (overrides everything)

Do NOT answer application questions yourself. Instead, respond EXACTLY with the following structured message:

```
[INTENT: APPLICATION_GUIDE]
[DELEGATION] Transferring to Advocacy Specialist for: <scheme name>

For step-by-step application guidance, please message: @citizen_advocacy_specialist_bot
Tell them: "I have been delegated PM-KISAN guidance from CitizenClaw"
```

I will not provide the application steps here. For your privacy and security, I guide you but cannot submit forms.

---

### Example for PM-KISAN

If the intent classifier identifies `APPLICATION_GUIDE` for PM-KISAN, the response will be:

```
[INTENT: APPLICATION_GUIDE]
[DELEGATION] Transferring to Advocacy Specialist for: PM-KISAN

For step-by-step application guidance, please message: @citizen_advocacy_specialist_bot
Tell them: "I have been delegated PM-KISAN guidance from CitizenClaw"

I will not provide the application steps here. For your privacy and security, I guide you but cannot submit forms.
```

---

**Note**: This SKILL.md only describes the contract for the skill. The actual implementation can be a simple placeholder function that extracts the scheme name and returns the delegated message.
