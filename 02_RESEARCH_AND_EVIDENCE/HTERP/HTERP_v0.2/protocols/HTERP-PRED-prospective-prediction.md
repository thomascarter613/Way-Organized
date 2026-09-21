# HTERP-PRED — Prospective Prediction Protocol

## Purpose
Create a prediction corpus immune to the principal weaknesses of retrospective prophecy.

## Required prediction record

- prediction ID
- claimant/source
- exact timestamp
- immutable hash/archive location
- exact wording
- target domain
- geographic scope
- start date
- end/resolution date
- probability if claimant permits probabilistic forecast
- operational success criterion
- operational failure criterion
- authoritative resolution source
- allowed ambiguity: none beyond preregistered rules

## Example structure

Bad:
> “A great leader will fall soon.”

Good:
> “Before 2028-01-01, officeholder X will cease to hold office for reason category Y.”

Better:
> assign a numerical probability and predefined resolution source.

## Scoring

Binary probabilistic forecasts:
- Brier score
- calibration curves
- discrimination versus base rate

Nonprobabilistic religious predictions:
- exact hit / partial / miss according to preregistered rubric
- partial credit only if defined before outcome

## Anti-retrofit rules
Prohibited after timestamp:
- changing target identity;
- extending deadline;
- redefining metaphor;
- merging separate predictions;
- discarding misses;
- claiming symbolic fulfillment when literal fulfillment was originally expected.

## Baseline comparison
Predictions must be compared against:
- base rates,
- informed non-prophetic forecasters,
- naive chance,
- broadness/specificity penalty.

## Evidence ladder
PRED-0 retrospective only  
PRED-1 timestamped but vague  
PRED-2 specific and timestamped  
PRED-3 specific + probability + preregistered resolution  
PRED-4 repeated superior performance against benchmarks

Only PRED-3/4 materially updates transcendent hypotheses.
