##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal: 
#   1. get input from user
#   2. print it
#   3. when a certain string is entered, clear the terminal
#
##


#we'll print an escape sequence
#chr does like this:
#  (ascii symbol) = chr(integer value of ascii code)
escape_sequence = chr(27) + "[2j"

while True:
  input = raw_input("Computer: \"What?\"\n: ")
   
  if input == escape_sequence:
    print escape_sequence
    continue

  print input 
