phone_book = {
    "Ростислав": ["0681603636", "0962270839"],
    "Марія": ["0567369129"],
    "Олег": ["0970463441", "0672347642", "0970463441"]
}

def add_phone_number(contact_name, new_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(new_number)
        print(f"Додано новий номер телефону для контакту {contact_name}.")
    else:
        print(f"Контакт {contact_name} не знайдено.")

add_phone_number("Марія", "0974485987")
add_phone_number("Ростислав", "0675573213")

print("\nСписок номерів телефонів для всіх контактів:")
for name, numbers in phone_book.items():
    print(f"{name}: {', '.join(numbers)}")
