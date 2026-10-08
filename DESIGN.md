---
name: Sunny Side Power Washing
description: Phone-first pitch one-pager; the brand's sun mascot over a live sheet of clean, moving water.
colors:
  sky-deep: "#0a2c52"
  sky-navy: "#0d3b6e"
  sky-blue: "#1d5fa3"
  sky-glow: "#2a6db4"
  water-deep: "#1a62ad"
  water: "#2a8fd6"
  spray: "#57c3f2"
  water-pale: "#dff1fc"
  mist: "#eef6fc"
  cream: "#fbf6e9"
  sunny-gold: "#f9bf00"
  sunny-gold-hover: "#ffcb1f"
  gold-pale: "#fff1bf"
  ink: "#10233d"
  ink-soft: "#34496a"
  on-dark: "#ffffff"
  on-dark-soft: "#c9def3"
  placeholder: "#5b6f8c"
  error-text: "#a3261b"
  error-border: "#c2382b"
typography:
  display:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.2rem, 10.4vw, 4.9rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 8vw, 3.5rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.01em"
  title:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.0625rem, 0.9rem + 0.7vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  button:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 800
    lineHeight: 1
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.04em"
rounded:
  jet: "6px"
  focus: "12px"
  field: "16px"
  card: "22px"
  pill: "999px"
  circle: "50%"
spacing:
  gutter-phone: "16px"
  gutter-wide: "28px"
  stack-sm: "12px"
  stack-md: "22px"
  stack-lg: "28px"
  section: "72px"
  section-end: "96px"
  container: "1180px"
components:
  button-primary:
    backgroundColor: "{colors.sunny-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "58px"
  button-primary-hover:
    backgroundColor: "{colors.sunny-gold-hover}"
  button-line-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "58px"
  button-line-on-light:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "58px"
  button-line-on-light-hover:
    backgroundColor: "{colors.water-pale}"
  chip:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "44px"
  chip-selected:
    backgroundColor: "{colors.sunny-gold}"
    textColor: "{colors.ink}"
  input:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.field}"
    padding: "14px 16px"
    height: "54px"
  ba-tag-after:
    backgroundColor: "{colors.sunny-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  review-card:
    backgroundColor: "{colors.sky-blue}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.card}"
    padding: "26px 22px"
  sticky-bar:
    backgroundColor: "{colors.sky-deep}"
    padding: "10px 12px"
---

# Design System: Sunny Side Power Washing

Everything lives in one file, `index.html`. Styles are in the main `<style>` block in labelled sections (TOKENS, BASE, BUTTONS, HEADER, HERO, WAVE SEAMS, PROOF, SERVICES, WHY + REVIEW, QUOTE BUILDER, CLOSE + FOOTER, STICKY BAR, WIDER SCREENS). Behavior is in one `<script>`: a `TUNE` object at the top, then one IIFE per behavior. The CSS custom properties in `:root` are the source of truth for the color hexes in the frontmatter above. Where a value is hard-coded outside `:root` (seam fills, the water gradient in JS, the hero glow), this file says so.

## Overview

**Creative North Star: "Morning Sun Over Clean Water"**

The page is the client's own mascot (a sun holding a pressure-wash wand) rising over a deep morning sky, with a live sheet of water at the foot of every big dark section. Gold comes from their wordmark, and the dark ground is sky navy, never black. The water is something you touch: it ripples and throws spray when a finger or mouse sweeps through it, the before/after divider is a running water jet that washes the dirty photo into the clean one, and the job photos float in water bubbles that drift and get pushed aside.

It is designed at phone width (360 to 430px) first and adapted up. The first phone screen holds the wordmark, a call pill, the sun mascot, the benefit headline, the one-line pitch, the Call and Free quote buttons, and the living water under them. Type is the system font stack with heavy uppercase headings, which is deliberate: it loads instantly and matches the brand's blocky wordmark. Sections alternate dark sky and light grounds, and animated three-line wave seams join them instead of hard color edges.

Depth comes from soft shadows tinted navy and from the shading inside water and bubbles, never from hairline highlights. Every moving thing runs on one shared animation loop, pauses when off screen, and stops under reduced motion.

**Key Characteristics:**
- Sky navy and gold on dark sections; cream and mist on light ones; water blues hold them together.
- Heavy uppercase system-font headings (900), plain sentence-case body.
- Pill buttons with a 3px gold outline; the gold and line variants are always the same height.
- One living material (water) carried through the hero, seams, before/after jets, photo bubbles and close.
- Phone first: 58px buttons, a sticky Call / Quote bar, `tel:`/`sms:`/`mailto:` as the main actions.

