def checkEspecialCharacter(character):
  asciiCharacter = ord(character)
  if asciiCharacter < 97 or asciiCharacter > 122:
    return True
  else:
    return False