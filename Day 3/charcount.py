"""Contains methods to test"""
# pylint: disable=W0612

def character_count(phrase):
    """Returns the number of characters in the given string."""
    total_count = 0
    for character in phrase:
        total_count +=1  #totalCount = totalCount+1
        print(total_count)

def main():
    """Main function for input to character_count"""
    character_count(input("Enter a phrase to count the characters of: "))

main()
