str = "K YZWLNKXKJWGN QUGN ETNMX MPLMZOMXYM K TMMJOXA XEN TKZ ZMQEBMF TZEQ KJKZQ EX KXKJWDOXA KXF MPLJEZM NHM TJEEF ET XMI CXEIJMFAM IHOYH MKYH WMKZ RZOXAG IONH ON "

freq = {chr(i + ord("A")):0 for i in range(26)}

for char in str:
	if char == " ":
		continue
	else:
		freq[char] += 1

print(freq)