-- Keep a log of any SQL queries you execute as you solve the mystery.

/*
Note to self:

Authorities believe that the thief stole the duck and then, shortly
afterwards, took a flight out of town with the help of an accomplice.
Your goal is to identify:

Who the thief is,
What city the thief escaped to, and
Who the thief’s accomplice is who helped them escape


All you know is that the theft took place on July 28, 2021 and that it
took place on Humphrey Street.
*/

-- Starting with a .sch to get a feel for the general layout.
.sch

/*
10 Tables:

1)  crime_scene_reports
    -   descriptions will be worth looking at
    -   not sure what the id primary key means in this context -
            crime id?

2)  interviews
    -   this has transcripts in it, probably should look at all of
        those

3)  atm_transactions
    -   will likely be relevant for the escape? paying for flight?

4)  bank_accounts
    -   if they're dumb enough to use their bank account for this then
        maybe it's related to escape/flight

5)  airports
    -   maybe will use this to figure out where they landed? idk if this
        will be useful if i have flight info

6)  FLIGHTS
    -   WILL CONTAIN ITEM #2: CITY

7)  passengers
    -   probably will use this to verify suspect is on plane to
        destination city
    -   not sure if this is like just a list of sold tickets or like a
        confirmed list of passengers in attendance on the plane

8)  phone_calls
    -   no transcripts or anything here

9)  PEOPLE
    -   WILL CONTAIN ITEM #1: NAME OF THIEF
    -   WILL CONTAIN ITEM #3: NAME OF ACCOMPLICE
    -   this has the primary key id thing too so maybe it connects to
        the other tables? seems crazy to associate a crime id with a
        person

10) bakery_security_logs
    -

*/

























