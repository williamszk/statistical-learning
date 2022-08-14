defmodule M do
  def main do
    name = IO.gets("What is your name? " |> String.trim())

    IO.puts("Hello #{name}. Welcome to the Elixir programming language.")

    data_stuff()
  end

  def data_stuff do
    my_int = 123

    IO.puts("Integer: #{is_integer(my_int)}")

    my_float = 3.141589

    IO.puts("Float: #{is_float(my_float)}")

    # about Atom
    IO.puts("Atom: #{is_atom(:Sao_Paulo)}")
    :"New York"

    # Range
    one_to_ten = 1..10

    # Stoped at:
    #  https://youtu.be/pBNOavRoNL0?t=402
  end
end
