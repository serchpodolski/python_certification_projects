import re

def verify_card_number(digits: str):
  digits = re.sub(r'[ -]', '', digits)
  if not digits.isdigit():
    return False

  end_index = len(digits)-1
  # print(f'End Index: {end_index}')

  for i in range(end_index-1, -1, -2):
    if int(digits[i]) * 2 > 9:
      digits = digits[:i] + str(int(digits[i]) * 2 - 9) + digits[i + 1:]
    else:
      digits = digits[:i] + str(int(digits[i]) * 2) + digits[i + 1:]

  return 'VALID!' if sum(map(int, digits)) % 10 == 0 else 'INVALID!'

print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