## Colors

The palette is a morning sky and clean water from deep navy to pale mist, with one warm gold accent taken from the wordmark.

### Primary
- **Sunny Gold** (`--gold`): sampled from the client's wordmark. Used for the primary button fill and every button's 3px outline, the hero headline's emphasized words (`<em>`), the slider knob and "After" tag, the selected service cue and chips, pillar icon discs, the review quote mark, the close tagline, focus rings, and `::selection`. On dark grounds it is the light; on light grounds it marks what's chosen or what to press.
- **Gold Hover** (`#ffcb1f`, hard-coded in `.btn-gold:hover`): the primary button's hover fill only.
- **Pale Gold** (`--gold-100`): the review attribution on the blue review card.

### Secondary
- **Sky Navy** (`--sky-900`): the main dark ground (hero, Why, close, the services tally pill, the light-section line-button outline). Also the page `theme-color`.
- **Sky Deep** (`--sky-950`): the sticky phone bar.
- **Sky Blue** (`--sky-700`): the review card, service group headings, service-row hover text, the white cue icon color, chip focus ring, scrollbar thumb.
- **Sky Glow** (`#2a6db4`, hard-coded): the bright top of the hero and close radial gradients, where morning light comes in behind the sun.

### Tertiary (water)
- **Water** (`--water-500`): the middle seam line, input focus border, caret color.
- **Water Deep** (`--water-600`): the bottom of the water body; the footer ground is this exact color, so the close section's water flows straight into the footer.
- **Spray** (`--water-300`): the value behind the seam's back line (`rgba(87,195,242,.55)`). The front seam line and the water surface top use the lighter `#74d3f8`.
- **Water Pale** (`--water-100`): placeholder fill behind photos while they load, line-button hover on light grounds, footer small text.

### Neutral
- **Cream** (`--cream`): the body background and the Proof and Quote grounds. Warm, so the light sections feel sunlit.
- **Mist** (`--mist`): the Services ground and scrollbar track. Cool, so Services reads as "in the water" between two cream sections.
- **Ink** (`--ink`): all text on light grounds and text on gold. Navy-black, never pure black.
- **Ink Soft** (`--ink-2`): supporting paragraphs, captions, hints on light grounds.
- **On Dark** (`--on-dark`, white) and **On Dark Soft** (`--on-dark-2`): headings and body text on navy grounds.
- **Placeholder** (`#5b6f8c`), **Error Text** (`#a3261b`), **Error Border** (`#c2382b`): form-only, hard-coded in the QUOTE BUILDER section.

### Named Rules
**The Never-Black Rule.** No page ground is black or near-black. The darkest surface is Sky Deep. The brand's black stays inside the wordmark artwork only.

**The Gold Is Light Rule.** Gold marks the sun and the next action: primary buttons, selected states, the slider knob, emphasized headline words. Don't use it for large fills or body text on light grounds; gold text belongs on navy only.

**The Seam Fill Rule.** Each wave seam's `data-fill` attribute is the hex of the section *below* it (`#fbf6e9` cream, `#eef6fc` mist, `#0d3b6e` sky navy). If you change a ground token, change the matching `data-fill` values too, or a color step shows under the wave.

## Typography

**Display Font:** system-ui (with -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif), set once as `--font`.
**Body Font:** the same stack.

