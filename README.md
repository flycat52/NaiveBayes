# Perceptron

Dr. Rachel Nicholson is a Professor, who lives far away from her university. So, she prefer to work at home and she only comes to her office if she has research meetings with her postgraduate students, or teaching lectures for undergraduate students, or she has both meetings and teaching:

- The probability for Rachel to have meetings is 70%, the probability of Rachel has lectures is 60%.
- If Rachel has both meetings and lectures, the probability of Rachel comes to her office is 95%.
- If Rachel only has meetings (without lectures), the probability of Rachel comes to her office is 75% because she can Skype with her students.
- If Rachel only has lectures (without meetings), the probability of Rachel comes to her office is 80%.
- If Rachel has neither meetings nor lectures, there is a only 6% chance that she comes to the office.
- When Rachel is in her office, half the time her light is off (when she is trying to hide from others to get work done quickly).
- When she is not in her office, she leaves her light on only 2% of the time since the cleaners come for cleaning.
- When Rachel is in her office, 80% of the time she logged onto the computer.
- Because she sometimes work from home, 20% of the time she is not in her office, she is still logged onto the computer.

## Requirements
Construct a Bayesian network to represent the above scenario. (Hint: First decide what your domain variables are; these will be your network nodes. Then decide what the causal relationships are between the domain variables and add directed arcs in the network from cause to effect. Finally, you have to add the prior probabilities for nodes without parents, and the conditional probabilities for nodes that have parents.)


## Prerequisite
- Python 3.6 or higher
- Please keep all the related data files in the same folder (i.e.part2).


## Running Steps
1. Open Terminal console
2. Go to the project part2 directory
3. Run command: python NaiveBayes.py spamLabelled.dat spamUnlabelled.dat
4. An output file (sampleoutput.txt) will be generated in the same project folder. Check it for the result.



