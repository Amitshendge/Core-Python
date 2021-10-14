'''
@Author: Amit Shendge
@Date: 14-10-2021 09:15PM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 09:15PM
@Title : StopWatch Demnstration Program
'''

import time

def function_strInput(string):
    """
Description:
    Function is used to take user input with input validation chaecks for valueError
Parameter:
      string which should be shown in terminal
Return:
       user Input
"""

    while True:
        try:
            return input(string)
        except ValueError:
            print('Plz enter valid str input')
            continue


def function_stratStopWatch():
    """
Description:
    Function is used to start the StopWatch when user enters start
Parameter:
      no parameters required
Return:
       time in seconds
"""

    while True:
        a='enter start to start StopWatch : '
        if function_strInput(a) == 'start':
            return round(time.time(),2)
        else:
            print('Plz enter start to start StopWatch')


def function_stopStopWatch():
    """
Description:
    Function is used to stop the StopWatch when user enters stop
Parameter:
      no parameters required
Return:
       time in seconds
"""

    while True:
        a = 'enter stop to stop StopWatch : '
        if function_strInput(a) == 'stop':
            return round(time.time(),2)
        else:
            print('Plz enter stop to stop StopWatch')


strat_time = function_stratStopWatch()
end_time = function_stopStopWatch()

print('Time escalaped : ' ,round(end_time-strat_time,2), ' sec')