def remove_duplicates(sequence):
    new_elements = []

    for item in sequence:
        if item not in new_elements:
            new_elements.append(item)

    return new_elements

sequence1 = [1,3,1,4,5,3,6,7,5,2]   
print(remove_duplicates(sequence1))     