# program removes duplicate email addresse========================================================================================================================================================

emails = [
    'john@example.com',
    'jane@example.com',
    'john@example.com',
    'alex@example.com'
]

# Zamieniamy listę na zbiór, usuwając powtórzenia
unique_emails = set(emails)

print(unique_emails)

# program identifies students who are absent========================================================================================================================================================

all_students = {'Alice', 'John', 'Sara', 'Bob'}
attended_students = {'Alice', 'Bob'}

# Odejmujemy obecnych studentów od wszystkich studentów
absent_students = all_students - attended_students

print(absent_students)

# program below finds spam in received emails========================================================================================================================================================

emails_received = {
    'john@example.com',
    'spam1@example.com',
    'spam2@example.com',
    'jane@example.com'
}

spam_list = {
    'spam1@example.com',
    'spam2@example.com'
}

# Znajdujemy część wspólną zbiorów
spam_emails = emails_received & spam_list

print('Spam emails:', spam_emails)

# program that combines these lists and simultaneously removes duplicates========================================================================================================================================================

contacts_A = {
    'john@example.com',
    'alice@example.com',
    'bob@example.com'
}

contacts_B = {
    'bob@example.com',
    'michael@example.com',
    'sara@example.com'
}

# Łączymy zbiory bez powtarzających się elementów
merged_contacts = contacts_A | contacts_B

print('Merged contacts:', merged_contacts)

# program that checks whether the user has the required persmission========================================================================================================================================================

required_permissions = {'read', 'write', 'execute'}
user_permissions = {'read', 'write'}

# Sprawdzamy, czy użytkownik posiada wszystkie wymagane uprawnienia
has_permissions = required_permissions.issubset(user_permissions)

print(has_permissions)