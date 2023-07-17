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
        person with a phone call etc though

10) bakery_security_logs
    -   idk what the bakery's relevance is, maybe getaway car? license
        plate number is one of the things in here, activity could be
        useful too maybe
*/

-- Gonna look at the transcripts.
SELECT *
  FROM interviews;

-- Too much info lol god there's so many of them
-- 191 in total, looks like they're chronological
-- don't wanna read all these maybe i'll find the word duck or something
SELECT *
  FROM interviews
 WHERE transcript LIKE '%duck%';

-- Literally not a single one that uses the word "duck"?
-- I'll try "theft"

SELECT *
  FROM interviews
 WHERE transcript LIKE '%theft%';

/* Perfect, looks like #161 Ruth 2021 07/28 says this:

"Sometime within ten minutes of the theft, I saw the thief get into a
car in the bakery parking lot and drive away. If you have security
footage from the bakery parking lot, you might want to look for cars
that left the parking lot in that time frame."

Gonna go back and glance at the interview transcripts around #161 Ruth
to see if there's anything interesting.

















