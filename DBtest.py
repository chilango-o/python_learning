import sqlite3

def linkGenerator(link1):
    page_select = '_Desde_01'
    order_by_price = '_OrderId_PRICE'
    select_used = '_ITEM*CONDITION_2230581'
    free_shipping = '_CostoEnvio_Gratis'
    MSI = '_Installments_NoInterest'
    print("link generator starts:\n")
    link1 += order_by_price
    print(link1)
    used_input = input("search only used items? (y/n)")
    if used_input.lower() == 'y':
        link1 += select_used
    print(link1)
    free_shipping_input = input("search items with free shipping? (y/n)")
    if free_shipping_input.lower() == 'y':
        link1 += free_shipping
    print(link1)
    MSI_input = input("search items with 'Meses sin intereses'? (y/n)")
    if MSI_input.lower() == 'y':
        link1 += MSI
    print(link1)
    link1 += page_select
    print(link1)
    print('\nGeneration completed...\n')
    return link1

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('ML_scrapping.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sqlite_select_query = """SELECT * from listing"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchone()
        #print("Total rows are:  ", len(records))
        #print("Printing each row")
        #for row in records:
        #print("Title: ", records[1]) 
        #print("Link: ", records[2])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The SQLite connection is closed")
    return records

item = linkGenerator(readSqliteTable()[2])
#print(item)