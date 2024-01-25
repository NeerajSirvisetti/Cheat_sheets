
#Operations
$str = "hello" . "world";       # Concatenates strings.
$num = 5 + 10;                  # adds two numbers.
$mul = 4 * 5;                   # multiplies two numbers.
$mix = $str . $num;             # concatenates string and number.

print "str = $str\n";
print "num = $num\n";
print "mul = $mul\n";
print "mix = $mix\n\n";

#Multiline 
print <<EOF;
This is
a multiline
string
EOF

#V-strings
$smile  = v9786;
$foo    = v102.111.111;
$martin = v77.97.114.116.105.110; 

print "smile = $smile\n";
print "foo = $foo\n";
print "martin = $martin\n";

#Special literals
print "File name ". __FILE__ . "\n";
print "Line Number " . __LINE__ ."\n";
print "Package " . __PACKAGE__ ."\n";

# they can not be interpolated
print "__FILE__ __LINE__ __PACKAGE__\n";