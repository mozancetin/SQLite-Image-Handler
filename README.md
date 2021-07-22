# SQLite Image Handler
Simple to use image handler for python sqlite3.

# Functions
Function Name | Parameters | Returns
------------- | ---------- | -------
**init** | **databasePath** : *str* <br> **tableName** : *str* | - |
**startConnection** | - | - |
**imageSelector** | **path** : *str* | **bytesContent** : *bytes* <br> **extensionType** : *str* |
**addImage** | **imageName** : *str* <br> **imageBytes** : *bytes* <br> **extensionType** : *str* | - |
**getSaveImage** | **imageName** : *str* <br> **savePath** : *str* | - |
**isImageExists** | **imageName** : *str* | **isExists** : *bool* |
**deleteImage** | **imageName** : *str* | - |
**updateImage** | **imageName** : *str* <br> **newImageBytes** : *bytes* <br> **newExtensionType** : *str* | - |

# Usage
- <h3> Importing & Creating Handler </h3>

```python
from SQLiteImageHandler import SQLiteImageHandler

handler = SQLiteImageHandler(databasePath = "database.db", tableName = "myimages")
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
handler.getSaveImage(imageName = "Image 1", savePath = r"C:\Users\mozancetin\Desktop\savedImage.png")ü
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

# TODO's
- [x] Write a readme file
- [x] Add different types of images (Right now just png is supported)
- [x] Add more explanation to functions
- [x] Add deletePhoto, updatePhoto functions
- [x] Raise some errors
- [x] Add Usage to readme
- [x] Upload to pypi
- [ ] Write a description of each function for README
- [ ] Add some cmd things
