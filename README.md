## Day of The Week Prediction Algorithm
> When I was in college I saw a movie that interviewed savant children and their families.
> One particular child had the ability to tell you what day of the week any date fell on.
> This program is simply me just being curious as to the answer!

#### The Answer
> There are two categorization types of years; they are leap and non-leap years.
> The following is a list of months during this particular type of year with the day of the week difference between months listed. <br/>
> Ex. From December 1st to January 1st the day of the week difference is 2 (Monday -> Wednesday)
>    <br/>EXAMPLE TABLE
>    <br>Month 1(Jan) 2(Feb)
>    <br>Gap &nbsp;&nbsp;&nbsp;2      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3

> **Leap Year** (year % 4 == 0): [2,3,0,0,2,3,2,3,3,2,3,2] <br/>
> **Non-Leap** Year: [2,3,1,0,2,3,2,3,3,2,3,2] <br/>

> **Leap Years** have a gap of **2** (from Tues, Jan 1st to Wednesday, Dec 31st)<br/>
> **Non-Leap** Years have a gap of **1** with the subsequent year starting on the next day of the week from the current year (from Tues, Jan 1st to Tuesday, Dec 31st)

#### Final Algorithm
1) Parameters
   - Prediction Date <br>

2) Calculate<br/>
   ```
   leapYearMonthDayGapArr = [2,3,0,0,2,3,2,3,3,2,3,2]
    nonLeapYearMonthDayGapArr = [2,3,1,0,2,3,2,3,3,2,3,2]
   
   startYear = 2000
   yDiff = predictionYear - startYear 
   if yDiff >= 0: #date is current or in future
        dayGap = yDiff # non-leap year day gap is 1
        dayGap += yDiff//4+1 # leap year day gap is 2, +1 cause 200 is a leap year
        .... i got bored but it is pretty easy to think of the rest from here
        
        
   else: # date is in past
   
   
   
    
    
   ```

