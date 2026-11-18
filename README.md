# Superbug Down: The Antibiotic Resistance Files
A branching terminal adventure game built in Python. Play as a researcher investigating a mysterious disease outbreak, racing to identify the bacteria responsible, trace its resistance gene, find the source, and recommend a treatment plan, before your Lab Credibility runs out.

## Features
- **Five-scene branching story** - every scene presents a real choice, and earlier decisions carry consequences into later scenes.
- **Lab Credibility system** - a tracked reputation score that rises and falls based on your choices and a little luck. Let it drop too low, and your supervisor pulls you from the case.
- **Random outcomes with a safety net** - lab tests have a genuine chance of error or failure, but capped retries and guaranteed fallbacks mean the game can never leave you permanently stuck.
- **Consequences that carry forward** - choices made early (like whether you interview a colleague for a clue) change how later scenes play out, through persistent flags.
- **Typewriter-style text** - story text is revealed character by character for a more classic old-school immersive feel.
- **Multiple endings** - the quality of your ending depends on a combination of what you discovered and the treatment plan you choose, not just one single choice.
- **Real microbiology woven into the story** - "Did you know?" facts throughout the game cover real concepts like Gram staining, beta-lactamase enzymes, and horizontal gene transfer.

## How to Play
1. Run the script in your preferred code editor or terminal.
2. Read the introduction, which explains antibiotic resistance and your mission as the researcher on the case.
3. At each decision point, type the letter of your choice (`a`, `b`, or `c`) and press Enter to continue.
4. Pay attention to your Lab Credibility, shown after each scene. Poor decisions (and some bad luck) can cost you credibility, and dropping too low ends the investigation early.
5. Reach Scene 5 and choose a treatment plan to close the case. Your ending depends on what you uncovered along the way.

## How It Works (Technical Overview)
- The game runs as a single linear script, with each scene separated by clearly labelled sections.
- Player choices are collected with `input()` and validated using `while` loops with finite retry attempts, falling back to `sys.exit()` if the player repeatedly enters invalid input.
- Boolean flags (such as `talked_to_DrGrey`, `gene_identified_independently`, and `source_found`) are set in earlier scenes and checked in later ones, allowing earlier decisions to influence later outcomes and final endings.
- Random chance is handled with Python's built-in `random` module, using `random.randint()` for lab test outcomes.
- `lab_credibility` is a running score adjusted throughout the game, with tiered messages and a threshold check that can end the game early if credibility drops too low.
- A custom `typewriter()` function uses `time.sleep()` to reveal story text character by character, rather than printing it all at once.

## Requirements
- Python 3
- No external libraries - uses only Python's built-in `random`, `sys`, and `time` modules

## Running the Game
```
python terminal_game.py
```

## Author's Note and Disclaimer
This game was built to be more than just a terminal adventure. It's meant to be something anyone can play and enjoy, while also understanding real knowledge about antibiotic resistance: how researchers investigate disease outbreaks, how bacteria are tested and identified, and how they can develop resistance to antibiotics over time.

**This is a work of fiction, not a medical or scientific reference**. The "Did you know?" fun facts throughout the game are accurate to real microbiology, and some aspects of the adventure (like E. coli and the blaCTX-M resistance gene) are based on real organisms and real genes. However, the overall storyline, characters, specific events, and outcomes are fictionalised for the sake of gameplay and **should not be taken as an accurate account of how a real outbreak investigation would unfold**. 

In reality, sequencing protocols are much more detailed and time-consuming than the game shows. A real investigation is also not carried out by one researcher alone. Many professionals are involved when an outbreak happens, not just a doctor and a researcher. This game simply aims to give people without a scientific background a glimpse of the process, to introduce antibiotic resistance and how it affects healthcare, and, hopefully, to make players curious enough to learn more about it after they have played.

I made this as my first Python checkpoint project, when I had just begun learning Python, so it only uses what I had learned by then: variables, control flow, loops and a few modules.
