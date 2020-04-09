# breakme
stupid automated Caesar's Cipher

With this cipher you'll be able to astonish your geek friends. 
Tell them you've built AI capable to find the correct decrypted string between a puzzling bunch of random sentences.
To get the encrypted string run the program with a meaningful sentence and then copy one of the generated string
(or simply write down a pointless one like "Dobxq arab jxab qefp").
Run again the program and plug in the string (between quotation marks) and press enter to see the magic.

If you are so sorrowful to get to this point then I must explain how this works. Trust me this is not funny for your life.
Letters in vocabulary have a certain frequency so if we compare this recurrence with the frequency in our sentence and plug these values in entropy formula we'll get a number that tells us how much this sentence can be a real meaningful one. With Caesar's Cipher we can have as much possible combinations as the number of letters in the alphabet. So it's easy to calculate the entropy for each case and take out the sentence with the lower entropy. It's going to be the only meaningful one.
