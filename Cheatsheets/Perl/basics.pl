my $name = "Raven" ;
print("Hello $name") ;

# This is case of interpolation.
$str = "Welcome to \ntutorialspoint.com!";
print("$str\n");

# This is case of non-interpolation.
$str = 'Welcome to \ntutorialspoint.com!';
print("$str\n");

# Only W will become upper case.
$str = "\uwelcome to tutorialspoint.com!";
print("$str\n");

# Whole line will become capital.
$str = "\UWelcome to tutorialspoint.com!";
print("$str\n");

# A portion of line will become capital.
$str = "Welcome to \Ututorialspoint\E.com!"; 
print("$str\n");

# Backslash non alpha-numeric including spaces.
$str = "\QWelcome to tutorialspoint's family";
print("$str\n\n");


########################
#Variable Declarations
########################

#Scalars

$age = 25;             # An integer assignment
$name = "John Paul";   # A string 
$salary = 1445.50;     # A floating point

print("Age = $age\n");
print("Name = $name\n");
print("Salary = $salary\n\n");

$integer = 200;
$negative = -300;
$floating = 200.340;
$bigfloat = -1.2E-23;

# 377 octal, same as 255 decimal
$octal = 0377;

# FF hex, also 255 decimal
$hexa = 0xff;

print "integer = $integer\n";
print "negative = $negative\n";
print "floating = $floating\n";
print "bigfloat = $bigfloat\n";
print "octal = $octal\n";
print "hexa = $hexa\n\n";

# Array
@ages = (25, 30, 40);             
@names = ("John Paul", "Lisa", "Kumar");

print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n\n";

#Hashes
%names = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);

print "\$names{'John Paul'} = $names{'John Paul'}\n";
print "\$names{'Lisa'} = $names{'Lisa'}\n";
print "\$names{'Kumar'} = $names{'Kumar'}\n\n";

#Variable context
@names = ('John Paul', 'Lisa', 'Kumar');

@copy = @names;
$size = @names;

print "Given names are : @copy\n";
print "Number of names are : $size\n\n";

