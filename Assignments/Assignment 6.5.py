text = "X-DSPAM-Confidence:    0.8475"

text1 = text.find("0")

x = text[text1:]

print(float(x))