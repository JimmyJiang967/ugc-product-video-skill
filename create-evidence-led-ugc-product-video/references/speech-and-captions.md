# Synchronized Speech and Final-Media ASR Captions

## Direct one embodied performance

Define one listener behind the phone, one reason to speak now, the current activity, and a small product-triggered reaction. Use restrained breathing, blinking, eye shifts, grip adjustments, and body-weight changes motivated by the product action.

For English, target roughly 22–32 words in 15 seconds. Prefer one connected observation with uneven clause lengths and one 0.25–0.45 second pause. Avoid feature-list cadence, repeated brand names, hard CTA rhythm, generic intros, and personal experience claims without an authorized testimonial.

Generate the visible performance and speech together. If unavailable, use only an authorized recording that drives the visible mouth. Do not add detached narration to a talking presenter.

Describe performance rather than imitating a real person:

- language and locale when requested;
- conversational register and lightly varied pitch;
- energy curve linked to product actions;
- natural breaths and a relaxed ending;
- ordinary room acoustics and phone-camera distance;
- mouth, gaze, hand, and product-action timing.

Judge the returned voice with music muted. Reject even, breathless, announcer-like, emotionally detached, or visibly unsynchronized delivery.

## Generate captions from the final media

Finish the spoken video and final mix first. Transcribe the final media or its unchanged final speech track with real ASR. The draft script may be used only for meaning comparison, never as transcript or timing.

Require word-level timestamps. When an adapter returns only sentence or phrase cues, obtain word timestamps from the unchanged speech before segmentation.

Use `word_timed_microphrases`:

- start at or immediately after the first audible word; maximum early tolerance 0.05 seconds;
- do not expose a word whose spoken start is more than 0.60 seconds after card appearance;
- split on semantic boundaries, breaths, and pauses of about 0.25 seconds or longer;
- normally use 2–6 English words per card and no more than two lines;
- normally keep cards about 0.4–1.8 seconds, with a 0.1–0.2 second reading tail when it does not cover the next phrase.

Default to adaptive lower-center placement. Keep the bottom and right platform UI zones clear and move cards to avoid the product, visible mouth, hands, labels, controls, and hero action.

Use restrained medium-bold sans-serif text, high contrast, a dark outline or soft shadow, and at most one quiet keyword accent per card. Avoid dense decoration, large opaque boxes, and persistent character-by-character karaoke.

After rendering, watch the entire result at normal speed and with music muted. Verify transcript, first-word onset, future-text exposure, readable duration, two-line maximum, safe areas, avoidance, mouth/action sync, and absence of flashing cards.

If reliable ASR or caption rendering is unavailable, disclose an uncaptioned partial result or obtain approval for another real-ASR adapter. Never fabricate timestamps from the script.

