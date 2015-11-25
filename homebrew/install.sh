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

# Install homebrew packages
brew install grc coreutils spark brew-cask ghc cask cabal-install zsh libsndfile mongodb maven30 libsamplerate liblo jack nodejs sox

brew install Caskroom/cask/anki
brew install Caskroom/cask/atom
brew install Caskroom/cask/eclipse-java
brew install Caskroom/cask/evernote
brew install Caskroom/cask/github-desktop
brew install Caskroom/cask/iterm2
brew install Caskroom/cask/libreoffice
brew install Caskroom/cask/robomongo
brew install Caskroom/cask/viscosity
brew install Caskroom/cask/spotify
brew install Caskroom/cask/vagrant
brew install Caskroom/cask/vagrant-manager
brew install Caskroom/cask/virtualbox
brew install Caskroom/cask/anvil

exit 0
