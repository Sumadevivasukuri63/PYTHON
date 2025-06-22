names = input("Enter names separated by commas: ").split(',')
longest = max(names, key=len)
print("Longest name:", longest.strip())