"""Form -> (concept_phrase, question_what, goal_text) mapping.

Authoritative cross-fable bones for boy-wolf metaphor-rich examples.
Forms used by atom subjects (G1-01..08) are deliberately excluded —
atom subjects show the form via {form_display} (the lesson is copy-
from-prompt), so they MUST keep goal_text="" or the FORM_LEAK check
will fire when the same form happens to appear in a metaphor subject.
"""

GOALS: dict[str, dict[str, str]] = {
    "'()": {
        "concept": 'an empty list',
        "what":    'the empty list',
        "goal":    'create an empty list',
    },
    "'(1 2 3)": {
        "concept": 'using the quote reader macro',
        "what":    'the form read by the quote reader',
        "goal":    'use the quote reader macro to read a list of three numbers',
    },
    '(#(* % %) 6)': {
        "concept": 'using the anonymous-function reader macro',
        "what":    'the result of calling the generated function',
        "goal":    'use the #(...) reader macro to create a function that squares its argument',
    },
    '(#(* %1 %2) 3 4)': {
        "concept": 'the multi-argument shorthand syntax',
        "what":    'the result of using the #() shorthand to create a function that multiplies two arguments and applying it to 3 and 4',
        "goal":    'use the shorthand syntax to create a function that multiplies two arguments and apply it to 3 and 4',
    },
    '(#(+ % 1) 5)': {
        "concept": 'the shorthand function syntax',
        "what":    'the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5',
        "goal":    'use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5',
    },
    '((comp inc inc) 5)': {
        "concept": 'composing inc twice',
        "what":    'the result of chaining two inc recipe-cards and applying them to 5',
        "goal":    'compose two inc functions and apply them to 5',
    },
    '((comp str inc) 9)': {
        "concept": 'composing str and inc',
        "what":    'the result of chaining the str and inc recipe-cards and applying them to 9',
        "goal":    'compose str and inc functions and apply them to 9',
    },
    '((fn [a b c] (+ a b c)) 1 2 3)': {
        "concept": 'the three-argument anonymous function call',
        "what":    'the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3',
        "goal":    'create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3',
    },
    '((fn [a b] (* a b)) 3 4)': {
        "concept": 'the two-argument anonymous function call',
        "what":    'the result of applying an anonymous fn with two parameters that multiplies them to 3 and 4',
        "goal":    'create an anonymous function that multiplies its two arguments and apply it to 3 and 4',
    },
    '((fn [f x] (f (f x))) inc 5)': {
        "concept": 'applying a function twice',
        "what":    'the result of inc applied twice',
        "goal":    'apply the inc function twice to 5',
    },
    '((fn [x] (* x x)) 6)': {
        "concept": 'the function call with self-multiplication',
        "what":    'the result of applying an anonymous fn that multiplies its argument by itself to 6',
        "goal":    'apply a function that squares its argument to 6',
    },
    '((fn [x] (+ x 1)) 4)': {
        "concept": 'the anonymous function call',
        "what":    'the result of applying an anonymous fn that adds 1 to its argument to the value 4',
        "goal":    'create an anonymous function that adds 1 to its argument and apply it to 4',
    },
    '((fn [x] x x x 99) 1)': {
        "concept": 'the function body with multiple expressions',
        "what":    'the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1',
        "goal":    'create an anonymous function with multiple forms in its body but return only the last one',
    },
    '((fn [x] {:pre [(pos? x)]} (* x 2)) 5)': {
        "concept": 'the result of a function call that satisfies its precondition',
        "what":    'what the function returns when the precondition holds',
        "goal":    'call a function with a positive precondition on a positive number, doubling it',
    },
    '((juxt inc dec) 5)': {
        "concept": 'juxtaposing inc and dec',
        "what":    'the pair of results produced by asking both the inc and dec recipe-cards about 5',
        "goal":    'apply both inc and dec functions to 5 and return both results as a vector',
    },
    '((partial + 10) 5)': {
        "concept": 'partial application of +',
        "what":    'the result of applying the half-loaded + card pre-filled with 10 to the count 5',
        "goal":    'apply + with 10 as the first argument and 5 as the second',
    },
    '(* (+ 1 2) (+ 3 4))': {
        "concept": 'the nested product of sums',
        "what":    'the product of two nested sums',
        "goal":    'multiply the sum of 1 and 2 by the sum of 3 and 4',
    },
    '(* (+ 1 2) 3)': {
        "concept": 'the nested multiplication',
        "what":    'the result of multiplying a nested sum by 3',
        "goal":    'multiply the sum of 1 and 2 by 3',
    },
    '(* 1 2 3 4 5)': {
        "concept": 'the multi-arg product',
        "what":    'the product of 1 through 5',
        "goal":    'multiply the integers 1 through 5',
    },
    '(* 10 10)': {
        "concept": 'repeated multiplication',
        "what":    '10 to the second power',
        "goal":    'multiply 10 by itself',
    },
    '(* 1000000 1000000)': {
        "concept": 'the large multiplication',
        "what":    'the product of one million and one million',
        "goal":    'multiply one million by one million',
    },
    '(* 2 2 2)': {
        "concept": 'repeated multiplication',
        "what":    '2 to the third power',
        "goal":    'multiply 2 by itself three times',
    },
    '(* 2 3 4)': {
        "concept": 'the multi-arg product',
        "what":    'the product of 2, 3, and 4',
        "goal":    'multiply 2, 3, and 4',
    },
    '(* 2/3 3/4)': {
        "concept": 'the product of two ratios',
        "what":    'the product of two-thirds and three-quarters',
        "goal":    'multiply two-thirds by three-quarters',
    },
    '(* 3 3 3 3)': {
        "concept": 'repeated multiplication',
        "what":    '3 to the fourth power',
        "goal":    'multiply 3 by itself four times',
    },
    '(* 5 5 5)': {
        "concept": 'the inline multiplication without binding',
        "what":    'the result of multiplying 5 by itself three times without any binding',
        "goal":    'compute 5 cubed using direct values',
    },
    '(* 5 5)': {
        "concept": 'repeated multiplication',
        "what":    '5 to the second power',
        "goal":    'multiply 5 by itself',
    },
    '(* 7 6)': {
        "concept": 'the multiplication',
        "what":    'the product of 7 and 6',
        "goal":    'multiply 7 by 6',
    },
    '(+\n  1\n  2)': {
        "concept": 'the addition split across lines',
        "what":    'the result of an addition formatted across multiple lines',
        "goal":    'add 1 and 2 in a form whose arguments are on separate lines',
    },
    '(+    1    2)': {
        "concept": 'the addition with extra spacing',
        "what":    'the result of an addition formatted with extra spaces',
        "goal":    'add 1 and 2 in a form with extra spaces between tokens',
    },
    '(+ (* 2 3) (* 4 5))': {
        "concept": 'the sum of two products',
        "what":    'the sum of two nested products',
        "goal":    'add the product of 2 and 3 to the product of 4 and 5',
    },
    '(+ (* 3 8) (* 2 4))': {
        "concept": 'the sum of products',
        "what":    'the result of adding the product of 3 and 8 to the product of 2 and 4',
        "goal":    'compute the product of 3 and 8, add the product of 2 and 4',
    },
    '(+ 1 (if true 10 20))': {
        "concept": 'the arithmetic expression with conditional',
        "what":    'the result of adding 1 to the conditional value',
        "goal":    'add 1 to the result of choosing between 10 and 20 based on a true condition',
    },
    '(+ 1 2 3 4 5 6 7 8 9 10)': {
        "concept": 'the sum of ten numbers',
        "what":    'the sum of integers 1 through 10',
        "goal":    'add the integers 1 through 10',
    },
    '(+ 1 2 3 4)': {
        "concept": 'the multi-arg sum',
        "what":    'the sum of 1, 2, 3, and 4',
        "goal":    'add 1, 2, 3, and 4',
    },
    '(+ 1 2) ; sum of one and two': {
        "concept": 'the addition with a trailing comment',
        "what":    'the result, ignoring the comment',
        "goal":    'add 1 and 2 with a trailing comment',
    },
    '(+ 10 20 30)': {
        "concept": 'the sum of three numbers',
        "what":    'the sum of 10, 20, and 30',
        "goal":    'add 10, 20, and 30',
    },
    '(+ 2 3)': {
        "concept": 'the simple addition',
        "what":    'the result of adding 2 and 3',
        "goal":    'add 2 and 3',
    },
    '(+ 7 8)': {
        "concept": 'the addition',
        "what":    'the sum of 7 and 8',
        "goal":    'add 7 and 8',
    },
    '(+ 99999999999 1)': {
        "concept": 'the large addition',
        "what":    'the sum of 99999999999 and 1',
        "goal":    'add 1 to 99999999999',
    },
    '(- (* 5 4) 7)': {
        "concept": 'the nested arithmetic',
        "what":    'the result of multiplying 5 and 4, then subtracting 7',
        "goal":    'compute 5 times 4, then subtract 7',
    },
    '(- 100 (* 5 5))': {
        "concept": 'the nested subtraction',
        "what":    '100 minus a nested product',
        "goal":    'subtract the product of 5 and 5 from 100',
    },
    '(- 100 1 2 3)': {
        "concept": 'the multi-arg subtraction',
        "what":    '100 minus 1, 2, and 3',
        "goal":    'subtract 1, 2, and 3 from 100',
    },
    '(- 20 7)': {
        "concept": 'the subtraction',
        "what":    'the difference of 20 and 7',
        "goal":    'subtract 7 from 20',
    },
    '(- 5 3)': {
        "concept": 'the subtraction',
        "what":    'the difference of 5 and 3',
        "goal":    'subtract 3 from 5',
    },
    '(-> 5 inc inc inc)': {
        "concept": 'threading a value through multiple functions in sequence',
        "what":    'the result of threading 5 through three increments',
        "goal":    'thread the value 5 through inc three times using thread-first',
    },
    '(->> [1 2 3 4] (filter even?) (map inc) (reduce +))': {
        "concept": 'threading a vector through filter, map, and reduce as the last argument',
        "what":    'the sum of mapped values after filtering even numbers',
        "goal":    'thread a vector through filter, map, and reduce using thread-last',
    },
    '(. "abc" toUpperCase)': {
        "concept": 'the alternate dot form for a host method',
        "what":    'the uppercase form of the string abc produced by the host method toUpperCase via the alternate dot syntax',
        "goal":    'call the host method toUpperCase using the alternate dot form',
    },
    '(.toUpperCase "abc")': {
        "concept": 'the host method toUpperCase',
        "what":    "the capitalized result the host's toUpperCase returns on the three-letter string abc",
        "goal":    "call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention",
    },
    '(/ 1.0 2)': {
        "concept": 'the division operation',
        "what":    'the result of 1.0 divided by 2',
        "goal":    'divide 1.0 by 2',
    },
    '(/ 10 2)': {
        "concept": 'the division operation',
        "what":    'the result of using / on 10 and 2',
        "goal":    'divide 10 by 2',
    },
    '(/ 10 3)': {
        "concept": 'the division operation',
        "what":    'the exact rational result of using / on 10 and 3',
        "goal":    'divide 10 by 3',
    },
    '(:cmd {:cmd "ls" :args ["-l"]})': {
        "concept": 'the command string from a shell-call descriptor',
        "what":    'what command string is in the descriptor',
        "goal":    'extract the command name from a shell-call descriptor map',
    },
    '(:deps {:deps {:a 1 :b 2}})': {
        "concept": 'accessing a key from a nested map structure',
        "what":    'the value at the :deps key in a deps-style map',
        "goal":    'extract the value at the :deps key from a nested map',
    },
    '(:doc (meta \'^{:doc "adds two"} plus))': {
        "concept": "the documentation string from a symbol's metadata",
        "what":    'what documentation string is attached to a symbol',
        "goal":    'extract the :doc metadata value from a symbol',
    },
    "(:private (meta '^:private x))": {
        "concept": 'accessing the :private flag from metadata',
        "what":    'whether the :private metadata is set on a symbol',
        "goal":    'check whether the :private flag is present in the metadata of a symbol with :private marker',
    },
    "(:private (meta 'x))": {
        "concept": 'accessing the :private flag from metadata',
        "what":    'whether the :private metadata is set on a plain symbol',
        "goal":    'check whether the :private flag is present in the metadata of a plain symbol without markers',
    },
    '(< 1 2 3)': {
        "concept": 'the less-than chain',
        "what":    'whether 1 < 2 < 3',
        "goal":    'test whether 1 is less than 2 and 2 is less than 3',
    },
    '(< 3 2 1)': {
        "concept": 'the less-than chain',
        "what":    'whether 3 < 2 < 1',
        "goal":    'test whether 3 is less than 2 and 2 is less than 1',
    },
    '(<= 1 1 2)': {
        "concept": 'the less-than-or-equal chain',
        "what":    'whether 1 ≤ 1 ≤ 2',
        "goal":    'test whether 1 is less than or equal to 1 and 1 is less than or equal to 2',
    },
    '(= "a" "a")': {
        "concept": 'the string equality',
        "what":    'whether two equal strings are equal',
        "goal":    'test whether the string "a" equals itself with =',
    },
    "(= 'a.b 'a.b)": {
        "concept": 'testing equality of two namespace symbols',
        "what":    'whether two identical namespace symbols are equal',
        "goal":    'test whether two references to the same namespace symbol are equal',
    },
    '(= (+ 1 2) 3)': {
        "concept": 'the equality assertion at the heart of test checking',
        "what":    'the truth value showing the assertion passes',
        "goal":    'test whether the sum of 1 and 2 equals 3 using equality',
    },
    '(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))': {
        "concept": 'testing equality of two identical function calls',
        "what":    'whether two calls to the same function with the same argument produce the same result',
        "goal":    'test whether two calls to the fully-qualified string uppercasing function with the same argument are equal',
    },
    '(= (reverse (reverse [1 2 3])) [1 2 3])': {
        "concept": 'the property that reversing twice restores the original',
        "what":    'the result of checking the double-reverse property',
        "goal":    'verify the property that reversing a vector twice returns the original vector',
    },
    '(= 1 1 1 1)': {
        "concept": 'the multi-arg equality',
        "what":    'whether four 1s are all equal',
        "goal":    'test with = whether four 1s are all equal',
    },
    '(= 1 1 1)': {
        "concept": 'the equality check',
        "what":    'whether all three are equal',
        "goal":    'test whether 1, 1, and 1 are all equal',
    },
    '(= 1 1 2)': {
        "concept": 'the equality check',
        "what":    'whether all three are equal',
        "goal":    'test whether 1, 1, and 2 are all equal',
    },
    "(= [1 2 3] '(1 2 3))": {
        "concept": 'testing equality of different collection types',
        "what":    'whether vector and list are equal',
        "goal":    'test whether a vector with elements 1, 2, 3 equals a list with the same elements',
    },
    "(= [1 2 3] (vec '(1 2 3)))": {
        "concept": 'the type-conversion behavior between sequences and vectors',
        "what":    'the result of comparing a vector to its converted seq counterpart',
        "goal":    'verify that converting a seq to a vector produces the same data structure',
    },
    '(> 5 4 3 2 1)': {
        "concept": 'the greater-than chain',
        "what":    'whether the numbers are strictly decreasing',
        "goal":    'test whether 5 > 4 > 3 > 2 > 1',
    },
    '(>= 3 3 2)': {
        "concept": 'the greater-than-or-equal chain',
        "what":    'whether 3 ≥ 3 ≥ 2',
        "goal":    'test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2',
    },
    '(Math/abs -7)': {
        "concept": 'the static host method Math/abs',
        "what":    'the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation',
        "goal":    'call the static host method Math/abs with the argument -7',
    },
    '(Math/max 3 9)': {
        "concept": 'the static host method Math/max',
        "what":    'the maximum value of the integers 3 and 9 produced by calling the static host method Math/max via slash notation',
        "goal":    'call the static host method Math/max to find the larger of two numbers',
    },
    '(abs (- 3 8))': {
        "concept": 'the absolute value',
        "what":    'the absolute value of the difference between 3 and 8',
        "goal":    'find the absolute value of 3 minus 8',
    },
    '(abs -5)': {
        "concept": 'the absolute value',
        "what":    'the absolute value of negative 5',
        "goal":    'find the absolute value of negative 5',
    },
    '(abs 0)': {
        "concept": 'the absolute value',
        "what":    'the absolute value of 0',
        "goal":    'find the absolute value of 0',
    },
    '(abs 5)': {
        "concept": 'the absolute value',
        "what":    'the absolute value of 5',
        "goal":    'find the absolute value of 5',
    },
    '(and 1 2 3)': {
        "concept": 'the and conjunction',
        "what":    'the last truthy value',
        "goal":    'return the last value when all values are truthy',
    },
    '(and true false)': {
        "concept": 'the logical and',
        "what":    'the result of using and on true and false',
        "goal":    'test true and false with the and operator',
    },
    '(and true true)': {
        "concept": 'the logical and',
        "what":    'the result of passing true and true through the and-chain of gates',
        "goal":    'test whether two trues both pass through an and-chain of gates',
    },
    '(apply + [1 2 3 4])': {
        "concept": 'applying + to vector elements',
        "what":    'the result of spreading the basket of 1, 2, 3, 4 as ingredients into +',
        "goal":    'apply + to the elements of the vector [1 2 3 4]',
    },
    '(apply max [3 1 4 1 5])': {
        "concept": 'applying max to vector elements',
        "what":    'the largest count found after spreading the basket of 3, 1, 4, 1, 5 into max',
        "goal":    'apply max to the elements of the vector [3 1 4 1 5]',
    },
    '(assoc {:a 1} :a 99)': {
        "concept": 'the assoc operation',
        "what":    'the map after using assoc to change the key :a to value 99',
        "goal":    'update the key :a to value 99 in a map that binds :a to 1',
    },
    '(assoc {:a 1} :b 2)': {
        "concept": 'the assoc operation',
        "what":    'the basket after associating value 2 with the :b compartment',
        "goal":    'associate value 2 with the :b compartment of a basket already binding :a to 1',
    },
    '(boolean "")': {
        "concept": 'the boolean conversion',
        "what":    'the result of using boolean on the empty string',
        "goal":    'convert the empty string to a boolean',
    },
    "(boolean (:private (meta '^:private hidden)))": {
        "concept": 'converting the :private metadata to a boolean',
        "what":    'whether a symbol with :private marker evaluates to true when converted to boolean',
        "goal":    'convert the :private metadata flag of a symbol marked with :private to a boolean',
    },
    "(boolean (:private (meta 'public)))": {
        "concept": 'converting the :private metadata to a boolean',
        "what":    'whether a symbol without :private marker evaluates to false when converted to boolean',
        "goal":    'convert the :private metadata flag of a plain symbol to a boolean',
    },
    '(boolean 0)': {
        "concept": 'the boolean conversion',
        "what":    'the result of using boolean on 0',
        "goal":    'convert 0 to a boolean',
    },
    '(boolean false)': {
        "concept": 'the boolean conversion',
        "what":    'the result of using boolean on false',
        "goal":    'convert false to a boolean',
    },
    '(boolean nil)': {
        "concept": 'the boolean conversion',
        "what":    'the result of using boolean on nil',
        "goal":    'convert nil to a boolean',
    },
    '(case 2 1 :one 2 :two 3 :three :default)': {
        "concept": 'the case statement',
        "what":    'the matched branch',
        "goal":    'match the value 2 against clauses and return the corresponding value',
    },
    '(case 99 1 :one 2 :two :default)': {
        "concept": 'the case statement with default',
        "what":    'the default branch',
        "goal":    'match the value 99 against clauses and return the default when no match is found',
    },
    '(clojure.edn/read-string "42")': {
        "concept": 'parsing a number string with edn/read-string',
        "what":    'the parsed value from the EDN source',
        "goal":    'use edn/read-string to parse a number from a string',
    },
    '(clojure.edn/read-string "[:a :b :c]")': {
        "concept": 'parsing a vector string with edn/read-string',
        "what":    'the parsed vector from the EDN source',
        "goal":    'use edn/read-string to parse a vector of keywords from a string',
    },
    '(clojure.edn/read-string "{:a 1}")': {
        "concept": 'the map parsed from an edn string',
        "what":    'what map is read from the string',
        "goal":    'parse an edn map from a string',
    },
    '(clojure.edn/read-string (pr-str [1 2 3]))': {
        "concept": 'the vector after writing and reading back via edn',
        "what":    'what vector is recovered from the roundtrip',
        "goal":    'serialize a vector to a string with pr-str and read it back into data with clojure.edn/read-string',
    },
    '(clojure.edn/read-string (pr-str {:a 1 :b 2}))': {
        "concept": 'the map after writing and reading back via edn',
        "what":    'what map is recovered from the roundtrip',
        "goal":    'serialize a map to a string with pr-str and read it back into data with clojure.edn/read-string',
    },
    '(clojure.string/split "a\\nb\\nc" #"\\n")': {
        "concept": 'the vector of lines from splitting a string',
        "what":    'what lines result from splitting a string on newlines',
        "goal":    'split a multi-line string on newlines',
    },
    '(clojure.string/split "src:test" #":")': {
        "concept": 'splitting a string by a delimiter',
        "what":    'the vector of parts after splitting a colon-separated path string',
        "goal":    'split a colon-separated classpath-like string into its individual entries',
    },
    '(clojure.string/upper-case "a")': {
        "concept": 'calling a function from a required namespace',
        "what":    'the uppercase form of the character a produced by clojure.string/upper-case',
        "goal":    'call the string uppercasing function from clojure.string on the character a',
    },
    '(cond (= 1 2) :a (= 1 1) :b :else :c)': {
        "concept": 'the multi-clause conditional',
        "what":    'the value of the first arm whose stone reads true',
        "goal":    'walk three condition-stones in order, taking the arm whose stone first reads true',
    },
    '(cond false :a false :b :else :c)': {
        "concept": 'the cond with default clause',
        "what":    'the default value when no clauses match',
        "goal":    'fall through all false conditions and return the default value',
    },
    '(conj [1 2] 3)': {
        "concept": 'the conj operation',
        "what":    'the vector after conjing',
        "goal":    'append 3 to the end of a vector containing 1 and 2',
    },
    "(cons 0 '(1 2 3))": {
        "concept": 'the cons operation',
        "what":    "the seq after cons'ing",
        "goal":    'prepend 0 to the front of a list containing 1, 2, and 3',
    },
    "(contains? #{'clojure.string} 'clojure.set)": {
        "concept": 'testing membership in a set of namespaces',
        "what":    'whether a different namespace is in the set of required namespaces',
        "goal":    'test whether the clojure.set namespace is in the set of required namespaces',
    },
    "(contains? #{'clojure.string} 'clojure.string)": {
        "concept": 'testing membership in a set of namespaces',
        "what":    'whether a namespace is in the set of required namespaces',
        "goal":    'test whether the clojure.string namespace is in the set of required namespaces',
    },
    '(contains? #{1 2 3} 2)': {
        "concept": 'testing set membership',
        "what":    'whether an element is in the set using contains?',
        "goal":    'check whether 2 is a member of a set containing 1, 2, and 3',
    },
    '(contains? #{1 2 3} 4)': {
        "concept": 'testing set membership',
        "what":    'whether an element is in the set using contains?',
        "goal":    'check whether 4 is a member of a set containing 1, 2, and 3',
    },
    '(count "hello")': {
        "concept": 'the count operation',
        "what":    'the result of using count on the string hello',
        "goal":    'count the characters in the string hello',
    },
    '(count #{1 1 1})': {
        "concept": 'the size of a set',
        "what":    'the size of the set',
        "goal":    'count the unique elements in a set literal with duplicate 1s',
    },
    '(count #{1 2 3})': {
        "concept": 'the size of a set',
        "what":    'the size of the set',
        "goal":    'count the elements in a set containing 1, 2, and 3',
    },
    '(count #{:a :b :c})': {
        "concept": 'the count of a collection',
        "what":    'the number of elements in the collection',
        "goal":    'count the elements in a set containing the keywords :a, :b, and :c',
    },
    '(count (:args {:cmd "echo" :args ["hello" "world"]}))': {
        "concept": 'the number of arguments in a shell-call descriptor',
        "what":    'how many arguments are in the descriptor',
        "goal":    'count the number of arguments in a shell-call descriptor map',
    },
    '(count (clojure.string/split-lines "a\\nb\\nc"))': {
        "concept": 'the number of lines in a multi-line string',
        "what":    'how many lines are in the text',
        "goal":    'count the lines in a multi-line string',
    },
    '(count (keys {:a 1 :b 2 :c 3}))': {
        "concept": 'counting keys in a map',
        "what":    'the number of keys in the map',
        "goal":    'count how many keys are in a map binding :a, :b, and :c',
    },
    '(count (range 5))': {
        "concept": 'counting elements in a range',
        "what":    'the count of range 0..4',
        "goal":    'count how many numbers are generated by a range from 0 to 4',
    },
    '(count (rest [10 20 30]))': {
        "concept": 'removing the first element and counting',
        "what":    'the count after removing first',
        "goal":    'count the elements remaining after removing the first element from a vector with 10, 20, and 30',
    },
    '(count (seq [1 2 3]))': {
        "concept": 'creating a sequence from a vector and counting',
        "what":    'the count of seq over a vector',
        "goal":    'convert a vector containing 1, 2, and 3 to a sequence and count its elements',
    },
    '(count ["src" "test" "resources"])': {
        "concept": 'counting the number of elements in a vector',
        "what":    'the number of entries in a classpath-like vector',
        "goal":    'count the number of entries in a vector of classpath directories',
    },
    '(count [1 2 3 4 5])': {
        "concept": 'the count of a collection',
        "what":    'the number of elements in the collection',
        "goal":    'count the elements in the vector [1 2 3 4 5]',
    },
    '(count [1 2 3])': {
        "concept": 'the count operation',
        "what":    'the result of using count on the vector containing 1, 2, and 3',
        "goal":    'count the elements in the vector containing 1, 2, and 3',
    },
    '(count [])': {
        "concept": 'the count operation',
        "what":    'the result of using count on the empty vector',
        "goal":    'count the elements in an empty vector',
    },
    '(count nil)': {
        "concept": 'the number of elements in nil',
        "what":    'how many elements nil contains',
        "goal":    'count the number of elements in nil',
    },
    '(count {:a 1 :b 2})': {
        "concept": 'the count of a collection',
        "what":    'the number of entries in the collection',
        "goal":    'count the key-value pairs in a map',
    },
    '(dec 0)': {
        "concept": 'the decrement operation',
        "what":    '0 minus 1',
        "goal":    'decrement 0',
    },
    '(dec 5)': {
        "concept": 'the decrement operation',
        "what":    '5 minus 1',
        "goal":    'decrement 5 by 1',
    },
    '(dissoc {:a 1 :b 2} :a)': {
        "concept": 'the dissoc operation',
        "what":    'the map after using dissoc to remove a key',
        "goal":    'remove the key :a from a map binding :a to 1 and :b to 2',
    },
    '(distinct [1 1 2 3 3 4])': {
        "concept": 'removing duplicates from a sequence',
        "what":    'the sequence produced by passing [1 1 2 3 3 4] through the dedup-sieve',
        "goal":    'remove duplicate elements from the vector [1 1 2 3 3 4]',
    },
    '(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)': {
        "concept": 'selecting code by host at read time',
        "what":    'the marker for the reader-conditional lesson',
        "goal":    'learn how reader-conditionals choose code per host',
    },
    '(do "(:import (java.util Date)) imports a host class" :imported)': {
        "concept": 'importing a host class',
        "what":    'the marker for the import-form lesson',
        "goal":    'understand how to import a host class into a namespace',
    },
    '(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)': {
        "concept": 'the core.async channel and block primitives',
        "what":    'the keyword marking the core.async lesson',
        "goal":    'study the core.async primitives that form the foundation for async patterns',
    },
    '(do "(deftest …), (is …), (testing …) are the core test forms" :studied)': {
        "concept": 'the fundamental test definition and assertion forms',
        "what":    'the keyword marking the clojure.test lesson',
        "goal":    'study the core test forms: deftest, is, and testing',
    },
    '(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)': {
        "concept": 'ClojureScript to JavaScript interop',
        "what":    'the marker for the cljs-js interop lesson',
        "goal":    'understand how ClojureScript calls JavaScript globals and reads fields',
    },
    '(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)': {
        "concept": 'the fixture pattern for test setup and teardown',
        "what":    'the keyword marking the test fixtures lesson',
        "goal":    'study how use-fixtures wraps every deftest in setup and teardown',
    },
    '(do "*unchecked-math* turns off overflow checking on prims" :studied)': {
        "concept": 'overflow checking in Clojure arithmetic',
        "what":    'the marker for the checked/unchecked lesson',
        "goal":    'understand how to disable overflow checking',
    },
    '(do ".cljc files share code across multiple hosts" :cljc)': {
        "concept": 'files that work on multiple Clojure hosts',
        "what":    'the marker keyword for the .cljc lesson',
        "goal":    'understand the role of .cljc files',
    },
    '(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)': {
        "concept": 'understanding host runtimes',
        "what":    'the marker value when the host overview has been studied',
        "goal":    'understand that Clojure runs on multiple hosts',
    },
    '(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)': {
        "concept": 'the ClojureScript compilation process',
        "what":    'the marker for studying the cljs host',
        "goal":    'understand how ClojureScript compiles to JavaScript',
    },
    '(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)': {
        "concept": 'the family of immutable, time-aware datalog databases',
        "what":    'the keyword marking the datalog database lesson',
        "goal":    'study Datomic and XTDB as immutable, time-aware database systems using datalog',
    },
    '(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)': {
        "concept": 'the host runtime variants',
        "what":    'the marker keyword for the host family',
        "goal":    'name the Clojure implementations for different hosts',
    },
    '(do "Leiningen reads project.clj at the project root" :lein)': {
        "concept": 'the project root configuration discovery mechanism',
        "what":    'the keyword marking the Leiningen configuration lesson',
        "goal":    'understand how Leiningen reads project.clj from the project root',
    },
    '(do "Pedestal layers interceptors over Ring for richer pipelines" :web)': {
        "concept": 'the interceptor architecture that Pedestal builds on Ring',
        "what":    'the keyword marking the Pedestal pattern lesson',
        "goal":    'understand how Pedestal layers interceptors over Ring to create rich request-processing pipelines',
    },
    '(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)': {
        "concept": 'the Reagent library as a Clojure wrapper around React',
        "what":    'the keyword marking the Reagent foundation lesson',
        "goal":    'study how Reagent wraps React with Hiccup-shaped Clojure data structures',
    },
    '(do "Ring models HTTP as request-map -> response-map" :studied)': {
        "concept": 'the HTTP-as-data abstraction that Ring provides',
        "what":    'the keyword marking the Ring foundation lesson',
        "goal":    'study how Ring models HTTP requests and responses as Clojure maps',
    },
    '(do "`clj -M:test` runs the :test alias from deps.edn" :studied)': {
        "concept": 'the alias execution mechanism in the Clojure CLI',
        "what":    'the keyword marking the alias usage lesson',
        "goal":    'study how the clj command with -M flag runs aliases defined in deps.edn',
    },
    '(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))': {
        "concept": 'calling an anonymous function to add two arguments',
        "what":    'the sum of 3 and 4',
        "goal":    'use an anonymous function to add two numbers',
    },
    '(do "aliases compose extra paths, deps, and main opts" :aliases)': {
        "concept": 'the composition of paths, dependencies, and options via aliases',
        "what":    'the keyword marking the alias composition lesson',
        "goal":    'understand how aliases compose extra classpath entries, dependencies, and JVM options',
    },
    '(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)': {
        "concept": 'basilisp Python interop',
        "what":    'the marker keyword for basilisp interop',
        "goal":    'learn how basilisp calls Python code',
    },
    '(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)': {
        "concept": 'the basilisp implementation',
        "what":    'the marker for studying basilisp',
        "goal":    'understand that basilisp is Clojure on Python',
    },
    '(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)': {
        "concept": 'where ClojureScript runs',
        "what":    'the marker for the cljs-runtime lesson',
        "goal":    'learn where ClojureScript executes',
    },
    '(do "components are functions returning Hiccup vectors" :reagent)': {
        "concept": 'the function-based component model in Reagent',
        "what":    'the keyword marking the Reagent component lesson',
        "goal":    'learn how Reagent components are functions that return Hiccup vectors',
    },
    '(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)': {
        "concept": 'the deps.edn configuration manifest for the Clojure CLI',
        "what":    'the keyword marking the deps.edn lesson',
        "goal":    'study the deps.edn file and how it declares dependencies and aliases for the Clojure CLI',
    },
    '(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)': {
        "concept": 'the tools that interpret the deps.edn configuration',
        "what":    'the keyword marking the CLI tools lesson',
        "goal":    'understand how the official clj and clojure CLI tools read deps.edn',
    },
    '(do "fixtures provide setup/teardown around deftests" :fixtures)': {
        "concept": 'the environment-preparation role of fixtures in testing',
        "what":    'the keyword marking the fixture-purpose lesson',
        "goal":    'understand how fixtures provide setup and teardown around tests',
    },
    '(do "go-blocks let you write async code as if it were synchronous" :async)': {
        "concept": 'the synchronous-style pattern that go-blocks enable',
        "what":    'the keyword marking the go-block pattern lesson',
        "goal":    'learn how go-blocks let you write asynchronous code in a synchronous style',
    },
    '(do "good libraries expose data, then functions, then macros sparingly" :studied)': {
        "concept": 'the library-design hierarchy from data through functions to macros',
        "what":    'the keyword marking the design-hierarchy lesson',
        "goal":    'study the library-design principle that good APIs expose data first, functions second, macros sparingly',
    },
    '(do "host stack traces leak through interop; learn to read them" :studied)': {
        "concept": 'debugging host-runtime errors',
        "what":    'the marker for the host-leaks lesson',
        "goal":    'learn to read and debug host runtime errors',
    },
    '(do "import is a top-of-file ns clause" :studied)': {
        "concept": 'import as a namespace clause',
        "what":    'the marker for studying import',
        "goal":    'understand where import forms go in a file',
    },
    '(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)': {
        "concept": 'ClojureScript interop conventions',
        "what":    'the marker keyword for the conventions',
        "goal":    'learn the conventions for ClojureScript-JavaScript interop',
    },
    '(do "kebab-case names, two-space indent, threading for deep nests" :studied)': {
        "concept": 'the community formatting and nesting conventions',
        "what":    'the keyword marking the basic style lesson',
        "goal":    'study the Clojure style guide basics: kebab-case naming, two-space indentation, and threading macros for nesting',
    },
    '(do "pipe, mult, mix, pipeline-async route values across channels" :studied)': {
        "concept": 'the composition operators for building async pipelines',
        "what":    'the keyword marking the async pipeline lesson',
        "goal":    'study how pipe, mult, mix, and pipeline-async route values across channels',
    },
    '(do "pipelines transform streams of values channel-to-channel" :pipelines)': {
        "concept": 'the stream-transformation capability of pipelines',
        "what":    'the keyword marking the pipeline transformation lesson',
        "goal":    'understand how pipelines transform streams of values flowing between channels',
    },
    '(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))': {
        "concept": 'applying a function to each element of a collection',
        "what":    'the incremented values',
        "goal":    'use map to increment each element of a list',
    },
    '(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)': {
        "concept": 'the naming conventions for functions and predicates in idiomatic Clojure',
        "what":    'the keyword marking the naming-conventions lesson',
        "goal":    'learn the Clojure naming conventions: pure function preference, question-mark suffixes for predicates, exclamation marks for side-effectful operations',
    },
    '(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)': {
        "concept": 'the project configuration manifest for Leiningen',
        "what":    'the keyword marking the project.clj lesson',
        "goal":    'study the project.clj file and how it declares dependencies, main entry points, and profiles for Leiningen',
    },
    '(do "queries are written in datalog over EDN-shaped data" :datalog)': {
        "concept": 'the query language and data shape used in datalog databases',
        "what":    'the keyword marking the datalog query lesson',
        "goal":    'learn how queries are written in datalog over EDN-structured data',
    },
    '(do "s/exercise produces sample inputs for a spec" :studied)': {
        "concept": 'the sample-generation capability of s/exercise',
        "what":    'the keyword marking the spec-generator lesson',
        "goal":    'study how s/exercise produces sample inputs from a spec',
    },
    '(do "small public API surface, plain data inputs, return values" :design)': {
        "concept": 'the minimal API surface and data-centric design pattern',
        "what":    'the keyword marking the API design lesson',
        "goal":    'understand the Clojure convention of a small public API surface with plain data inputs and outputs',
    },
    '(do "spec generators turn specs into property-based test inputs" :gens)': {
        "concept": 'the generation mechanism that converts specs to test data',
        "what":    'the keyword marking the test-input generation lesson',
        "goal":    'understand how spec generators turn specs into property-based test inputs',
    },
    '(do "test.check generates inputs and checks properties hold" :studied)': {
        "concept": 'the property-checking library and its capabilities',
        "what":    'the keyword marking the property-based testing lesson',
        "goal":    'study how test.check generates inputs and verifies that properties hold',
    },
    '(do "type hints are metadata that guide compilation" :studied)': {
        "concept": 'the purpose of type hints in Clojure',
        "what":    'the marker keyword for the type-hint lesson',
        "goal":    'understand that type hints guide compilation',
    },
    '(do (+ 1 1) (+ 2 2) (+ 3 3))': {
        "concept": 'the do form with multiple expressions',
        "what":    'the final result evaluated by do from the sequence of expressions',
        "goal":    'evaluate three arithmetic expressions in sequence and return the result of the last one',
    },
    '(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)': {
        "concept": 'the dynamic var rebound inside a binding form, read inside, then read again outside',
        "what":    'the value of the dynamic var when read after the binding form unwound',
        "goal":    'define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits',
    },
    '(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))': {
        "concept": 'the dynamic var rebound inside a binding form and read',
        "what":    'the value of the dynamic var when read inside the binding form after defining it and rebinding',
        "goal":    'define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside',
    },
    '(do (def a (atom 0)) (compare-and-set! a 0 1) @a)': {
        "concept": 'the atom updated via compare-and-set and read',
        "what":    'the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1',
        "goal":    'construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference',
    },
    '(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)': {
        "concept": 'atom with watch',
        "what":    'the log vector after defining an atom a, defining a log atom, adding a watch that records each new value, swapping a, and dereferencing the log',
        "goal":    'construct an atom a, construct a log atom, add a watch to a that conjoins new values to the log, swap a, and dereference the log',
    },
    '(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)': {
        "concept": 'atom with validator',
        "what":    'the value returned by dereferencing a after defining an atom, setting a number? validator, swapping by applying inc, and dereferencing',
        "goal":    'construct an atom holding 0, set a number? validator on it, atomically swap by applying inc, and dereference',
    },
    '(do (def a (atom 0)) (swap! a inc) @a)': {
        "concept": 'the atom updated atomically and then read',
        "what":    'the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing',
        "goal":    'construct an atom holding 0, atomically swap it by applying inc, and dereference',
    },
    '(do (def a (atom 10)) (swap! a + 5) @a)': {
        "concept": 'the atom updated atomically and then read',
        "what":    'the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5',
        "goal":    'construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result',
    },
    '(do (def a (atom 5)) (compare-and-set! a 0 99) @a)': {
        "concept": 'the atom guarded by a compare-and-set whose expected value did not match',
        "what":    'the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails',
        "goal":    'construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference',
    },
    '(do (def a (atom 7)) (deref a))': {
        "concept": 'constructing an atom and extracting its value using the deref function',
        "what":    'the value extracted from an atom using the deref function',
        "goal":    'construct an atom holding 7 and dereference it using the deref function',
    },
    '(do (def a (atom 7)) @a)': {
        "concept": 'constructing an atom and extracting its value using the @ shorthand',
        "what":    'the value extracted from an atom using @',
        "goal":    'construct an atom holding 7 and dereference it using @',
    },
    '(do (def a (atom :start)) (reset! a :done) @a)': {
        "concept": 'the atom reset to a new value and then read',
        "what":    'the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done',
        "goal":    'construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result',
    },
    '(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])': {
        "concept": 'two refs, coordinated alter',
        "what":    'the pair of values returned by dereferencing both a and b after defining them as refs, coordinating their alters inside dosync, and dereferencing',
        "goal":    'construct refs a and b, perform a coordinated transaction that alters both by applying inc, and dereference both',
    },
    '(do (def ag (agent 0)) (send ag inc) (await ag) @ag)': {
        "concept": 'the agent sent a function asynchronously, awaited, and read',
        "what":    'the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing',
        "goal":    'construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference',
    },
    '(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)': {
        "concept": 'the agent sent two updates in succession, awaited, and read',
        "what":    'the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing',
        "goal":    'construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference',
    },
    '(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)': {
        "concept": 'the agent dispatched via send-off, awaited, and read',
        "what":    'the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing',
        "goal":    'construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference',
    },
    '(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)': {
        "concept": 'the agent sent a function asynchronously, awaited, and read',
        "what":    'the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing',
        "goal":    'construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference',
    },
    '(do (def counter (atom 0)) (swap! counter inc) @counter)': {
        "concept": 'binding an atom to counter, atomically incrementing it, and dereferencing the result',
        "what":    'the value after atomically swapping counter with inc and dereferencing',
        "goal":    'construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result',
    },
    '(do (def g 5) (let [g 99] (+ g 1)))': {
        "concept": 'the scope shadowing and computation',
        "what":    'the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def',
        "goal":    'define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let',
    },
    '(do (def lock (Object.)) (locking lock (+ 1 2)))': {
        "concept": 'the arithmetic evaluated inside a critical section guarded by locking',
        "what":    'the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock',
        "goal":    'create an object to use as a monitor, acquire the lock, and evaluate an addition inside',
    },
    '(do (def lock (Object.)) (locking lock 42))': {
        "concept": 'the literal value evaluated inside a critical section guarded by locking',
        "what":    'the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock',
        "goal":    'create an object to use as a monitor, acquire the lock, and evaluate a literal inside',
    },
    '(do (def p (promise)) (deliver p 42) @p)': {
        "concept": 'the promise delivered a value and then dereferenced',
        "what":    'the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing',
        "goal":    'construct a promise, deliver 42 to it, and dereference to get the delivered value',
    },
    '(do (def p (promise)) (deliver p :done) @p)': {
        "concept": 'the promise delivered a value and then dereferenced',
        "what":    'the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing',
        "goal":    'construct a promise, deliver a completion keyword to it, and dereference to get the delivered value',
    },
    '(do (def progress (atom :idle)) (reset! progress :running) @progress)': {
        "concept": 'binding an atom to progress, atomically resetting it to a new value, and dereferencing the result',
        "what":    'the value after atomically resetting progress and dereferencing',
        "goal":    'construct an atom holding an idle value as progress, atomically reset it to running, and dereference the result',
    },
    '(do (def r (ref 0)) (dosync (alter r inc)) @r)': {
        "concept": 'the ref altered inside a transaction and read',
        "what":    'the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing',
        "goal":    'construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference',
    },
    '(do (def r (ref 10)) (dosync (alter r + 5)) @r)': {
        "concept": 'the ref altered inside a transaction and read',
        "what":    'the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing',
        "goal":    'construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference',
    },
    '(do (def r (ref 100)) (dosync (ref-set r 7)) @r)': {
        "concept": 'the ref reset inside a transaction and read',
        "what":    'the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing',
        "goal":    'construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference',
    },
    '(do (def step1 1) (def step2 (+ step1 1)) step2)': {
        "concept": 'evaluating definitions in sequence to establish dependency order',
        "what":    'the value of the second variable after both definitions are loaded in order',
        "goal":    'define step1 as 1, then define step2 as step1 plus 1, then return step2',
    },
    '(do (def v (volatile! 0)) (vswap! v inc) @v)': {
        "concept": 'the volatile updated by vswap! and read',
        "what":    'the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing',
        "goal":    'construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference',
    },
    '(do (def v (volatile! 5)) (vreset! v 99) @v)': {
        "concept": 'the volatile reset by vreset! and read',
        "what":    'the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing',
        "goal":    'construct a volatile holding 5, perform a non-transactional reset to 99, and dereference',
    },
    '(do (def x 1) (def x 99) x)': {
        "concept": 'the redefined binding',
        "what":    'the value of x after redefining it with def from 1 to 99',
        "goal":    'bind x to 1, then redefine it as 99 and return it',
    },
    '(do (def x 10) (let [x 99] x) x)': {
        "concept": 'the outer binding after the let scope',
        "what":    'the value of x in the outer scope after the let scope ends',
        "goal":    'define x, shadow it in a let, then look up x again in the outer scope',
    },
    '(do (def x 10) (let [x 99] x))': {
        "concept": 'the inner binding shadowing the outer',
        "what":    'the value of x inside the let scope where it shadows the def binding',
        "goal":    'define x at the top level, then shadow it locally and return the inner value',
    },
    '(do (def x 42) x)': {
        "concept": 'the top-level binding and lookup',
        "what":    'the value of x after using def to bind x to 42',
        "goal":    'bind x to 42 and return it',
    },
    '(do (def y 7) y)': {
        "concept": 'the top-level binding',
        "what":    'the value of y after using def to bind y to 7',
        "goal":    'bind y to 7 and return it',
    },
    '(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))': {
        "concept": 'calling a macro that emits an addition form',
        "what":    'the sum returned when add-mac expands to an addition of the unquoted arguments',
        "goal":    'define a macro add-mac and call it to add 3 and 4',
    },
    '(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))': {
        "concept": 'defining a conditional macro and invoking it',
        "what":    'the value the rewritten if-do form returns when the test is true and the body has three expressions',
        "goal":    'define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body',
    },
    '(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))': {
        "concept": 'defining and calling a hygienic if-let macro',
        "what":    'the result returned when safe-if-let expands to if-let with binding [x 5] and then-branch (* x 2)',
        "goal":    'define a safe-if-let macro and call it with x bound to 5',
    },
    '(do (defmacro twice [x] `(do ~x ~x)) (twice 7))': {
        "concept": 'defining a macro that repeats its argument',
        "what":    'the value returned by twice expanding to a do-block with the unquoted argument repeated',
        "goal":    'define a macro named twice that emits its argument twice in a do block, then call it',
    },
    '(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))': {
        "concept": 'calling a plain function that adds two numbers',
        "what":    'the sum returned by calling add-fn with arguments 3 and 4',
        "goal":    'define a function add-fn and call it to add 3 and 4',
    },
    '(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))': {
        "concept": 'the multi-argument function definition and call',
        "what":    'the result of calling the function add3, defined via defn to add three arguments, with 1, 2, and 3',
        "goal":    'define a function add3 that adds three arguments, then call it with 1, 2, and 3',
    },
    '(do (defn dbl [x] (* x 2)) (dbl 5))': {
        "concept": 'the named recipe-card and its first call',
        "what":    'the doubled count after defining a recipe named dbl and calling it on 5',
        "goal":    'define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches',
    },
    '(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])': {
        "concept": 'calling methods from two independent protocols',
        "what":    'the vector of results after defining protocols A and B with methods a-op and b-op, extending both to String independently, then calling both methods on the string "x"',
        "goal":    'define two protocols A and B, each with a method, extend both to String type independently, then call both methods',
    },
    '(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))': {
        "concept": 'calling a protocol method on a number',
        "what":    'the value returned after defining protocol Greet with method hail, extending it to Long with an implementation, then calling hail on a number',
        "goal":    'define a protocol named Greet with one method hail, extend it to Long type with an implementation, then call hail on a number',
    },
    '(do (defprotocol Greet (hail [this])) (some? Greet))': {
        "concept": 'a protocol definition',
        "what":    'whether the protocol var Greet is truthy after defining a protocol named Greet with one method hail taking a single argument this',
        "goal":    'define a protocol named Greet with one method hail that takes a single argument this',
    },
    '(do (println "hi") 42)': {
        "concept": 'the do form with side-effects and final return',
        "what":    'the final value evaluated by do, ignoring the intermediate println side-effect',
        "goal":    'execute a print statement for side-effects, then return a different value',
    },
    "(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))": {
        "concept": 'the spec validation check for int? against 42',
        "what":    'the result of validating 42 against the int? spec',
        "goal":    'use spec to validate that 42 conforms to the int? predicate',
    },
    "(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))": {
        "concept": 'the spec validation check for string? against 42',
        "what":    'the result of validating 42 against the string? spec',
        "goal":    'use spec to validate that 42 conforms to the string? predicate',
    },
    '(do 1 2 3)': {
        "concept": 'the do form with multiple values',
        "what":    'the final value evaluated by do from the sequence',
        "goal":    'evaluate a sequence of values and return the last one',
    },
    '(drop 2 [10 20 30 40 50])': {
        "concept": 'dropping elements from a sequence',
        "what":    'the sequence produced by dropping 2 elements from the row of 10, 20, 30, 40, 50',
        "goal":    'drop the first 2 elements from the vector [10 20 30 40 50]',
    },
    '(empty? "")': {
        "concept": 'checking if a string is empty',
        "what":    'whether the string is empty using empty?',
        "goal":    'test whether an empty string is empty',
    },
    '(empty? [1])': {
        "concept": 'checking if a collection is empty',
        "what":    'whether the collection is empty',
        "goal":    'test whether a vector containing 1 is empty',
    },
    '(empty? [])': {
        "concept": 'checking if a collection is empty',
        "what":    'whether the collection is empty',
        "goal":    'test whether an empty vector is empty',
    },
    "(eval '(+ 1 2 3))": {
        "concept": 'evaluating a quoted form at runtime',
        "what":    'the result of evaluating the quoted addition',
        "goal":    'evaluate a quoted addition form at runtime',
    },
    "(eval (list '+ 4 5))": {
        "concept": 'evaluating a dynamically constructed form',
        "what":    'the result of evaluating the constructed list',
        "goal":    'construct a list that represents addition and evaluate it',
    },
    '(every? even? [1 2 3])': {
        "concept": 'checking if all elements satisfy a predicate',
        "what":    'whether every pebble in 1, 2, 3 passes the even? sieve',
        "goal":    'check if all elements in the vector containing 1, 2, and 3 are even',
    },
    '(every? pos? [1 2 3])': {
        "concept": 'checking if all elements satisfy a predicate',
        "what":    'whether every pebble in 1, 2, 3 passes the pos? sieve',
        "goal":    'check if all elements in the vector containing 1, 2, and 3 are positive',
    },
    '(filter even? [1 2 3 4])': {
        "concept": 'filtering even elements from a vector',
        "what":    'the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4',
        "goal":    'keep the even elements from the vector [1 2 3 4]',
    },
    '(filter pos? [-2 -1 0 1 2])': {
        "concept": 'filtering positive elements from a vector',
        "what":    'the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2',
        "goal":    'keep the positive elements from the vector [-2 -1 0 1 2]',
    },
    '(first (range 1 100))': {
        "concept": 'getting the first element of a range',
        "what":    'the first of range 1..99',
        "goal":    'get the first element of a range starting at 1 and ending before 100',
    },
    '(first [10 20 30])': {
        "concept": 'getting the first element',
        "what":    'the first element',
        "goal":    'get the first element of a vector containing 10, 20, and 30',
    },
    '(first nil)': {
        "concept": 'the first element of nil',
        "what":    'what the first element of nil is',
        "goal":    'get the first element of nil',
    },
    '(get {:a 1 :b 2} :a)': {
        "concept": 'map lookup',
        "what":    'the value at :a',
        "goal":    'look up the value at key :a in a map binding :a to 1 and :b to 2',
    },
    '(get {:a 1} :missing :default)': {
        "concept": 'map lookup with default',
        "what":    'the default value when key missing',
        "goal":    'look up a missing key in a map, returning a default value',
    },
    '(get-in {:paths ["src"]} [:paths 0])': {
        "concept": 'accessing a nested value in a map using a path vector',
        "what":    'the first element from a :paths vector in a deps-style map',
        "goal":    'extract the first entry from the :paths vector in a deps-style map',
    },
    '(if (> 5 3) :a :b)': {
        "concept": 'the conditional',
        "what":    "the if's branch",
        "goal":    'choose between :a and :b based on whether 5 is greater than 3',
    },
    '(if false :a :b)': {
        "concept": 'the conditional',
        "what":    'which of :a or :b is returned',
        "goal":    'choose between :a and :b based on a false condition',
    },
    '(if true :a :b)': {
        "concept": 'the conditional',
        "what":    'which of :a or :b is returned',
        "goal":    'choose between :a and :b based on a true condition',
    },
    '(if-let [x 7] (* x x) 0)': {
        "concept": 'using the built-in if-let with an explicit binding',
        "what":    'the result of the then-branch when the binding succeeds',
        "goal":    'use if-let to bind x to 7 and return the square of x',
    },
    '(inc -1)': {
        "concept": 'the increment operation',
        "what":    'negative 1 plus 1',
        "goal":    'increment negative 1',
    },
    '(inc 0)': {
        "concept": 'the increment operation',
        "what":    '0 plus 1',
        "goal":    'increment 0',
    },
    '(inc 5)': {
        "concept": 'the increment operation',
        "what":    '5 plus 1',
        "goal":    'increment 5 by 1',
    },
    '(inst? #inst "2024-01-01")': {
        "concept": 'testing whether a tagged literal reads as an instant',
        "what":    'whether the inst? predicate returns true',
        "goal":    'test that a tagged literal with #inst reads as an instant',
    },
    '(into #{} (map inc) [1 2 3])': {
        "concept": 'the transducer-powered construction of a set from incremented elements',
        "what":    'the set produced by reifying the map-inc transducer into an empty set via into, applied to the vector containing 1, 2, 3',
        "goal":    'use the map-inc transducer with into to create a set from the incremented elements of the vector containing 1, 2, 3',
    },
    '(into #{} [1 2 2 3])': {
        "concept": 'building a set from a vector',
        "what":    'the set built from a vector',
        "goal":    'convert a vector containing duplicates into a set, keeping unique elements',
    },
    "(into [] '(1 2 3))": {
        "concept": 'building a vector from a list',
        "what":    'the vector built from a list',
        "goal":    'convert a list containing 1, 2, and 3 into a vector',
    },
    '(into [] (comp (map inc) (filter even?)) [1 2 3 4])': {
        "concept": 'the composed transducer pipeline of map-inc then filter-even',
        "what":    'the vector result of reifying the composed transducer via into, applying map-inc then filter-even to the vector containing 1, 2, 3, 4',
        "goal":    'compose map-inc and filter-even into a transducer pipeline; apply it with into to the vector [1 2 3 4]',
    },
    '(into [] (filter even?) [1 2 3 4 5])': {
        "concept": 'the filter-even transducer applied via into',
        "what":    'the vector of even elements reified via into with the filter-even transducer applied to the vector containing 1, 2, 3, 4, 5',
        "goal":    'use the filter-even transducer with into to keep only the even numbers from the vector [1 2 3 4 5]',
    },
    '(into [] (map inc) [1 2 3])': {
        "concept": 'the map-inc transducer applied via into',
        "what":    'the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3',
        "goal":    'use the map-inc transducer with into to increment the vector containing 1, 2, 3',
    },
    '(into [] (take 3) (range 100))': {
        "concept": 'the transducer-powered collection of the first few elements',
        "what":    'the vector produced by reifying the take-3 transducer into an empty vector via into, applied to the range of 100 numbers',
        "goal":    'use the take-3 transducer with into to collect the first three elements from a range of 100 numbers',
    },
    '(isa? java.lang.Long java.lang.Number)': {
        "concept": 'checking Java type hierarchy',
        "what":    "whether Long is a type of Number in Java's type hierarchy",
        "goal":    "check whether Long is a type of Number in Java's type system",
    },
    '(isa? java.lang.String java.lang.Number)': {
        "concept": 'checking Java type hierarchy',
        "what":    "whether String is a type of Number in Java's type hierarchy",
        "goal":    "check whether String is a type of Number in Java's type system",
    },
    '(let [+ 99] +)': {
        "concept": 'the shadowed operator binding',
        "what":    'the value locally bound to the + operator via let',
        "goal":    'shadow the plus operator with a local binding and return the bound value',
    },
    '(let [^String s "abc"] (.toUpperCase s))': {
        "concept": 'using a type hint in a binding',
        "what":    'the uppercase form of the type-hinted string abc produced by calling the host method toUpperCase on the binding',
        "goal":    'add a type hint to a binding and call a method on the typed value',
    },
    '(let [a (gensym "x_") b (gensym "x_")] (= a b))': {
        "concept": 'comparing two gensyms created with the same prefix',
        "what":    'whether two fresh gensyms are identical',
        "goal":    'generate two gensyms with the same prefix and check if they are equal',
    },
    '(let [a (int-array [1 2 3])] (alength a))': {
        "concept": 'getting the length of a host array',
        "what":    'the length of the int-array [1 2 3] via the alength function',
        "goal":    'get the length of a host array',
    },
    '(let [a (int-array [10 20 30])] (aget a 1))': {
        "concept": 'indexing into a host array',
        "what":    'the element at index 1 of the int-array [10 20 30] via the aget function',
        "goal":    'access an element in a host array by index',
    },
    '(let [a 1 b (+ a 1)] (+ a b))': {
        "concept": 'establishing local bindings with dependent values',
        "what":    'the sum of two variables with the second depending on the first',
        "goal":    'bind a to 1, bind b to a plus 1, then return the sum of a and b',
    },
    '(let [a 1 b 2] (+ a b))': {
        "concept": 'the multi-binding and addition',
        "what":    'adding a and b after binding both via let to 1 and 2',
        "goal":    'bind a to 1 and b to 2, then add them',
    },
    '(let [a 2 b 3 c 4] (+ a b c))': {
        "concept": 'the three-binding sum',
        "what":    'adding a, b, and c after binding via let to 2, 3, and 4',
        "goal":    'bind a to 2, b to 3, c to 4, and add them',
    },
    '(let [a 3 b (+ a 1) c (* b 2)] c)': {
        "concept": 'the chained bindings with sequential references',
        "what":    'the value of c, bound via let to twice b, after a is 3 and b is a+1',
        "goal":    'bind a to 3, b to a+1, c to 2*b, and return c',
    },
    '(let [a 5 b (* a 2)] b)': {
        "concept": 'the sequential binding where later refers to earlier',
        "what":    'the value of b, bound to twice a via let, after a is bound to 5',
        "goal":    'bind a to 5, then bind b to twice a, and return b',
    },
    '(let [a 5] a)': {
        "concept": 'the local binding and lookup',
        "what":    'the value of a after binding it locally to 5 via let',
        "goal":    'bind a to 5 and return it',
    },
    '(let [a 7] (+ a a))': {
        "concept": 'the binding referenced multiple times',
        "what":    'the result of adding a to itself after binding a locally to 7 via let',
        "goal":    'bind a to 7 and add a to itself',
    },
    '(let [m {:a 1}] (assoc m :a 99) m)': {
        "concept": 'immutability of maps',
        "what":    'the original map after assoc',
        "goal":    'demonstrate that assoc returns a new map without modifying the original',
    },
    '(let [m {:a 1}] (assoc m :b 2) m)': {
        "concept": 'binding a map, adding an entry to a new map, and returning the original',
        "what":    'the original map after assoc returns a new map',
        "goal":    'bind a map m, call assoc to add :b 2 to a new map, then return the unchanged m',
    },
    '(let [n 10] (* n n))': {
        "concept": 'the local binding and multiplication',
        "what":    'multiplying n by itself after binding n locally to 10 via let',
        "goal":    'bind n to 10 and compute n squared',
    },
    '(let [n 5] (* n n n))': {
        "concept": 'the named binding used multiple times',
        "what":    'the result of multiplying n by itself three times after binding n locally to 5 via let',
        "goal":    'bind n to 5 and compute n cubed',
    },
    '(let [v [1 2 3]] (conj v 4) v)': {
        "concept": 'binding a vector, conjoining a new element to a new vector, and returning the original',
        "what":    'the original vector after conj returns a new vector',
        "goal":    'bind a vector v, call conj to add 4 to a new vector, then return the unchanged v',
    },
    '(let [x 10] `(+ ~x ~x))': {
        "concept": 'building a form by unquoting a variable twice inside syntax-quote',
        "what":    'the form produced when x is 10 and unquoted twice',
        "goal":    'build a form where a variable is inserted twice into an addition form',
    },
    '(let [x 3] (+ x 1))': {
        "concept": 'the local binding and addition',
        "what":    'the running total after binding x to 3 and adding 1',
        "goal":    'bind a value of 3 to a local name x for one stretch, then return that value plus one',
    },
    '(let [x 5 y 3] (- x y))': {
        "concept": 'the multi-binding and subtraction',
        "what":    'subtracting y from x after binding via let to 5 and 3',
        "goal":    'bind x to 5 and y to 3, then subtract y from x',
    },
    '(let [x 5] `(a ~x b))': {
        "concept": 'a syntax-quoted form with the variable unquoted',
        "what":    'what you get when unquoting x inside a syntax-quoted form',
        "goal":    'create a form that when x is 5 produces a list containing the value of x',
    },
    '(let [xs [1 2 3]] `(list ~@xs))': {
        "concept": 'building a form by splicing a vector into syntax-quote',
        "what":    'the form produced when splicing a three-element vector',
        "goal":    'build a form that inserts all elements of a vector into a list call',
    },
    '(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))': {
        "concept": 'a factorial computation via loop and recur',
        "what":    'the factorial of 5 computed by walking a circuit',
        "goal":    'walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero',
    },
    "(macroexpand '(-> 1 inc inc))": {
        "concept": 'the complete expansion of the thread-first call',
        "what":    'the final form after threading the value through all steps',
        "goal":    'fully expand a thread-first macro call to see how the value threads through',
    },
    "(macroexpand '(-> x f g))": {
        "concept": 'the expanded form of a thread-first call',
        "what":    'the nested function calls after expansion',
        "goal":    'expand a thread-first macro to see how functions compose',
    },
    "(macroexpand '(when true 1))": {
        "concept": 'the complete expansion of the when-macro call',
        "what":    'the fully expanded form after all macro passes',
        "goal":    'fully expand a when-macro call to reveal the if-form it becomes',
    },
    "(macroexpand-1 '(or a b))": {
        "concept": 'the one-step expansion of the or-macro call',
        "what":    'the intermediate form after expanding the macro once',
        "goal":    'expand an or-macro call one step to reveal its internal structure',
    },
    "(macroexpand-1 '(when true 1))": {
        "concept": 'the one-step expansion of the when-macro call',
        "what":    'the expanded form after one level of macro expansion',
        "goal":    'expand a when-macro call one step to see what code it produces',
    },
    '(map #(* % %) [1 2 3 4])': {
        "concept": 'mapping a squaring operation over a vector',
        "what":    'the sequence produced by mapping a squaring rule over the vector containing 1, 2, 3, and 4',
        "goal":    'apply a squaring operation to each element of the vector [1 2 3 4] returning a sequence',
    },
    '(map (partial * 3) [1 2 3])': {
        "concept": 'mapping partial multiplication over a vector',
        "what":    'the sequence produced by mapping the half-loaded * card pre-filled with 3 over the vector containing 1, 2, and 3',
        "goal":    'apply a partially applied multiplication to each element of the vector containing 1, 2, and 3',
    },
    '(map inc [1 2 3])': {
        "concept": 'mapping increment over a vector',
        "what":    'the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve',
        "goal":    'pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element',
    },
    '(max 1 2 3)': {
        "concept": 'the maximum of three numbers',
        "what":    'the largest of 1, 2, and 3',
        "goal":    'find the maximum of 1, 2, and 3',
    },
    '(max 7 3 9 1 5)': {
        "concept": 'the maximum of five numbers',
        "what":    'the largest of 7, 3, 9, 1, and 5',
        "goal":    'find the maximum of 7, 3, 9, 1, and 5',
    },
    '(min -3 -1 -5)': {
        "concept": 'the minimum of three numbers',
        "what":    'the smallest of -3, -1, and -5',
        "goal":    'find the minimum of -3, -1, and -5',
    },
    '(min 1 2 3)': {
        "concept": 'the minimum of three numbers',
        "what":    'the smallest of 1, 2, and 3',
        "goal":    'find the minimum of 1, 2, and 3',
    },
    '(min 7 3 9 1 5)': {
        "concept": 'the minimum of five numbers',
        "what":    'the smallest of 7, 3, 9, 1, and 5',
        "goal":    'find the minimum of 7, 3, 9, 1, and 5',
    },
    '(mod -7 3)': {
        "concept": 'the modulo operation',
        "what":    'negative seven mod 3',
        "goal":    'find negative 7 modulo 3',
    },
    '(mod 17 5)': {
        "concept": 'the modulo operation',
        "what":    '17 mod 5',
        "goal":    'find 17 modulo 5',
    },
    "(name 'clojure.string)": {
        "concept": 'extracting the string form of a namespace symbol',
        "what":    'the string form of a quoted namespace symbol',
        "goal":    'extract the string form of a quoted namespace symbol',
    },
    "(name 'foo.bar)": {
        "concept": 'extracting the string form of a namespace symbol',
        "what":    'the string form of a quoted namespace symbol',
        "goal":    'extract the string form of a quoted namespace symbol',
    },
    '(neg? -3)': {
        "concept": 'the negative check',
        "what":    'whether -3 is negative',
        "goal":    'check whether -3 is negative using neg?',
    },
    '(neg? 4)': {
        "concept": 'the negative check',
        "what":    'whether 4 is negative',
        "goal":    'check whether 4 is negative using neg?',
    },
    '(not "")': {
        "concept": 'the logical not',
        "what":    'the result of using not on the empty string',
        "goal":    'negate the empty string',
    },
    '(not (> 1 2))': {
        "concept": 'the negation',
        "what":    'the negated comparison',
        "goal":    'negate the result of checking whether 1 is greater than 2',
    },
    '(not 0)': {
        "concept": 'the logical not',
        "what":    'the result of using not on 0',
        "goal":    'negate the value 0',
    },
    '(not false)': {
        "concept": 'the logical not',
        "what":    'the result of using not on false',
        "goal":    'negate the value false',
    },
    '(not nil)': {
        "concept": 'the logical not',
        "what":    'the result of using not on nil',
        "goal":    'negate the value nil',
    },
    '(not true)': {
        "concept": 'the logical not',
        "what":    'the result of using not on true',
        "goal":    'negate the value true',
    },
    '(not= 1 1 2)': {
        "concept": 'the inequality check',
        "what":    'whether at least one differs',
        "goal":    'test whether at least one of 1, 1, and 2 is not equal to the others',
    },
    '(not= 1 1)': {
        "concept": 'the inequality check',
        "what":    'whether 1 differs from itself',
        "goal":    'test whether 1 and 1 are not equal',
    },
    '(not= 1 2)': {
        "concept": 'the inequality check',
        "what":    'whether 1 differs from 2',
        "goal":    'test whether 1 and 2 are not equal',
    },
    '(nth [10 20 30] 0)': {
        "concept": 'accessing by index',
        "what":    'the value at index 0',
        "goal":    'get the element at index 0 of a vector containing 10, 20, and 30',
    },
    '(nth [10 20 30] 2)': {
        "concept": 'accessing by index',
        "what":    'the value at index 2',
        "goal":    'get the element at index 2 of a vector containing 10, 20, and 30',
    },
    '(or false false)': {
        "concept": 'the logical or',
        "what":    'the result of using or on false and false',
        "goal":    'test false or false with the or operator',
    },
    '(or false true)': {
        "concept": 'the logical or',
        "what":    'the result of using or on false and true',
        "goal":    'test false or true with the or operator',
    },
    '(or nil false 5)': {
        "concept": 'the logical or',
        "what":    'the result of using or on nil, false, and 5',
        "goal":    'apply or to nil, false, and 5',
    },
    '(or nil false :found)': {
        "concept": 'the or disjunction',
        "what":    'the first truthy value',
        "goal":    'return the first truthy value from a sequence of values',
    },
    '(pos? -2)': {
        "concept": 'the positive check',
        "what":    'whether -2 is positive',
        "goal":    'check whether -2 is positive using pos?',
    },
    '(pos? 7)': {
        "concept": 'the positive check',
        "what":    'whether 7 is positive',
        "goal":    'check whether 7 is positive using pos?',
    },
    '(print "x")': {
        "concept": 'the print call',
        "what":    'the return value of using print on the string "x"',
        "goal":    'print the string "x" without a newline',
    },
    '(println "hello")': {
        "concept": 'the print-line call',
        "what":    'the return value of using println on the string "hello"',
        "goal":    'print the string "hello" with a newline',
    },
    '(quot (+ 100 50) 5)': {
        "concept": 'the nested quotient',
        "what":    'the integer quotient of the sum of 100 and 50 divided by 5',
        "goal":    'add 100 and 50, then divide by 5',
    },
    '(quot 100 7)': {
        "concept": 'the integer quotient',
        "what":    '100 divided by 7, without remainder',
        "goal":    'find the integer quotient of 100 divided by 7',
    },
    '(quot 17 5)': {
        "concept": 'the integer quotient',
        "what":    '17 divided by 5, without remainder',
        "goal":    'find the integer quotient of 17 divided by 5',
    },
    '(quote (+ 1 2))': {
        "concept": 'quoting an addition form',
        "what":    'what you get when you quote an addition form',
        "goal":    'quote an addition form so it evaluates to a list without computing',
    },
    '(reduce * [1 2 3 4 5])': {
        "concept": 'the fold operation',
        "what":    'the product produced by walking 1, 2, 3, 4, 5 with * as the combine step',
        "goal":    'fold * over the vector [1 2 3 4 5] computing their product',
    },
    '(reduce + 0 [])': {
        "concept": 'the fold with initial value over empty sequence',
        "what":    'the tally returned when walking an empty row with + and an opening tally of 0',
        "goal":    'fold + over an empty sequence starting from an initial accumulator of 0',
    },
    '(reduce + 100 [1 2 3])': {
        "concept": 'the fold with initial value',
        "what":    'the sum produced by walking 1, 2, 3 with + and an opening tally of 100',
        "goal":    'fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100',
    },
    '(reduce + [1 2 3 4])': {
        "concept": 'the fold operation',
        "what":    'the running tally after walking 1, 2, 3, 4 with + as the combine step',
        "goal":    'walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total',
    },
    '(reduce max [3 1 4 1 5 9 2 6])': {
        "concept": 'the fold operation',
        "what":    'the largest pebble found by walking [3 1 4 1 5 9 2 6] with max as the combine step',
        "goal":    'fold max over the vector [3 1 4 1 5 9 2 6] finding the maximum',
    },
    '(rem 100 7)': {
        "concept": 'the remainder',
        "what":    'the remainder when 100 is divided by 7',
        "goal":    'find the remainder when 100 is divided by 7',
    },
    '(rem 17 5)': {
        "concept": 'the remainder',
        "what":    'the remainder when 17 is divided by 5',
        "goal":    'find the remainder when 17 is divided by 5',
    },
    '(seq [])': {
        "concept": 'creating a sequence from an empty vector',
        "what":    'the result of seq on an empty vector',
        "goal":    'convert an empty vector to a sequence',
    },
    '(some even? [1 3 5 8 7])': {
        "concept": 'checking if any element satisfies a predicate',
        "what":    'whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve',
        "goal":    'check if any element in the vector [1 3 5 8 7] is even',
    },
    '(some neg? [1 2 3])': {
        "concept": 'checking if any element satisfies a predicate',
        "what":    'whether any pebble in 1, 2, 3 passes the neg? sieve',
        "goal":    'check if any element in the vector containing 1, 2, and 3 is negative',
    },
    '(some? 0)': {
        "concept": 'whether 0 is considered some',
        "what":    'the result of testing if 0 is some',
        "goal":    'test whether the number 0 is considered some',
    },
    '(some? nil)': {
        "concept": 'whether nil is considered some',
        "what":    'the result of testing if nil is some',
        "goal":    'test whether nil is considered some',
    },
    '(sort [3 1 2])': {
        "concept": 'sorting a sequence',
        "what":    'the sequence produced by sorting the row of 3, 1, 2 into ascending order',
        "goal":    'sort the vector containing 3, 1, and 2 in ascending order',
    },
    '(str 1 "+" 2 "=" 3)': {
        "concept": 'the mixed string concatenation',
        "what":    'the result of using str to join 1, "+", 2, "=", and 3',
        "goal":    'use str to join the integer 1, the plus sign, the integer 2, the equals sign, and the integer 3',
    },
    '(symbol? (gensym))': {
        "concept": 'testing whether gensym produces a symbol',
        "what":    'whether a generated symbol is of type symbol',
        "goal":    'test that gensym returns a symbol',
    },
    '(symbol? 42)': {
        "concept": 'the symbol-predicate on an integer',
        "what":    'whether an integer is a symbol',
        "goal":    'ask whether the integer 42 is a symbol, using the symbol? predicate',
    },
    '(take 3 [10 20 30 40 50])': {
        "concept": 'taking elements from a sequence',
        "what":    'the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50',
        "goal":    'take the first 3 elements from the vector [10 20 30 40 50]',
    },
    '(tap> 42)': {
        "concept": 'the result of tapping a number into the tap pool',
        "what":    'what tap> returns when sending a number',
        "goal":    'send a number into the tap pool',
    },
    '(tap> :hello)': {
        "concept": 'the result of tapping a keyword into the tap pool',
        "what":    'what tap> returns when sending a value',
        "goal":    'send a keyword into the tap pool',
    },
    '(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])': {
        "concept": 'the composed transducer summing the incremented-then-filtered elements',
        "what":    'the sum accumulated via transduce using the composed transducer of map-inc then filter-even, starting from 0, applied to the vector containing 1, 2, 3, 4, 5',
        "goal":    'compose map-inc and filter-even; use transduce to sum the kept elements from the vector [1 2 3 4 5] starting from 0',
    },
    '(try (Math/sqrt 4) (catch Exception _ :err))': {
        "concept": 'catching exceptions from a host method call',
        "what":    'the square root of 4 produced by the static host method Math/sqrt via slash notation when the call succeeds',
        "goal":    'wrap a static host method call in error handling',
    },
    '(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))': {
        "concept": 'the message extracted from a caught Exception',
        "what":    'what message is inside the caught Exception',
        "goal":    'throw an Exception with a message and extract the message from the caught exception',
    },
    '(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))': {
        "concept": 'the data map from a caught ex-info',
        "what":    'what data map is attached to the ex-info',
        "goal":    'throw an ex-info with attached data and extract the data map from the caught exception',
    },
    '(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))': {
        "concept": 'the message extracted from a caught ex-info',
        "what":    'what message is inside the caught ex-info',
        "goal":    'throw an ex-info with a message and extract the message from the caught exception',
    },
    '(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))': {
        "concept": "a single value extracted from the caught ex-info's data",
        "what":    "what value is at a specific key in the ex-info's data",
        "goal":    'throw an ex-info with data, catch it, and extract the value at key :k',
    },
    '(try 42 (catch Exception e :caught))': {
        "concept": 'a try block with no error',
        "what":    'what the try block returns when no error occurs',
        "goal":    'evaluate a number in a try block when no error is thrown',
    },
    '(uuid? #uuid "00000000-0000-0000-0000-000000000000")': {
        "concept": 'testing whether a tagged literal reads as a uuid',
        "what":    'whether the uuid? predicate returns true',
        "goal":    'test that a tagged literal with #uuid reads as a uuid',
    },
    '(when false 1 2 3)': {
        "concept": 'executing expressions when a condition is false',
        "what":    'the result when the condition does not hold',
        "goal":    'evaluate a when-form where the condition is false',
    },
    '(when false :yes)': {
        "concept": 'the when conditional',
        "what":    'the value when the condition is false',
        "goal":    'evaluate a when form with a false condition',
    },
    '(when true 1 2 3)': {
        "concept": 'executing multiple expressions when a condition is true',
        "what":    'the result of the last expression when the condition holds',
        "goal":    'execute three expressions and return the value of the last when the condition is true',
    },
    '(when true :yes)': {
        "concept": 'the when conditional',
        "what":    'the value when the condition is true',
        "goal":    'evaluate a when form with a true condition',
    },
    '(when-not false :ok)': {
        "concept": 'executing an expression when a negated condition is true',
        "what":    'the result when using when-not with a false condition',
        "goal":    'use when-not to execute an expression when the condition is false',
    },
    '(with-out-str (print "x"))': {
        "concept": 'the output captured by redirecting the output stream',
        "what":    'what is captured when output is redirected',
        "goal":    'redirect the output stream and capture what is printed',
    },
    '(with-out-str (println))': {
        "concept": 'the output captured from a bare print-line call',
        "what":    'what is captured when a bare println is redirected',
        "goal":    'redirect the output stream and capture what a bare println produces',
    },
    '(with-out-str (prn 42))': {
        "concept": 'the output captured from printing a number',
        "what":    'what string is produced when printing the number 42',
        "goal":    'print the number 42 and capture the output string',
    },
    '(zero? 0)': {
        "concept": 'the zero check',
        "what":    'whether 0 is zero',
        "goal":    'check whether 0 is zero using zero?',
    },
    '(zero? 5)': {
        "concept": 'the zero check',
        "what":    'whether 5 is zero',
        "goal":    'check whether 5 is zero using zero?',
    },
    '42 ;; the answer': {
        "concept": 'the literal with a trailing comment',
        "what":    'the literal value, ignoring the comment',
        "goal":    'submit the integer 42 with a double-semicolon trailing comment',
    },
    '@(future (* 6 7))': {
        "concept": 'the multiplication wrapped in a future and dereferenced',
        "what":    'the value returned by dereferencing a future that multiplies 6 and 7',
        "goal":    'construct a future that multiplies 6 and 7, and dereference it',
    },
    '@(future (+ 1 2))': {
        "concept": 'the addition wrapped in a future and dereferenced',
        "what":    'the value the messenger returns from adding 1 and 2',
        "goal":    'dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer',
    },
    '["a" "b"]': {
        "concept": 'a vector of strings',
        "what":    'the vector of strings',
        "goal":    'create a vector containing the strings a and b',
    },
    '[1 #_ 2 3]': {
        "concept": 'using the discard reader macro to skip an element',
        "what":    'the vector after the middle element is discarded',
        "goal":    'use the #_ reader macro to skip an element in a vector',
    },
    '[1 2 3]': {
        "concept": 'a vector of three numbers',
        "what":    'the vector',
        "goal":    'create a vector containing 1, 2, and 3',
    },
    '[]': {
        "concept": 'an empty vector',
        "what":    'the empty vector',
        "goal":    'create an empty vector',
    },

    # ── slice yTpz: per-form GOALS for the most common atom-form
    #    GOAL_FALLBACK_GENERIC offenders (G1-01..G1-09 and beyond).
    #    Each entry replaces the generic "evaluate the literal /
    #    predicate / form" fallback with a concrete verb-phrase that
    #    flows naturally into "To {goal_text}, X composed Y" templates.
    "(quote wolf)": {
        "concept": 'the quote special form on the symbol wolf',
        "what":    'the quoted symbol wolf',
        "goal":    'use quote to obtain the symbol wolf without evaluating it',
    },
    "(symbol? 'wolf)": {
        "concept": 'the symbol predicate on a quoted name',
        "what":    'whether the quoted form is a symbol',
        "goal":    'test whether the quoted form is a symbol',
    },
    "(symbol? 'java.util.Date)": {
        "concept": 'the symbol predicate on a quoted host name',
        "what":    'whether the host class name is a symbol',
        "goal":    'test whether the quoted host class name is a symbol',
    },
    "(name 'village.shepherd)": {
        "concept": 'the name lookup on a quoted symbol',
        "what":    'the unqualified portion of the symbol',
        "goal":    'extract the unqualified name from the quoted symbol',
    },
    "(name 'java.util.Date)": {
        "concept": 'the name lookup on a host class symbol',
        "what":    'the unqualified portion of the host class name',
        "goal":    'extract the unqualified name from the host class symbol',
    },
    "(namespace :village/shepherd)": {
        "concept": 'the namespace lookup on a qualified keyword',
        "what":    'the namespace portion of the qualified keyword',
        "goal":    'extract the namespace from the qualified keyword',
    },
    "(map name ['village.shepherd 'village.elder])": {
        "concept": 'mapping name across a list of symbols',
        "what":    'the list of unqualified names',
        "goal":    'apply name across the two qualified symbols and collect the results',
    },
    "(count ['village.shepherd 'village.elder 'village.wolf])": {
        "concept": 'counting a vector of qualified symbols',
        "what":    'the number of items in the vector',
        "goal":    'count the number of qualified symbols in the vector',
    },
    "(:wolf {:wolf 1 :flock 2})": {
        "concept": 'keyword lookup on a map',
        "what":    'the value associated with the wolf key',
        "goal":    'look up the wolf key in the map by invoking the keyword',
    },
    "(clojure.string/lower-case \"WOLF\")": {
        "concept": 'lowercasing a string with clojure.string/lower-case',
        "what":    'the lower-cased form of the input string',
        "goal":    'lowercase the alarm string with clojure.string/lower-case',
    },
    "(clojure.string/reverse \"flock\")": {
        "concept": 'reversing a string with clojure.string/reverse',
        "what":    'the reversed form of the input string',
        "goal":    'reverse the flock string with clojure.string/reverse',
    },
    "(count \"wolf\\nshepherd\\n\")": {
        "concept": 'counting characters in a multi-line string',
        "what":    'the total character count including newlines',
        "goal":    'count every character in the multi-line alarm string',
    },
    "(.startsWith \"shepherd-elder\" \"shepherd\")": {
        "concept": 'host-method check for a string prefix',
        "what":    'whether the compound name begins with shepherd',
        "goal":    'test whether the compound name begins with the shepherd prefix',
    },
    "(try (/ 1 0) (catch Exception e :caught))": {
        "concept": 'a try form with a catch returning a sentinel keyword',
        "what":    'the value the catch branch returns',
        "goal":    'catch the divide-by-zero error and return the caught keyword',
    },
    "(let [flock-size 8 stray-count 2] (- flock-size stray-count))": {
        "concept": 'a let-bound subtraction of flock and stray counts',
        "what":    'the remaining flock after subtracting strays',
        "goal":    'bind flock-size and stray-count, then subtract strays from the flock',
    },
    "(let [a (int-array [5 10 15])] (aget a 0))": {
        "concept": 'binding a host int-array and reading the first slot',
        "what":    'the value at the first array index',
        "goal":    'bind a host int-array and read its first slot with aget',
    },
    "(= 1 1)": {
        "concept": 'the equality check on two equal integers',
        "what":    'whether 1 equals 1',
        "goal":    'test whether 1 equals 1 with =',
    },
    "(= 1 2)": {
        "concept": 'the equality check on two distinct integers',
        "what":    'whether 1 equals 2',
        "goal":    'test whether 1 equals 2 with =',
    },
    "(= 'village.shepherd 'village.shepherd)": {
        "concept": 'the equality check on two identical qualified symbols',
        "what":    'whether the two qualified symbols are equal',
        "goal":    'test whether the two qualified shepherd symbols are equal',
    },
    # ─────── round3 group4 (V7dL): per-form GOALS for atom subjects
    # that previously fell back to "evaluate the literal/predicate/..."
    # Skipped: forms whose answer-string IS a literal substring of the
    # form (FORM_LEAK / ANSWER_LEAK_STRING risk), e.g. (= :wolf :wolf)
    # answers ":wolf" which is in the form. Those keep the placeholder
    # fallback path with empty goal_text.
    "(:missing {:wolf 1})": {
        "concept": 'looking up an absent key in a small map',
        "what":    'what comes back when a key is not in the map',
        "goal":    'look up an absent key in a one-entry map and observe the runtime result',
    },
    "(count ['village.shepherd 'village.elder 'village.flock])": {
        "concept": 'counting the elements of a quoted-symbol vector',
        "what":    'how many elements the vector holds',
        "goal":    'count the elements in a vector of qualified shepherd symbols',
    },
    "(last  [10 20 30])": {
        "concept": 'the last element of a vector',
        "what":    'what last returns from a small vector',
        "goal":    'fetch the last element of a small vector via last',
    },
    "(symbol? 'village.flock)": {
        "concept": 'the symbol-predicate on a qualified name',
        "what":    'whether a qualified quoted name is a symbol',
        "goal":    'test whether a qualified quoted name is a symbol',
    },
}


