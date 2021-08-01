import sqlite3
import os
import sys
from typing import Tuple

class ImageHandler:

    def __init__(self, databasePath : str = "database.db", tableName : str = "images"):
        self.databasePath = databasePath
        self.tableName = tableName
        self.startConnection()

    def startConnection(self) -> None:
        """
        ### Explanation
        Starts the connection with SQLite Database.
        """

        self.connection = sqlite3.connect(f"{self.databasePath}")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tableName} (Name TEXT, Data BLOB, Type TEXT)")
        self.connection.commit()

    def imageSelector(self, path : str = None) -> Tuple[bytes, str]:
        """
        ### Explanation
        Selects an image and returns the image's bytes content and extension type.
        
        -------------------------------------------------
        ### Parameters
        - path[str]: The path of the picture you choose.

        -------------------------------------------------
        ### Returns
        - bytesContent[bytes]
        - extensionType[str]
        -------------------------------------------------
        """

        if path == None:
            raise ValueError("Path can't left blank!")

        with open(path, "rb") as file:
            bytesContent = file.read()

        extensionType = os.path.splitext(path)[1][1:]
        return bytesContent, extensionType

    def addImage(self, imageName : str, imageBytes : bytes, extensionType : str = "png") -> None:
        """
        ### Explanation
        Adds an image to database.

        -------------------------------------------------
        ### Parameters
        - imageName[str]:   Save name of image.
        - imageBytes[bytes]: Bytes of new image.
        - extensionType[str]: Extension type like png, jpg or something...
        -------------------------------------------------
        """

        if self.isImageExists(imageName):
            raise ValueError("There is an image with this name!")
        try:
            self.cursor.execute(f"INSERT INTO {self.tableName} VALUES (?, ?, ?)", (imageName, imageBytes, extensionType))
            self.connection.commit()
            print("Image successfully saved!")
        except Exception as error:
            print(error)

    def getSaveImage(self, imageName : str = None, savePath : str = "savedImage") -> None:
        """
        ### Explanation
        Saves the previously saved image in the database as an image to the given path.

        -------------------------------------------------
        ### Parameters
        - imageName[str]:   Name of image in the database.
        - savePath[str]:    Save path. (default: savedImage.png)
        -------------------------------------------------
        """
        if imageName == None:
            raise ValueError("Give me an image boss. (imageName parameter has not declared.)")

        path, extension = os.path.splitext(savePath)

        if extension != "":
            savePath = path

        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE Name = ?", (imageName,))
            data = self.cursor.fetchone()
            if data != None:
                with open(savePath + "." + data[2], "wb") as file:
                    file.write(data[1])
            else:
                print("There is no image with this name in the database!")
        except Exception as error:
            print(error)

        print(f"{imageName} saved successfully. Path:\n{savePath}")

    def isImageExists(self, imageName : str = None) -> bool:
        """
        ### Explanation
        Checks if image exists in database by image name.

        -------------------------------------------------
        ### Parameters
        - imageName[str]:   Name of image in the database.

        -------------------------------------------------
        ### Returns
        - isExists[bool]
        -------------------------------------------------
        """

        if imageName == None:
            raise ValueError("Image name can't left blank!")
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE Name = ?", (imageName,))
            data = self.cursor.fetchone()
            if data != None:
                return True
            return False
        except Exception as error:
            print("Error occurred in isImageExists func. Error: " + str(error))

    def deleteImage(self, imageName : str = None) -> None:
        """
        ### Explanation
        Deletes image by name in database.

        -------------------------------------------------
        ### Parameters
        - imageName[str]:   Name of image in the database.
        -------------------------------------------------
        """

        if imageName == None:
            raise ValueError("Image name can't left blank!")
        
        if not self.isImageExists(imageName):
            raise NameError("There is no image with this name in the database!")
        
        try:
            self.cursor.execute(f"DELETE FROM {self.tableName} WHERE Name = ?", (imageName,))
            self.connection.commit()
            print("Image successfully deleted.")
        except Exception as error:
            print(error)

    def updateImage(self, imageName : str = None, newImageBytes : bytes = None, newExtensionType : str = None) -> None:
        """
        ### Explanation
        Updates image by name in database.

        -------------------------------------------------
        ### Parameters
        - imageName[str]:   Name of image in the database.
        - newImageBytes[bytes]: Bytes of new image.
        - extensionType[str]: Extension type like png, jpg or something...
        -------------------------------------------------
        """

        if imageName == None:
            raise ValueError("Image name can't left blank!")
        
        if not self.isImageExists(imageName):
            raise NameError("There is no image with this name in the database!")

        if newImageBytes == None:
            raise ValueError("New image bytes can't left blank!")

        try:
            if newExtensionType == None:
                self.cursor.execute(f"UPDATE {self.tableName} SET Data = ? WHERE Name = ?", (newImageBytes, imageName))
                self.connection.commit()
            else:
                self.cursor.execute(f"UPDATE {self.tableName} SET Data = ? , Type = ? WHERE Name = ?", (newImageBytes, newExtensionType, imageName))
                self.connection.commit()
            print("Image updated successfully")
        except Exception as error:
            print(error)