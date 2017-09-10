def is_permutation(str1, str2):
  if len(str1) != len(str2):
      return False

  lst1 = list(str1)
  lst2 = list(str2)

  return lst1.sort() == lst2.sort()


is_permutation("about", "aoubt")