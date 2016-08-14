less_than_10 = {0:0, 1:3, 2: 3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
number_11_to_19 = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7 , 17:9 , 18:8 , 19:8}
tens={2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
hundred = 7
thousand = 8
and_count = 3

def digit_sum(number):
    if number < 10:
        return less_than_10.get(number)
    elif number >= 10 and number < 20:
        return number_11_to_19.get(number)
    elif number >= 20 and number < 100:
        return tens.get(number / 10) + less_than_10.get(number % 10)
    elif number >= 100 and number < 1000:
        sub = less_than_10.get( number / 100) + hundred
        if digit_sum(number % 100):
            sub = sub + digit_sum(number % 100) + and_count
        return sub
    elif number == 1000:
        return less_than_10.get(number / 1000) + thousand


def no_of_letters_in_words(number):
    total =  0
    for i in range (1, number + 1):
        sub_total = digit_sum(i)
        total+= sub_total

    return total

print no_of_letters_in_words(1000)