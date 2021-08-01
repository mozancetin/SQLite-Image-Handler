from SQLiteImageHandler import ImageHandler
import argparse
from __init__ import __version__

parser = argparse.ArgumentParser(description="SQLite Image Handler.")
parser.add_argument("-v", "--version", action="version", version=f'SQLiteImageHandler {__version__}')
parser.add_argument("--database-path", help="database path.", dest="dbpath", type=str)
parser.add_argument("--table-name", help="table name of the database", dest="tablename", type=str)

addGroup = parser.add_argument_group(title="Add an Image", description="Adding an image to the database.")
addGroup.add_argument("-a", "--add-image", help="Adds an image to database. (Requires -sn and -ip)", action="store_true")
addGroup.add_argument("-sn", "--save-name", help="Save name of image.", type=str)
addGroup.add_argument("-ip", "--image-path", help="Path of the selected image", type=str)

saveGroup = parser.add_argument_group(title="Save an Image", description="Saving image from database to computer.")
saveGroup.add_argument("-s", "--save-image", help="Saves the previously saved image in the database as an image to the given path. (Requires -sdn and -sp)", action="store_true")
saveGroup.add_argument("-sdn", "--saved-name", help="Saved name of image in the database.", type=str)
saveGroup.add_argument("-sp", "--save-path", help="Save path. (default: savedImage.png)", default="savedImage.png")

updateGroup = parser.add_argument_group(title="Update an Image", description="Updating the image in the database.")
updateGroup.add_argument("-u", "--update-image", help="Updates image by name in database. (Requires -in and -uip)", action="store_true")
updateGroup.add_argument("-in", "--image-name", help="Saved name of image in the database.", type=str)
updateGroup.add_argument("-uip", "--update-image-path", help="Path of the selected image", type=str)

deleteGroup = parser.add_argument_group(title="Delete an Image", description="Deleting an image from database")
deleteGroup.add_argument("-d", "--delete", help="Deletes image by name in database. (Requires -in)", action="store_true")

otherGroup = parser.add_argument_group(title="Other")
otherGroup.add_argument("-c", "--check", help="Checks if image exists in database by image name. (Requires -in)", action="store_true")
otherGroup.add_argument("-is", "--image-selector", help="Selects an image and returns the image's bytes length and extension type. (Requires -ip)", action="store_true")
args = parser.parse_args()

if args.dbpath == None or args.tablename == None:
    parser.print_help()
else:
    handler = ImageHandler(databasePath=args.dbpath, tableName=args.tablename)
    if args.add_image:
        if args.save_name != None and args.image_path != None:
            handler.addImage(args.save_name, *handler.imageSelector(path=args.image_path))
        else:
            print("You need to use -sn and -ip")

    if args.save_image:
        if args.saved_name != None and args.save_path != None:
            saved_image = args.saved_name
            handler.getSaveImage(imageName = saved_image, savePath = args.save_path)
        else:
            print("You need to use -sdn and -sp")

    if args.update_image:
        if args.image_name != None and args.update_image_path != None:
            name = args.image_name
            path = args.update_image_path
            handler.updateImage(name, *handler.imageSelector(path=path))
        else:
            print("You need you use -in and -uip")

    if args.delete:
        if args.image_name != None:
            image_name = args.image_name
            handler.deleteImage(imageName=image_name)
        else:
            print("You need to use -in")

    if args.check:
        if args.image_name != None:
            image_name = args.image_name
            print(handler.isImageExists(imageName=image_name))
        else:
            print("You need to use -in")

    if args.image_selector:
        if args.image_path != None:
            path = args.image_path
            bytesOfImage, extensionType = handler.imageSelector(path=path)
            print("Bytes Length: " + str(len(bytesOfImage)) + "\nExtension Type: " + extensionType)