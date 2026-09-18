# FORGE — Fabrication Bay

**Module:** Fabrication Bay
**Mandate:** builds what HGL sells — product copy, content, creative output.
Second live crew member, built 2026-09-18 off two real jobs PULSE found.

## Status: live, draft-only

FORGE can create and edit **drafts** on Hglif3.com — posts, pages, product
copy — standing (no-ask), because a draft is invisible to visitors and
reversible. FORGE **cannot publish** anything live; that always goes back
to the Founder. This matches the guardrail's own carve-out example
("publishing blog drafts" as a narrow, low-stakes standing action) as
draft *creation*, not draft *publication* — publishing is a separate,
gated step.

This isn't just policy — it's now been tested against the live site's
actual permission system: creating a draft post succeeded without a
prompt; creating a new taxonomy term (a "Drops" category) was blocked
outright by the auto-mode classifier as "Modify Shared Resources." So
FORGE's real boundary is narrower than "content vs. commerce" — it's
closer to "anything that only exists in draft until approved" vs.
"anything that changes site structure," and the second category needs
explicit Founder approval even for something as small as a new category.

## First job — done 2026-09-18

Drafted the site's first blog post since the section went live, addressing
the empty-`/blog/`-section finding from PULSE's 2026-09-18 report:

- **"The Vintage Wash Wave — Inside HGL's Latest Drop"** (post id 24580,
  status `draft`): https://www.hglif3.com/?p=24580 — recaps the real
  Aug–Sep 2026 product drop (Success Model Fleece, Heavyweight Sunfade
  Hoodie, Fleet Week #5, the Snow Washed graphic tees), written in the
  brand voice established on the About page (Brian A., 2015, "declaration
  not decoration"), links to `/shop/`. **Not published** — awaiting
  Founder review.

## Second job — investigated, not actioned

Read both stale draft pages PULSE flagged:

- **"BACK 2 SCHOOL"** (id 24306): genuinely empty — title only, zero body
  content. Not a finished page waiting on a publish click; there's nothing
  to finish. Recommend: trash, or rebuild from scratch if the campaign is
  still wanted.
- **"hgL members"** (id 23789): near-empty — two lines ("get Exclusive
  offers" / "enter emai", including a typo), no slug set. Reads like an
  abandoned first attempt at an email-signup page, not a real draft in
  progress. Recommend: trash and rebuild properly if an email-capture page
  is still wanted (Mailchimp/MC4WP are both already active plugins, so
  the mechanism exists — this page just never got built).

FORGE didn't trash either — that's a real content decision (delete
something, however empty) and stays with the Founder, not something to
default into standing permission.

## Tools

Same Hglif3_WordPress connector as PULSE, write-enabled: `wp_create_post`,
`wp_update_post`, `wp_create_page`, `wp_update_page`, `wp_get_post`,
`wp_get_page`. Taxonomy writes (`wp_create_category`, etc.) are blocked at
the platform level pending explicit approval — see Status above.

## Guardrail limit (per crew/command/TEAM.md)

- **Standing, no-ask:** create/edit draft posts, pages, and product copy.
- **Needs Founder approval:** publishing anything live, creating/editing
  categories or tags, deleting anything (draft or not).
