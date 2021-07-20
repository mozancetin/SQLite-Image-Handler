import sqlite3

class SQLiteImageHandler():

    def __init__(self, databasePath : str = "database.db", tableName : str = "images"):
        self.startConnection()
        self.databasePath = databasePath
        self.tableName = tableName

    def photoSelector(path : str):
        with open(path, "rb") as file:
            byteContent = file.read()

        return byteContent

    def startConnection(self):
        self.connection = sqlite3.connect(f"{self.databasePath}.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tableName} (Name TEXT, Data BLOB)")
        self.connection.commit()

    def addPhoto(self, name : str, photoByte : bytes):
        if self.isPhotoExists():
            print("There is an image with this name!")
            return False
        try:
            self.cursor.execute(f"INSERT INTO {self.tableName} VALUES (?, ?)", (name, photoByte))
            self.connection.commit()
            print("Image successfully saved!")
        except Exception as error:
            print(error)

    def getSavePhoto(self, photoName : str = None, savePath : str = "savedImage.png"):
        """
        ### Explanation
        Saves the previously saved image in the database as an image to the given path.

        -------------------------------------------------
        ### Parameters
        - photoName[str]:   Name of photo in the database.
        - savePath[str]:    Save path. (default: savedImage.png)
        -------------------------------------------------
        """
        if photoName == None:
            print("Give me an image boss. (photoName parameter has not declared.)")
            return

        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE Name = ?", (photoName,))
            data = self.cursor.fetchone()
            if data != None:
                with open(savePath, "wb") as file:
                    file.write(data[1])
            else:
                print("There is no image with this name in the database!")
        except Exception as error:
            print(error)

    def isPhotoExists(self, photoName : str):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE Name = ?", (photoName,))
            data = self.cursor.fetchone()
            if data != None:
                return True
            return False
        except Exception as error:
            print("Error occurred in isPhotoExists func. Error: " + str(error))