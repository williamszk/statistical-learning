Perl tutorial:

https://www.youtube.com/watch?v=WEghIXs8F6c&ab_channel=DerekBanas

Had problems of locale with perl, I solved using:
https://stackoverflow.com/a/39761477/15875971

We need to install locale-gen in the container and generate the locale configuration

Then perl will stop the warning about locale gen.