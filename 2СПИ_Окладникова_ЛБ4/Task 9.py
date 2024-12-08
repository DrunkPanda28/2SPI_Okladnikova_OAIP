vowels = 'аеёиеоуюяАЕЁИЕОУЮЯ'

password = input("Введите пароль: ")
encrypted_password = ''.join('0' if char in vowels else '1' for char in password if char.isalpha())
print(encrypted_password)