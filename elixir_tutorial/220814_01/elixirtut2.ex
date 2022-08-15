defmodule M do
  def main do
    do_stuff()
  end

  def do_stuff do
    my_str = "My sentence"

    # print the length of the string
    IO.puts("Length: #{String.length(my_str)}")

    # combine strings
    longer_str = my_str <> " " <> "is longer"

    # compare two strings
    IO.puts("Equal: #{"Egg" === "egg"}")
    # === compares the value and datatype

    # check if a string contains another string
    IO.puts("My ? #{String.contains?(my_str, "My")}")

    # return the first character in the string
    IO.puts("First: #{String.first(my_str)}")

    # check what is inside the index 4
    IO.puts("Index 4: #{String.at(my_str, 4)}")

    # get substring
    IO.puts("Substring: #{String.slice(my_str, 3, 7)}")

    IO.inspect(String.split(longer_str, " "))

    # Reverse the order of chars in string
    IO.puts(String.reverse(longer_str))

    # make all chars uppercase
    IO.puts(String.upcase(longer_str))

    # make all chars lower case
    IO.puts(String.downcase(longer_str))

    # make only the first char of the string uppercase
    IO.puts(String.capitalize(longer_str))

    # example of piping
    (4 * 10) |> IO.puts()
  end
end
