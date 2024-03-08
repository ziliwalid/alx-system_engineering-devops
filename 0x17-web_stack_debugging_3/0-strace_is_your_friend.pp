# replaces line in a file given

$filePath = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${filePath}",
  path    => ['/bin','/usr/bin']
}
