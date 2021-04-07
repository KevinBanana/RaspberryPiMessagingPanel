<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KevinBanana/RaspberryPiMessagingPanel">
    <img src="src/RPlogo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Raspberry Pi Messaging Panel</h3>

  <p align="center">
    A messaging panel created with Raspberry Pi which sends texts when a button is pressed
    <br />
    <a href="https://github.com/KevinBanana/RaspberryPiMessagingPanel"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KevinBanana/RaspberryPiMessagingPanel">View Demo</a>
    ·
    <a href="https://github.com/KevinBanana/RaspberryPiMessagingPanel/issues">Report Bug</a>
    ·
    <a href="https://github.com/KevinBanana/RaspberryPiMessagingPanel/issues">Request Feature</a>
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://user-images.githubusercontent.com/59422394/113928968-76a3ee00-97bd-11eb-9cf5-9879cfbdbb97.png" width="488">


I created this project to have a quick way of messaging my girlfriend. It's primary purpose is to either text her
"On my way!" when I head out the door or "I love you" whenever I'm thinking about her. I wanted this to be as easy
as pushing a button instead of having to unlock my phone, go to my messaging app, and type a message.


### Built With

* [Raspberry Pi](https://www.raspberrypi.org/)
* [Twilio](https://www.twilio.com/)
* [Python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This guide assumes you already have your raspberry pi set up with an OS and that it is connected to the internet.
You'll need a keyboard and mouse connected to it during the setup but after that you will not need any
peripherals at all.

You'll also need a Twilio account with an API key. For more information, visit https://www.twilio.com/console/video/project/api-keys.

If you're using the trial, set up the destination phone numbers
<a href=https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account>here</a>.


### Installation

1. On your raspberry pi, clone the repo
   ```sh
   git clone https://github.com/KevinBanana/RaspberryPiMessagingPanel.git
   ```
2. Install the twilio package
   ```sh
   pip install twilio
   ```

3. Go to your twilio <a href=https://www.twilio.com/console>console</a> and get your trial number, account SID,
and auth token

4. Create a file called config.py and save the previously gathered details like this

![Config screenshot][setup-config]

5. Wire up your raspberry pi with 2 LEDs and 3 buttons on the corresponding GPIO ports:

Green Light: Port 12

Red Light: Port 18

Button 1: Port 11

Button 2: Port 13

Button 3: Port 15

![Ports][ports-chart]


6. Run ButtonListener.py from the Raspberry Pi


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/KevinBanana/RaspberryPiMessagingPanel/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Kevin Bonanno - kbonanno3@gatech.edu

Project Link: [https://github.com/KevinBanana/RaspberryPiMessagingPanel](https://github.com/KevinBanana/RaspberryPiMessagingPanel)


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-url]: https://github.com/KevinBanana/repo/graphs/contributors
[forks-url]: https://github.com/KevinBanana/repo/network/members
[issues-url]: https://github.com/KevinBanana/repo/issues
[license-url]: https://github.com/KevinBanana/repo/blob/master/LICENSE.txt
[linkedin-url]: https://linkedin.com/in/KevinBanana
[setup-config]: src/configExample.png
[ports-chart]: src/portChart.jpg
