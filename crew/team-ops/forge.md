# FORGE — Fabrication Bay

**Module:** Fabrication Bay
**Mandate:** builds what HGL sells — product copy, content, creative output.
Second live crew member, built 2026-09-18 off two real jobs PULSE found.

## Status: live, draft-only in practice — daily blog publish authorized but technically blocked

FORGE can create and edit **drafts** on Hglif3.com — posts, pages, product
copy — standing (no-ask), because a draft is invisible to visitors and
reversible.

**2026-09-18 — Founder decision:** daily blog publishing is now explicitly
authorized as a standing task (see "Daily blog task" below), not just
drafting. This matches the guardrail's own original carve-out example
("publishing blog drafts... without asking each time"). Scope: blog posts
only, one per day. Everything else FORGE touches (pages, product copy,
site structure) stays draft-only pending separate approval.

**But publishing is currently blocked by Claude Code itself, not WordPress.**
Correction to this file's original version: the "Drops" category block
from FORGE's first run was mischaracterized as the live site's own
permission system. It's actually **Claude Code's own auto-mode
classifier** — a harness-level safety control that intercepts the tool
call before it reaches WordPress at all. Confirmed twice now:

- Creating a draft post → succeeded, no prompt.
- Creating a category → denied, reason `Modify Shared Resources`.
- **Publishing a post (`wp_update_post` with `status: publish`) → denied,
  reason `External System Writes`.**

This can't be worked around from inside a session — the tool's own error
says so explicitly: *"the user can add a Bash permission rule to their
settings"* to allow it. Until that happens, the daily blog task is fully
specified and ready to run, but each day's post will land as a draft, not
published, and needs the Founder to either flip it to `publish` manually
or grant the permission so FORGE can do it directly.

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

## Daily blog task (defined 2026-09-18)

**Cadence:** one blog post per day. **Same scheduling gap as PULSE**
applies — see `crew/README.md` "Known platform gap": this org can't
attach the WordPress connector to a scheduled Routine, so "daily" means
on-demand each time a session runs this task, not truly unattended. Ask
me to run it, or re-ask each day, until that's resolved.

**Procedure**, each time it runs:

1. Check `wp_list_posts(status: "any", per_page: 1)` for the most recent
   post's date. If a post already went out today, skip — don't double-post.
2. Pull a content signal for the day, in priority order:
   - New products published since the last post (`wp_list_cpt_items`,
     `rest_base: "product"`, filtered by date) → drop recap, like day 1.
   - No new products → fall back to a rotating angle so it doesn't run dry:
     styling/outfit ideas using existing catalog pieces, brand story
     (About page has real material — founding, mission), a restock or
     care/quality note. Rotate angle so consecutive days don't repeat.
3. Write ~300-400 words in the established brand voice (see day 1's post,
   id 24580, and the About page for tone reference).
4. `wp_create_post` with `status: publish` directly — no draft
   intermediate step, since this task has standing authorization. (Today
   it lands as `draft` instead, because the publish call itself is
   blocked — see Status above. Flip to `publish` once that's resolved.)
5. Log the post id/title/date in `crew/team-ops/knowledge/`.

**Out of scope for this task:** anything beyond one blog post a day.
Product pages, site pages, categories, pricing — none of that is covered
by this authorization; those stay under FORGE's normal draft-only rule.

## Tools

Same Hglif3_WordPress connector as PULSE, write-enabled: `wp_create_post`,
`wp_update_post`, `wp_create_page`, `wp_update_page`, `wp_get_post`,
`wp_get_page`, `wp_list_posts`. Taxonomy writes (`wp_create_category`,
etc.) and live-publish writes are both blocked by Claude Code's own
auto-mode classifier pending a permission-settings change — see Status
above.

## Guardrail limit (per crew/command/TEAM.md)

- **Standing, no-ask, Founder-authorized:** one blog post per day,
  written and published — currently lands as draft only because the
  publish action itself is blocked at the Claude Code permission level,
  not by this guardrail.
- **Standing, no-ask:** create/edit drafts for anything else (pages,
  product copy).
- **Needs Founder approval:** publishing anything other than the daily
  blog post, creating/editing categories or tags, deleting anything
  (draft or not).
