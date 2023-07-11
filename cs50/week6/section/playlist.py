import cs50
import csv

def main():
    min_tempo = cs50.get_int("Minimum tempo: ")
    max_tempo = cs50.get_int("Maximum tempo: ")

    playlist = []
    # TODO: Read songs from 2018_top100.csv into playlist
    with open("2018_top100.csv") as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            if min_tempo < tempo or tempo < max_tempo:
                playlist.append(tempo)

    # TODO: Print song titles from playlist

main()