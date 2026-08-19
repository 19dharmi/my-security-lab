def reversestr():
	name = input("enter name:")
	print("reverse string:",name[::-1])
reversestr()

text = input("enter sentence:")
def vowel_count(text):
	return sum(1 for char in text if char.lower() in 'aeiou')
print(f"vowel count: {vowel_count(text)}")
