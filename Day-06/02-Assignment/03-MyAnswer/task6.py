# ## Task 6: Identity and Membership Operators

# 1. Create a list `my_list` containing a few elements.
# 2. Use identity operators (`is` and `is not`) to check if two variables are the same object.
# 3. Use membership operators (`in` and `not in`) to check if an element is present in `my_list`.
# 4. Print the results.
def check_identity_and_membership(my_list):
    """
    This function checks identity and membership of the elements with respect to the provided list.
    
    Parameters:
    - my_list: The list to check against.
    
    Takes inputs from the command line for identity and membership checks.
    """
    import sys
    
    if len(sys.argv) < 4:
        print("Please provide two elements for identity checks and one element for membership check.")
        print("Usage: python script.py <element1> <element2> <element_for_membership>")
        return

    # Extract elements from command line arguments
    element1 = sys.argv[1]
    element2 = sys.argv[2]
    element_for_membership = sys.argv[3]

    # Identity checks using `is` and `is not`
    identity_check_is = element1 is element2
    identity_check_is_not = element1 is not element2

    # Membership checks using `in` and `not in`
    element_in_list = element_for_membership in my_list
    element_not_in_list = element_for_membership not in my_list

    # Print the results
    print(f"`element1 is element2`: {identity_check_is}")
    print(f"`element1 is not element2`: {identity_check_is_not}")
    print(f"`element_for_membership in my_list`: {element_in_list}")
    print(f"`element_for_membership not in my_list`: {element_not_in_list}")

# Predefined list for membership check
my_list = [1, "2", 3, 4, 5, "apple", "banana", "cherry"]

if __name__ == "__main__":
    check_identity_and_membership(my_list)
