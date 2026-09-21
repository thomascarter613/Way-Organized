# EXP-004 — Prospective Prophecy Registry

## Purpose
Replace retrospective prophecy collections with timestamped falsifiable claims.

## Eligibility
A registered prophecy must specify:
- exact wording;
- claimant;
- date/time;
- target domain;
- deadline/resolution window;
- geographic scope where applicable;
- operational success criterion;
- operational failure criterion;
- authoritative resolution source.

## Preferred probability format
Claimants assign probabilities when possible.

Example:
> “There is a 70% probability that X will occur by DATE under criterion Y.”

## Prohibited after registration
- changing deadline;
- changing target;
- redefining literal claim as symbolic;
- deleting misses;
- splitting one vague claim into several successes;
- merging unrelated events.

## Public timestamp
Store:
- canonical text;
- cryptographic hash;
- immutable/public timestamp;
- version ID.

Clarifications are new records; original remains visible.

## Scoring

### Probabilistic
Brier score and calibration.

### Binary categorical
Hit/miss plus base-rate comparison.

### Rare event
Compare with:
- informed forecasters;
- prediction markets/consensus where available;
- historical base rate.

## Prophecy classes
P0 vague/unscorable  
P1 specific but retrospective  
P2 timestamped, specific  
P3 probability + fixed resolution + baseline  
P4 repeated performance significantly exceeding benchmarks

Only P3/P4 can materially update HTERP.

## Publication
Publish all registered predictions, not only hits.

## Religious neutrality
The registry can accept claims from:
- Christian prophets;
- Muslim visionaries;
- astrologers;
- psychics;
- channelers;
- secular forecasters;
under the same scoring rules.
