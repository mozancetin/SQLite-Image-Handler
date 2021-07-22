# SQLite Image Handler
Simple to use image handler for python sqlite3.

# Functions
Function Name | Parameters | Returns
------------- | ---------- | -------
**[init](#-__init__(self,-databasePath-:-str-=-"database.db",-tableName-:-str-=-"images")-->-None)** | **databasePath** : *str* <br> **tableName** : *str* | - |
**[startConnection][2]** | - | - |
**[imageSelector][3]** | **path** : *str* | **bytesContent** : *bytes* <br> **extensionType** : *str* |
**[addImage][4]** | **imageName** : *str* <br> **imageBytes** : *bytes* <br> **extensionType** : *str* | - |
**[getSaveImage][5]** | **imageName** : *str* <br> **savePath** : *str* | - |
**[isImageExists][6]** | **imageName** : *str* | **isExists** : *bool* |
**[deleteImage][7]** | **imageName** : *str* | - |
**[updateImage][8]** | **imageName** : *str* <br> **newImageBytes** : *bytes* <br> **newExtensionType** : *str* | - |

<br>


[See definitions](#definitions)

# Usage
- <h3> Importing & Creating Handler </h3>

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

# Definitions

### __init__(self, databasePath : str = "database.db", tableName : str = "images") -> None

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

# TODO's
- [x] Write a readme file
- [x] Add different types of images (Right now just png is supported)
- [x] Add more explanation to functions
- [x] Add deletePhoto, updatePhoto functions
- [x] Raise some errors
- [x] Add Usage to readme
- [x] Upload to pypi
- [x] Write a description of each function for README
- [ ] Add some cmd things
