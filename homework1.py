"""
Author: Jose Pablo Murillo
File: homework1
Description: Use of if clause
Last update: 29/11/2018
Python version 3.6.4
"""

#Exercise 1
def miniCalculator(number1: int, number2: int, operation: str) -> int:
    """
    Inputs: first number, second number, operation code
    Output: arithmetic operation result or error
    Process: If for every specified operator, and do the
        corresponding operation
    Restrictions: First two parameters must be integers
    and third must be string
    """
    if (operation == '+'):
        return number1 + number2
    elif (operation == '-'):
        return number1 - number2
    elif (operation == '*'):
        return number1 * number2
    elif (operation == '/'):
        if (number2 != 0):
            return number1 // number2
        else:
            return "Error: cannot divide by 0"
    else:
        return "Error: operation not available, must be +, -, / or *"



#Exercise 2
def isLeap(year: int) -> bool:
    """
    Inputs: a year
    Output: boolean or error
    Process: Determines if year is a leap year by checking if the year is
    divisible by 4
    Restrictions: year must be an integer, year must be >= 2000 and have 4 digits
    """
    if (year < 2000 or year > 9999):
        return "Error: year not in permitted range"
    else:
        return (year % 4 == 0)



#Execise 3
def dateValid(date: int) -> bool:
    """
    Inputs: a date as int with format ddmmaaaa
    Output: boolean
    Process: the date is broken down into separate components day, month and year
    and performs the validation acording to the provided restrictions
    Restrictions: date must be int
    year must be >= 1900
    month must be between 1 and 12
    february has 29 days if year is leap, else it has 28
    january, march, may, july, august, october and december have 31 days
    april, june, september and november have 30 days
    """
    year:int = date % 10000
    date = date // 10000
    month:int = date % 100
    day:int = date // 100

    if (year >= 1900):
        if (month >= 1 and month <= 12):
            if (month == 2):
                if (isLeap(year)):
                    if (day >= 1 and day <= 29):
                        return True
                else:
                    if (day >= 1 and day <= 28):
                        return True
            else:
                if (month == 1 or month == 3 or month == 5 or month == 7 \
                    or month == 8 or month == 10 or month == 12):
                    if (day >= 1 and day <= 31):
                        return True
                else:
                    if (month == 4 or month == 9 or month == 11):
                        if (day >= 1 and day <= 30):
                            return True
    return False



#Exercise 4
def dateAsWords(date: int) -> str:
    """
    Inputs: date as int in format ddmmaaaa
    Output: Date as words or boolean
    Process: date is validated and then an if is done for the month to return the
    corresponding one in words
    Restrictions: date must be int
    """
    if (dateValid(date)):
        year:int = date % 10000
        date = date // 10000
        month:int = date % 100
        day:int = date // 100
        strMonth:str = ""
        if (month == 1):
            strMonth = "january"
        if (month == 2):
            strMonth = "february"
        if (month == 3):
            strMonth = "march"
        if (month == 4):
            strMonth = "april"
        if (month == 5):
            strMonth = "may"
        if (month == 6):
            strMonth = "june"
        if (month == 7):
            strMonth = "july"
        if (month == 8):
            strMonth = "august"
        if (month == 9):
            strMonth = "september"
        if (month == 10):
            strMonth = "october"
        if (month == 11):
            strMonth = "november"
        if (month == 12):
            strMonth = "december"
        return str(day) + " of " + strMonth + " " + str(year)
    else:
        return False



#Exercise 5
def deleteDigit(digit: int, number: int) -> int:
    """
    Inputs: a digit and a number 
    Output: number without the specified digit
    Process: the four digits are extracted from the number and then are added
    to the result if they are different than the digit we want to delete
    Restrictions: digit is between 0 and 9
    number must be positive and have four digits
    """
    numberRestriction:bool = (number >= 1000 and number <= 9999)
    digitRestriction:bool = (digit >= 0 and digit <= 9)
    errorMessage: str = ""

    if (not numberRestriction):
        errorMessage = "Error in number"

    if (not digitRestriction):
        if (errorMessage == ""):
            errorMessage = "Error in digit"
        else:
            errorMessage = errorMessage + " and in digit"
    if (errorMessage != ""):
            return errorMessage
    else:
        firstDigit = number // 1000
        number = number % 1000
        secondDigit = number // 100
        number = number % 100
        thirdDigit = number // 10
        fourthDigit = number % 10

        if (firstDigit == digit):
            firstDigit = 0
        if (secondDigit == digit):
            secondDigit = 0
        if (thirdDigit == digit):
            thirdDigit = 0
        if (fourthDigit == digit):
            fourthDigit = 0

        return firstDigit * 1000 + secondDigit * 100 + \
               thirdDigit * 10 + fourthDigit



#Exercise 6
def convertSeconds(seconds: int, unit: str) -> float:
    """
    Inputs: an amount of seconds and a unit of time
    Output: The amount of seconds converted into the unit specified
    Process: amount of seconds is divided according to corresposponding unit
    Restrictions: amount of seconds must be integer and unit of time
    must be: 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months'
    """
    errorMessage: str = ""
    if (seconds < 0):
        errorMessage = "Error in number"
        return errorMessage

    if (unit == "seconds"):
        return seconds
    if (unit == "minutes"):
        return seconds / 60
    if (unit == "hours"):
        return seconds / 3600
    if (unit == "days"):
        return seconds / 86400
    if (unit == "weeks"):
        return seconds / 604800
    if (unit == "months"):
        return seconds / 2628000
        
        
    
            
                

    
