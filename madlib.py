import sys

if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        file_contents = input_file.read()

        output = ""
        # I think line == The [animal] looked at the [object] and blah to [verb].
        for line in file_contents.split("\n"):
            replacement_line = ""

            # print line.split(" ")
            # I think maybe word is each of the words... IE word == [animal]
            for word in line.split(" "):
                replacement_word = word
                if word.startswith("[") or word.endswith("]"):

                    beginning = word.index('[')
                    end = word.index(']')

                    word = word[beginning+1:end]
                    replacement_word = input(f"Please provide a {word}: ")
                replacement_line += replacement_word + " "
            output += replacement_line + "\n"
            # print(f"the new line is: <{replacement_line}>")

    print(f"the output: {output}")

    with open(output_file_name, 'w', encoding='utf-8') as outputfile:
        print("writing output file")
        outputfile.write(output)
        print("output file written")
