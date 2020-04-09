# breakme
stupid automated Caesar's Cipher

With this cipher you'll be able to astonish your geek friends. 
Tell them you've built AI capable to find the correct decrypted string between a puzzling bunch of random sentences.
To get the encrypted string run the program with a meaningful sentence and then copy one of the generated string
(or simply write down a pointless one like "Dobxq arab jxab qefp").
Run again the program and plug in the string (between quotation marks) and press enter to see the magic.

If you are so sorrowful to get to this point then I must explain how this works. Trust me this is not funny for your life.
Letters in vocabulary have a certain frequency so if we compare this recurrence with the frequency in our sentence and plug these values in entropy formula we'll get a number that tells us how much this sentence can be a real meaningful one. With Caesar's Cipher we can have as much possible combinations as the number of letters in the alphabet. So it's easy to calculate the entropy for each case and take out the sentence with the lower entropy. It's going to be the only meaningful one.

Here an example of execution:

Encrypted string:cerff ragre gb frr gur zntvp

Possible combinations (entropy):
cerff ragre gb frr gur zntvp (7.634171923682128)
dfsgg sbhsf hc gss hvs aouwq (7.495465509526806)
egthh tcitg id htt iwt bpvxr (6.638816512515912)
fhuii udjuh je iuu jxu cqwys (9.25983041004416)
givjj vekvi kf jvv kyv drxzt (11.255160540556659)
hjwkk wflwj lg kww lzw esyau (9.501909747872803)
ikxll xgmxk mh lxx max ftzbv (12.504128922651855)
jlymm yhnyl ni myy nby guacw (8.765701033682351)
kmznn ziozm oj nzz ocz hvbdx (12.888446782719585)
lnaoo ajpan pk oaa pda iwcey (6.910745402875582)
mobpp bkqbo ql pbb qeb jxdfz (10.747379926174812)
npcqq clrcp rm qcc rfc kyega (9.407789388176761)
oqdrr dmsdq sn rdd sgd lzfhb (8.065589419256323)
press enter to see the magic (5.729213651338546)
qsftt foufs up tff uif nbhjd (8.479243506244625)
rtguu gpvgt vq ugg vjg ocike (9.289343837494235)
suhvv hqwhu wr vhh wkh pdjlf (8.159105750046761)
tviww irxiv xs wii xli qekmg (8.548784420257757)
uwjxx jsyjw yt xjj ymj rflnh (13.214573551192853)
vxkyy ktzkx zu ykk znk sgmoi (11.795639739814794)
wylzz lualy av zll aol thnpj (8.987892362366528)
xzmaa mvbmz bw amm bpm uioqk (9.389192755153939)
yanbb nwcna cx bnn cqn vjprl (7.83467613431303)
zbocc oxdob dy coo dro wkqsm (7.614322873719411)
acpdd pyepc ez dpp esp xlrtn (8.48136021900547)
bdqee qzfqd fa eqq ftq ymsuo (12.459878570082504)

Decrypted string:
press enter to see the magic
