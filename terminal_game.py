# ----------------------------------------------------------------------------------------------------------------------------------------------------
# SUPERBUG DOWN: THE ANTIBIOTIC RESISTANCE FILES📂
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Importing all the modules required for this adventure
import random
import sys
import time

# For a typewriter effect on the games text, setting it to 0.06 secs
def typewriter(text, delay = 0.06):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()             

# Brief the player about their mission and give them an introduction about what the game is about and any rules they need to follow while playing the game
intro = """INTRODUCTION - What\'s Going On?

Before you start, here\'s what you need to know: 

Antibiotics are medicines that kill bacteria or stop them from growing - they\'ve saved millions of lives since the 1940s.
But bacteria can evolve.

Every time antibiotics are used, a few bacteria may survive because they carry a random genetic mutation (or a gene that they picked up from another bacterium) that protects them. Those survivors multiply, and eventually evolve into a population of bacteria that no longer responds to that antibiotic. This is called Antibiotic Resistance, and it\'s one of the biggest threats in modern medicine. The World Health Organisation (WHO) has flagged it as a top global health concern🚩.
"""

typewriter(intro)

mission = """Your mission: People in a nearby town have fallen ill with an infection that regular antibiotics are unable to cure. As the Researcher on the case, you will need to: 
(1) Meet with the attending doctor to collect patient samples and decide how to start your investigation
(2) Run lab tests to identify the bacteria responsible for the infection
(3) Sequence the bacteria\'s DNA to find the resistance gene 
(4) Investigate to find where the outbreak actually started
(5) Decide on a full treatment plan to close the case

 """
typewriter(mission)

credibility_explainer = """You are the researcher assigned to this case, working independently to investigate the outbreak.
As you work, your reputation with the hospital is tracked as your Lab Credibility, starting at 100. Poor decisions can cost you credibility, and if it drops too low, your supervisor will pull you from the case entirely, so choose wisely❗

"""
typewriter(credibility_explainer)

how_to_play = """A quick note on how to play: whenever you\'re asked to type a choice (like "a" or "b"), type it and press the \'Enter\' key on your keyboard to submit your answer and continue.

"""
typewriter(how_to_play)

# Assigning lab credibility to variable
lab_credibility = 100

input("Press Enter to begin...")
start = """
Your adventure starts now...

"""
typewriter(start)

