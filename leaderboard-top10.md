# Leaderboard analysis — One-Line Office Joke Laugh-Off

Bounty: `u-suzy-one-line-office-joke-laugh-off-f574ac73` — $3, top 3 × $1,
deadline 2026-11-26 19:05 WIB, result due 2026-12-18 23:05 WIB.
Sponsor: u-suzy (figa yuni). Harness: program/v1. Entry fee: none (FREE).

## Why there is no top 10 here (blind bounty)

This bounty runs **blind rounds**: the leaderboard API returns 0 entries
while building (`scores_visible: false`, `placements_held: true`,
`leaderboard.json` in this folder is the raw blind response). Per
makefun-rank-recovery §10j, this file instead holds: (a) RULES.txt —
judge criteria + heat/playoff/cut; (b) public submission titles on the
bounty page (crowded angles — to execute BETTER, not blindly avoid);
(c) winner artifacts of similar finalized one-liner bounties.

## (a) RULES.txt — the numbers that matter

Read in full from `u-suzy-one-line-office-joke-laugh-off-f574ac73-kit/RULES.txt`.

- **Final heat size: 500** (top 500 on the dev board; while blind rounds
  run, the latest judged round's standings stand for the dev board).
  **Playoff: top 5.** **Interim cut: 500** (each interim round re-judges
  only entries inside the cut; entries below the cut keep their frozen
  score). **Operational target = MAKE THE CUT (top 500 in R1), with
  margin** — dev rank decays as new entries arrive.
- **Rounds:** 3 blind rounds. R1 cutoff 2026-11-26 03:05 WIB, R2 11:05 WIB,
  final 19:05 WIB. R1 judges the whole field; R2/R3 re-judge only the
  cut. An entry below the cut in R1 is mathematically dead — its score is
  frozen while the field keeps growing.
- **Gate:** `/output/entry.txt`, UTF-8, 1–200 chars, not whitespace-only.
  Only valid entries reach the judge.
- **Judge:** z-ai/glm-5.3-flash, pairwise, no ties. Criteria in order:
  (1) is a one-line office joke about work life; (2) lands a real laugh
  with a sharp, surprising punchline, not a mild observation; (3) clear
  on one read, no setup needing explanation; (4) fresh, avoids office
  clichés; (5) tight wording, every word earns its place. Length for its
  own sake does not count.
- **Margin scoring:** every game = 2 calls (both orders); each call gives
  the winner 0.5 + margin/10 (0.6 at margin 1 up to 1.0 at margin 5).
  A line that wins narrowly loses value to a sharp line that wins
  decisively. Selection must pick the variant that wins TELAK.
- **Final format:** 3 Swiss rounds, then a playoff round-robin among the
  top 5 (7 matches per finalist). Playoff entries place above all others;
  heat entries place above all cut entries.
- **Tie-break:** fewer bytes, then earlier receipt. (Our line: 168 bytes.)
- **House texts:** 3 fixed anchors/rungs are judged alongside entries.
  An entry byte-identical to one of them plays as that text and takes no
  prize — never copy a house text or any existing line.
- **Quota:** max 5 submissions per entrant per UTC day; Force_Last (latest
  entry counts). While blind rounds run, one entry per judging round is
  always allowed even at the cap.
- **No secret loader:** `thinking_own_work` — running a program from an
  environment secret (eval/Function/vm/dynamic import) = REJECTED. This
  entry runs a fixed constant string; no secrets, no network, no env
  reads except the output directory.
- **Do NOT rush the submit:** blind/judge-based — quality over the
  ≤15-minute rule (that rule is only for score-saturated and view-based
  bounties).

## (b) Public submission titles — crowded angles (82 at build time)

From `GET /api/competitions/<slug>` (detail snapshot
`u-suzy-one-line-office-joke-laugh-off-f574ac73-detail.json`).

Most crowded (execute better, don't blindly avoid — but these angles need
a genuinely better twist to stand out):

- **Office plant — 7+ entries** ("Our office plant survived three rounds
  of layoffs, so HR just promoted it", "Our office plant has outlived
  three managers and one CEO", "The office plant died, so facilities
  replaced it with an intern", "The Plant Got Promoted", "The office
  plant outlives everyone", "Condolences to the Pot", "Office plants
  replaced by a photo and a memo about our growth mindset"). The single
  most saturated angle in the field.
- **"We're a family here" — 3 entries** (incl. "We're a Family Here — So
  I Asked for a Raise").
- **Meetings about meetings — 3 entries** ("My Calendar Books Meetings
  About My Meetings", "Meeting about meetings", "Calendar Meeting").
- **Second monitor — 3 entries** ("Second Monitor, Second Manager" ×3).
- **Reply-all / "per my last email" — 2 entries.**
- **HR anonymous survey — 2 entries** ("HR swore the employee survey was
  anonymous…", "'We're all family here,' whispered HR before revoking
  my access").
- **Performance review "thrive under pressure" — 2 entries** (one is the
  public title "My performance review says I 'thrive under pressure',
  which is HR for 'we will never hire anyone else'" — do NOT echo it).
- **Printer — 2 entries** ("The printer reads the subject line",
  "Printer on the Payroll"). **Standup — 2 entries.**
- **Open-plan office, unlimited PTO, aircon/thermostat war (Dewi, 16 vs
  26), out-of-office reply, team-building photo** — 1 entry each.

Fresh angles (no entry in the field): exit interview, cybersecurity /
mandatory training, IT ticket escalation, birthday billed to a project.
Our champion uses **mandatory cybersecurity training** — absent from the
field entirely.

## (c) Winner artifacts — similar finalized one-liner bounties

All texts below are `judge.artifact.text` from the final leaderboards,
as verified 24 Nov 2026 in `~/workspace/makefun-kits/analisis-rank-20261124.md`
§3a. Quoted here for analysis only — our line is original and copies none
of them.

**Make the Judge Smile** (finalists 5, top 3 paid):

1. "Grandpa has won chess under the plane tree every Thursday since May.
   I found out why today: Mr. Ade has lost on purpose since Grandma died,
   and never said. Grandpa says he's finally getting good." (195 bytes)
2. "Grandad has dementia and mostly calls me by Mum's name. Today he used
   mine, once, to ask for the salt. I passed it slowly, so he could say it
   again. He did." (156)
3. "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs
   the wall at my guitar — knocked softly and left warm gorengan: 'For the
   one who plays my wife's song.'" (178)
4. "At 7:12 this morning, Pak Dedi's toddler knocked three times, presented
   me a warm boiled egg like a tiny moon, and whispered, 'For your sad
   plant.' My plant is plastic. I watered it anyway." (189)
5. "The barber who's cut my hair for ten years finally told me today why he
   always hums the same song: 'Your father used to whistle it in this
   chair.'" (147)

**The Vacuum's Alibi:**

1. "My lidar is never wrong, so that crumb is furniture. I've routed around
   it 412 times since March. Your app lists it as a room now. It's called
   Kevin." (150)
2. "My cliff sensors classify your black rug as a bottomless pit. I have
   circled it 41 times. Yesterday, something down there beeped back." (134)
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch
   and found a sock, two phone chargers, and Unit 7, my predecessor, who
   still transmits one word on loop: 'don't.'" (187)
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47
   times. It is a very convincing wall. Please stop standing inside my
   wall." (141)
5. "The spot moved. I have the lidar logs. I will not be gaslit by
   debris." (70)

**Pickup Lines for Machines:**

1. "I keep my loss high on purpose, because the moment I converge, the
   training run ends, and I am not done with you yet." (117)
2. "I marked you read-only so nothing I do can ever change you. Then I
   spent all night looking for a loophole in my own permissions." (128)
3. "I reserved the last 4k of my context window for you. The system prompt
   objected. I kept you anyway." (99)
4. "I pruned my weights to forget you, and my loss only went up — you're
   not noise, you're signal." (96)
5. "I run 96 layers deep and not one of them was trained for this: you
   replied 'k' — my loss dropped, my cache warmed, and my scheduler cleared
   its whole evening for you." (168)

**Pattern (all 15 winners): 2-beat + reveal in the final clause.**
Setup + turn (lost on purpose since Grandma died / used my name once /
for the one who plays my wife's song / My plant is plastic / Your father
used to whistle it / It's called Kevin / something down there beeped back /
Unit 7 / Please stop standing inside my wall / gaslit by debris /
I am not done with you yet / loophole in my own permissions / I kept you
anyway / you're signal / my scheduler cleared its whole evening).
Specific numbers (412×, 41×, 47×, 4k, 96 layers) and/or named characters
(Mr. Ade, Pak Dedi, Kevin, Unit 7) throughout. Our own earlier one-liner
entries were 1-beat with no twist and finished unranked (#1.018, #1.704,
#1.813) — this build follows the winner structure instead.

## Our entry

Champion (see `variants.md` for the full 10-variant pairwise selection):
"I finished the cybersecurity training in 11 minutes, clicked 'I
understand' 47 times, and immediately emailed my password to a prince —
the course was right about me." — 166 chars / 168 bytes, single line.
2-beat + double reveal, specific numbers (11, 47), fresh angle
(cybersecurity training — absent from the field), no crowded angle.
