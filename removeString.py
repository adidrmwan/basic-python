def remove_string(text1):
    lentgh = len(text1)
    arr1 = list(text1)
    checked = set()

    for i in range (lentgh):

        if arr1[i] not in checked:
            checked.add(arr1[i])

        res = list(checked)

    return res

text1 = raw_input ()
print(remove_string(text1))











