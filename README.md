# SQLite Image Handler
Simple to use image handler for python sqlite3.

# Functions
Function Name | Parameters | Returns
------------- | ---------- | -------
startConnection | - | - |
imageSelector | path : str | bytesContent : bytes <br> extensionType : str |
addImage | imageName : str <br> imageBytes : bytes <br> extensionType : str | - |
getSaveImage | imageName : str <br> savePath : str | - |
isImageExists | imageName : str | isExists : bool |
deleteImage | imageName : str | - |
updateImage | imageName : str <br> newImageBytes : bytes <br> newExtensionType : str | - |

# TODO's
- [x] Write a readme file
- [x] Add different types of images (Right now just png is supported)
- [x] Add more explanation to functions
- [x] Add deletePhoto, updatePhoto functions
- [x] Raise some errors
- [ ] Add Usage to readme