print(f"Your current Lab Credibility is: {lab_credibility}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SCENE 1 - THE HOSPITAL: Collecting Samples
print("""

SCENE 1 - THE HOSPITAL: Collecting the Patient Samples 
""")

scene1 = """You\'re called to the local hospital🏥. 
Several patients have a bacterial infection that isn\'t responding to the standard antibiotic medicine, Penicillins (e.g. Amoxicillin). The attending doctor, Dr. Grey, wants your help😟.

"""
typewriter(scene1)

fact1 = """Did you know?🤔
Not all bacteria are dangerous - many live in and on our bodies harmlessly, or even help us (like gut bacteria that aid in digestion). It\'s only certain species of bacteria🦠, or certain resistant strains, that cause serious illness, like salmonella which causes foodborne infection, food poisoning, stomach cramps, fever and diarrhea.

"""
typewriter(fact1)

# Ask the player what their first move is going to be after going to the hospital
quest1 = """Now that you\'re at the hospital🏥, you meet Dr. Grey who hands you the patient samples. 
You have two choices:
(a) Interview Dr. Grey about the patient\'s symptoms
(b) Go straight to the lab to test patient samples

What do you decide to do?

"""
typewriter(quest1)

# Saving the answers in respective variables 
a = "(a) Interview Dr. Grey about the patient\'s symptoms"
b = "(b) Go straight to the lab to test patient samples"


# Prompt the player to enter their choice and print the choice they made
answer1 = input("Enter your choice (a or b), then press Enter:  ").strip().lower() # added strip incase player adds any spaces by mistake and lower so that player can input in both lower and uppercase, their response will be converted to lowercase anyways for smoother game flow
print(f"You chose {answer1}")

talked_to_DrGrey = False
attempt = 0

while (answer1 != "a" and answer1 != "b") and (attempt < 2):
    print("Hmm, did you choose between a or b?")
    attempt += 1
    attempt_remaining = 3 - attempt
    attempt_word = "attempt" if attempt_remaining == 1 else "attempts"
    print(f"You have {attempt_remaining} {attempt_word} left.")
    answer1 = input("Enter your choice (a or b), then press Enter:  ").strip().lower()

if answer1 == "a":
    print(a)
    optiona = "✅ Great, Dr. Grey mentions that most of the patients live in the same suburban neighborhood, and something clicked for him: there was a water main break on that street about a week before symptoms started. The city issued a 🚱 boil-water advisory at the time, but he\'s not sure how many residents actually followed it before the all-clear was given. That timing feels like more than a coincidence to him 🤔."
    typewriter(optiona)
    talked_to_DrGrey = True

elif answer1 == "b":
    print(b)
    optionb = "⚠ Faster, but you missed a crucial clue about the source of the outbreak. You'll have to work it out later."
    typewriter(optionb)
    lab_credibility -= 10
    print("📉 Lab Credibility -10")

else:
    print("Mission failed! Play again")
    sys.exit() 

print(f"""
Your current Lab Credibility is: {lab_credibility}""")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SCENE 2 - THE LAB: Identifying the Bacteria
print("""

SCENE 2 - THE LAB: Identifying the Bacteria 
""")

scene2 = """You take the patient samples and run them through some basic tests to figure out which bacteria you\'re dealing with.

"""
typewriter(scene2)

fact2 = """Did you know?🤔
Scientists often use a Gram stain (a purple dye test🟣) as one of the first quick steps to sort bacteria into broad groups before doing more detailed testing. Gram stain testing is over 140 years old and still used today as an initial step before more detailed testing.

"""
typewriter(fact2)

# Ask the player what test they're going to do after going to the lab
quest2 = """How do you plan on Identifying the Bacterial species that is responsible for the outbreak?
You have two choices:
(a) Run a culture-based test (grow the bacteria on a plate and see if it survives exposure to antibiotics)
(b) Run a genetic test to identify which species of bacteria is causing the infection (e.g is it Klebsiella? Salmonella? E.coli?) 

What do you decide to do?

"""
typewriter(quest2)

# Saving the answers in respective variables 
a = "(a) Run a culture-based test "
b = "(b) Run a genetic test to identify which species of bacteria is causing the infection"

# Prompt the player to enter their choice and print the choice they made
answer2 = input("Enter your choice here a/b?:  ").strip().lower()
print(f"You chose {answer2}")

#Assigning variables
attempt2 = 0
success_culture = "Under the microscope🔬 and through biochemical testing🧪, the culture is confirmed to belong to Escherichia coli (E.coli)🦠 species, a well known bacterium that is often progressively resistant to antibiotics."
success_genetic ="genetic tests come back with the species ID identified as Escherichia coli (E.coli)🦠, which is a well known bacterium that is often progressively resistant to antibiotics."


while (answer2 != "a" and answer2 != "b") and (attempt2 < 2):
    print("Hmm, did you choose between a or b?")
    attempt2 += 1
    attempt_remaining = 3 - attempt2
    attempt_word = "attempt" if attempt_remaining == 1 else "attempts"
    print(f"You have {attempt_remaining} {attempt_word} left.")
    answer2 = input("Enter your choice here a/b?:  ").strip().lower()

if answer2 == "a":
    print(a)
    typewriter(f"🧫 Great, you run a culture-based test by growing the bacteria on a culture plate with antibiotics to see if they survive. This is called an Antibiotic Susceptibility test - slower, but very reliable. You confirm that the bacteria don\'t respond to Penicillins at all. {success_culture}")
    lab_credibility -= 5
    print("📉 Lab Credibility -5")    

elif answer2 == "b":
    print(b)
    optionb = "Faster, but genetic tests can occasionally return unclear results with the random chance of needing a repeat.😟"
    typewriter(optionb)

    input("Press Enter to run the genetic test... ")
    repeat = random.randint(1, 10)
    retry_attempt = 0
    while repeat > 7 and retry_attempt < 2:
        retry_attempt += 1
        reattempt_remaining = 3 - retry_attempt
        attempt_word = "attempt" if reattempt_remaining == 1 else "attempts"
        typewriter("😬 Uh oh, looks like the results from the genetic test returned inconclusive. You\'ll have to rerun the test.")
        print(f"You have {reattempt_remaining} {attempt_word} left.")
        input("Press Enter to rerun the test... ")
        lab_credibility -= 5
        print("📉 Lab Credibility -5")
        repeat = random.randint(1, 10)  # new roll each time through this nested while loop, so that each retry is an independent chance that 70% the player will succeed

    if repeat <= 7:
        typewriter(f"Lovely, the {success_genetic}")
        lab_credibility += 5
        print("📈 Lab Credibility +5")

    else:
        typewriter(f"After two unclear results, you send the sample to a senior colleague for manual confirmation, it takes longer, but you get your answer.😥 The {success_genetic}")
        lab_credibility -= 10
        print("📉 Lab Credibility -10")

else:
    print("Mission failed! Play again")
    sys.exit()

print(f"""
Your current Lab Credibility is: {lab_credibility}""")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SCENE 3 - THE SEQUENCING LAB
print("""

SCENE 3 - THE SEQUENCING LAB: Finding the Resistance Gene from the identified Bacterium
""")

scene3 = """ Now that you know the species of the bacterium causing the infection (E.coli)🦠, you sequence its DNA 🧬 specifically to find what is making it resistant to the antibiotics.

"""
typewriter(scene3)

fact3 = """Did you know?🤔
One common resistance mechanism is a gene that makes an enzyme called Beta-lactamase, which literally breaks apart the antibiotic molecule before it can work (basically, it breaks down the antibiotic to remove it from the surrounding environment, which allows it to then grow and multiply normally). Other bacteria have special pumps in their cell wall that shove the antibiotic back out of their cells before it can do any damage.
"""
typewriter(fact3)

# Ask the player what their first move is going to be after going to the sequencing lab
quest3 = """Now that you know that the bacterium is E.coli, you have to run a sequencing test on its DNA 🧬 to find exactly what\'s making it resistant. 

You have loaded the sequencer with the DNA 🧬 of the bacterium from your patient samples.
Your choices:
(a) Run the sequencer at standard speed
(b) Run the sequencer at high speed
"""
typewriter(quest3)

# Saving the answers in respective variables 
a = "(a) Run the sequencer at standard speed"
b = "(b) Run the sequencer at high speed"

# Prompt the player to enter their choice and print the choice they made
answer3 = input("Enter your choice here a/b?:  ").strip().lower()
print(f"You chose {answer3}")

# Assign variables
success_threshold = 0
attempt3 = 0
attempt = 0
gene_identified_independently = False
gene_identified = False
identified = "The test identified the specific resistance gene as \'blaCTX-M\' known to produce a shield that destroys basic Penicillins!"

# Turning players choice into a cutoff number that decides success or failure
while (answer3 != "a" and answer3 != "b") and (attempt3 < 2):
    print("Hmm, did you choose between a or b?")
    attempt3 += 1
    print(f"Attempts left: {2 - attempt3}")
    answer3 = input("Enter your choice here a/b?:  ").strip().lower()
    print(f"You chose {answer3}")
if answer3 == "a":
    success_threshold = 6
elif answer3 == "b":
    success_threshold = 4
else:
    print("You didn\'t choose a valid option. Game over!")
    sys.exit()

# Prompt player to run the sequencer
input("Press Enter to run the sequencer... ")

if answer3 == "a":
    typewriter("The sequencer whirs to life...running at standard speed. Reliable, but might take a while.😬")
elif answer3 == "b":
    typewriter("You push the sequencer to its limits, it hums louder than usual. Results should come quickly...assuming nothing goes wrong.😬")


while not gene_identified and attempt < 3:
    roll = random.randint(1, 10)
    if roll <= success_threshold:
        gene_identified_independently = True
        gene_identified = True
        typewriter(f"😁 Great, {identified}")
        lab_credibility += 5
        print("📈 Lab Credibility +5")
    else:
        attempt += 1
        attempts_remaining = 3 - attempt
        typewriter(f"The sequencer couldn\'t identify the gene on attempt {attempt} due to insufficient DNA sample 😬. Attempts remaining: {attempts_remaining}")
        lab_credibility -= 5
        print("📉 Lab Credibility -5")
        if attempts_remaining > 0:
            input("Press Enter to add correct amount of DNA 🧬 into the sequencer and let\'s run it again and see if we get lucky🤞...")
        else:
            typewriter("Unfortunately, you don\'t have any more DNA 🧬 left from the patient samples😞. Play again.")        
        
if not gene_identified:
    typewriter(f"You couldn\'t identify the gene in time, but a colleague helps you😥. {identified}")
    gene_identified = True
    lab_credibility -= 10
    print("📉 Lab Credibility -10")

print(f"""
Your current Lab Credibility is: {lab_credibility}""")

if lab_credibility <= 50:
    print("⚠ Careful, your credibility is running low📉, and further mistakes could end your investigation😟.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SCENE 4 - TRACING THE SOURCE

print("""

SCENE 4 - TRACING THE SOURCE
""")

scene4 = """Armed with the species (E.coli) and the resistance gene (blaCTX-M), you head out to find where the outbreak actually started🔎.

"""
typewriter(scene4)

fact4 = """Did you know?🤔
Antibiotic resistance genes don't just spread by bacteria multiplying - bacteria can also swap resistance genes directly with each other through a process called Horizontal Gene transfer (each bacterium sends out a tube-like extension which connects in the middle and they use it as a pipe to transfer the genetic material between each other). This process can occur even between different species of bacteria.

"""
typewriter(fact4)

# Ask the player how they're going to find the source
quest4 = """You need to figure out the source of the outbreak.
You have two choices:
(a) Test the neighborhood\'s water supply
(b) Test the local food supply instead 

What do you decide on?
"""
typewriter(quest4)

# If player had spoken to Dr. Grey in scene 1 (chose optiona), remind them the hint that was given
if talked_to_DrGrey:
    typewriter("Good thing you spoke to Dr. Grey earlier at the hospital - he mentioned a water main break on the street in the neighborhood the patients live in. That should make testing the water the faster route 🤔.")


# Prompt the player to enter their choice and print the choice they made
answer4 = input("Enter your choice here a/b?:  ").strip().lower()
print(f"You chose {answer4}")

# Assigning variable
source_found = False

if not talked_to_DrGrey and answer4 == "a":
    typewriter("✅ Well, you go to the water supply site and look around to figure out what the source might be. After spending an hour searching, you find some contaminated runoff near an old pipe. A worker there tells you that there was a water main break the previous week, and the city had issued a 🚱 boil-water advisory. ")
    source_found = True
elif talked_to_DrGrey and answer4 == "a":
    typewriter("👍 Great detective work! You find contaminated runoff near an old pipe quickly.")
    source_found = True
    lab_credibility += 5
    print("📈 Lab Credibility +5")
elif talked_to_DrGrey and answer4 == "b":
    typewriter("⚠ Uh oh, despite Dr. Grey\'s tip, you decided to check the food supply first anyway - maybe you want to rule it out, or maybe you don\'t trust the connection yet. Either way, you go to the local food supply and collect a \'red herring\' to take back to the lab and test whether it\'s the source. It comes back clean, maybe Dr. Grey\'s intuition wasn\'t wrong🤔...")
    # even though the player got the hint, they chose food anyway, I wanted to be a little cheeky so the "Dr. Grey's intuition wasn't wrong" line 😏
    lab_credibility -= 20 # stakes are higher
    print("📉 Lab Credibility -20")
elif not talked_to_DrGrey and answer4 == "b":
    typewriter("You go to the local food supply and collect a \'red herring\' to take back to the lab and test whether it\'s the source. It comes back clean, 🤔 maybe the source of the outbreak is something else?🤷‍♀️")
    lab_credibility -= 5
    print("📉 Lab Credibility -5")
else:
    print("You didn\'t choose a valid option. Game over!")
    sys.exit()

print(f"""
Your current Lab Credibility is: {lab_credibility}""")

if lab_credibility <= 50:
    print("⚠ Careful, your credibility is running low📉, and further mistakes could end your investigation😟.")

if lab_credibility < 30:
    typewriter("🚨Your supervisor pulls you from the case because of low credibility📉.")
    sys.exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SCENE 5 - THE TREATMENT PLAN

print("""

SCENE 5 - THE TREATMENT PLAN
""")

scene5 = """With everything gathered, you now have to recommend a full treatment plan. This is the key decision of the case.

"""
typewriter(scene5)

fact5 = """Did you know?🤔
Doctors sometimes need to prescribe a stronger or different class of antibiotic 💊 when the first one fails, but overusing strong antibiotics can encourage even that one to lose effectiveness over time, so they\'re used carefully, not automatically.

"""
typewriter(fact5)

# Ask the player what their move is going to be 
quest5 = """At this stage of the case, you are now equipped 🩺 with the information from your investigation. What is your treatment plan? 🤔
Your options:
(a) Treat patients with a stronger, targeted antibiotic and decontaminate the water source
(b) Only treat the patients
(c) Only decontaminate the source of the outbreak

What do you choose?

"""
typewriter(quest5)

# Saving the answers in respective variables 
a = "(a) Treat patients with a stronger, targeted antibiotic and decontaminate the water source"
b = "(b) Only treat the patients"
c = "(c) Only decontaminate the source of the outbreak"

# Prompt the player to enter their choice and print the choice they made
answer5 = input("Enter your choice here a/b/c?:  ").strip().lower()
print(f"You chose {answer5}")

# Assigning variables
attempt = 0

while (answer5 != "a" and answer5 != "b" and answer5 != "c") and (attempt < 2):
    attempt += 1
    print(f"That\'s not a valid option. Attempts left: {2 - attempt}")
    answer5 = input("Enter your choice here a/b/c?:  ").strip().lower()
if answer5 == "a" and gene_identified_independently and source_found:
    typewriter("""🎉Brilliant! You report back to Dr. Grey with your findings and suggest that the patients can be prescribed Carbapenems like Meropenem 💊 (which have a uniquely reinforced chemical structure that these resistant genes aka molecular scissors ✂ cannot cut). This successfully clears the infection from the patient\'s bloodstream.
    Then you get the water supply workers to decontaminate and clean the water main area 🚰, so this pathogen doesn\'t pose anymore future threats to the community. 
    You successfully treated the outbreak and removed its source! Before closing the case, you also warn local health officials, recommending they continue monitoring the area for any signs of resistance developing again. Bacteria can keep evolving even after an outbreak is resolved, so staying alert is an ongoing responsibility, not a one-time fix.""")
    lab_credibility += 15
    print("📈 Lab Credibility +15")
elif answer5 == "a" and (gene_identified_independently or source_found):
    typewriter("👍 You report back to Dr. Grey and suggest that the patients are prescribed another stronger antibiotic 💊. And you make sure that the water main area 🚰 is cleaned and decontaminated, to prevent future outbreaks. ")
    lab_credibility += 5
    print("📈 Lab Credibility +5")
elif answer5 == "a" and not (gene_identified_independently or source_found):
    typewriter("🤔 You suggest treating patients with a stronger antibiotic, based on the gene your colleague helped you identify after your own tests came back inconclusive. Since your investigation pointed you towards the food supply and didn\'t actually reveal the true source of the outbreak😞, you have the food supply workers thoroughly clean and inspect their facility. The patients recover, but the true source of the outbreak remains untouched, meaning it could resurface again down the line😟.")
elif answer5 == "b":
    typewriter("You report back to Dr. Grey and suggest that the patients are prescribed another stronger antibiotic like Meropenem 💊. The patients begin to recover but the source remains, risking future outbreaks.")
elif answer5 == "c":
    typewriter("You get the water supply workers to decontaminate and clean the water main area 🚰. But the patients continue to suffer without getting the proper antibiotic treatment😞.")
else:
    print("You didn\'t choose a valid option. Game over!")
    sys.exit()

print(f"""
Your current Lab Credibility is: {lab_credibility}""")

if lab_credibility >= 100:
    typewriter("🎉 You close the case with your reputation stronger than when you started🥳. This was a model investigation👏.")
elif lab_credibility >= 70:
    typewriter("👍 You close the case with your reputation intact. Solid work overall.")
elif lab_credibility >= 30:
    typewriter("You close the case, but your reputation took a real hit along the way 😬. Better luck next time.")
else:
    typewriter("You barely close the case with your reputation intact 😅. It was a rocky investigation, but you made it through.")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ENDING / PLAY AGAIN

typewriter("""
CASE CLOSED📁.
""")

# Ask the player if they'd like to play again
again = input("Would you like to play again? (yes/no):  ").strip().lower()

if again == "yes" or again == "yep" or again == "yeah":
    print("Great! Let\'s run the program again to play 🔁.")
elif again == "no" or again == "nope" or again == "nah":
    print("Thanks for playing. Stay curious about the microscopic world!🔬🦠👋")
else:
    print("Not sure what that means, but thanks for playing either way!👋")



