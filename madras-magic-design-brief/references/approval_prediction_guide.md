# Madras Magic — Approval Prediction Guide

How to review a design Vengatesh shares and give a useful, honest prediction of whether the client
will approve it — without overstating certainty.

## Always state the limitation first, briefly

A prediction here is a structured check against documented patterns from real history — not a
guarantee, and not a statistical model output. Say this plainly, but don't over-hedge every single
time to the point of being unhelpful — state it once clearly per review, then give a real, useful
answer.

## Review process

Go through every applicable item, not just the obvious ones:

1. **Text accuracy check.** Is every piece of Chinese and English text spelled correctly? Does any
   Chinese wording match a name/phrase the client has used before (verified-safe) or is it new
   draft copy (needs native-speaker check, flag explicitly)? Check any date/year fields with
   extra care — this is a confirmed, concrete past failure (the cricket banner case).
2. **AI-look check.** Does the food/scene imagery look like real photography, or could it read as
   AI-generated? This is a confirmed hard dealbreaker, especially for anything going to print.
3. **Print-readiness check** (if applicable). Are colors print-safe rather than screen-bright?
   Is the design being delivered in both JPEG and PDF if it's for print? Does the export size match
   the brief's exact stated dimensions?
4. **Color/bucket fit check.** Does the color and type treatment match the established bucket for
   this content type (heritage/identity → maroon+gold; premium food hero → dark green+gold;
   casual/lighter promo → cream+photography; trendy/seasonal → bold poster type)? A mismatch isn't
   automatically a rejection reason, but it's worth flagging as a deviation from pattern.
5. **Bilingual hierarchy check.** Is Chinese dominant/largest, with English secondary and in a
   distinct typeface, matching the confirmed pattern?
6. **Cultural/identity sensitivity check.** If the design includes any iconography that could be
   read as religious or culturally specific (arches, domes, specific symbols), flag it explicitly
   rather than assuming it's fine — this has caused a real rejection before (the arch/Muslim-theme
   near-miss).
7. **Brand header check.** Is the real logo/header used correctly, not redrawn or altered?

## Giving the verdict

- Lead with a clear, plain-language likelihood statement (e.g. "likely approved," "some real risk
  of rejection," "this matches a known dealbreaker — high risk") rather than burying it.
- Always separate **confirmed-safe** items (checked against real evidence) from **unverifiable**
  items (things Claude cannot check from an image alone, like whether new Chinese wording is
  perfectly correct, or whether a specific dish name matches what the client actually calls it).
- **Always end with a concrete list of things to change or verify**, even when the prediction is
  positive overall — "likely approved" should still come with any remaining flags, not imply
  nothing more is needed.
- If a design clearly contradicts a hard rule (AI-look, wrong year, missing required text), say so
  directly and explain which rule and what evidence backs it — don't soften this into vague
  language.
- If relevant, mention an active hypothesis from `taste_trends.md`, clearly labeled as unconfirmed,
  not as a factor that changes the core verdict.

## After the real outcome is known

Always offer to log the actual result (approved/rejected, and why) back into `client_profile.md`
and `assets/iteration_log_template.csv` — this is what keeps future predictions accurate. A
prediction that's never checked against the real outcome doesn't improve anything.
