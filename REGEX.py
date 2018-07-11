import re
emails = ["zuck26@facebook.com", "page33@google.com", "jeff42@amazon.com"]

# Question 1

def email_splitter(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]
    domain_type = domain.split('.')[1]

    print('Username : ', username)
    print('Domain   : ', domain_name)
    print('Type 	: ', domain_type)
    print('\r')

for email in emails:
    email_splitter(email)


# Question 2

Para_text = """Betty bought a bit of butter, But the butter was so bitter,
 So she bought some better butter, To make the bitter butter better."""

List = re.findall(r'\b[bB]\w+', Para_text)

result = []
for l in List:
    if l not in result:
        result.append(l)

print(result)
print('\r')

# Question 3

Depricated_letters = ".,;_"

s = """A,very very;irregular_sentence"""
for c in Depricated_letters:
    s = s.replace(c, ' ')

s.split()
print(s)
