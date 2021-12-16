#! python2.7
# coding: utf-8

import re, os, shutil

file_path = raw_input( 'Drop .html file here and press Return...\n' )[ 1 : -1 ]

f = open( file_path, 'rt' )
content = f.read()
f.close()

match = re.search( '<title>(Index von (file:///.*/(.*)/))</title>', content )
print match.groups()
heading = match.group( 1 )
common_prefix = match.group( 2 ).replace( ' ', '%20' )
folder_name = match.group( 3 )

content = content.replace( heading, folder_name )
content = content.replace( common_prefix, '' )

# match = re.search( '<p id="UI_goUp"><a class="up" href="(file:///.*)">In den übergeordneten Ordner wechseln</a></p>', content )
# content = content.replace( match.group( 1 ), '..' )

icons_folder = 'icons'

files_folder = file_path[ : -5 ] + '-Dateien'
print files_folder
try:
	shutil.rmtree( icons_folder )
except:
	pass
os.rename( files_folder, icons_folder )

files_folder_basename = os.path.basename( files_folder )
content = content.replace( files_folder_basename.replace( ' ', '%20' ), icons_folder )

f = open( 'index.html', 'wt' )
f.write( content )
f.close()

os.remove( file_path )