def get_goal(form: str, concept: str, what: str) -> str:
    """Look up goal_text for `form`.

    Returns the canonical goal_text from GOALS if present, otherwise
    derives a verb-phrase ONLY for explicit boy-wolf-specific
    constructs that are missing (`defprotocol Alarm`,
    `defmacro with-careful-watch`, type-hinted `(let [^…])`). Anything
    else (including the broader metaphor-rich forms that already work
    via canonical entries, atom forms, and parametric forms) stays on
    its existing path with empty goal_text.

    Audited by the boy-wolf XOE6 deep-audit slice.
    """
    canon = GOALS.get(form, {})
    g = canon.get("goal", "")
    if g:
        return g
    if not what or not form:
        return ""
    f = form.strip()
    needs_synthesis = (
        "defprotocol" in f
        or "defmacro" in f
        or "deftype" in f
        or "defrecord" in f
        or "defmulti" in f
        or "extend-protocol" in f
        or "extend-type" in f
        or "let [^" in f  # type-hinted binding
    )
    if not needs_synthesis:
        return ""
    w = what.strip().rstrip("?").rstrip()
    low = w.lower()
    if low.startswith("whether "):
        return f"determine {w}"
    if low.startswith("what "):
        return f"find {w}"
    if low.startswith("which "):
        return f"identify {w}"
    if low.startswith("the "):
        return f"compute {w}"
    return f"compute {w}"
