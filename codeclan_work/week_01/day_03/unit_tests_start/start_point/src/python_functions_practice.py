def return_10():
    return(10)


def add(num1, num2):
    return(num1 + num2)

def subtract(num1, num2):
    return(num1 - num2)

def multiply(num1, num2):
    return(num1 * num2)

def divide(num1, num2):
    return(num1 / num2)

def length_of_string(string):
    return len(string)

def join_string(str1, str2):
    return(str1 + str2)

def add_string_as_number(str1, str2):
    return(int(str1) + int(str2))

def number_to_full_month_name(num):
    if num == 1:
        month = "January"
    elif num == 2:
        month = "February"
    elif num == 3:
        month = "March"
    elif num == 4:
        month = "April"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "June"
    elif num == 7:
        month = "July"
    elif num == 8:
        month = "August"
    elif num == 9:
        month = "September"
    elif num == 10:
        month = "October"
    elif num == 11:
        month = "November"
    elif num == 12:
        month = "December"
    
    return(month)

def number_to_full_month_name(num):
    if num == 1:
        month = "January"
    elif num == 2:
        month = "February"
    elif num == 3:
        month = "March"
    elif num == 4:
        month = "April"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "June"
    elif num == 7:
        month = "July"
    elif num == 8:
        month = "August"
    elif num == 9:
        month = "September"
    elif num == 10:
        month = "October"
    elif num == 11:
        month = "November"
    elif num == 12:
        month = "December"
    
    return(month)

def number_to_full_month_name(num):
    if num == 1:
        month = "January"
    elif num == 2:
        month = "February"
    elif num == 3:
        month = "March"
    elif num == 4:
        month = "April"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "June"
    elif num == 7:
        month = "July"
    elif num == 8:
        month = "August"
    elif num == 9:
        month = "September"
    elif num == 10:
        month = "October"
    elif num == 11:
        month = "November"
    elif num == 12:
        month = "December"
    
    return(month)

def number_to_short_month_name(num):
    if num == 1:
        month = "Jan"
    elif num == 2:
        month = "Feb"
    elif num == 3:
        month = "Mar"
    elif num == 4:
        month = "Apr"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "Jun"
    elif num == 7:
        month = "Jul"
    elif num == 8:
        month = "Aug"
    elif num == 9:
        month = "Sept"
    elif num == 10:
        month = "Oct"
    elif num == 11:
        month = "Nov"
    elif num == 12:
        month = "Dec"
    
    return(month)

def number_to_short_month_name(num):
    if num == 1:
        month = "Jan"
    elif num == 2:
        month = "Feb"
    elif num == 3:
        month = "Mar"
    elif num == 4:
        month = "Apr"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "Jun"
    elif num == 7:
        month = "Jul"
    elif num == 8:
        month = "Aug"
    elif num == 9:
        month = "Sept"
    elif num == 10:
        month = "Oct"
    elif num == 11:
        month = "Nov"
    elif num == 12:
        month = "Dec"
    
    return(month)

def number_to_short_month_name(num):
    if num == 1:
        month = "Jan"
    elif num == 2:
        month = "Feb"
    elif num == 3:
        month = "Mar"
    elif num == 4:
        month = "Apr"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "Jun"
    elif num == 7:
        month = "Jul"
    elif num == 8:
        month = "Aug"
    elif num == 9:
        month = "Sept"
    elif num == 10:
        month = "Oct"
    elif num == 11:
        month = "Nov"
    elif num == 12:
        month = "Dec"
    
    return(month)

def test_volume_of_cube(self):
    cube_result = pow(4, 3)
    self.assertEqual(64, cube_result)
    pass

  #Given a String, return the String reversed
  def test_reverse_string(self):
    string_reversed = "Hello"[::-1]
    self.assertEqual("olleH", string_reversed)
    pass

  #Given a value in farenheit, convert this into celsius.
  def test_fahrenheit_to_celsius(self):
    multiplied_celsius = multiply(22, 1.8)
    converted_celsius = add(39.6, 32 )
    self.assertEqual(71.6, converted_celsius)
    pass 


if __name__ == '__main__':
    unittest.main()
                         
                                                

            
     
