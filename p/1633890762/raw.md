<!--
name: wicked array
peek: Dice math. An alternative way of rolling characters in 5E.
tags: homebrew dnd
date: 1633890762
-->

## standard

4d6 drop the lowest is biased and lacks control and predictability.

- Some characters will have a maxed out stat at level 1. All you need is a +2 racial and a pinch (1d10) of luck.
- Others will end up too well-rounded, leaving no opportunity to exaggerate their flaws via stats.
- Someone will roll everything below average and feel even more left out.

Rolling dice is exciting and simply is not worth giving up for the standard array.

See [anydice](https://anydice.com/program/24b28).

```
W: [highest 3 of 4d6]

ABILITIES: 6 d (W)
loop A over {1..6} {
    output (A @ ABILITIES) named "Ability [A]"
}
```

## wicked

- Roll 3d10 and write down the highest. Repeat six times.
- Take a value from (1 2 3 4 5 6) and add it to a roll of your choice. Repeat for each stat. Each value can only be used once. Each roll can only receive one bonus value.

See [anydice](https://anydice.com/program/24b25).

```
W: [highest 1 of 3d10]

ABILITIES: 6 d (W)
loop A over {1..6} {
    output (A @ ABILITIES + (7 - A)) named "Ability [A]"
}
```

- De-emphasises dice rolls while keeping them exciting.
- Players have more control. They can either focus on the primary ability or settle for a more balanced build.
- The resulting values are more befitting of a novice adventurer and allow for a better sense of progression.
- Both strengths and flaws are more prevalent.

The total is 68.9 (59-78) compared to 73.5 (61-86).

The 4 point decrease in power is negated by the fact that players can bring stats to even breakpoints via the bonus array.

Variability between totals is also reduced by 4 points.
