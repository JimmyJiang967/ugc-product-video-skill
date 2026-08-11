# Budget and Provider Adapters

## Keep the core provider-neutral

Describe capabilities, inputs, outputs, and acceptance criteria. Do not require one vendor's model name, internal parameter, private endpoint, credit unit, or engineering path.

Possible capability interfaces include:

- authorized image inspection;
- one composite state-sheet generation;
- continuous 15-second 9:16 video generation;
- synchronized visible speech or authorized-recording lipsync;
- final-media word-level ASR;
- timed caption rendering;
- playable-media readback.

An adapter may implement one or more interfaces. Record the adapter name in the plan and result without making it part of the generic schema.

## Cost policy

Use a configurable budget object with a unit chosen by the operator, such as credits, USD, or another currency. Do not assume a fixed conversion.

Before each paid call:

1. inspect capability and duration support without spending;
2. obtain the provider's current quote;
3. record the purpose and estimated cost;
4. compare it with the user-approved ceiling;
5. obtain explicit approval.

Default to at most one paid state-sheet generation and one paid video generation. A second paid attempt requires a new quote, defect explanation, and explicit approval. Caption-only fixes must not trigger a new video generation when the spoken video is correct.

## Async jobs and failures

Record the job ID and wait for a terminal playable result. A progress percentage is not completion. If an attempt fails after charging, record the provider's refund or void status before retrying.

Never silently switch providers, split the video into shorter paid clips, generate another presenter, or create a detached voice asset. Offer the fallback, its cost, and its quality tradeoff before proceeding.

