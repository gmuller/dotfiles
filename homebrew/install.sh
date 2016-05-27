#!/bin/sh
#
# Homebrew
#
# This installs some of the common dependencies needed (or at least desired)
# using Homebrew.

# Check for Homebrew
if test ! $(which brew)
then
  echo "  Installing Homebrew for you."
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
brew install cask
brew tap caskroom/versions

brew install Caskroom/cask/java
brew cask install java7
brew install homebrew/versions/maven30

# Install homebrew packages
brew install grc coreutils spark ghc cabal-install zsh libsndfile mongodb libsamplerate liblo jack nodejs sox

brew cask install anki
brew cask install atom
brew cask install eclipse-java
brew cask install evernote
brew cask install github-desktop
brew cask install iterm2
brew cask install libreoffice
brew cask install robomongo
brew cask install viscosity
brew cask install spotify
brew cask install vagrant
brew cask install vagrant-manager
brew cask install virtualbox
brew cask install anvil
brew cask install openemu
brew cask install obs
brew cask install steam
brew cask install flux

exit 0
