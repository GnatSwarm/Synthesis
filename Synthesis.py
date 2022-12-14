# this is the main for Synthesis
from ast import main
import calendar
from datetime import datetime, timedelta
from email.policy import default
from time import time

#---Settings----------------------------------------------#

#Time category muti-dimensional arrays
taskCategories = [{'Monday':    {{730,900}:    'morningPrep',\
                                {}:     'work',\
                                {900,1830}:     'school',\
                                {1830,2100}:     'open',\
                                {2100,2200}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Tuesday':     {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Wednesday':   {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Thursday':    {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Friday':      {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Saturday':    {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}},\
                {'Sunday':      {{}:    'morningPrep',\
                                {}:     'work',\
                                {}:     'school',\
                                {}:     'open',\
                                {}:     'bedTime',\
                                {{000,730},{2200,2400}}:     'sleep'}}]

#Default item properties
defaultTitle = "Item" # + currentDatetime
defaultDescription = ''
defaultDeadline = datetime
defaultTotalDuration = int
defaultTags = ['','']
defaultPrepTime = int
defaultLocation = ''
defaultStatus = ''
default

#---Variables---------------------------------------------#





#---Classes/Functions-------------------------------------#



class InboxManager:    
# The Inbox inteacts with the Inbox database
    
    def NewItem(title = str,\
                description = str,\
                deadline = datetime,\
                totalDuration = int,\
                tags = list,\
                prepTime = int,\
                location = str,\
                status = str,\
                remainingDuration = int):


        # Set newValues to defaults or respective input argument
        ##!!!## THIS IS NOT A LOOP TO LEAVE ROOM FOR CONTEXTUAL DEFAULTS ##!!!##
        
        
        ## if title argument was left blank, use the default
        if title == '':
            newTitle = defaultTitle
        ## else (I.e. title argument was populated), use the argument value
        else:
            newTitle = title
           
        ## if description argument was left blank, use the default
        if description == '':
            newDescription = defaultDescription
        ## else (I.e. description argument was populated), use the argument value
        else:
            newDescription = description
        
        ## if deadline argument was left blank, use the default
        if deadline == '':
            newDeadline = defaultDeadline
        else:
            newDeadline = deadline
        
        ## if totalDuration argument was left blank, use the default
        if totalDuration == '':
            newTotalDuration = defaultTotalDuration
        else:
            newDescription = totalDuration
        
        ## if tags argument was left blank, use the default
        if tags == '':
            newTags = defaultTags
        else:
            newTags = tags
            
        ## if prepTime argument was left blank, use the default
        if prepTime == '':
            newPrepTime = defaultPrepTime
        else:
            newPrepTime = prepTime
            
        ## if location argument was left blank, use the default
        if location == '':
            newLocation = defaultLocation
        else:
            newLocation = location
            
        ## if status argument was left blank, use the default
        if status == '':
            newStatus = defaultStatus
        else:
            newStatus = status
            
        ## if remainingDuration argument was left blank, use the default
        if remainingDuration == '':
            newRemainingDuration = totalDuration
        else:
            newDescription = remainingDuration
    
        # init new Item using new values

        # identify priority position in inbox.db
    
        # insert the new item there
        return
    
    def itemList():
        
        return
    
    def topNItems(n = int):
        topN = []
        
        #get top N items
        
        return(topN)

class Timeline:
    
    def FindGaps(timelineStart = datetime, timelineEnd = datetime):
    
        #Input cleaning
        if timelineEnd - timelineStart == 0:
            print("error: list interval has zero duration")
            return
    
        if timelineEnd - timelineStart < 0:
            print("error: list interval has negative duration")
            return
    
        #naming the list of gaps
        gaps = {}
    
        # identify and record the first gap.
        gaps.append(Find_Next_Gap(timelineStart))
        
        # while the beginning of the last gap in the list occurs BEFORE the timelineEnd, find the next gap.
        lastGapIndex = (len(gaps)-1)
        nextGapCheckDate, dummyDate = gaps[lastGapIndex]
        while  nextGapCheckDate < timelineEnd:
            Find_Next_Gap(nextGapCheckDate)
            
            return
        
        #return list of gaps
        return(gaps)
    
    def Suggest():
        suggestions = []
        return(suggestions)



# Given a date (very often "today's date", a deadline, and a specific taskCategory,
# sum up the total time available for that taskCategory between the date and the deadline.
def Available_Time_Between(thisDateTime = datetime, deadline = datetime, taskCategory = str):
    availableTime = timedelta
    timeStamp = thisDateTime
    
    while timeStamp <= deadline:
        # create sum for the specified taskCategory
        # account for time taken up by existing event items 
        availableTime = availableTime + 1
        
        timeStamp += timedelta(minutes=15)
    return(availableTime)

def Find_Next_Gap(thisDateTime = datetime):
    #find next bit that doesn't have an assigned event item
    
    gapStart = datetime
    gapEnd = datetime
    gap = (gapStart, gapEnd)
    return(gap)



#---Main---------------------------------------#

def main():
    
    print('ran main')
    return