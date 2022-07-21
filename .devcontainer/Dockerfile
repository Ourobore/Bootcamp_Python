FROM python:3.10.5-bullseye

# Setting up working environment
RUN apt-get update && apt-get -y install \
    # Utilities
    make \
    curl \
    git \
    # Install zsh and oh-my-zsh and make zsh the default shell
    zsh ;\
    cd / && sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" \
    && chsh -s $(command -v zsh)
