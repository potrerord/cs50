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

Found a couple others - gonna consolidate below with ruth:

| 161 | Ruth        | 2021 | 7     | 28  |
Sometime within ten minutes of the theft, I saw the thief get into a car
in the bakery parking lot and drive away. If you have security footage
from the bakery parking lot, you might want to look for cars that left
the parking lot in that time frame.

    -   find security footage from the bakery parking lot within 10
        minutes of the theft
        -   need to figure out the time of the theft
        -   would be looking for the car/license plate, specifically
            leaving

| 162 | Eugene      | 2021 | 7     | 28  |
I don't know the thief's name, but it was someone I recognized. Earlier
this morning, before I arrived at Emma's bakery, I was walking by the
ATM on Leggett Street and saw the thief there withdrawing some money.

    -   ATM withdrawal from Leggett St morning of the theft
    -   "before i arrived at emma's bakery" probably relevant - bet i
        can find eugene in a transaction or something to figure out the
        time he got there
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 163 | Raymond     | 2021 | 7     | 28  |
As the thief was leaving the bakery, they called someone who talked to
them for less than a minute. In the call, I heard the thief say that
they were planning to take the earliest flight out of Fiftyville
tomorrow. The thief then asked the person on the other end of the phone
to purchase the flight ticket.

    -   call duration < 1min
    -   call time when leaving bakery
    -   earliest flight from Fiftyville july 29 2021
    -   accomplice purchased flight ticket, would be under their name
*/

-- let's look at the bakery info

SELECT *
  FROM bakery_security_logs;

-- okay there's 468 of these, gives time, entrance/exit, license plate
-- date 25 - 31, all july 2021, military time
-- gonna consolidate this to only the relevant day

SELECT *
  FROM bakery_security_logs
 WHERE day = 28;

-- this looks useful and i don't want to have to run this again so i'll
-- make a view

CREATE VIEW bakery_logs_28th AS
SELECT b.id, b.hour, b.minute, b.activity, b.license_plate
  FROM bakery_security_logs AS b
 WHERE b.day = 28;

-- so now i should be able to use bakery_logs_28th when i need it again
-- gonna check it

SELECT *
  FROM bakery_logs_28th;

-- much easier to look at now
-- looks like it has logs from 8am to 6pm
-- looking back at my notes it looks like only the exits are relevant,
-- so i'll redefine the view

-- deleting view
DROP VIEW bakery_logs_28th;

-- making new one
CREATE VIEW bakery_logs_28th AS
SELECT b.id, b.hour, b.minute, b.activity, b.license_plate
  FROM bakery_security_logs AS b
 WHERE b.day = 28
   AND b.activity = 'exit';

-- checking it
SELECT *
  FROM bakery_logs_28th;

-- short list now of possible cars

-- I think i need the crime time so i'll check reports

SELECT *
  FROM crime_scene_reports;

/*
Found something:

| 295 | 2021 | 7     | 28  | Humphrey Street      |
Theft of the CS50 duck took place at 10:15am at the Humphrey Street
bakery. Interviews were conducted today with three witnesses who were
present at the time – each of their interview transcripts mentions the
bakery. |

-   okay so it looks like the theft of the duck actually took place *at*
    the bakery
-   10:15am
-   so 10:15am <= x <= 10:25am for the getaway car
*/

SELECT *
  FROM bakery_logs_28th
 WHERE hour = 10
   AND minute >= 15
   AND minute <= 25;















