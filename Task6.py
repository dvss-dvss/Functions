def caesar_cipher(text, shift, mode='encrypt'):
  """
  Функція для шифрування та дешифрування за допомогою шифру Цезаря.

  Args:
    text (str): Вхідний текст для шифрування/дешифрування.
    shift (int): Кількість позицій для зсуву літер.
    mode (str, optional): Режим роботи (шифрування або дешифрування). 
      Можливі значення: 'encrypt' (за замовчуванням) або 'decrypt'.

  Returns:
    str: Зашифрований або дешифрований текст.
  """

  result = ""
  # Переводимо весь текст у нижній регістр для спрощення
  text = text.lower()

  # Ітерація по кожному символу тексту
  for char in text:
    # Якщо символ - літера алфавіту
    if char.isalpha():
      # Знаходимо числовий код символу в ASCII
      char_code = ord(char)
      # Розраховуємо новий код символу зі зсувом,
      # враховуючи обертання алфавіту
      if mode == 'encrypt':
        new_code = (char_code - ord('a') + shift) % 26 + ord('a')
      else:
        new_code = (char_code - ord('a') - shift) % 26 + ord('a')
      # Отримуємо новий символ за його кодом
      result += chr(new_code)
    else:
      # Якщо символ не літера, додаємо його без змін
      result += char

  return result

# Приклад використання:
text = "привіт світ"
shift = 3

# Шифрування
encrypted_text = caesar_cipher(text, shift)
print("Зашифрований текст:", encrypted_text)

# Дешифрування
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print("Дешифрований текст:", decrypted_text)