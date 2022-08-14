
# Install Elixir

# https://elixir-lang.org/install.html#gnulinux


apt install wget
apt update
wget https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb && sudo dpkg -i erlang-solutions_2.0_all.deb
apt-get install esl-erlang
apt-get install elixir


# https://gist.github.com/rubencaro/6a28138a40e629b06470#install-asdf-and-its-plugins
cd
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.7.4

# For Ubuntu or other linux distros
echo '. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo '. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc

asdf plugin-add erlang
asdf plugin-add elixir

asdf install erlang 24.0.4
asdf install elixir 1.12.1

asdf global erlang 24.0.4
asdf global elixir 1.12.1


erl
iex
# interactive elixir
# use ctrl+C to exit iex
# write clear to clear the screen


# tutorial in Elixir
# https://www.youtube.com/watch?v=pBNOavRoNL0&ab_channel=DerekBanas 

# How to execute the Elixir program?
# cd into where the program is
iex
c("elixirtut.ex")
M.main

# to rerun the program we need to reload the program
# using c("nameoftheprogram.ex")


