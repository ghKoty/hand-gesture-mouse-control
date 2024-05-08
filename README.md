

# Hand gesture mouse control




**[Hand gesture mouse control](https://github.com/ghKoty/hand-gesture-mouse-control) © 2024 by [ghKoty](https://github.com/ghKoty) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1).**

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**



## What is it




*Hand mouse control* is simple software, that allows you to control the mouse cursor using webcam and your hands.
With this software you can move mouse cursor, left click, right click, and scroll using [hand gestures](#supported-hand-gestures).


> So, this is a simple software to control your mouse using hand gestures.


## How to setup


> This code can run on ***Windows, Linux-based systems, and MacOS***


1. Download this project by clicking `Code` button, then `Download ZIP`, then unpack downloaded archive


2. To run this project you need latest version of **Python**([link](https://www.python.org/))
    
    Please note that Python is preinstalled in the most of Linux-based OSes, you can check installation by entering `python3 --version` in your terminal

    > It's recommend to **`Add Python to PATH`**, with this setting you will be able to run python by typing `python` in cmd


3. You need to install all required modules:

    ```
    pyautogui
    mediapipe
    opencv-python	(cv2)
    ```

    You can do this in many ways

    * Using `pip3`: type in cmd/terminal `pip3 install <module>`, for example `pip3 install pyautogui`

    * Or using `requirements.txt`: open the project folder in cmd/terminal and type `pip3 install -r requirements.txt

4. Run `hand-gesture-mouse-control.py` and after webcam window appears, try to move mouse cursor using [hand gesture](#supported-hand-gestures)

5. If everything works fine enjoy using this software, otherwise if you can\`t use any gestures(clicks are not registering) try increasing `press_threshold_multiplyer` variable in code, or if you experience random clicks, try decreasing that variable.
    > Please note that some random clicks can appear because of bad webcam image quality.

## Supported hand gestures


![hand screenshot](readme-resources/hand-main.png "all tracked points"


You can **move** mouse cursor  by touching <span style="color:blue">**thumb**</span> with <span style="color:green">**middle finger**</span> and moving hand


You can perform **left click** by touching <span style="color:blue">**thumb**</span> with <span style="color:skyblue">**index finger**</span>


You can perform **right click** by touching <span style="color:blue">**thumb**</span> with <span style="color:yellow">**ring finger**</span>


You can **scroll** by touching <span style="color:red">**red point**</span>(i dont know how to name it ¯\\\_(ツ)\_\/¯ )  with <span style="color:blue">**thumb**</span> and moving hand up or down


> Tip: you can combine some actions, for example: *press LMB* and *move cursor* to select text, or use scrollbar
