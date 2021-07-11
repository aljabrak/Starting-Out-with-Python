# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 364.
# Q 11. Web Page Generator.

name = input("Enter Your Name: ")
describe = input("Describe Yourself: ")
profile = open(r'profile.html', 'w')
profile.write('<html>\n<head>\n</head>\n<body>\n\t<center>')
profile.write('\n\t\t<h1>')
profile.write(name)
profile.write('<h1>\n\t<center>\n\t<hr />\n\t')
profile.write(describe)
profile.write('\n\t<hr />\n</body>\n</html>')