**Character:** one native family in two voices. Headings are 900-weight uppercase with balanced wrapping, chunky like the wordmark. Body is plain sentence case at a comfortable 17px. Choosing the system stack is deliberate (Ellie's house style), not a placeholder.

### Hierarchy
- **Display** (900, `clamp(2.2rem,10.4vw,4.9rem)`, line-height 1, uppercase): the hero headline only. Sells the benefit, not the business name. Emphasized words go in `<em>`, which renders upright in gold.
- **Headline** (900, `clamp(2rem,8vw,3.5rem)`, 1, uppercase): section h2s. The close section's business-name h2 is a little bigger (`clamp(2.1rem,9vw,4.25rem)`).
- **Title** (900, 1.25rem, uppercase): service group headings (Sky Blue) and pillar headings (line-height 1.15).
- **Lead** (400, `clamp(1.0625rem,.9rem+.7vw,1.25rem)`): the hero pitch line, max 36ch, 20px cap. `<strong>` inside goes to white 700.
- **Body** (400, 1.0625rem, 1.55): all paragraphs. Section intros are capped at 44 to 46ch, pillar text at 56ch.
- **Button** (800, 1.0625rem, 1): every `.btn`. In the tally, bar and "sent" panel, buttons drop to 1rem or 0.9375rem.
- **Row label** (700, 1.125rem, 1.25): service rows.
- **Quote** (600, 1.25rem, 1.45; 1.5rem from 900px): the testimonial blockquote.
- **Label** (800, 0.8125rem, letter-spacing 0.04em, uppercase): the Before / After tags only.

### Named Rules
**The Shout-and-Talk Rule.** Headings shout (900, uppercase, line-height 1, -0.01em). Everything else talks (sentence case, 400 to 800). Don't uppercase body copy, buttons or chips.

**The Sixteen-Plus Rule.** No reading text below 15px (0.9375rem). Body stays at 17px on phones.

## Layout

- **Container:** `.wrap`, max 1180px, centered, 16px side gutters on phones and 28px from 600px.
- **Breakpoints:** 600px (paired hero/close buttons side by side, two-column before/after list, the quote form's send buttons as a 2-up grid with the gold one spanning the full row) and 900px (desktop: sticky bar hidden, bigger header and wordmark, hero split 1.25fr / 0.75fr with the sun on the right, three-column before/after list, services split into list plus a sticky bubble zone, three pillars across, quote section split 0.8fr / 1.2fr). JS uses a separate `PHONE` flag at `max-width: 699px` for particle counts and for dropping the fifth (desktop-only) bubble.
- **Section order and grounds:** header (absolute, over the hero) → **Hero** (sky radial) → seam → **Proof** before/after (cream) → seam → **Services** (mist) → seam → **Why + review** (sky navy) → seam → **Quote** (cream) → seam → **Close** (sky radial, mascot, water) → **Footer** (water deep) → sticky **bar** (phones). Dark and light sections alternate. Each dark radial section (hero, close) ends in a water canvas.
- **Vertical rhythm:** content sections use 72px top and 96px bottom padding; the extra bottom room is where the next seam overlaps. Hero and close start at 84px (110px hero on desktop) to clear the absolute header. Proof starts tight (28px, 40px desktop) because it sits right under the hero's water.
- **Inner stacks:** 12px between heading and intro and between paired buttons, 22 to 28px between groups, 26 to 36px between pillars.
- **Anchors:** `scroll-padding-top: 72px`, smooth scrolling (turned off under reduced motion).
- **Footer** reserves `110px + safe-area` bottom padding on phones so the sticky bar never covers it.

### Named Rules
**The Thumb Rule.** Primary actions are at least 54px tall (58px standard) and full width on phones; every tap target is at least 44px.

## Elevation & Depth

A hybrid: grounds are flat, and objects that sit on them (photos, buttons, cards, bubbles) get soft shadows tinted navy that fall downward, with a negative spread so they read as a glow under the object rather than an outline. The water and bubbles get their depth from internal gradients.

### Shadow Vocabulary
- **Lift** (`--shadow-1`: `0 10px 24px -10px rgba(13,59,110,.45)`): the "message ready" panel.
- **Float** (`--shadow-2`: `0 22px 48px -18px rgba(10,44,82,.55)`): before/after frames and the review card.
- **Gold glow** (`0 10px 22px -10px rgba(249,191,0,.75)`): gold buttons only.
- **Bubble** (`0 18px 36px -14px rgba(13,59,110,.5)`): photo bubbles.
- **Knob** (`0 8px 18px -6px rgba(10,44,82,.6)`): the slider knob. Small cue discs use `0 4px 10px -4px rgba(13,59,110,.4)`.
- **Bar** (`0 -10px 24px -12px rgba(0,0,0,.45)`): the sticky bar, cast upward.

### Named Rules
**The Tinted Shadow Rule.** Shadows are navy-tinted, blurred, and spread negative. No hard offset shadows, no neutral grey.

**The No-Glint Rule.** No thin decorative highlight lines (white arcs, inset top lines on buttons). The only highlight is the soft radial sheen inside the photo bubbles.

## Shapes

Everything is round, like water. Buttons, chips, tags, the tally and the header call link are full pills (999px). Photo frames and the review card use one soft card radius (`--radius`, 22px). Text inputs use 16px. Bubbles, knobs, cues and pillar icons are circles. The water-jet divider is a 12px bar with 6px rounded ends. Focus rings are a 3px gold outline with 3px offset and 12px radius. Section edges are never straight: the wave seams overlap the section above by their own height (56px, 76px from 900px).

Icons are inline SVG `<symbol>`s at the top of `<body>` (phone, mail, text, plus, check, swap, down, leaf, shield, sun, rays), drawn as 2.2px round strokes on a 24-unit grid and shown at 22px by default (`.ico`). Add new icons as symbols in the same style.

## Components

### Buttons
Confident pills, one component everywhere.
- **Shape:** full pill (999px), `--btn-h` tall (58px), 0 22px padding, 3px Sunny Gold border on every variant so pairs always match.
- **Primary (`.btn-gold`):** gold fill, Ink text, gold glow shadow. Hover goes to `#ffcb1f`.
- **Line (`.btn-line`):** transparent with white text on dark grounds (hover: 14% gold wash). Inside a section with the `on-light` class it switches automatically to Ink text with a Sky Navy border (hover: Water Pale fill). New light sections need `on-light` on the section or line buttons stay white.
- **Press:** `scale(.97)`. Transitions are 0.2s on color, background and transform with `cubic-bezier(.2,.8,.2,1)`.
- **Icons:** a leading 22px stroke icon with a 10px gap.
- **Pairing:** gold first, line second. Stacked full-width on phones, two-up from 600px (hero and close cap at 560px / 420px wide).

### Header
The header sits absolutely over the hero, 68px tall (84px desktop). On the left is the wordmark (a CSS background from `--wordmark`, 152px wide, 210px on desktop). On the right is a translucent white pill call link that reads "Call" on phones and shows the full number on desktop.

### Hero sun
`.sun` stacks three layers: a warm radial glow, a 12-ray SVG (`#rays`, gold at 22% opacity) spinning once every 60s, and the mascot (`--mascot`) bobbing on a 2.4s ease-in-out loop (±6px, ±2deg). On phones it floats right with `shape-outside: circle(48%)` so the headline wraps around it. On desktop it moves into the right grid column at up to 340px. The close section reuses it centered (150px, 200px on desktop).

### Water canvas (signature)
`<div class="water" data-water>` holding `.water-still` and a `<canvas>`. The `--band` custom property sets how deep the water body is (hero 150px, 220px desktop; close 120px, 170px desktop), and the element is `band + 120px` tall so spray has room to fly. `.water-still` is the CSS fallback gradient, shown until JS adds `.live`. The canvas draws, from back to front: the water body gradient (`#74d3f8` → `#38a6e6` → `#1a62ad`, hard-coded in JS `resize()`), a warm gold glow under the sun, three faint drifting caustic ribbons, sun-glitter sparkles (55% clustered under the sun's x position) that ride the surface and get shoved by the pointer, then spray droplets that arc under gravity and splash back into the surface as ripples. `data-sun-follow` (hero only) lines the glitter path up under the mascot. Without it the path is centered. The canvas never takes pointer events, so it can't block a tap.

**TUNE constants** (top of the script):
| Constant | Default | What it does |
|---|---|---|
| `swellSpeed` | 1.9 | Speed of the rolling swell, radians/s. Higher is livelier. |
| `swellAmp` | 0.1 | Swell height as a share of `--band`. |
| `rippleTension` | 0.24 | How fast finger ripples travel along the surface. |
| `rippleDamp` | 0.992 | How long ripples last; closer to 1 lasts longer. |
| `glints` / `glintsPhone` | 360 / 130 | Number of sun sparkles on desktop / phone. |
| `maxDrops` / `maxDropsPhone` | 260 / 120 | Cap on spray droplets alive at once. |
| `leapEvery` | 0.28 | Seconds between ambient spray leaps (×1.6 on phones, randomized ±50%). Half the leaps happen under the sun. |
| `pushRadius` | 110 | Pointer reach in px on sparkles and ripples (×0.8 on phones), and the base reach for pushing bubbles (×0.6 plus the bubble's radius). |
| `seamSpeed` | 2.2 | Speed of the wave seam lines. |
| `bubbleDrift` | 14 | Px the photo bubbles wander around their home spots. |
| `baIntro` | 1.5 | Seconds for the first water-jet sweep on each before/after. |

### Wave seams
`<div class="seam" data-seam data-fill="#HEX"><svg></svg></div>` placed between sections, 56px tall (76px desktop), pulled up over the previous section by its own height. JS draws three moving lines from layered sines: a back line (`rgba(87,195,242,.55)`, 5px), a middle line (`#2a8fd6`, 6px) with the next section's color filled beneath it, and a front line (`rgba(116,211,248,.75)`, 4px). Each seam's phase is offset by its index so no two match. Moving the pointer across a seam raises a local wobble that decays. To add a section, add a seam before it with the new ground's hex as `data-fill`.

### Before / after sliders
`figure.ba > .ba-frame[data-ba]` holds the after image, then the before image (`.ba-before`, clipped from the right by `--p`), the Before tag (Ink at 78%, white text, left) and After tag (gold, right), and the `.ba-jet` slider. The frame has a 9:8 aspect, card radius, and Float shadow. The jet is a 12px animated stripe of white and pale-blue water scrolling downward (0.5s loop) with a 52px gold knob carrying the swap icon. Interaction: mouse and pen drag at once. Touch only takes over after a clearly sideways drag (more than 8px and more horizontal than vertical), so vertical scrolling still works (`touch-action: pan-y`). A tap with no drag sets the position. Arrow keys move it 4% (10% with Shift), and Home/End go to 0 and 100. On first view (45% visible) the jet sweeps from 84% to 50% over `baIntro` seconds with an ease-out, and stops for good once touched. Image pairs must share the same framing so the divider lines up. Captions are a bold title plus a soft-ink line.

### Photo bubbles
`.bubbles[data-bubbles]` contains `.bub` circles, each with an inline `--s` size and `data-x` / `data-y` home positions as fractions of the zone. `data-desk` marks a bubble that is removed on phones. Each bubble has a photo, a soft radial sheen top-left, and a blue rim darkening at the edge (`::after`), plus the Bubble shadow. They drift on per-bubble sine phases, get pushed by the pointer with a spring back (stiffness 38, damping 6.5), and squash slightly in the direction they move. On phones the zone is 300px tall and bleeds to the screen edges. On desktop it is sticky beside the list at 620px with bubbles scaled ×1.6 (`--z`). The zone is decorative (`aria-hidden`) and passes taps through to images.

### Service rows and tally
Each service is a full-width `button.svc-row[data-svc]` (60px min height, 700 at 1.125rem, 2px Sky Blue at 14% bottom rule) with a 38px white circular cue on the right. Pressing toggles `aria-pressed`. The cue turns gold, spins 360deg and swaps plus for check. Rows mirror the quote form's checkbox chips; the chip list is generated from the rows, so add a service by adding a row only. Once anything is picked, a Sky Navy pill tally appears with the count and a "Finish quote" gold button, and the sticky bar's count badge shows the number.

### Chips (quote form)
White pills, 44px tall, 2px border in Sky Blue at 25%, 700 at 0.9375rem. Selected: gold fill and border. Keyboard focus: 3px Sky Blue outline. The Property choice uses the same chips as a two-column segmented control.

### Inputs / Fields
- **Style:** white fill, 2px border in Sky Blue at 28%, 16px radius, 54px min height (textarea 110px), body type.
- **Labels:** 800-weight block labels above, with optional soft-ink 400 hints in parentheses.
- **Focus:** border goes to Water with a soft blue under-glow (`0 6px 16px -8px rgba(42,143,214,.6)`). No outline.
- **Error:** the field gets `.bad`. The border goes to Error Border and a bold Error Text message appears below in plain language.

### Quote builder flow
Pick services, property, town, details, name, then contact. Validation requires a service or details, plus a phone number (10+ digits) or email. Submitting composes a plain-text message and opens `mailto:` or `sms:`, and reveals a white "Your message is ready" panel (Lift shadow, card radius) with the message in a read-only textarea, a Copy button and plain-text fallback addresses. Clipboard is only a convenience; the text is always visible. Calling is always offered next to it.

### Why pillars and review
Pillars are a 56px gold icon disc beside a title and soft text. They are stacked on phones and three across from 900px. The review is a Sky Blue card (card radius, Float shadow) with a gold mask-drawn quote mark (`--quote-mark` SVG), the testimonial in 600 weight, and the attribution in Pale Gold 800.

### Sticky bar (phones)
A fixed Sky Deep bar with two equal buttons (gold Call, line Free quote with a gold count badge), 54px tall, padded for the safe area. It slides up (`translateY(110%)` → 0, 0.35s) only when the hero buttons have left the screen and the quote form's send buttons aren't 25% visible. Hidden from 900px.

### Footer
The footer ground is Water Deep, joining the close section's water. It holds the wordmark, the phone and email links (44px targets; middle-dot separators on desktop), and the small Water Pale line "Demo one-pager — free sample."

### Motion system
- **One shared loop:** `Loop` runs a single `requestAnimationFrame` for every living thing (both water canvases, every seam, the bubbles, the before/after intros). Register new motion with `Loop.add({tick: function(t, dt){...}}, element)`. `t` is seconds and `dt` is clamped to 50ms. Don't start another rAF.
- **Off-screen pausing:** `Loop.add` attaches an IntersectionObserver (120px margin) that switches each job on only while its element is near the viewport. The loop stops entirely when no job is on and is woken when one comes back.
- **Shared pointer:** `P` tracks mouse, pen and touch (all passive listeners), with per-frame velocity. All pointer reactions read from it.
- **Transform-only DOM updates:** bubbles move by `translate3d` and scale. Water draws on canvas. Seams rewrite SVG path data.
- **Reduced motion:** with `prefers-reduced-motion: reduce`, every job ticks once for a still frame and the loop never runs. Before/after sliders sit at 50% with no intro. CSS kills all animations and transitions (sun spin, mascot bob, jet stripes, bar slide) and smooth scrolling.
- **Phones get fewer particles** (see TUNE) and the canvas DPR is capped at 2.
- **Lively, not sleepy:** the swell and seams use three layered sines at different speeds and directions, and the swell amplitude itself breathes over time.

### Images and embedding
Photos and brand art are embedded so the page is one self-contained file. Source WebPs live in `assets/` (photos: crew, deck, walk, fence, house, siding/pavers/dumpster before and after; brand: `wordmark.webp`, `mascot.webp`). Raw originals stay in the git-ignored `src-assets/`. In the page:
- `<img data-img="NAME">` has no `src`. The LAZY PHOTOS script copies the data URI from `<script type="text/plain" id="img-NAME">` once the image is within 800px of the viewport. Those blocks sit between the `<!-- IMAGE-DATA -->` and `<!-- /IMAGE-DATA -->` markers at the end of the file, so buttons and motion work before photos arrive.
- The wordmark and mascot are CSS variables `--wordmark` and `--mascot` in `<style id="brand-art">` at the top of `<head>`.
- **To swap or add an image:** drop a `.webp` in `assets/` (named to match `data-img` / the `img-NAME` id) and run `python3 tools/embed.py`. It rewrites both the brand-art block and the IMAGE-DATA blocks from `assets/`. Never paste base64 by hand. Keep photos around 20 to 60 KB each.

## Do's and Don'ts

### Do:
- **Do** take every color from the `:root` tokens. When changing a ground color, also update the seam `data-fill` hexes and, for water, the JS body gradient in `resize()`.
- **Do** use `.btn` with `.btn-gold` / `.btn-line` for every action, in gold-then-line pairs at the same height (58px; 54px in the sticky bar).
- **Do** put `on-light` on any light-ground section so line buttons flip to Ink.
- **Do** separate every section with an animated wave seam; never a straight color edge.
- **Do** register new motion with `Loop.add` and tune speeds and counts through `TUNE`, keeping phone counts lower.
- **Do** keep touch listeners passive and draggable things on `touch-action: pan-y`.
- **Do** frame photos in the water world (bubbles, jet-washed before/after frames) and route them through `assets/` + `tools/embed.py`.
- **Do** keep navy-tinted, negative-spread shadows (`--shadow-1`, `--shadow-2`).

### Don't:
- **Don't** use black or near-black grounds; the darkest is Sky Deep (`#0a2c52`).
- **Don't** add thin decorative highlight lines or glints to buttons, bubbles or frames.
- **Don't** use hard offset or grey shadows.
- **Don't** add a second `requestAnimationFrame`, `setInterval` animation, or motion that ignores reduced motion.
- **Don't** set body or chip text below 0.9375rem, or tap targets below 44px.
- **Don't** use gold for text on cream or mist grounds.
- **Don't** add small uppercase labels above headings; the only uppercase small text is the Before / After tag.
- **Don't** make copy-to-clipboard the only way to get information; the Facebook in-app browser may block it.
