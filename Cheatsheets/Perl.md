### **Perl Cheat Sheet:**

**1. Basics:**
   - **Printing:**
     - Display information to the console.
     ```perl
     print "Hello, Perl!\n";
     ```
   - **Taking Inputs:**
     - Receive user input.
     ```perl
     my $userInput = <STDIN>;
     chomp($userInput); # Remove newline
     ```

**2. Control Flow:**
   - **For Loops:**
     - Iterate over a range of values.
     ```perl
     for my $i (0..4) {
         # code block
     }
     ```

**3. Subroutines:**
   - **Defining Subroutines:**
     - Encapsulate reusable code.
     ```perl
     sub mySubroutine {
         my ($parameter) = @_;
         # code block
         return $result;
     }
     ```

**4. Variables:**
   - **Variable Declaration:**
     - Variables are dynamically typed.
     ```perl
     my $myVar = "Hello, Perl!";
     ```
   - **Variable Interpolation:**
     - Substitute variable values in strings.
     ```perl
     print "Value: $myVar\n";
     ```

**5. Arrays and Lists:**
   - **Array Operations:**
     - Manipulate and modify arrays.
     ```perl
     my @myArray = (1, 2, 3, 4, 5);

     # Push and pop
     push @myArray, 6;
     my $poppedItem = pop @myArray;

     # Shift and unshift
     my $shiftedItem = shift @myArray;
     unshift @myArray, 7, 8;

     # Index and scalar context
     my $indexOf2 = grep { $myArray[$_] == 2 } 0..$#myArray;
     my $arrayLength = scalar @myArray;

     # Sorting
     my @sortedArray = sort { $a <=> $b } @myArray;
     ```

**6. File Handling:**
   - **Reading from a File:**
     ```perl
     open my $file, '<', 'file.txt' or die "Couldn't open file: $!";
     my $content = do { local $/; <$file> };
     close $file;
     ```
   - **Writing to a File:**
     ```perl
     open my $file, '>', 'new_file.txt' or die "Couldn't open file: $!";
     print $file "Hello, Perl!\n";
     close $file;
     ```

**7. Exception Handling:**
   - **Try-Catch Blocks:**
     ```perl
     eval {
         # code block
     };
     if ($@) {
         # handle error
     }
     ```

**8. Strings:**
   - **String Manipulation:**
     ```perl
     my $myString = "Hello, Perl!";

     # Uppercase and lowercase
     my $upperCase = uc $myString;
     my $lowerCase = lc $myString;

     # String length
     my $length = length $myString;

     # String concatenation
     my $newString = $myString . " Welcome!";

     # Substring
     my $slicedString = substr $myString, 7, 5;

     # Check if a substring exists
     my $isPresent = index($myString, "Perl") != -1;
     ```

**9. Control Structures:**
   - **Conditional Statements:**
     ```perl
     if ($condition) {
         # code block
     } elsif ($anotherCondition) {
         # code block
     } else {
         # code block
     }
     ```

**10. Regular Expressions:**
   - **Pattern Matching:**
     ```perl
     my $pattern = "\\d+";
     if ("123" =~ /$pattern/) {
         # code block
     }
     ```

**11. Hashes:**
   - **Hash Operations:**
     - Manipulate and modify hashes.
     ```perl
     my %myHash = ('key1' => 'value1', 'key2' => 'value2');

     # Adding and deleting
     $myHash{'key3'} = 'value3';
     delete $myHash{'key1'};

     # Accessing values
     my $valueForKey2 = $myHash{'key2'};

     # Checking existence
     my $keyExists = exists $myHash{'key1'};
     ```

**12. Modules:**
   - **Using Modules:**
     ```perl
     use MyModule;
     my $result = MyModule::myFunction();
     ```

**13. Object-Oriented Programming:**
   - **Class Definition:**
     ```perl
     package MyClass;
     sub new {
         my $class = shift;
         my $self = {};
         bless $self, $class;
         return $self;
     }
     ```

**14. Regular Expressions:**
   - **Pattern Matching:**
     ```perl
     my $pattern = "\\d+";
     if ("123" =~ /$pattern/) {
         # code block
     }
     ```

**15. Database Interaction:**
   - **Using DBI (Database Interface):**
     ```perl
     use DBI;
     my $dbh = DBI->connect("dbi:mysql:database=testdb", "user", "password");
     my $sth = $dbh->prepare("SELECT * FROM table");
     $sth->execute();
     my $result = $sth->fetchrow_array();
     ```

