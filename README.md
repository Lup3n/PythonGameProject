# PythonGameProject

## Welcome to Zoombies

<ul>Team members:
    <li>Tolga Uluturk</li/>
    <li>Kamil Urbanski</li>
    <li>Omar Alaa Eldin Abou Hussein</li/>
</ul>


Scoring system: Zombie kills
Health: Healthbar



When a zombies is kill you have a change to receive between 0 and 5 bullets.
When you are killed the game will restart.

### How To Run

For Uni Professor:

    Download the provided code into the same strucutre as uploaded 
    Then nagivate into the directory with the game.
    Run the game.py file with python.



For Linux:

    Open your terminal and navigate to the directory where you want to download the game.
    Clone the repository by typing git clone https://github.com/Lup3n/PythonGameProject.git and press Enter.
    Navigate into the downloaded directory by typing cd PythonGameProject and press Enter.
    Type python3 game.py and press Enter to start the game.

For Windows:

    Open your web browser and navigate to https://github.com/Lup3n/PythonGameProject.
    Click on the "Code" button and select "Download ZIP".
    Extract the downloaded ZIP file to a location of your choice.
    Open the extracted folder and locate the game.py file.
    Open Command Prompt by pressing the Windows key + R, type cmd and press Enter.
    Navigate to the directory where you extracted the game by typing cd path\to\extracted\folder and press Enter.
    Type python game.py and press Enter to start the game.





What each file does:
    
    bullet.py - Responsible for being a bullet, so it a sprite which has a velocity.
    
    camera.py - Responsible for offsetting all stationary sprite as well as moving ones according to the players movement.
    
    clock.py - Responsible for counting.
    
    enemy.py - Responsible for the zombies that are used in the game.
    
    gui.py - Responsible for some gui aspects of the game.
    
    interaction.py - Responsible performing movement and actions of a player.
    
    keyboard.py  - Responsible for defining which keys are to be used and their action.
    
    level.py - Responsible for loading the level onto the screen and drawing it.
    
    levelOptions.py - Responsible for defining the layout of the maps using lists.
    
    player.py - Responsible for keeping all stats and sprite of the player in the game.
    
    spritesheet.py - Responsible for helping sprites have animations via spritesheets.
    
    statusbar.py - Responsible for having the gui bar on the screen informing the player how many bullets,zombies, health is left.
    
    vector.py - Responisble for all vector handling.
    
    wall.py - Responsible for drawing and updating the wall sprites witin the game.
    
    weapon.py - Responsible for firing bullets via the bullet class and the direction in which the bullet should be fired.