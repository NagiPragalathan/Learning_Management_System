def remove_space(string):
  out = ""
  for i in string:
    if i != " ":
      out = out +  i
  return out

print(remove_space("dcjhe ecxxkjw xercx x "))