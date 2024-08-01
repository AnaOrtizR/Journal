from utils.BD_Connection import create_connection
from crudDiary import *
from crudEntry import *


connection = create_connection("localhost", "anaortiz", "user1101", "lockednotes")

#=================================== DIARY ===================================
#------- CREAR
#diary1 = newDiary(connection, "Holidays", "pass123")
#print(diary1)
#diary2 = newDiary(connection, "Holidays", "passw1234")
#print(diary2)
#diary3 = newDiary(connection,"Work", "passd1234")
#print(diary3)
#diary4 = newDiary(connection, "otro", "password1")
#print(diary4)

#------- LISTAR
#diaries = listDiary(connection)
#for diary in diaries:
#    print("=========================")
#    print(f"Diary name: {diary[1]}")

#------- SEARCH
#diary = searchDiary(connection, 1)
#print(f"Diary name: {diary[1]}")

#------- EDIT DIARY NAME
#diary = editDiaryName(connection, 1, "Holidays 2024")

#------- EDIT DIARY PASSWORD
#editdiary1 = editDiaryPasswd (connection, 1, "pass123")
#print(editdiary1)
#editdiary2 = editDiaryPasswd(connection, 1, "PASSW1234")
#print(editdiary2)

#------- DELETE DIARY
#deldiary = deleteDiary(connection, 3)


#=================================== ENTRY ===================================
#------- CREAR
#newDiaryEntry1 = newEntry(connection, "First Day", "I sleept through almost all my first day of vacation", 1)
#print(newDiaryEntry1)
#newDiaryEntry2 = newEntry(connection, "Second Day", "I ate pizza today!", 1)
#print(newDiaryEntry2)
#newDiaryEntry3 = newEntry(connection, "Day 3", "Went for a walk", 1)
#print(newDiaryEntry3)
#newDiaryEntry4 = newEntry(connection, "Day 4", "Went for a walk", 1)
#print(newDiaryEntry4)

#------- EDIT ENTRY TITLE
#edEntry = editEntryTitle(connection, 1, "Day 1")
#edEntry = editEntryTitle(connection, 2, "Day 2")

#------- EDIT ENTRY BODY
#edEntry = editEntryBody(connection, 1, "Sleep! Sleep! Sleep!")

#------- SEARCH BY ID
#entryy = searchEntry(connection,1)
#print(f"Title: {entryy[1]}\nBody: {entryy[2]}\nDate Posted: {entryy[3]} ")

#------- SEARCH BY WORD
#word = "first"
#entry = searchEntryByWord(connection, word)
#for entries in entry:
#    print("=============================================================")
#    print(f"Title: {entries[1]}\nBody: {entries[2]}\nDate Posted: {entries[3]}")

#------- SEARCH BY DATE POSTED
#entryy = searchEntryByDate(connection, '2024-07-30')
#for entries in entryy:
#    print("=============================================================")
#    print(f"Title: {entries[0]}\nBody: {entries[1]}\nDate Posted: {entries[2]}")

#------- LISTAR
#entries = listEntries(connection)
#for entry in entries:
#    print("=============================================================")
#    print(f"Title: {entry[1]}\nBody: {entry[2]}\nDate Posted: {entry[3]}")

#------- LIST BY DATE POSTED
#entries = listEntriesByDatePosted(connection)
#for entry in entries:
#    print("=============================================================")
#    print(f"Title: {entry[1]}\nBody: {entry[2]}\nDate Posted: {entry[3]}")

#------- LIST BY DATE UPDATED
#entries = listEntriesByDateUpdated(connection)
#for entry in entries:
#    print("=============================================================")
#    print(f"Title: {entry[1]}\nBody: {entry[2]}\nDate Posted: {entry[3]}")

#------- DELETE ENTRY
#delEntry = deleteEntry(connection, 4)