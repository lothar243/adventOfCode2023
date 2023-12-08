import sys
import multiset
from pprint import pprint

char_map = {"A": "a", 
            "K": "b", 
            "Q": "c", 
            "J": "d",
            "T": "e",
            "9": "f",
            "8": "g",
            "7": "h",
            "6": "i",
            "5": "j",
            "4": "k",
            "3": "l",
            "2": "m"
            }

sample_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def has_5_of_kind(hand: multiset.Multiset):
    return max(hand.values()) == 5

def has_4_of_kind(hand: multiset.Multiset):
    return max(hand.values()) == 4

def has_full_house(hand: multiset.Multiset):
    return max(hand.values()) == 3 and min(hand.values()) == 2

def has_3_of_kind(hand: multiset.Multiset):
    return max(hand.values()) == 3 and min(hand.values()) == 1

def has_3_of_kind(hand: multiset.Multiset):
    return max(hand.values()) == 3 and min(hand.values()) == 1

def has_2_pair(hand: multiset.Multiset):
    return list(hand.values()).count(2) == 2 and max(hand.values()) == 2

def has_1_pair(hand: multiset.Multiset):
    return list(hand.values()).count(2) == 1 and max(hand.values()) == 2

def has_high_card(hand: multiset.Multiset):
    return max(hand.values()) == 1

def encodeHand(handString: str):
    ms = multiset.Multiset(handString)
    encodedHandList = []
    if has_5_of_kind(ms):
        encodedHandList.append("a")
    elif has_4_of_kind(ms):
        encodedHandList.append('b')
    elif has_full_house(ms):
        encodedHandList.append('c')
    elif has_3_of_kind(ms):
        encodedHandList.append('d')
    elif has_2_pair(ms):
        encodedHandList.append('e')
    elif has_1_pair(ms):
        encodedHandList.append('f')
    elif has_high_card(ms):
        encodedHandList.append('g')
    else:
        print(f"Error, unable to interpret hand: {handString}")
    for char in handString:
        encodedHandList.append(char_map[char])
    return ''.join(encodedHandList)

def handKey(lineDict: dict):
    return lineDict['encodedString']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    
    for i, line in enumerate(lines):
        handString, bidString = line.split(" ")
        lines[i] = {'handString': handString, 'bid': int(bidString), 'encodedString': encodeHand(handString)}
    
    lines.sort(key=handKey, reverse=True)
    
    totalWinnings = 0
    for i, line in enumerate(lines):
        totalWinnings += (i + 1) * line['bid']

    print(totalWinnings)
        
        