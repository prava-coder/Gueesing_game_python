#user should guess the word
secret_word = "giraffe"
guess = ""
guess_count = 0
#user should guess the word in 3 chances
guess_limit= 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("enter your guess:")
        guess_count+=1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("out_of_guesses,YOU LOSE:")
else:
    print("you win:")