# Sunny Side Power Washing — handoff at ~60%

**Live file:** index.html · **Live site:** https://10elizabethbell.github.io/sunnySidePowerWashing/ · **Repo:** https://github.com/10elizabethbell/sunnySidePowerWashing · **Built:** 2026-10-08 from Muse brief (run 2026-10-08, found via the "NJ CONTRACTORS, BUILDERS & GC's" Facebook group flyer)

## What's built
- **World:** their own mascot (a sun in sunglasses holding a pressure-wash wand) shining over live water. Sky-navy ground (never black), their wordmark gold `#F9BF00`.
- **Signature element:** a canvas sheet of water at the foot of the hero and the closing section. Three layered swells plus a ripple field; the sun's glitter path sparkles on the water under the mascot; little spray leaps happen on their own. Sweep a finger or mouse through it and it ripples and throws spray that arcs and splashes back; sparkles get pushed aside and spring back. Wave seams between every section move the same way and bump when you sweep across them.
- **Sections:** hero (benefit headline, "Soft-wash & pressure washing across New Jersey. Fully insured.", Call + Free quote) → 3 before/after sliders with a solid water-blue divider whose edge is moving water: the dirty side has a wobbling wet edge with foam, sheen and spray that gets livelier the faster you drag (sweeps in once on first view; drag sideways, arrow keys work) → "What we wash": their 12 services, each row toggles it into the quote, with job photos floating in water bubbles you can push → "Why Sunny Side?" (their three pillars, their wording) + John G.'s review verbatim → quote builder → close with mascot, name, tagline → footer with "Demo one-pager — free sample."
- **Quote builder** (this is the pitch: their site has no form): service chips synced with the service rows, grouped and named exactly like the list; services picked in the list arrive as just those chips plus "+ Add another service". Home/Business, town, details, name, phone-or-email (required). Composes one message and opens it by email (primary, known channel) or text, plus Call. A "message ready" box with the text and a copy button shows as a fallback for Facebook's in-app browser. The draft survives a webview reload (sessionStorage) after Mail/Messages opens.
- **Small touches:** gold outline on hover for chips, fields and the service + buttons; a little water spray off the + when a service goes into the quote; sun-ray halos (the hero's own rays) behind the Why icons; footer has their Facebook link.
- **Phone:** sticky bottom bar (Call | Free quote with a count of picked services) appears once the hero buttons scroll away and hides over the quote form's own buttons.
- **Weight:** 617 KB single file, ~90% images as lazy-loaded WebP data blocks at the end; motion and buttons start before photos arrive. Safe crops are in `assets/`; after swapping one, run `python3 tools/embed.py`.

## Assumptions I made
- **Brief said no logo/photos; their Wix site had them.** Muse couldn't get direct URLs, but the page HTML lists the owner's uploads (`static.wixstatic.com/media/e77978_*`). I used the logo, wordmark, 3 before/after composites and 5 job photos from there. Raw originals stay in ignored `src-assets/`.
- **Before/after captions** ("Green mildew off the vinyl", "Moss out of the joints, the red back in the brick", "Stained walls and pad, cleared and washed") describe what the photos show; the owner didn't write them.
- **Service groups** (Homes / Driveways & outdoors / Commercial) are my grouping of the 12 services listed on their site; the names are theirs, verbatim.
- **Headline** "Your home, back on the sunny side." is mine. Their own line "The gold standard in exterior cleaning." is used as the closing tagline.
- **Pillar copy** is lightly trimmed from their site's "Why Sunny Side?" section (third person "we" removed in two places).
- **Email is the primary quote channel**, text second, because the brief says whether the number takes texts is unknown.
- **Crew photos:** the worker in the gold hoodie appears in their own site photos. I used the back-view shot (no face) in a bubble and skipped the front-facing ones.
- **Gold** sampled from their wordmark PNG; the navy and water blues are mine.

## Placeholders and gaps
- No hours, prices, owner name, street address or list of towns (statewide NJ only). The page says nothing about them.
- Only one review (John G., no platform or date). More would help.
- 4th before/after (gable vent) not used: the before and after are shot from different angles, so a slider won't line up.
- Their flyer prints **SUNNYSIDEPOWERWASHING.CO**, which doesn't resolve; the working site is the .com. Worth raising in outreach (not mentioned on the page).
- The trademark application (serial 98462104, filed 2024-03-22) isn't on the page; it's an outreach angle.

## Questions for the owner
- Does (732) 344-0712 take texts? If yes, make "Send as a text" the primary quote button and add text-to-book per service.
- Which towns/counties do you actually cover? (A service-area line or map would help local search.)
- Hours, and how fast you usually reply to a quote request?
- Any price ranges you're happy to publish (e.g. "house wash from…")?
- More before/after pairs, especially roofs, driveways and a house wash (the most common jobs)?
- Google Business Profile? Reviews there could feed the proof section.
- OK to show the crew's faces?

## Ideas not built (yours to pick)
- **From the 2026-10-09 critique (24/32), not done:** shrink the hero water on phones (~160px) so the first before/after peeks above the fold (I left the signature water alone); put the crew in gold hoodies at real size near the review instead of only in a bubble; link the review to a Facebook source if one exists; split "Phone or email" into a phone field (numeric keypad) and an email field; make "Free quote, in a minute" true on a 360px phone by cutting a field.
- **From the finish review (ceiling notes, not fixed):** the before/after frames are plain rounded rectangles on cream, the only photos not set in the water world (could become rounded glass/water frames with spray at the divider's foot); the Why section is a standard icon + heading + text row with nothing moving; on phones the quote chips repeat the 12 services right after the services list (could collapse to "Your picks: …" with an edit link).
- **Runner-up world:** "the grime wipe": a dirty film over the hero photo that the finger pressure-washes clean in a surface-cleaner swirl, then slowly regrows. Very on-trade, more of a gimmick; the water world carries the brand (sun + water) better.
- Other worlds considered: surface-cleaner spinning rings, sunlit spray fan with a rainbow, wet-driveway sheen with water sheeting off.
- A 4th proof slot using a photo pair from a roof job, once they supply one.
- Text-to-book rows (one pre-filled SMS per service) if they confirm texts.
- `book.html` full booking page with day/time window, same water and seams.
- QR code on the page for their flyers pointing at the new site (their old site has one).
- Pointer-follow mascot wand (built as a demo on 2026-10-09, tried and removed by Ellie).
- Copy alternatives for the hero: "Grime off. Shine on." / "The gold standard in exterior cleaning." (their line) as the headline instead.

## Not verified
- Real-device touch (tested with simulated touch events in headless Chrome only), and how the water feels at 60fps on an older phone.
- Real SMS handoff on iOS/Android (`sms:+17323440712?&body=` form) and mailto in the Facebook in-app browser.
- Clipboard copy inside Facebook's in-app browser (fallback text box is always shown).
- Direction was chosen unattended (no Impeccable concept roll or decision page, per the pitch-site skill), so the contract has no seed key.
- Headless quirks: tall desktop captures sometimes render blank, and the sticky bar's slide-in transition doesn't finish under virtual time; both looked right in other captures.
- Impeccable's detector ran in degraded mode (parser modules not installed): 0 findings is an undercount. Contrast was checked by hand.
