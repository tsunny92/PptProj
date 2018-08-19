case $facts['cloud'] {
	'aws': {
	 	notice('This is AWS')
		}

	'gcp': {
		notice('This is Google cloud')
		}
	'default': {
		notice('Default set')
		}
}
