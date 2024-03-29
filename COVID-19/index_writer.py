#! python2.7
# coding: utf-8

import re, os, shutil

file_path = raw_input( 'Drop .html file here and press Return...\n' ).strip( '" ' )

f = open( file_path, 'rt' )
content = f.read()
f.close()

match = re.search( '<title>(Index von (file:///.*/(.*)/))</title>', content )
heading = match.group( 1 )
common_prefix = match.group( 2 ).replace( ' ', '%20' )
folder_name = match.group( 3 )

content = content.replace( heading, folder_name )
content = content.replace( common_prefix, '' )

parent_folder_line = '<p id="UI_goUp"><a class="up" href="%s">In den übergeordneten Ordner wechseln</a></p>'
content = re.sub( parent_folder_line % '(file:///.*)', parent_folder_line % '..', content )

icons_folder = 'icons'

files_folder = file_path[ : -5 ] + '-Dateien'
try:
	shutil.rmtree( icons_folder )
except:
	pass
os.rename( files_folder, icons_folder )

files_folder_basename = os.path.basename( files_folder )
content = content.replace( files_folder_basename.replace( ' ', '%20' ), icons_folder )

content = re.sub( ' <td sortable-data="1icons">.*?</tr><tr>', '', content, flags = re.DOTALL )

f = open( 'index.html', 'wt' )
f.write( content )
f.close()

os.remove( file_path )
