# SQLite Image Handler
Simple to use image handler for python sqlite3.

# Functions
Function Name | Parameters | Returns
------------- | ---------- | -------
**[init]** | **databasePath** : *str* <br> **tableName** : *str* | - |
**[startConnection]** | - | - |
**[imageSelector]** | **path** : *str* | **bytesContent** : *bytes* <br> **extensionType** : *str* |
**[addImage]** | **imageName** : *str* <br> **imageBytes** : *bytes* <br> **extensionType** : *str* | - |
**[getSaveImage]** | **imageName** : *str* <br> **savePath** : *str* | - |
**[isImageExists]** | **imageName** : *str* | **isExists** : *bool* |
**[deleteImage]** | **imageName** : *str* | - |
**[updateImage]** | **imageName** : *str* <br> **newImageBytes** : *bytes* <br> **newExtensionType** : *str* | - |

[See definitions](#definitions)

[init]: #initselfdatabasepath--str--databasedb-tablename--str--images---none

[startConnection]: #startconnectionself---none

[imageSelector]: #imageselectorself-path--str--none---bytescontentbytes-extensiontypestr

[addImage]: #addimageself-imagename--str-imagebytes--bytes-extensiontype--str--png---none

[getSaveImage]: #getsaveimageself-imagename--str--none-savepath--str--savedimage---none

[isImageExists]: #isimageexistsself-imagename--str--none---isexistsbool

[deleteImage]: #deleteimageself-imagename--str--none---none

[updateImage]: #updateimageself-imagename--str--none-newimagebytes--bytes--none-newextensiontype--str--none---none

# Usage

- <h3>Importing & Creating Handler</h3>

```python
from SQLiteImageHandler.SQLiteImageHandler import ImageHandler

handler = ImageHandler(databasePath = "database.db", tableName = "myimages")
```
<hr>

- <h3>Adding an image to the database</h3>

```python
handler.addImage(imageName = "Image 1", *handler.imageSelector(path = r"C:\Users\mozancetin\Desktop\myimage1.png"))
```
<hr>

- <h3>Saving image from database to computer</h3>

```python
# If you want, use a save name like "savedImage" instead of "savedImage.png"
# ..because whatever you write, it will automatically fetch the extension from the database.
handler.getSaveImage(imageName = "Image 1", savePath = r"C:\Users\mozancetin\Desktop\savedImage.png")
```
<hr>

- <h3>Updating the image in the database</h3>

```python
handler.updateImage(imageName = "Image 1", *handler.imageSelector(path=r"C:\Users\mozancetin\Desktop\myimage2.png"))
```
<hr>

- <h3>Deleting an image from database</h3>

```python
handler.deleteImage(imageName = "Image 1")
```
<hr>

- <h3>Check if image exists in the database</h3>

```python
isExists = handler.isImageExists(imageName = "Image 1")
print(isExists)
```
<hr>

- <h3>Get bytes of image and extension type</h3>

```python
bytesOfImage, extensionType = handler.imageSelector(path=r"C:\Users\mozancetin\Desktop\myimage1.png")
print("Bytes Length: " + str(len(bytesOfImage)) + "\nExtension Type: " + extensionType)
```
<hr>
<br>

# Definitions

### __init__(self,databasePath : str = "database.db", tableName : str = "images") -> None

- Sets the *self.databasePath*, *self.tableName* and calls *startConnection()* func.

<hr>

### startConnection(self) -> None

- Starts the connection with SQLite Database.

<hr>

### imageSelector(self, path : str = None) -> bytesContent[bytes], extensionType[str]

- Selects an image and returns the image's *bytes content* and *extension type*.
- **bytesContent[bytes]:** *Bytes content of image.*
- **extensionType[str]:** *Extension type like png, jpg or something...*

<hr>

### addImage(self, imageName : str, imageBytes : bytes, extensionType : str = "png") -> None

- Adds an image to database.

<hr>

### getSaveImage(self, imageName : str = None, savePath : str = "savedImage") -> None

- Saves the *previously saved image in the database* as an *image to the given path*.

<hr>

### isImageExists(self, imageName : str = None) -> isExists[bool]

- Checks if image exists in database *by image name*.
- **isExists[bool]:** *True if image exists in the database otherwise False*

<hr>

### deleteImage(self, imageName : str = None) -> None

- Deletes image *by name in database*.

<hr>

### updateImage(self, imageName : str = None, newImageBytes : bytes = None, newExtensionType : str = None) -> None

- Updates image *by name in database*.

<hr>
<br>

# CMD Things

```cmd
C:\Users\mozancetin\Desktop\Handler>python SQLiteImageHandler

usage: SQLiteImageHandler [-h] [-v] [--database-path DBPATH] [--table-name TABLENAME] [-a] [-sn SAVE_NAME]
                          [-ip IMAGE_PATH] [-s] [-sdn SAVED_NAME] [-sp SAVE_PATH] [-u] [-in IMAGE_NAME]
                          [-uip UPDATE_IMAGE_PATH] [-d] [-c] [-is]

SQLite Image Handler.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --database-path DBPATH
                        database path.
  --table-name TABLENAME
                        table name of the database

Add an Image:
  Adding an image to the database.

  -a, --add-image       Adds an image to database. (Requires -sn and -ip)
  -sn SAVE_NAME, --save-name SAVE_NAME
                        Save name of image.
  -ip IMAGE_PATH, --image-path IMAGE_PATH
                        Path of the selected image

Save an Image:
  Saving image from database to computer.

  -s, --save-image      Saves the previously saved image in the database as an image to the given path. (Requires -sdn
                        and -sp)
  -sdn SAVED_NAME, --saved-name SAVED_NAME
                        Saved name of image in the database.
  -sp SAVE_PATH, --save-path SAVE_PATH
                        Save path. (default: savedImage.png)

Update an Image:
  Updating the image in the database.

  -u, --update-image    Updates image by name in database. (Requires -in and -uip)
  -in IMAGE_NAME, --image-name IMAGE_NAME
                        Saved name of image in the database.
  -uip UPDATE_IMAGE_PATH, --update-image-path UPDATE_IMAGE_PATH
                        Path of the selected image

Delete an Image:
  Deleting an image from database

  -d, --delete          Deletes image by name in database. (Requires -in)

Other:
  -c, --check           Checks if image exists in database by image name. (Requires -in)
  -is, --image-selector
                        Selects an image and returns the image's bytes length and extension type. (Requires -ip)
```

# TODO's
- [x] Write a readme file
- [x] Add different types of images (Right now just png is supported)
- [x] Add more explanation to functions
- [x] Add deletePhoto, updatePhoto functions
- [x] Raise some errors
- [x] Add Usage to readme
- [x] Upload to pypi
- [x] Write a description of each function for README
- [x] Add some cmd things
