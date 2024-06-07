import tensorflow as tf
from tqdm import tqdm
import random

tf.debugging.set_log_device_placement(True)

# Create some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = [(rank, suit) for rank in ranks for suit in suits]

random.shuffle(deck)

pair = False
previous = deck[0]
count = 0

with tqdm(total=len(deck)) as pbar:
    while not pair and count < len(deck) - 1:
        count += 1
        card = deck[count]

        if card[0] == previous[0]:
            pair = True

        previous = card
        pbar.update(1) 

if pair:
    print(f"Pair found after {count} iterations.")
else:
    print("No pair")
