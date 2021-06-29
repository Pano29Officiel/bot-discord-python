# :discord: Créer un BOT DISCORD avec PYTHON

[![Discord](https://img.shields.io/discord/702114006399189062?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://pterodactyl-installer.se/discord)
[![Python](https://img.shields.io/pypi/dm/discord?logo=python&logoColor=fff)](https://pypi.org/project/discord.py/)

Unofficial scripts for installing Pterodactyl Panel & Wings. Works with the latest version of Pterodactyl!

Read more about [Pterodactyl](https://pterodactyl.io/) here. This script is not associated with the official Pterodactyl Project.

## Features

- Automatic installation of the Pterodactyl Panel (dependencies, database, cronjob, nginx).
- Automatic installation of the Pterodactyl Wings (Docker, systemd).
- Panel: (optional) automatic configuration of Let's Encrypt.
- Panel: (optional) automatic configuration of UFW (firewall for Ubuntu/Debian).

## Help and support

For help and support regarding the script itself and **not the official Pterodactyl project**, you can join the [Discord Chat](https://pterodactyl-installer.se/discord).

## Supported installations

List of supported installation setups for panel and Wings (installations supported by this installation script).

### Supported panel operating systems and webservers

| Operating System | Version | nginx support      | PHP Version |
| ---------------- | ------- | ------------------ | ----------- |
| Ubuntu           | 14.04   | :red_circle:       |             |
|                  | 16.04   | :red_circle: \*    |             |
|                  | 18.04   | :white_check_mark: | 8.0         |
|                  | 20.04   | :white_check_mark: | 8.0         |
| Debian           | 8       | :red_circle: \*    |             |
|                  | 9       | :white_check_mark: | 8.0         |
|                  | 10      | :white_check_mark: | 8.0         |
| CentOS           | 6       | :red_circle:       |             |
|                  | 7       | :white_check_mark: | 8.0         |
|                  | 8       | :white_check_mark: | 8.0         |

### Supported Wings operating systems

| Operating System | Version | Supported          |
| ---------------- | ------- | ------------------ |
| Ubuntu           | 14.04   | :red_circle:       |
|                  | 16.04   | :red_circle: \*    |
|                  | 18.04   | :white_check_mark: |
|                  | 20.04   | :white_check_mark: |
| Debian           | 8       | :red_circle:       |
|                  | 9       | :white_check_mark: |
|                  | 10      | :white_check_mark: |
| CentOS           | 6       | :red_circle:       |
|                  | 7       | :white_check_mark: |
|                  | 8       | :white_check_mark: |

_\* Ubuntu 16 and Debian 8 no longer supported since Pterodactyl does not actively support it._

## Using the installation scripts

To use the installation scripts, simply run this command as root. The script will ask you whether you would like to install just the panel, just the daemon or both.

```bash
bash <(curl -s https://pterodactyl-installer.se)
```

_Note: On some systems, it's required to be already logged in as root before executing the one-line command (where `sudo` is in front of the command does not work)._

Here is a [YouTube video](https://www.youtube.com/watch?v=E8UJhyUFoHM) that illustrates the installation process.

## Firewall setup

The installation scripts can install and configure a firewall for you. The script will ask whether you want this or not. It is highly recommended to opt-in for the automatic firewall setup.

## Development & Ops

### Testing the script locally

To test the script, we use [Vagrant](https://www.vagrantup.com). With Vagrant, you can quickly get a fresh machine up and running to test the script.

If you want to test the script on all supported installations in one go, just run the following.

```bash
vagrant up
```

If you only want to test a specific distribution, you can run the following.

```bash
vagrant up <name>
```

Replace name with one of the following (supported installations).

- `ubuntu_focal`
- `ubuntu_bionic`
- `debian_buster`
- `debian_stretch`
- `centos_8`
- `centos_7`

Then you can use `vagrant ssh <name of machine>` to SSH into the box. The project directory will be mounted in `/vagrant` so you can quickly modify the script locally and then test the changes by running the script from `/vagrant/install_panel.sh` and `/vagrant/install_wings.sh` respectively.

### Creating a release

There are a couple of files that each release commit should always change. Firstly, update the `CHANGELOG.md` so that the release date and release tag are both displayed. No changes should be made to the changelog points themselves. Secondly, update `GITHUB_SOURCE` and `SCRIPT_RELEASE` in both `install-panel.sh` and `install-wings.sh`. Thirdly, update `SCRIPT_RELEASE` in `install.sh`. Finally, you can now push a commit with the message `Release vX.Y.Z`. Create a release on GitHub. See [this commit](https://github.com/vilhelmprytz/pterodactyl-installer/commit/90aaae10785f1032fdf90b216a4a8d8ca64e6d44) for reference.

When the release is published, push another commit which revers the changes you made to `install-wings.sh` and `install-panel.sh`. See [this commit](https://github.com/vilhelmprytz/pterodactyl-installer/commit/be5f361523d1d546d49eef8b3ce1a9145eded234) for reference.

## Contributors ✨

Copyright (C) 2018 - 2021, Vilhelm Prytz, <vilhelm@prytznet.se>

Created and maintained by [Vilhelm Prytz](https://github.com/vilhelmprytz).

Special thanks to the Discord moderators [sam1370](https://github.com/sam1370), [Linux123123](https://github.com/Linux123123) and [sinmineryt](https://github.com/sinmineryt) for helping on the Discord server!





# Créer un BOT DISCORD avec PYTHON

Bienvenue sur le repo officiel de la série de vidéos "Crée un bot discord avec python" réalisée par Pano29Officiel.

[![Alt text](https://cdn.discordapp.com/attachments/775770838309404722/856615611094663188/baniere_parent.png)](http://www.pano29officiel.tk)

Cette série de vidéos vous permet d'apprendre à développer un BOT DISCORD avec PYTHON. Tous les scripts du projet sont en Python et il est recommandé de suivre la série en version 3.8 ou plus.

Le contenu du projet pour chaque épisode est disponible [ICI](https://github.com/Pano29Officiel/bot-discord-python/tree/master/episodes), choisissez la branche de votre choix, téléchargez là et ouvrez le projet sur votre éditeur de code.

► Si vous suivez cette série et/ou utilisez ce repo GitHub pensez à vous abonner a ma [chaine](https://bitly.com/Pano29YTB) ! Ce n'est pas obligatoire mais c'est fortement apprécié !


